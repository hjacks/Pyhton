#文件和模式
#1.打开文件
#open(name[,module[,buffering]])
f=open('txt.txt','r')
print(f.read(1))
#1.1模式
#r------读模式
#w------写模式
#a------追加模式
#b------二进制模式（可添加到其他模式中使用）
#+------读写模式（可添加到其他模式中使用）
#2.基本文件方法
#2.1.读和写
f=open('somefile.txt','w')
f.write('hello,')
f.write('world!')
f.close()
f=open('somefile.txt','r')
#数字代表读多少字符，第二次读完剩下的
print(f.read(4))
print(f.read())
#2.2.管式输出
# import sys
# text=sys.stdin.read()
# words=text.split()
# wordcount=len(words)
# print('wordcount:',wordcount)
#2.3.读写行
#file.readlines:读取单独一行(直到换行符的出现，包括这个换行符)，不使用
#参数（读取完整一行）或使用完整参数作为读取的字符的最大值
#writellines:传给它一个字符串列表，他会把所有字符串写入文件。
#2.4.关闭文件
#open your file here
#try:
#    write data to your file
#finally:
#    file.close()

#with open('somefile.txt') as somefile:
#   do_something(some_file)
#

#2.5.使用基本文件方法
f=open('somefile1.txt')
print(f.read(7))
print(f.read(4))
f.close()
f=open('somefile1.txt')
print(f.read())
f.close()
f=open('somefile1.txt')
print(f.readlines())
f.close()

import pprint
pprint.pprint(open('somefile1.txt').readlines())
f.close()

f=open('somefile2.txt')
lines=f.readlines()
print(lines)
f.close()
lines[1]='is not a\n'
f=open('somefile2.txt','w')
f.writelines(lines)
f.close()
f=open('somefile2.txt')
print(f.read())
f.close()

#3.对文件内容进行迭代
#process函数,用来表示每个字符或每行的处理过程
def process(string):
    print('Processing:',string)
#3.1.按字节处理
#用read方法对每个字符进行循环
f=open('somefile.txt')
char=f.read(1)
while char:
    process(char)
    char=f.read(1)
f.close()
#用不同方式写循环
f=open('somefile.txt')
while True:
    char=f.read(1)
    if not char:
        break
    process(char)
f.close()
#3.2.按行操作
f=open('somefile1.txt')
while True:
    line=f.readline()
    if not line:
        break
    process(line)
f.close()
#3.3.读取所有内容
#用read迭代所有内容
f=open('somefile2.txt')
for char in f.read():
    process(char)
f.close()
#用readlines迭代行
f=open('somefile1.txt')
for line in f.readlines():
    process(line)
f.close()
#3.4.使用fileinput实现懒惰行迭代
import fileinput
for line in fileinput.input('somefile1.txt'):
    process(line)
#3.5.文件迭代器
#迭代文件
f=open('somefile2.txt')
for line in f:
    process(line)
f.close()
#对文件进行迭代，而不使用变量存储文件对象
for line in open('somefile2.txt'):
    process(line)
f.close()
#迭代标准输入中的所有行
# import  sys
# for line in sys.stdin:
#     process(line)

f=open('somefile3.txt','w')
f.write('first line\n')
f.write('second line\n')
f.write('third line\n')
f.close()
lines=list(open('somefile3.txt'))
print(lines)
a,b,c=open('somefile3.txt')
print(a)
print(b)
print(c)




