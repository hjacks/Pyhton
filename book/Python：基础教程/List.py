#3.1 list函数
a=list('hello')
print(a)

#3.2 基本操作
#删除
del a[2]
print(a)

#改变列表，元素赋值
x=[1,2,3]
x[1]=4
print(x)

#分片赋值
b=list('Perl')
b[2:]='ar'
print(b)
numbers=[1,5]
numbers[1:1]=[2,3,4]
print(numbers)

#3.3列表方法
#1.append
c=[1,2,3]
c.append(4)
print(c)
#2.count
lis=[1,2,2,3,2,4,5,6,7,2]
print(lis.count(2))
#3.extend
a=[1,2,3]
b=[4,5,6]
a.extend(b)
print(a)
print(c+b)
print(c)
#4.index
a=[1,2,3,4,5,6,7,8]
print(a.index(5))
#5.insert
a.insert(3,'four')
print(a)
a[4:4]=['five']
print(a)
#6.pop
a=[1,2,3]
b=a.pop()
print(b)
print(a)
#7.remve(第一个匹配）
x=['to','be','or','not','to','be']
x.remove('be')
print(x)
#8.reverse
x=[1,2,3]
x.reverse()
print(x)
#9.sort(修改原数组并返回空值）
x=[4,2,5,3,8,7,1,9]
x.sort()
print(x)
y=x.sort()
print(y)
d=[4,1,3,2,9,7,8,6]
b=sorted(d)#sorted返回修改的值，原值不变
print(d)
print(b)
print(sorted('python'))
#10.高级排序
# print(cmp(32,22))
# print(cmp(22,32))
# print(cmp(22,22))  python3用operator模块代替
x=['xutao','xuleie','wangzhi','jeer']
x.sort(key=len)
print(x)
x=[9,5,1,7,3,8,2,6,4]
x.sort(reverse=True)
print(x)

#tuple函数
x=tuple('hello')
print(x)