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