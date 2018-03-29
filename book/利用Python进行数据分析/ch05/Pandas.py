
# coding: utf-8

# # Pandas

# # 一，Pandas的数据结构介绍

# ## 1，Series

# **定义：一组数据和一组索引组成**

# In[4]:

import pandas as pd
from pandas import Series,DataFrame


# **创建Series**

# In[5]:

obj=Series([4,5,-7,3])


# In[6]:

obj


# In[7]:

obj.values


# In[8]:

obj.index


# In[9]:

obj2=Series([1,3,4,5],index=['s','v','f','g'])


# In[10]:

obj2


# In[11]:

obj2.index


# In[12]:

obj2['s']


# In[13]:

obj2[['s','v']]
#多个值时用双中括号


# **numpy数组运算都会保留索引和值之间的链接**

# In[14]:

obj2[obj2>2]


# In[15]:

obj2*2


# In[16]:

import numpy as np


# In[17]:

np.exp(obj2)


# **Series可以看成一个定长有序字典，它可以用在原本需要字典参数的函数中**

# In[18]:

'v' in obj2


# In[19]:

'k' in obj2


# **先创建字典，再创建Series**

# In[20]:

sdata={'adf':234,'das':3456,'gjjrg':4345,'dfga':2435}


# In[21]:

obj3=Series(sdata)


# In[22]:

obj3


# In[23]:

state={'adf','das','dfga','jjg'}


# In[24]:

obj4=Series(sdata,index=state)


# In[25]:

obj4


# **NAN(非数字，即not a number，在pandas中，它表示缺失或NA值)，isnull参数或notnull参数可以检测缺失数据**

# In[26]:

pd.isnull(obj4)


# In[27]:

pd.notnull(obj4)


# In[28]:

obj4.isnull()


# **Series会在算术运算中自动对齐不同索引的数据**

# In[29]:

obj3


# In[30]:

obj4


# In[31]:

obj3+obj4


# **Series有个属性为name属性**

# In[32]:

obj4.name='pollution'


# In[33]:

obj4.index.name='state'


# In[34]:

obj4


# **索引可以通过赋值就地进行修改**

# In[35]:

obj4.index=['john','bob','tom','jerry']


# In[36]:

obj4


# ## 2，DataFrame

# **二维型表格数据，含有一组有序列，每列可以是不同的值类型（数值，字符串，布尔型）。既有行索引，也有列索引。**

# **创建DataFrame**

# In[37]:

data={'name':['Tom','Jerry','Jack','Ryu'],
       'age':[22,34,13,45,],
       'sex':['man','woman','man','man']}


# In[38]:

dataframe=DataFrame(data)
dataframe


# **columns指定列序列**

# In[39]:

dataframe=DataFrame(data,columns=['name','age','sex'])


# In[40]:

dataframe


# In[41]:

frame2=DataFrame(data,columns=['name','age','sex','address','phonenumber'],index=['one','two','three','four'])


# In[42]:

frame2


# In[43]:

frame2.columns


# In[44]:

frame2.name


# In[45]:

frame2.age


# In[46]:

frame2.phonenumber=13939934588


# In[47]:

frame2


# In[48]:

frame2['address']=['Tokyo','Londun','NewYork','Paris']


# In[49]:

frame2


# In[50]:

val=Series([1244,324,5145],index=['one','three','four'])


# In[51]:

frame2['phonenumber']=val


# In[52]:

frame2


# **创建新列，用del删除**

# In[53]:

frame2['bool']=frame2.name=='Tom'


# In[54]:

frame2


# In[55]:

del frame2['bool']


# In[56]:

frame2


# **嵌套字典，传给DataFrame，外层字典的键作为列，内层字典的键作为行**

# In[57]:

data={'Neveda':{2001:3.4,2002:34,2003:3.44},'Ohiio':{2001:23.3,2002:44.56,2003:234.32}}


# In[58]:

frame3=DataFrame(data)


# In[59]:

frame3


# **转置**

# In[60]:

frame3.T


# **可以用name给行标和列标定义名字**

# In[61]:

frame3.index.name='year'


# In[62]:

frame3.columns.name='state'


# In[63]:

frame3


# In[64]:

frame3.values


# In[65]:

frame2.values


# ## 3，索引对象

# In[66]:

obj=Series(range(3),index=['a','b','c'])


# In[67]:

index=obj.index


# In[68]:

index


# **Index对象不可修改**

# In[69]:

index[1]='d'


# In[70]:

import numpy as np


# In[71]:

index=pd.Index(np.arange(3))


# In[72]:

