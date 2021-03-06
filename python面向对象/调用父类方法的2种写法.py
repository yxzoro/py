

super 是用来解决多重继承问题的，直接用类名调用父类方法在使用单继承的时候没问题，
但是如果使用多继承，会涉及到查找顺序（MRO）、重复调用（钻石继承）等种种问题。总之前人留下的经验就是：保持一致性。
要不全部用类名调用父类，要不就全部用 super，不要一半一半。

普通继承
『代码』
[python]view plaincopy在CODE上查看代码片派生到我的代码片 
class FooParent(object):  
    def __init__(self):  
        self.parent = 'I\'m the parent.'  
        print 'Parent'  
      
    def bar(self,message):  
        print message, 'from Parent'  
          
class FooChild(FooParent):  
    def __init__(self):  
        FooParent.__init__(self)  
        print 'Child'  
          
    def bar(self,message):  
        FooParent.bar(self,message)  
        print 'Child bar function.'  
        print self.parent  
          
if __name__=='__main__':  
    fooChild = FooChild()  
    fooChild.bar('HelloWorld')  


super继承
『代码』
[python]view plaincopy在CODE上查看代码片派生到我的代码片 
class FooParent(object):  
    def __init__(self):  
        self.parent = 'I\'m the parent.'  
        print 'Parent'  
      
    def bar(self,message):  
        print message,'from Parent'  
  
class FooChild(FooParent):  
    def __init__(self):  
        super(FooChild,self).__init__()  
        print 'Child'  
          
    def bar(self,message):  
        super(FooChild, self).bar(message)  
        print 'Child bar fuction'  
        print self.parent  
  
if __name__ == '__main__':  
    fooChild = FooChild()  
    fooChild.bar('HelloWorld')  

程序运行结果相同，为：
Parent
Child
HelloWorld from Parent
Child bar fuction
I'm the parent.

****************************************************************************************************
从运行结果上看，普通继承和super继承是一样的。但是其实它们的内部运行机制不一样，这一点在多重继承时体现得很明显。
            在super机制里可以保证公共父类仅被执行一次，至于执行的顺序，是按照mro进行的（E.__mro__）
****************************************************************************************************

注意super继承只能用于新式类，用于经典类时就会报错。
新式类：必须有继承的类，如果没什么想继承的，那就继承object
经典类：没有父类，如果此时调用super就会出现错误：『super() argument 1 must be type, not classobj』





