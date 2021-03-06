

# copy from hubian's code

import requests
from ironic.common import exception
import json
import logging


def safe_get_from_info(info, keys_content, default):
    """
    safety parsing values from a json to protect from raising KeyError Exception

    :param info: dict
    :param keys_content: str,style: key1.key2.key3 ...
    :param default:

    :return: default
    """
    result = info
    for key in keys_content.split('.'):
        if key in result:
            result = result[key]
        else:
            return default
    return result


class HttpMethod:
    def __init__(self):
        self.log = logging.getLogger(__name__)

    def do_get_request(self, url, headers=None, body=None, auth=None, verify=False):
        status_code, text = self.__do_http_request("GET", url, headers, body, auth, verify)
        try:
            return json.loads(text)
        except (TypeError, ValueError):
            self.log.error("can not parse http response text to json", text)
            return None

    def do_post_request(self, url, headers=None, body=None, auth=None, verify=False):
        try:
            self.__do_http_request("POST", url, headers, body, auth, verify)
            return True
        except Exception as ex:
            self.log.error("send post http request raise an Exception \n %s" % ex)
            return False

    # --------------------- helper functions -------------------- #

    def __do_http_request(self, method, url, headers=None, body=None, auth=None, verify=False):
        try:
            self.__http_log_req(method, url, body, headers)
            resp = requests.request(method,
                                    url,
                                    data=body,
                                    headers=headers,
                                    auth=auth,
                                    verify=verify)
            self.__http_log_resp(resp, resp.text)
            status_code = resp.status_code
            return status_code, resp.text if status_code < 300 else self.__handle_fault_response(resp)
        except requests.exceptions.ConnectionError as e:
            self.log.debug("throwing ConnectionFailed : %s", e)
            raise exception.HTTPNotFound(url=url)

    def __handle_fault_response(self, resp):
        self.log.debug("Error message: %s", resp.text)
        try:
            error_body = json.loads(resp.text)
            if error_body:
                explanation = error_body['messages'][0]['explanation']
                recovery = error_body['messages'][0]['recovery']['text']
        except Exception:
            # If unable to deserialized body it is probably not a
            explanation = resp.text
            recovery = ''
        # Raise the appropriate exception
        kwargs = {'explanation': explanation, 'recovery': recovery}
        raise exception.XClarityInternalFault(**kwargs)

    def __http_log_req(self, method, url, body=None, headers=None):
        if not self.log.isEnabledFor(logging.DEBUG):
            return
        self.log.debug("REQ:%(method)s %(url)s %(headers)s %(body)s\n",
                       {'method': method,
                        'url': url,
                        'headers': headers,
                        'body': body})

    def __http_log_resp(self, resp, body):
        if not self.log.isEnabledFor(logging.DEBUG):
            return
        self.log.debug("RESP:%(code)s %(headers)s %(body)s\n",
                       {'code': resp.status_code,
                        'headers': resp.headers,
                        'body': body})


http = HttpMethod()
