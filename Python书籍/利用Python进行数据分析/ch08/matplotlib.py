
# coding: utf-8

# # 一，matplotlib API入门

# In[353]:

import numpy as np


# In[354]:

import pandas as pd


# In[355]:

import matplotlib.pyplot as plt


# ## 1，Figure和Subplot

# matplotlib的图像都位于Figure对象中

# In[356]:

fig=plt.figure()


# In[357]:

ax1=fig.add_subplot(2,2,1)


# In[358]:

ax2=fig.add_subplot(2,2,2)


# In[359]:

ax3=fig.add_subplot(2,2,3)


# In[360]:

from numpy.random import randn


# In[361]:

plt.plot(randn(50).cumsum(),'k--') #"k--"是一个线型选项，用于告诉matplotlib绘制黑色虚线图


# In[362]:

_=ax1.hist(randn(100),bins=20,color='k',alpha=0.3)


# In[363]:

ax2.scatter(np.arange(30),np.arange(30)+3*randn(30))


# In[364]:

plt.show()


# In[365]:

fig,axes=plt.subplots(2,3)


# In[366]:

axes


# ![_auto_0](attachment:_auto_0)

# ## 2，调整subplot周围的间距

# In[367]:

# fig.subplots_adjust(left=None,bottom=None,right=None,top=None,wspace=None,hspace=None)


# In[368]:

fig,axes=plt.subplots(2,2,sharex=True,sharey=True)


# In[369]:

for i in range(2):
    for j in range(2):
        axes[i,j].hist(randn(500),bins=50,color='k',alpha=0.5)


# In[370]:

plt.subplots_adjust(wspace=0,hspace=0)


# In[371]:

plt.show()


# ## 3，颜色、标记和线型

# In[372]:

plt.plot(randn(30).cumsum(),'ko--')
plt.show()


# In[373]:

plt.plot(randn(30).cumsum(),color='m',linestyle=':',marker='>')
plt.show()


# ![_auto_0](attachment:_auto_0)

# ![_auto_0](attachment:_auto_0)

# ![_auto_0](attachment:_auto_0)

# In[374]:

data=randn(30).cumsum()


# In[375]:

plt.plot(data,'c--',label='Default')
plt.show()


# In[376]:

plt.plot(data,'k-',drawstyle='steps-post',label='steps-post')
plt.show()


# ## 4，刻度，标签和图例

# 大多数图表装饰项，实现方式：1，使用过程型的pyplot接口；2，面向对象的原生matplotlib API

# pyplot接口含有诸多方法，使用方式有：
# + 调用时不带参数，则返回当前参数值。
# + 调用时带参数，则设置参数值。

# ### 设置标题、轴标签、刻度以及刻度标签

# In[377]:

fig=plt.figure()


# In[378]:

ax=fig.add_subplot(1,1,1)


# In[379]:

ax.plot(randn(1000).cumsum())


# set_xticks将刻度放置在数据范围的哪些位置。set_xticklabels是前者值得刻度标签。set_xlabel设置X轴名字。对于Y轴，将前面的x改为y。set_title设置表格名称

# In[380]:

ticks=ax.set_xticks([0,250,500,750,1000])


# In[381]:

labels=ax.set_xticklabels(['one','two','three','four','five'],rotation=30,fontsize='small')


# In[382]:

ax.set_title('My first matplotlib plot')


# In[383]:

ax.set_xlabel('Stages')


# In[384]:

plt.show()


# ### 添加图例

# 图例（legend）是另一种用于标识图表元素的重要工具

# 可以在添加subplot时传入label参数来添加图例

# In[385]:

fig=plt.figure()


# In[386]:

ax=fig.add_subplot(1,1,1)


# In[387]:

ax.plot(randn(1000).cumsum(),'k--',label='one')
plt.show()


# In[388]:

ax.plot(randn(1000).cumsum(),'k-',label='two')
plt.show()


