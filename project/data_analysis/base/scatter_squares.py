# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 02:18:20 2018

@author: 徐涛
"""

import matplotlib.pyplot as plt

# x = [1,2,3,4,5]
# y = [1,4,9,16,25]
x = list(range(1,1001))
y = [ i**2 for i in x]
# plt.scatter(x,y,s=40)
# plt.scatter(x,y,edgecolor='none',s=40)
# plt.scatter(x,y,c=(0,0,0.8),edgecolor='none',s=40)
plt.scatter(x,y,c=y,cmap=plt.cm.Blues,edgecolor='none',s=40)
# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both',which='major',labelsize=14)

# 设置每个坐标轴的取值范围
plt.axis([0,1100,0,1100000])
# plt.show()
plt.savefig('squares_plot.png',bbox_inches='tight')