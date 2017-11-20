# 1.类--一种对象，所有对象都属于某个类，称为类的实例
# 2.创建一个类
_metaclass_ =type #确定使用新式类
class Person:
    def setname(self,name): # self是对于对象自身的引用
        self.name=name
    def getname(self):
        return self.name
    def greet(self):
        print('Hello,I"m %s.'%self.name)

foo=Person()
bar=Person()
foo.setname('xutao')
bar.setname('wangzhi')
foo.greet()
bar.greet()

# 特性可以在外部访问
print(foo.name)
bar.name='xulei'
bar.greet()

# 3.特性，函数和方法
# self参数正是函数和方法的区别。方法（绑定方法）将它们的第一个参数绑定
# 到实例上，因此这个参数可以不必提供。所以可以将特性绑定到一个o普通函
# 数上，这样就不会有特殊的self参数了

class Class:
    def method(self):
        print("I have a self")
def function():
    print("I don't have ...")
instance=Class()
instance.method()
instance.method=function
instance.method()
# 注意，self参数并不取决于调用方法的方式，目前使用的是实例调用方法，
# 可以随意同一个方法的其他变量
class Bird:
    song='Squwaak'
    def sing(self):
        print(self.song)
bird=Bird()
bird.sing()
birdsong=bird.sing
birdsong()

# 为了让方法和特性私有（外部无法访问），只需在它的名字前加上双下划线即可
class Secretive:
    def __inaccessible(self):
        print("Bet you can't see me...")
    def accessible(self):
        print("The secrect is ...")
        self.__inaccessible()
# 现在__inaccessible外部无法访问，在内部可以
s=Secretive()
# s.__inaccessible()
# >>>Traceback (most recent call last):
#   File "C:/Users/zhou/Desktop/GitHub/Pyhton/Python/类.py", line 58, in <module>
#     s.__inaccessible()
# AttributeError: 'Secretive' object has no attribute '__inaccessible'
s.accessible()

# 类的内部定义中，所有双下滑线都被翻译成前面加上单下划线和类名的形式
# Secretive._Secretive____inaccessible
#
# s._Secretive__inaccessible()

# 4.类的命名空间
# 类命名时，所有位于class语句中的代码都在特殊的命名空间中执行--类命名
# 空间，该空间可由类内所有成员访问
class memberCounter:
    members=0
    def init(self):
        memberCounter.members+=1


m1=memberCounter()
m1.init()
print(m1.members)
m2=memberCounter()
m2.init()
print(m2.members)
print(m1.members)
m1.members='two'
print(m1.members)
print(m2.members)

# 2.5 指定超类
class Filter:
    def init(self):
        self.blocked=[]
    def filt(self,sequence):
        return [x for x in sequence if x not in self.blocked]

class SPAMFilter(Filter): #SPAMFilter是Filter的子类
    def init(self):  #重写init方法
        self.blocked=['SPAM']

f=Filter()
f.init()
print(f.filt([1,2,3]))

s=SPAMFilter()
s.init()
print(s.filt(['SPAM','SPAM','EGG','THU'])) # 不能直接调用filt，得先调用init
# 注意 1：重写了init定义，2：继承了filt函数

# 2.6 调查继承
# 用issubclass函数看一个类是否是另一个的子类
print(issubclass(SPAMFilter,Filter))
print(issubclass(Filter,SPAMFilter))

# 若已知类的基类(们)，可直接使用特殊属性__base__
print(SPAMFilter.__bases__)
print(Filter.__bases__)

#使用isinstance检查一个对象是否是一个类的实例
print(isinstance(s,SPAMFilter))
print(isinstance(f,Filter))
print(isinstance(s,str))

#可用__class__查看一个对象属于哪个类
print(s.__class__)
print(f.__class__)

# 2.7 多个超类
class Calculator:
    def calculate(self,expression):
        self.value=eval(expression)

class Talker:
    def talker(self):
        print('hi,my value is ',self.value)

class TalkerCalculator(Talker,Calculator):
    pass

tc=TalkerCalculator()
tc.calculate('1+4*4')
tc.talker()

#子类从所有超类继承所有方法，称为多重继承，除非非常熟悉，否则尽量避免使用多重继承。
#注意超类的顺序，先继承得超类中方法会重写后继承的超类方法

#2.8 接口和内省
#处理多态时，只需关心接口（协议）即可--公开的特性和方法
#python中，不用显示指定对象必须包含哪些方法才能作为参数接收
#可检查方法是否存在
print(hasattr(tc,'talker'))
print(hasattr(tc,'bav'))
#还可检查特性是否可调用
# print(hasattr(getattr(tc,'talker',None)),'__call__')
# print(hasattr(getattr(tc,'bav',None)),'__call__')
#getattr用来获得对象特性，并提供默认值
#setattr正好相反
# setattr(tc,'name','xuxiaobai')
# print(tc.name)

#3.关于对象的思考
#3.1将属于一类的对象放在一起
#3.2不要让对象过于亲密
#3.3小心继承，尤其是多重继承
#3.4简单就好