obj2=Series([2,3,4],index=index)


# In[73]:

obj2.index is index


# In[74]:

frame3


# In[75]:

'Ohiio' in frame3.columns


# In[76]:

2004 in frame3.index


# ### pandas中主要的index对象

# + Index：将轴标签表示成一个由Python对象组成的Numpy数组
# + Int64Index：针对整数
# + MultiIndex：“层次化”索引对象，表示单个轴上的多层索引。可看成由元组组成的数组
# + DatetimeIndex:储存纳秒级时间戳
# + PeriodIndex:针对period数据

# ### Index的方法和属性

# + append：连接另一个Index，产生一个新index
# + diff：计算差集，并得到一个新Index
# + intersection：计算交集
# + union：计算并集
# + isin：计算一个指示各值是否都在参数集合中的布尔型数据
# + delete：删除索引i处的元素，并得到一个新Index
# + drop:删除传入的值，并得到新Index
# + insert：将元素插入索引i处，并得到新Index
# + is_monotonic:当元素都大于前一元素时，返回True
# + is_union：当元素没有重复时，返回True
# + union：计算Index中唯一值得数组

# # 二，基本功能

# ## 1，重新索引

# In[77]:

obj=Series([2.3,4,5.66,35],index=['a','c','d','b'])


# In[78]:

obj


# reindex将会根据新索引进行重排

# In[79]:

obj2=obj.reindex(['a','b','c','d','e'])


# In[80]:

obj2


# In[81]:

obj2=obj.reindex(['a','b','c','d','e'],fill_value=0)


# In[82]:

obj2


# In[83]:

obj3=Series(['blue','yellow','red'],index=[0,2,4])


# In[84]:

obj3


# <a id='aaa'></a>
# ### method可以做一些插值处理

# * ffill或pad，前向填充（或搬运）值
# * bfill或backfill，后向填充（或搬运）值

# In[85]:

obj3.reindex(range(6),method='ffill')


# In[86]:

frame=DataFrame(np.arange(9).reshape((3,3)),index=['a','c','d'],columns=['Beijing','Shanghai','Tongling'])


# In[87]:

frame


# In[88]:

frame2=frame.reindex(['a','b','c','d'])


# In[89]:

frame2


# In[90]:

states=['Tongling','Shenzheng','Beijing']


# In[91]:

frame.reindex(columns=states)


# In[92]:

frame.reindex(index=['a','b','c','d'],method='ffill',columns=states)


# 利用标签索引功能ix，变得更简洁

# In[93]:

frame.reindex(['a','b','c','d'],columns=states)


# ### reindex函数的参数

# + fill_value:重新引用索引过程中，需要引入缺失值时使用的替代值
# + index：用在索引的新序列。可以是index实例，也可以是其他Python数据结构
# + [method](#aaa)：插值填充方式
# + copy:默认为True，无论如何都复制；如果为False，则新旧相等则不复制

# ## 2，丢弃指定轴上的项

# In[94]:

obj=Series(np.arange(5),index=('a','b','c','d','e'))


# In[95]:

obj


# In[96]:

new_obj=obj.drop('c')


# In[97]:

new_obj


# In[98]:

obj.drop(['d','c'])


# In[99]:

data=DataFrame(np.arange(16).reshape(4,4),columns=('one','two','three','four'),index=('beijing','shanghai','tianjing','chongqing'))


# In[100]:

data


# In[101]:

data.drop(['beijing','shanghai'])


# In[102]:

data.drop('two',axis=1)


# ## 3，索引，选取和过滤

# In[103]:

obj=Series(np.arange(4.),index=('a','b','c','d'))


# In[104]:

obj


# In[105]:

obj[1]


# In[106]:

obj['b']


# In[107]:

obj[2:4]


# In[108]:

obj[1:3]


# In[109]:

obj[['b','a','d']]


# In[110]:

obj[obj<2]


# **标签的切片运算包含最后一位**

# In[111]:

obj['a':'c']


# In[112]:

obj['a':'c']=5


# In[113]:

obj


# In[114]:

data


# In[115]:

data['two']


# In[116]:

data[:2]


# In[117]:

data[['two','one']]


# In[118]:

data[data['four']>7]


# In[119]:

data<5


# In[120]:

data[data<5]=0


# In[121]:

data


# In[122]:

data.ix['shanghai',['two','three']]


# In[123]:

data.ix[['shanghai','beijing'],[3,0,1]]


# In[124]:

data.ix[2]


# In[125]:

data.ix[:'chongqing','two']


# In[126]:

data.ix[data.three>5,:3]


