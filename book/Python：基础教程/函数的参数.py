# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 15:32:12 2017

@author: Administrator
"""

# 1.位置参数
def power(x):
    return x*x

print(power(5))

def power1(x,n):
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s

print(power1(5,5))

# 2.默认参数