# In[389]:

ax.plot(randn(1000).cumsum(),'m.',label='three')
plt.show()


# In[390]:

ax.legend(loc='best')


# ## 5，注解以及在Subplot上绘图

# In[391]:

from datetime import datetime


# In[392]:

fig=plt.figure()


# In[393]:

ax=fig.add_subplot(1,1,1)


# In[394]:

data=pd.read_csv('D:/PythonDataAnalysis/ch08/spx.csv',index_col=0,parse_dates=True)


# In[395]:

data


# In[396]:

spx=data['SPX']


# In[397]:

spx.plot(ax=ax,style='k-')


# In[398]:

crisis_data=[
    (datetime(2007,10,11),'Peak of bull market'),
    (datetime(2008,3,12),'Bear Stearns Fails'),
    (datetime(2008,9,15),'Lehman Bankruptcy')
]


# In[399]:

for date,label in crisis_data:
    ax.annotate(label,xy=(date,spx.asof(date)+50),
                xytext=(date,spx.asof(date)+200),
                arrowprops=dict(facecolor='black'),
                horizontalalignment='left',
                verticalalignment='top')


# In[400]:

ax.set_xlim(['1/1/2007','1/1/2001'])


# In[401]:

ax.set_ylim([600,1800])


# In[402]:

ax.set_title('Important date in 2008-2009 financial crisis')


# **绘制图形（patch）**

# In[403]:

fig=plt.figure()


# In[404]:

ax=fig.add_subplot(1,1,1)


# In[405]:

rect=plt.Rectangle((0.2,0.75),0.4,0.15,color='k',alpha=0.3)


# In[406]:

circ=plt.Circle((0.7,0.2),0.15,color='b',alpha=0.3)


# In[407]:

pgon=plt.Polygon([[0.15,0.15],[0.35,0.4],[0.2,0.6]],color='g',alpha=0.5)


# In[408]:

ax.add_patch(rect)


# In[409]:

ax.add_patch(circ)


# In[410]:

ax.add_patch(pgon)


# In[411]:

plt.show()


# ## 5，将图表保存到文件

# plt.savefig可以将当前图表保存到文件。该方法相当于Figure对象的实例方法savefig

# In[412]:

plt.savefig('figpath.svg')


# 图片有两个重要选项：dpi（控制“每英寸点数”分辨率）和bbox_inches(可以剪除当前图表周围的空白部分）

# In[413]:

plt.savefig('figpath.png',dpi=400,bbox_inches='tight')


# savefig不仅可以写入磁盘，也可以写入任何文件类型的对象，比如（StringIO）

# In[414]:

from io import StringIO


# In[415]:

buffer=StringIO()


# In[416]:

# plt.savefig(buffer)


# In[417]:

plot_data=buffer.getvalue()


# ![_auto_0](attachment:_auto_0)

# ## 6，matplotlib配置 

# 操作matplotlib配置系统的方式主要有两种。第一种是Python编程方式，即利用rc方法。比如将全局的图像默认大小设置为10*10

# In[418]:

plt.rc('figure',figsize=(10,10))


# rc第一个参数是希望自定义的对象，如‘figure’、‘axes’、‘xtick’、‘ytick’、‘grid’、‘legend’等

# In[419]:

font_options={'family':'monospace',
              'weight':'bold',
              'size':'big'}


# In[420]:

# plt.rc('font',**font_options)


# # 二，pandas中的绘图函数

# ## 1，线型图 

# In[421]:

from pandas import Series,DataFrame


# In[422]:

s=Series(np.random.randn(10).cumsum(),index=np.arange(0,100,10))


# In[423]:

s


# In[424]:

s.plot()
plt.show()


# In[425]:

df=DataFrame(np.random.randn(10,4).cumsum(0),
             columns=['A','B','C','D'],
             index=np.arange(0,100,10))


# In[426]:

df.plot()
plt.show()