# **DataFrame的索引选项**

# + obj[val]: **选取DataFrame的单个或一组列（布尔型数组，切片，布尔型DataFrame**
# + obj.ix[val]:**选取一行或一组行** 
# + obj.ix[:,val]:**选取单个列或列子集**
# + obj.ix[val,val]:**同时选取行和列**
# + reindex：**将一个或多个轴匹配到新索引**
# + xs:**根据标签选择单行或单列，并返回一个Series**
# + icol,irow:**根据整数位置选择单行或单列，并返回一个Series**
# + get_value,set_value:**根据行标签或列标签选择单个值**

# ## 4，算术运算和数据对齐

# In[127]:

s1=Series([4.2,4.6,12.3,7.5],index=['a','c','d','e'])


# In[128]:

s2=Series([5.2,6.3,6.2,8.4,7.5],index=['a','d','e','f','g'])


# In[129]:

s1


# In[130]:

s2


# In[131]:

s1+s2


# In[132]:

df1=DataFrame(np.arange(9.).reshape((3,3)),columns=list('bcd'),index=('j','h','d'))


# In[133]:

df2=DataFrame(np.arange(12.).reshape((4,3)),columns=list('bde'),index=('a','j','h','o'))


# In[134]:

df1


# In[135]:

df2


# In[136]:

df1+df2


# ## 5，在算术方法中填充值

# In[137]:

df1=DataFrame(np.arange(12.).reshape((3,4)),columns=list('abcd'))


# In[138]:

df2=DataFrame(np.arange(20.).reshape((4,5)),columns=list('abcde'))


# In[139]:

df1


# In[140]:

df2


# In[141]:

df1+df2


# In[142]:

df1.add(df2,fill_value=0)


# In[143]:

df1.reindex(columns=df2.columns,fill_value=0)


# + **add:加法**
# + **sub:减法**
# + **div:除法**
# + **mul:乘法**

# ## 6，DataFrame和Series之间的运算

# In[144]:

frame=DataFrame(np.arange(12.).reshape((3,4)),columns=list('bcde'),index=('jan','hfa','djj'))


# In[145]:

se=frame.ix[0]


# In[146]:

frame


# In[147]:

se


# In[148]:

frame-se


# In[149]:

se2=Series(np.arange(3),index=['b','d','f'])


# In[150]:

frame+se2


# In[151]:

se3=frame['b']


# In[152]:

se3


# In[153]:

frame.sub(se3,axis=0)


# ## 7,函数应用和映射 

# In[154]:

frame=DataFrame(np.random.randn(4,3),columns=list('bde'),index=('Utho','Ohio','Ehir','Hude'))


# In[155]:

frame


# In[156]:

np.abs(frame)


# In[157]:

f=lambda x:x.max()-x.min()


# In[158]:

frame=DataFrame(np.arange(9).reshape(3,3),columns=list('abc'),index=('U','b','d'))


# In[159]:

frame


# In[160]:

frame.apply(f)


# In[161]:

frame.apply(f,axis=1)


# In[162]:

def f(x):
    return Series([x.min(),x.max()],index=['min','max'])


# In[163]:

frame.apply(f)


# In[164]:

frame=DataFrame(np.random.randn(4,3),columns=list('bde'),index=('Utho','Ohio','Ehir','Hude'))


# In[165]:

frame


# In[166]:

format=lambda x:'%.2f' %x


# In[167]:

frame.applymap(format)


# In[168]:

frame['e'].map(format)


# ## 8，排序和排名

# In[169]:

obj=Series(range(4),index=['d','c','b','a'])


# In[170]:

obj.sort_index()


# In[171]:

frame=DataFrame(np.arange(8).reshape((2,4)),index=('two','one'),columns=('b','d','a','c'))


# In[172]:

frame.sort_index()


# In[173]:

frame.sort_index(axis=1)


# **默认升序，也可用降序**

# In[174]:

frame.sort_index(axis=1,ascending=False)


# **按值排列，用order**

# In[175]:

obj=Series([2,1,-5,0])


# In[176]:

obj


# In[177]:

frame=DataFrame({'b':[2,1,6,3],'a':[5,3,6,2]})


# In[178]:

frame.sort_index(by='b')


# In[179]:

frame.sort_index(by=['a','b'])


# In[180]:

obj=Series([6,-3,2,7,5])


# In[181]:

obj.rank ()


# In[182]:

obj.rank(method='first')


# In[183]:

obj.rank(ascending=False,method='max')


# In[184]:

