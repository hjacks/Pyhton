#1.什么是异常
#python用异常对象表示异常
#2.按自己的方式出错
#raise Exception
#raise  Exception('hyperdrive overload')
# import exceptions
# dir(exceptions)
# Exception:所有异常的基类
#AttributeError：特性引用或赋值失败时触发
#IOError：试图打不开文件时（或其他情况）引发
#IndexError:在使用序列中不存在的索引引发
#KeyError：在使用映射中不存在的键时引发
#NameError：在找不到名字（变量）时引发
#SyntaxError：在代码为错误形式时引发
#TypeError：在内建操作或函数引用错误对象时引发
#ValueError：在内建操作或函数引用正确对象时，但值不合适时引发
#ZeroDivisionError：在除法或者模除操作时第二个参数为0时引发
#2.2自定义异常类
