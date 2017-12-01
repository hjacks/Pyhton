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
#2.2.1为什么修改参数
def init(data):
    data['first']={}
    data['middle']={}
    data['last']={}
storage={}
init(storage)
print(storage)

def lookup(data,label,name):
    return data[label].get(name)
me='Magnus Lie Hetland'
storage['first']['Maguns']=[me]
storage['middle']['Lie']=[me]
storage['last']['Hetland']=[me]
print(lookup(storage,'middle','Lie'))
def store(data,full_name):
    names=full_name.split()
    if len(names)==2:
        names.insert(1,' ')
    labels=['first','middle','last']
    for label,name in zip(labels,names):
        people=lookup(data,label,name)
        if people:
            people.append(full_name)
        else:
            data[label][name]=full_name

MyNames={}
init(MyNames)
store(MyNames,'xu xian tt')
print(lookup(MyNames,'middle','xian'))
#2.2.2若我的参数不可变了
#若真想改变参数，可以将值放在列表中
def inc(x):
    x[0]=x[0]+1

foo=[10]
inc(foo)
print(foo)

#2.3关键字参数和默认值
def hello(greeting,name):
    print('%s,%s!'%(greeting,name))
hello(greeting='hello',name='world')
def hello_2(greeting='hello',name='world'):
    print('%s,%s!' % (greeting, name))
hello_2()
hello_2('greeting')
hello_2('greeting','universe')
hello_2(name='tom')
#4.3可变参数
def print_parm(*par):
    print(par)
print_parm('xu')
print_parm('xu','wang','li')
def print_parm1(**par):
    print(par)
print_parm1(x=1,y=2,z=3)
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

f1(1,2,3)
f1(1,2,3,4,5,6)
f1(1,2,3,4,5,6,x=1,y=2)

#4.5反转过程
def add(x,y):
    print(x+y)
arg=(1,2)
add(*arg)

def with_star(**kw):
    print(kw['name'],'is',kw['age'],'years old')
def without_star(kw):
    print(kw['name'], 'is', kw['age'], 'years old')
args={'name':'dongxin','age':23}
with_star(**args)
without_star(args)
#4.6练习使用参数
def story(**kw):
    return 'Once upon a time,there was a %(job)s called %(name)s.'%kw
def power(x,y,*args):
    if args:
        print( 'Recieve redundant parameters:',args)
    return pow(x,y)
def interval(start,stop=None,step=1):
    'Imitates range() for step > 0'
    if stop is None:
        start,stop=0,start
    result=[]
    i=start
    while i<stop:
        result.append(i)
        i+=step
    return result
print(story(job='king',name='Mr.Grubm'))
params={'job':'Language','name':'python'}
print(story(**params))
print(pow(2,3))
print(pow(4,5))
par=(5,)*2
print(pow(*par))
print(interval(10))
print(interval(1,5))
print(interval(3,18,4))
print(power(*interval(3,7)))
#5.作用域
x=1
scope=vars()
print(scope['x'])
scope['x']+=1
print(x)

def output(x):
    print(x)

x=1
y=2
output(y)
def combine(x):
    print(x+y)
y='xxc'
combine('xfag')

x=1
def change_global():
    global x
    x=x+1
change_global()
print(x)

#6.递归
#6.1.阶乘与幂
#可以使用循环写阶乘于幂
def factorial(n):
    result=n
    for i in range(1,n):
        result*=i
    return  result

def power(x,n):
    result=1
    for i in range(1,n):
        result*=x
    return x

#使用递归写阶乘于幂
def factorial2(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
def power2(x,n):
    if n==1:
        return x
    else:
        return x*pow(x,n-1)

print(factorial2(10))
print(power2(4,3))
#6.2二元查找
def search(sequence,num,lower,upper):
    if upper==lower:
        return upper
    else:
        middle=(upper+lower)//2
        if num>sequence[middle]:
            return search(sequence,num,middle+1,upper)
        else:
            return search(sequence,num,lower,middle)