frame=DataFrame({'a':[2,5,1,3,7],'b':[1,6,3,2,5],'c':[3,5,2,1,6]})


# In[185]:

frame


# In[186]:

frame.rank()


# In[187]:

frame.rank(axis=1)


# ### method选项

# + **average:默认，在相等排名中，为各个值分配平均排名**
# + **min：使用整个分组的最小排名**
# + **max：使用整个分组的最大排名**
# + **frist：按值在原始数据中的出现顺序分配排名**

# ## 9，带有重复值的轴索引

# In[188]:

obj=Series(range(5),index=('a','a','b','b','c'))


# In[189]:

obj


# **索引的is_unique属性判断是否唯一**

# In[190]:

obj.index.is_unique


# In[191]:

obj['a']


# In[192]:

obj['c']


# ## 10，汇总和计算描述统计 

# In[193]:

frame=DataFrame([[1,3],[np.nan,4],[np.nan,np.nan],[3,-4]],index=['a','b','c','d'],columns=['one','two'])


# In[194]:

frame


# In[195]:

frame.sum()


# In[196]:

frame.sum(axis=1)


# **NAN值自动排除，除非整个切片都是NAN。skipna可禁用**

# In[197]:

frame.sum(axis=1,skipna=False)


# In[198]:

frame.mean()


# **间接统计：返回最值得索引**

# In[199]:

frame.idxmax()


# 累计统计

# In[200]:

frame.cumsum()


# describe产生多个参数统计

# In[201]:

frame.describe()


# **对于非数值型数据。describe会产生另种统计**

# In[202]:

obj=Series(['a','a','b','v']*5)


# In[203]:

obj.describe()


# ![_auto_2](attachment:_auto_2)

# ![_auto_2](attachment:_auto_2)

# ## 11，相关系数和协方差 

# In[204]:

from pandas.io. import data 


# In[206]:

frame=DataFrame(np.random.randn(20).reshape([5,4]),index=['2009-12-24','2009-12-25','2009-12-26','2009-12-27','2009-12-28'],columns=['APPL','GOOG','IBM','MSFT'])


# In[207]:

frame.index.name='Date'


# In[208]:

frame


# **DataFrame的corr，cov将以DataFrame方法返回完整的相关系数或协方差方程.corrwith可计算其列或行跟另一Series或DataFrame间的相关系数**

# In[209]:

frame.corr()


# In[210]:

frame.cov()


# In[211]:

frame.corrwith(frame.IBM)


# ## 12，唯一值，值计数和成员资格

# In[212]:

obj=Series(['c','a','d','a','a','b','d','d','c'])


# In[213]:

obj


# In[215]:

obj.unique()


# **value_counts返回某值出现的频率,默认降序。还是一个顶级的pandas方法，可用于任何数组或序列**

# In[216]:

obj.value_counts()


# In[217]:

pd.value_counts(obj.values,sort=False)


# **isin;判断矢量化集合的成员资格**

# In[219]:

mask=obj.isin(['b','c'])


# In[220]:

mask


# In[222]:

obj[mask]


# ![_auto_0](attachment:_auto_0)

# In[225]:

data=DataFrame({'q1':[1,3,4,1,4],
                'q2':[2,4,5,3,2],
                'q3':[2,3,3,2,4]})


# In[226]:

data


# In[227]:

data.apply(pd.value_counts).fillna(0)


# ## 13，处理缺失数据

# In[228]:

string_data=Series(['adfadf','dafasdf','dffaf',np.nan])


# In[229]:

string_data


# In[230]:

string_data.isnull()


# **Python内置的None值也被当做NA处理**

# In[233]:

string_data[0]=None


# In[235]:

string_data.isnull()


# **NA处理方式**

# ![_auto_0](attachment:_auto_0)

# ## 14，虑除缺失数据

# In[236]:

from numpy import nan as NA


# In[237]:

data=Series([1,NA,3.5,NA,7])


# In[238]:

data


# In[239]:

data.dropna()


# In[244]:

frame=DataFrame([[1,3,NA,NA],
                 [2,4,NA,4],
                 [NA,NA,NA,NA],
                 [2,4,5,6]])


# In[245]:

frame


# **dropna默认丢弃含有NA的行**

# In[246]:

frame.dropna()


# **传入how='all'只会丢弃全是NA的行**

# In[249]:

frame.dropna(how='all')


# In[250]:

frame[4]=NA


# In[251]:

frame


# In[252]:

frame.dropna(axis=1,how='all')


# In[253]:

df=DataFrame(np.random.randn(7,3))


# In[254]:

df


# In[257]:

