#1.zip函数
names=['tom','jerry','mary']
age=[22,32,25]
d=zip(names,age)
print(d)
#可以对付不等长函数，直到短的用完
d=zip(range(5),range(100))
print(d)

#2.exec&eval
#exec动态执行字符串里的python代码
exec( "print('hello,world')")
#简单的exec语句不是好事，很多情况下可以给他提供命名空间，从而干扰python
#的命名空间，可以使用<scope>
from math import sqrt
scope={}
exec ("sqrt=1" ,scope)
print(sqrt(4))
print(scope['sqrt'])
print(scope.keys())
#>>>dict_keys(['__builtins__', 'sqrt'])
#__builtins__包含了所有内建函数和值

#eval
#执行字符串里的python表达式
print(eval('1+2+3'))
print(eval('a+1',{'a':99}))
#print(eval(input()))

#3.seek
#seek(offset[,whence]):把当前位置移动到由offset定义的位置whence.offset
#是一个字节（字符）数,默认是0，也就是偏移量从文件开头算起，可设置为1，
#相对于当前位置移动，也可设置为2，从文件结尾移动
f=open('test.txt','w')
f.write('0123456789')
f.seek(5)
f.write('hello,world!')
f.close()
f=open('test.txt','r')
print(f.read())
#tell返回当前文件位置
f=open('test.txt','r')
print(f.read(2))
print(f.read(2))
print(f.tell())