# ![_auto_0](attachment:_auto_0)

# ![_auto_0](attachment:_auto_0)

# ![_auto_0](attachment:_auto_0)

# ## 2，柱状图

# 在代码中加上kind='bar',(垂直柱状图）或kind='barh'(水平柱状图）即可生成柱状图

# In[427]:

fig,axes=plt.subplots(2,1)


# In[428]:

data=Series(np.random.rand(16),index=list('abcdefghigklmnop'))


# In[429]:

data


# In[430]:

data.plot(kind='bar',ax=axes[0],color='g',alpha=0.7)


# In[431]:

data.plot(kind='barh',ax=axes[1],color='k',alpha=0.7)


# In[432]:

plt.show()


# In[433]:

df=DataFrame(np.random.rand(6,4),
             index=['one','two','three','four','five','six'],
             columns=pd.Index(['A','B','C','D'],name='Genus'))


# In[434]:

df


# In[435]:

df.plot(kind='bar')
plt.show()


# 设置stacked=True即可为DataFrame生成堆积柱状图

# In[436]:

df.plot(kind='barh',stacked=True,alpha=0.5)
plt.show()


# In[437]:

tips=pd.read_csv('D:/PythonDataAnalysis/ch08/tips.csv')


# In[438]:

tips


# In[446]:

party_counts=pd.crosstab(tips.day,tips.size)


# In[455]:

party_counts=DataFrame({1:[1,2,0,1],
                        2:[16,53,39,48],
                        3:[1,18,15,4],
                        4:[1,13,18,5],
                        5:[0,1,3,1],
                        6:[0,0,1,3]},
                       index=['fri','sat','sun','thur'])


# In[456]:

party_counts.index.name='day'
party_counts.columns.name='size'


# In[457]:

party_counts


# In[458]:

party_counts=party_counts.ix[:,2:5]


# 规格化，使得各行为1（必须转换为浮点数）

# In[459]:

party_pcts=party_counts.div(party_counts.sum(1).astype(float),axis=0)


# In[460]:

party_pcts


# In[462]:

party_pcts.plot(kind='bar',stacked=True)
plt.show()


# ## 3，直方图和密度图

# 直方图是一种对值频率进行离散化显示的柱状图。数据点被拆分到离散的，间隔均匀的面元中，绘制的是各面元中数据点的数量

# In[463]:

tips['tip_pct']=tips['tip']/tips['total_bill']


# In[468]:

tips['tip_pct'].hist(bins=50)
plt.show()
# y轴是个数，x轴是百分比


# hist():画直方图,有许多参数

# + x : (n,) array or sequence of (n,) arrays-----这个参数是指定每个bin(箱子)分布的数据,对应x轴
# + bins : integer or array_like, optional------这个参数指定bin(箱子)的个数,也就是总共有几条条状图
# + normed : boolean, optional------这个参数指定密度,也就是每个条状图的占比例比,默认为1
# + color : color or array_like of colors or None, optional------这个指定条状图的颜色

# 密度图是通过计算“可能会产生观测数据的连续概率分布的估计”而产生的。一般是将该分布近似为一组核（如正态（高斯）分布）。因此也被称作KDE图。调用plot时加上kind=kde即可生成密度图（标准混合正态分布KDE）

# In[470]:

tips['tip_pct'].plot(kind='kde')
plt.show()


# In[471]:

comp1=np.random.normal(0,1,size=200)  # N(0,1)


# In[475]:

comp2=np.random.normal(10,2,size=200)  # N(10,2)


# In[476]:

values=Series(np.concatenate([comp1,comp2]))


# In[478]:

values.hist(bins=100,alpha=0.3,color='m',normed=True)


# In[479]:

values.plot(kind='kde',style='k--')


# In[480]:

plt.show()


# ## 4，散布图 

# 散布图可观测两个一维数据序列之间的关系。matplotlib中的scatter是绘制散布图的主要方法。

