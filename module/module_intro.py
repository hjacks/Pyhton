# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 18:03:57 2017

@author: Administrator
"""

import sys
sys.path.append('C:/Users/Administrator/Desktop')
import hello
hello.hello()

# 在主程序中，__name__的值是__main__，在导入的模块中是模块名
print(__name__)
print(hello.__name__)

def hello4():
    print('hhhh')

def test():
    print('This is test demo')

if __name__=='__main__':test()

#查看模块的存放地址
import pprint
pprint.pprint(sys.path)


# 2.1 模块中有什么
# 1 使用dir
import copy
print(dir(copy))
print([n for n in dir(copy) if not n.startswith('_')])

# 2 all变量
print(copy.__all__)
# 使用 from copy import * 代码，就只能使用all中的3个函数，使用其他的就得显示引入
 
# 2.2 使用help
help(copy.copy)

#2.3 文档
print(range.__doc__)

#2.4 阅读源代码
print(copy.__file__) #得到copy模块源代码地址

# 3 标准库
# 3.1 sys
# sys中一些重要函数和变量
# argv           命令行参数，包括脚本名称
# exit([arg])    退出当前程序，可选参数为给定的返回值或错误信息
# modules        映射模块名字到载入模块的字典
# path           查找模块所在目录的目录名列表
# platform       类似sunos5或win32的平台标识符
# stdin          标准输入流----一个类文件对象
# stdout         标准输出流----一个类文件对象
# stderr         标准错误流----一个类文件对象

#反序打印命令行参数
import sys
arg=sys.argv[1:]
arg.reverse()
print(' '.join(arg))

# 3.2 os
# os中一些重要函数和变量
# environ         对于环境变量进行映射
# system(command) 在子shell中执行操作系统命令
# sep             路径中的分隔符
# pathsep         分隔路径的分隔符
# linesep         行分隔符（\n,\r,\r\n）
# urandom(n)      返回n字节的加密强随机数据


#3.3 fileinput
#input([files[,inplace[,backup]]])   #便于遍历多个输入流的行
#filename          返回当前文件的名称
#lineno            返回当前（累计）的行数
#isfristline       查询当前行是否是文件的第一行
#isstdin           检测最后一行是否来自s'y'ssys