df.ix[:4,1]=NA;
df.ix[:2,2]=NA


# In[258]:

df


# In[265]:

df.dropna(thresh=3)


# **thresh等于x就保留所有含x个非空值的行**

# ## 15，填充缺失数据

# **fillna为常用函数，通过一个常数调用fillna函数就会以常数填充缺失值**

# In[266]:

df.fillna(0)


# **通过字典调用就会实现对不同的列填充不同的值**

# In[269]:

df.fillna({1: 0.5,2: 2})


# **fillna默认返回新对象，但也可以对现有对象进行修改**

# In[270]:

_=df.fillna(0,inplace=True)


# In[271]:

df


# In[272]:

df=DataFrame(np.random.randn(6,3))


# In[273]:

df


# In[279]:

df.ix[2:,1]=NA;
df.ix[4:,2]=NA


# In[280]:

df


# In[282]:

df.fillna(method='ffill')


# In[283]:

df.fillna(method='ffill',limit=2)


# In[284]:

obj=Series([1,NA,4.4,NA,5])


# In[285]:

obj


# In[286]:

obj.fillna(obj.mean())


# ![_auto_1](attachment:_auto_1)

# ![_auto_0](attachment:_auto_0)

# # 五，层次化索引

# **一个轴上拥有多个索引级别**

# In[287]:

data=Series(np.random.randn(10),index=[['a','a','a','b','b','c','c','c','d','d'],
                                       [1,2,3,1,2,1,2,3,2,3]])


# In[289]:

data


# In[290]:

data.index


# In[291]:

data['b']


# In[292]:

data['a':'c']


# In[295]:

data[['a','c']]


# **在内层进行选取**

# In[297]:

data[:,2]


# **层次化索引在数据重塑和基于分组的操作（如透视表生成）有重要作用**

# 上面数据可以用unstack方法重新安排到一个DataFrame中。逆运算是stack

# In[299]:

data.unstack()


# In[300]:

data.unstack().stack()


# 对于DataFrame，每条轴都可以有索引

# In[335]:

frame=DataFrame(np.arange(12).reshape(4,3),
                index=[['a','a','b','b'],[1,2,1,2]],
                columns=[['jack','jack','tom'],[1,2,1]])


# In[336]:

frame


# **各层都可有名字，注意names**

# In[337]:

frame.index.names=['key1','key2']


# In[338]:

frame.columns.names=['state','number']


# In[339]:

frame


# In[340]:

frame['jack']


# ## 1，重排分级排序

# **swaplevel接受两个级别编号或名称，并返回一个互换了级别的新对象（数据不变）**

# In[341]:

frame.swaplevel('key1','key2')


# **sortlevel会根据单个级别中的值对数据进行排序（稳定）**

# In[342]:

frame.sortlevel(1)


# In[343]:

frame.swaplevel(0,1).sortlevel(0)


# ## 2，根据级别进行汇总统计

# **level指定某条轴上的求和级别**

# In[344]:

frame.sum(level='key2')


# In[345]:

frame.sum(level='number',axis=1)


# ## 3,使用DataFrame的列

# In[346]:

frame=DataFrame({'a':range(7),
                 'b':range(7,0,-1),
                 'c':['one','one','one','two','two','two','two'],
                 'd':[0,1,2,0,1,2,3]})


# In[347]:

frame


# **set_index会将一个或多个列转换成行索引**

# In[351]:

frame2=frame.set_index(['c','d'])


# In[352]:

frame2


# **默认下，那些列被删除，但也可以保存下来**

# In[350]:

frame.set_index(['c','d'],drop=False)


# **reser_index()功能正好和set_index()相反**

# In[354]:

frame2.reset_index()


# # 六，其他有关Pandas的话题

# ## 1,整数索引

# In[356]:

ser=Series(np.arange(3.))


# In[359]:

ser


# **ser[-1]显示错误，对于非整数索引则没错**

# In[360]:

ser=Series(np.arange(3.),index=['a','b','c'])


# In[361]:

ser[-1]


# In[363]:

ser.ix[:1]


# **iget_value,irow,icol是可靠的，不考虑索引类型的，基于位置的索引**

# In[364]:

ser3=Series(np.arange(3.),index=[-5,1,2])


# In[365]:

ser3


# In[369]:

#  ser3.iget_value(2),python3没有该属性


# In[370]:

frame=DataFrame(np.arange(6.).reshape(3,2),index=[2,0,1])


# In[371]:

frame


# In[373]:

# frame.irow(2)，DataFrame也没有该属性


# ## 2，面板数据

# 看书

# 
