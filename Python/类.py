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
Secretive._Secretive____inaccessible

s._Secretive__inaccessible()

# 4.类的命名空间
# 类命名时，所有位于class语句中的代码都在特殊的命名空间中执行--类命名
# 空间，该空间可由类内所有成员访问