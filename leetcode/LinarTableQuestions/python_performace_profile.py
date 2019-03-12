

# 当数据量很大的时候, 就会遇到 性能瓶颈问题, 这时就需要考虑性能优化了.

# python的基础语法之类的是基础但不是重点, 系统地全局地理解项目/项目整体架构/数据库设计等方面/业务逻辑/ 更重要

1.python代码里的 for循环之类的 耗时耗内存 的 写法的 优化,

2.mysql数据库的 性能优化,但数据量很大时，包括web server或mysql server都会遇到·性能瓶颈·问题！！因为本质上：
  无论是nginx/apache之类的web server或是mysql之类的数据库，都是在一个端口监听并处理http请求，本质都是底层socket的数据读写处理！！
  其原理其实差不多，所以在数据量上来后都会有性能瓶颈问题，
  底层socket读写终究是linux上跑的一个程序，终究会有性能限制（比如linux能同时   打开的最大文件描述符数量等限制）！！

3.后台服务器的部署方案的选择, nginx的负载均衡等.

4.关系型数据库mysql/postgre还是重点,需要深入学习高级教程(数据库性能调优等), mongodb/redis等k-v数据库只做了解不用深入,

5.python的基础语法之类的是基础但不是重点, 系统地全局地理解项目/项目整体架构/数据库设计等方面/业务逻辑/ 更重要,

6.数据结构和算法,

7.设计模式,

8.大型web后台开发所会遇到的问题 例如 大访问量/高并发(C10k问题)/数据库数据量很大查询效率低下/ ,
  (当数据量很大的时候, 就会遇到 `性能瓶颈` 问题, 这时就需要 考虑`性能优化`的各种方案.)

9.全栈-完整地开发 中小型/大型 项目,包括各种common功能模块, 包括 web前端/hybrid app + web后台,

10.linux,

11.python内存性能优化方案之一: for循环的地方 改用 生成器/yield,

12.站在系统层面的大方向的把握/理解, 项目整体/全局 的业务逻辑/功能模块/ 的明确/熟悉,

'''反复提及的问题:
13.有 /web项目大访问量高并发/mysql大数据量/的 大型项目经验,处理相关C10k情况下的 性能优化问题的经验等.
'''

14.今年要做一个 hybrid app 产品, 包含前后端 产品设计/功能/定位/开发, 后端数据量要大/mock数据也行,
   仅当练习而已, 一个完整的/中大型的 移动互联网的项目练习, 全套的设计/开发.
   技术栈: ionic + python + mysql + linux

########################################################################################################
# 2017中级水平面试技术问题总结：
