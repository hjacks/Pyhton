#1.创建函数
#callable函数可以判断函数是否调用
import math
x=1
y=math.sqrt
print(callable(x))
print(callable(y))

def hello(name):
    print('hello,'+name+'!')
hello('xu')

def fib(nbr):
    result=[0,1]
    for i in range(nbr-2):
        result.append(result[-2]+result[-1])
    print(result)
fib(10)

#1.1记录函数
#在函数开头写上字符串，会作为函数一部分进行存储，称为文档字符串，可用
#属性__doc__访问
def square(x):
    '计算x的平方'
    return x*x
print(square(2))
print(square.__doc__)
help(square)
#1.2 并非真正函数的函数
def test():
    print('This is printed')
    return
    print('This is not')
test()
#这里的return只起到结束函数的作用

#2.参数
#2.2能改变参数吗
def try_to_change(n):
    n='Mr. xu'
name='Mr. Li'
try_to_change(name)
print(name)
#在函数内name获得新值，但没有影响全局变量
#工作方式如下
#name='Mr. Li'
#n=name
#n='Mr. xu'
#name
#>>>'Mr. Li'
#当n变时，name不变

def change(n):
    n[0]='Mr.Xu'
name=['Mr.Li','Mr.Xiao']
change(name)
print(name)
#两个变量引用同一列表，所以发生改变，避免这种情况，可以拷贝表
x=[1,2,3]
y=x[:]
print(x)
print(y)
print(y==x)
print( y is x)
name=['Mr.Li','Mr.Xiao']
change(name[:])
print(name)