# In[482]:

macro=pd.read_csv('D:/PythonDataAnalysis/ch08/macrodata.csv')


# In[483]:

data=macro[['cpi','m1','tbilrate','unemp']]


# In[484]:

trans_data=np.log(data).diff().dropna()


# In[485]:

trans_data[-5:]


# In[486]:

plt.scatter(trans_data['m1'],trans_data['unemp'])


# In[487]:

plt.title('Changes in log %s vs. log %s' % ('m1','unemp'))


# In[488]:

plt.show()


# 一组散布图被称作散布矩阵，pandas提供了一个能从DataFrame创建散布图矩阵的scatter_matrix函数，它还支持在对角线上放置各变量的直方图或密度图

# In[490]:

pd.scatter_matrix(trans_data,diagonal='kde',color='k',alpha=0.3)
plt.show()


# # 三，绘制地图：图形化显示海地地震危机数据

# In[492]:

data=pd.read_csv('D:/PythonDataAnalysis/ch08/Haiti.csv')


# In[493]:

data


# 提取时间，经度和维度

# In[494]:

data[['INCIDENT DATE','LATITUDE','LONGITUDE']][:10]


# CATEGORY字段含有一组以逗号分隔的代码，这些代码表示消息的类型

# In[495]:

data['CATEGORY'][:6]


# 调用describe能发现数据中存在一些异常的地理位置

# In[497]:

data.describe()


# 清除错误位置信息并移除缺失分类信息

# In[498]:

data=data[(data.LATITUDE>18)&(data.LATITUDE<20)&(data.LONGITUDE>-75)&(data.LONGITUDE<-70)&data.CATEGORY.notnull()]


# 对数据进行规整化处理：一是获取所有分类的列表，二是将各个分类信息拆分为编码和英语名称

# In[527]:

def to_cat_list(catstr):
    stripped=(x.strip() for x in catstr.split(','))
    return [x for x in stripped if x]


# In[528]:

def get_all_categories(cat_series):
    cat_sets=(set(to_cat_list(x)) for x in cat_series)
    return sorted(set.union(*cat_sets))


# In[529]:

def get_english(cat):
    code,names=cat.split('.')
    if '|' in names:
        names = names.split('|')[1]
    return code,names.strip()


# 测试一下get_english函数

# In[530]:

get_english('2. Urgeences logistiquew | Vital Lines')


# 接下来做一个将编码和名称映射起来的字典

# In[531]:

all_cats=get_all_categories(data.CATEGORY)


# In[532]:

# 生成器表达式


# In[534]:

english_mapping=dict(get_english(x) for x in all_cats)


# In[535]:

english_mapping['2a']


# In[536]:

english_mapping['6c']


# 根据分类选取记录的方式很多，其一是添加指标（或哑变量）列，每个分类一列。为此，我们首先抽取出唯一的分类编码，并构造出一个常用的全零的DataFrame（列为分类编码，索引和data的索引一样）

# In[537]:

def get_code(seq):
    return [x.split('.')[0] for x in seq if x]


# In[538]:

all_codes=get_code(all_cats)


# In[539]:

code_index=pd.Index(np.unique(all_codes))


# In[540]:

dummy_frame=DataFrame(np.zeros((len(data),len(code_index))),index=data.index,columns=code_index)


# In[541]:

dummy_frame.ix[:,:6]


# In[542]:

for row,cat in zip(data.index,data.CATEGORY):
    codes=get_code(to_cat_list(cat))
    dummy_frame.ix[row,codes]=1


# In[543]:

data=data.join(dummy_frame.add_prefix('category'))


# In[544]:

data.ix[:,10:15]


# basemap工具集能够用python在地图上绘制2D数据，basemap提供了许多不同的地球投影以及一种将地球上的经纬度坐标投影转换为二维matplotlib图的方式

# In[546]:

from mpl_toolkits.basemap import Basemap


# In[ ]:



