
# coding: utf-8

# 本章概要：
# + 根据一个或多个键（函数、数组或DataFrame列名）拆分pandas对象
# + 计算分组概要统计，如计数、平均值、标准差，或用户自定义函数
# + 对DataFrame的列应用各种各样的函数
# + 应用组内转换或其他运算，如规格化、线性回归、排名或选取子集等
# + 计算透视表或交叉表
# + 执行分位数以及其他分组分析

# # GroupBy技术

# ![_auto_0](attachment:_auto_0)

# 分组键形式和类型都不必相同：
# + 列表或数组，其长度与待分组的轴一样
# + 表示DataFrame某个列名的值
# + 字典或Series，给出待分组轴上的值与分组名之间的对应关系
# + 函数，用于处理轴索引或索引中的各个标签

# In[2]:

import pandas as pd
import numpy as np
from pandas import Series,DataFrame


# In[3]:

df=DataFrame({'key1':['a','a','b','b','a'],
              'key2':['one','two','one','two','one'],
              'data1':np.random.randn(5),
              'data2':np.random.randn(5)})


# In[4]:

df


# In[5]:

grouped=df['data1'].groupby(df['key1'])


# In[6]:

grouped


# In[7]:

grouped.mean()


# In[8]:

means=df['data1'].groupby([df['key1'],df['key2']]).mean()


# In[9]:

means


# In[10]:

means.unstack()


# In[11]:

states=np.array(['Ohio','California','California','Ohio','Ohio'])


# In[12]:

years=np.array([2005,2005,2006,2005,2006])


# In[13]:

df['data1'].groupby([states,years]).mean()


# In[14]:

df.groupby('key1').mean()


# In[15]:

df.groupby(['key1','key2']).size()


# ## 1，对分组进行迭代 

# GroupBy对象支持迭代，可产生一组二元元组(由分组名和数据块组成）

# In[16]:

for name,group in df.groupby('key1'):
    print (name)
    print (group)


# In[17]:

for (k1,k2),group in df.groupby(['key1','key2']):
    print(k2,k1)
    print(group)


# In[18]:

for (k1,k2),group in df.groupby(['key1','key2']):
    print(k1,k2)
    print(group)


# In[19]:

pieces=dict(list(df.groupby('key1')))


# In[20]:

pieces['b']


# In[21]:

pieces['a']


# In[22]:

df.dtypes


# In[23]:

grouped=df.groupby(df.dtypes,axis=1)


# In[24]:

dict(list(grouped))


# ## 2，选取一个或一组列

# 对应GroupBy对象，用一个（单个字符串）或一组（字符串数组）列名对其进行索引来实现选取部分列进行聚合的目的

# In[25]:

df.groupby('key1')['data1']
df.groupby('key1')[['data2']]


# 是以下代码的语法糖：

# In[26]:

df['data1'].groupby(df['key1'])
df[['data2']].groupby(df['key1'])


# In[27]:

df.groupby(['key1','key2'])['data2'].mean()


# In[28]:

df.groupby(['key1','key2'])[['data2']].mean()


# ## 3，通过字典或Series进行分组

# In[29]:

people=DataFrame(np.random.randn(5,5),
                 columns=['a','b','c','d','e'],
                 index=['Joe','Steve','Wes','Jim','Travis'])


# In[30]:

people


# In[31]:

people.ix[2:3,['c','b']]=np.nan


# In[32]:

people


# In[33]:

mapping={'a':'red','b':'red','c':'blue','d':'blue','e':'red','f':'orange'}


# In[34]:

by_column=people.groupby(mapping,axis=1)


# In[35]:

by_column.sum()


# In[36]:

map_series=Series(mapping)


# In[37]:

map_series


# In[38]:

people.groupby(map_series,axis=1).count()


# ## 4，通过函数进行分组

# In[39]:

people


# 任何被当做分组键的函数都会在各个索引值上被调用一次，其返回值被用作分组名称

# In[40]:

people.groupby(len).sum() # 根据人民的长度进行分组


# In[41]:

key_list=['one','one','one','two','two']


# In[42]:

people.groupby([len,key_list]).min()


# ## 5，根据索引级别分组

# 层次化索引能根据索引级别进行聚合。对此，可通过level关键字传入级别编号或名称

# In[43]:

columns=pd.MultiIndex.from_arrays([['US','US','US','JP','JP'],[1,3,5,1,3]],names=['cty','tenor'])


# In[44]:

hier_df=DataFrame(np.random.randn(4,5),columns=columns)


# In[45]:

hier_df


# # 二，数据聚合

# In[46]:

df


# In[47]:

grouped=df.groupby('key1')


# In[48]:

grouped['data1'].quantile(0.9) # quantile可以计算Series和DataFrame的样本分位数


# 要使用自己的聚合函数，只需传入aggregate或agg方法即可：

# In[49]:

def peak_to_peak(arr):
    return arr.max()-arr.min()


# In[50]:

grouped.agg(peak_to_peak)


# In[51]:

grouped.describe()


# ![_auto_0](attachment:_auto_0)

# In[52]:

tips=pd.read_csv('D:/PythonDataAnalysis/ch08/tips.csv')


# In[53]:

tips


# In[54]:

# 添加“小费占总额百分比”
tips['tip_pct']=tips['tip']/tips['total_bill']


# In[55]:

tips[:6]


# ## 1，面向列的多函数应用

# In[56]:

grouped=tips.groupby(['sex','smoker'])


# In[57]:

grouped_pct=grouped['tip_pct']


# In[58]:

grouped_pct.agg('mean')


# In[59]:

grouped_pct.agg(['mean','std',peak_to_peak])
# 主要函数和函数名的区别


# 若传入的是（name,function）元组组成的列表，则各元组的第一个元素就会被用作DataFrame的列名:

# In[60]:

grouped_pct.agg([('foo','mean'),('bar',np.std)])


# 对于DataFrame，可以定义一组应用于全部列的函数，或不同列应用不同的函数

# In[61]:

funs=['count','mean','max']


# In[62]:

result=grouped['tip_pct','total_bill'].agg(funs)


# In[63]:

result


# In[64]:

result['tip_pct']


# In[65]:

ftuples=[('Durchschnitt','mean'),('Abweichung',np.var)]


# In[66]:

grouped['tip_pct','total_bill'].agg(ftuples)

若对不同的列应用不同函数，方法是向agg传入一个从列名映射到函数的字典
# In[67]:

grouped.agg({'tip':np.max,'size':'sum'})


# In[68]:

grouped.agg({'tip_pct':['min','max','mean','std'],'size':'sum'})


# ## 2，以“无索引”形式返回聚合数据

# In[69]:

tips.groupby(['sex','smoker'],as_index=False).mean()


# # 三，分组即运算和转换 

# 本节提供transform和apply方法执行其他的分组操作

# 若为一个DataFrame添加一个用于存放各索引分组平均值得列，可以先聚合在合并

# In[73]:

df


# In[77]:

k1_means=df.groupby('key1').mean().add_prefix('mean_')


# In[78]:

k1_means


# In[80]:

pd.merge(df,k1_means,left_on='key1',right_index=True)


# In[81]:

key=['one','two','one','two','one']


# In[84]:

people


# In[85]:

people.groupby(key).mean()


# In[86]:

people.groupby(key).transform(np.mean)


# transform将一个函数应用到各个分组，然后将结果放置到适当的位置上

# In[87]:

def demean(arr):
    return arr-arr.mean()


# In[88]:

demeaned=people.groupby(key).transform(demean)


# In[89]:

demeaned


# In[91]:

demeaned.groupby(key).mean()


# ## 1，apply：一般性的“拆分-应用-合并”

# transform函数有着严格限制条件，传入函数只能产生：1，一个广播的标量值（np.mean）。2，一个相同大小的结果数组。

# 最一般话GroupBy方法是apply，apply会将待处理的对象拆分成许多片段，然后对各片段调用传入的函数，最后尝试将各片段组合到一起

# In[94]:

tips


# In[92]:

def top(df,n=5,columns='tip_pct'):
    return df.sort_index(by=columns)[-n:]


# In[93]:

top(tips,n=6)


# In[95]:

tips.groupby('smoker').apply(top)


# In[96]:

tips.groupby(['smoker','day']).apply(top,n=1,columns='total_bill')


# In[97]:

result=tips.groupby('smoker')['tip_pct'].describe()


# In[98]:

result


# In[101]:

result.unstack('smoker')


# ## 2，禁止分组键

# 传入group_keys=False即可禁止将分组键跟原始对象的索引共同构成结果对象中的层次化索引

# In[102]:

tips.groupby('smoker',group_keys=False).apply(top)


# ## 3，分位数和桶分析

# 将cut和qcut等函数跟GroupBy集合起来，就能实现对数据集的桶或分位数分析了

# In[104]:

frame=DataFrame({'data1':np.random.randn(1000),'data2':np.random.randn(1000)})


# In[105]:

frame


# In[106]:

factor=pd.cut(frame.data1,4)


# In[107]:

factor[:10]


# In[108]:

def get_stats(group):
    return {'min':group.min(),'max':group.max(),'count':group.count(),'mean':group.mean()}


# In[109]:

grouped=frame.data2.groupby(factor)


# In[111]:

grouped.apply(get_stats).unstack()


# 根据样本分位数得到大小相等的桶（数据点数量相等），使用qcut即可。传入labels=False即可获取分位数的编号

# In[114]:

grouping=pd.cut(frame.data1,10,labels=False)


# In[115]:

grouped=frame.data2.groupby(grouping)


# In[116]:

grouped.apply(get_stats).unstack()


# ## 4，示例：用特定于分组的值填充缺失值

# 用fillna函数填充缺失值

# In[117]:

s=Series(np.random.randn(6))


# In[119]:

s[::2]=np.nan


# In[120]:

s


# In[121]:

s.fillna(s.mean())


# 下面是有关美国几个州的示例

# In[122]:

state=['Ohio','New York','Vermont','Florida','Oregon','Nevada','Califonia','Idaho']


# In[123]:

group_key=['East']*4+['West']*4


# In[125]:

data=Series(np.random.randn(8),index=state)


# In[126]:

data[['Vermont','Nevada','Idaho']]=np.nan


# In[127]:

data


# In[129]:

data.groupby(group_key).mean()


# In[132]:

fill_mean=lambda g:g.fillna(g.mean())


# In[133]:

data.groupby(group_key).apply(fill_mean)


# 分组有一个name属性，可以拿来用一下

# In[134]:

fill_values={'East':0.5,'West':-1}


# In[135]:

fill_fun=lambda g: g.fillna(fill_values[g.name])


# In[136]:

data.groupby(group_key).apply(fill_fun)


# ## 5，示例：随机采样和排列

# 下面构造一副英语型扑克牌

# In[139]:

# 红桃（Hearts）、黑桃（Spades）、梅花（Culbs）、方片（Diamonds）


# In[140]:

suits=['H','S','C','D']


# In[144]:

card_val=(list(range(1,11))+[10]*3)*4


# In[146]:

base_names=['A']+list(range(2,11))+['J','K','Q']


# In[147]:

cards=[]


# In[149]:

for suit in ['H','S','C','D']:
    cards.extend(str(num)+suit for num in base_names)


# In[150]:

deck=Series(card_val,index=cards)


# In[151]:

deck


# 从整副牌中抽取5张

# In[157]:

def draw(deck,n=5):
    return deck.take(np.random.permutation(len(deck))[:n])
#np.random.permutation()返回一个随机排列


# In[154]:

draw(deck)


# 下面从每种花色中随机抽取两张牌

# In[155]:

get_suit=lambda card: card[-1] #只要最后一个字母就可以了


# In[160]:

deck.groupby(get_suit,group_keys=False).apply(draw,n=2)


# ## 6，示例：分组加权平均数和相关系数

# In[161]:

df=DataFrame({'category':['a','a','a','a','b','b','b','b'],
              'data':np.random.randn(8),
              'weights':np.random.rand(8)})


# In[162]:

df


# 利用category计算分组加权平均数

# In[163]:

grouped=df.groupby('category')


# In[164]:

get_wavg=lambda g : np.average(g['data'],weights=g['weights'])


# In[165]:

grouped.apply(get_wavg)


# 下面看来自Yahoo！Finance的数据集，其中含有标准普尔500指数（SPX字段）和几只股票的收盘价：

# In[172]:

close_px=pd.read_csv('D:/PythonDataAnalysis/ch09/stock_px.csv',parse_dates=True,index_col=0)


# In[173]:

close_px


# In[174]:

close_px[-4:]


# 计算一个由日收益率（通过百分数变化计算）与SPX之间的年度相关系数组成的DataFrame

# In[175]:

rets=close_px.pct_change().dropna()
# 计算百分数变化


# In[181]:

spx_corr=lambda x:x.corrwith(x['SPX'])


# In[182]:

by_year=rets.groupby(lambda x: x.year)


# In[183]:

by_year.apply(spx_corr)


# In[184]:

# 苹果和微软的年度相关系数


# In[188]:

by_year.apply(lambda g:g['AAPL'].corr(g['MSFT']))


# ## 7，示例：面向分组的线性回归

# 定义下面这个regress函数（利用statsmodels库）对各种数据执行普通最小二乘法回归

# In[193]:

import statsmodels.api as sm


# In[194]:

def regress(data,yvar,xvars):
    Y=data[yvar]
    X=data[xvars]
    X['intercept']=1.
    result=sm.OLS(Y,X).fit()
    return result.params


# 按年计算AAPL对SPX收益率的线性回归

# In[195]:

by_year.apply(regress,'AAPL',['SPX'])


# # 四，透视表和交叉表

# ## 1，透视表（pivot table）

# 透视表根据一个或多个键对数据进行聚合，并根据行和列上的分组将数据分配到各个矩形区域中

# 回到小费数据集，根据sex和smoker计算分组平均数（pivot_table的默认聚合类型），并将sex和smoker放到行上

# In[200]:

tips[:5]


# In[199]:

tips.pivot_table(index=['sex','smoker'])


# In[202]:

tips.pivot_table(['tip_pct','size'],index=['sex','day'],columns='smoker')


# 进一步处理，传入margins=True添加计分小项。这将会添加标签为All的行和列

# In[205]:

tips.pivot_table(['tip_pct','size'],index=['sex','day'],columns='smoker',margins=True)
# all值为平均数：不单独考虑烟民和非烟民（ALL列），不单独考虑行分组两个级别中的任何单项（All行）


# 要使用其他聚合函数，传给aggfunc即可.例如使用count和len可以得到有关分组大小的交叉表

# In[212]:

tips.pivot_table('tip_pct',index=['sex','smoker'],columns='day',aggfunc='count',margins=True)


# In[213]:

tips.pivot_table('tip_pct',index=['sex','smoker'],columns='day',aggfunc=len,margins=True)


# 若存在空的组合（也就是NA），可以设置fill_value

# In[217]:

tips.pivot_table('size',index=['time','sex','smoker'],columns='day',aggfunc='sum',fill_value=0)


# **pivot_table的参数**
# + values：待聚合的列的名称，默认聚合所有数值列
# + index：用于分组的列名或其他分组键，出现在透视表的行
# + columns：用于分组的列名或其他分组键，出现在透视表的列
# + aggfunc:聚合函数或函数列表，默认为‘mean’。可以是任何对groupby有效的函数
# + fill_value:用于替换缺失值
# + margins:添加行/列小计和总计，默认为False

# ## 2，交叉表（crosstab）

# 交叉表是一种计算分组频率的特殊透视表

# In[221]:

data=DataFrame({'Sample':[1,2,3,4,5,6,7,8,9,10],
                'Gender':['Female','Male','Female','Male','Male','Male','Female','Female','Male','Female'],
                'Handedness':['Right-handed','Left-handed','Right-handed','Right-handed','Left-handed','Right-handed','Right-handed','Left-handed','Right-handed','Right-handed']})


# In[222]:

data


# In[225]:

data.pivot_table(index='Gender',columns='Handedness',aggfunc='count',margins=True)


# In[227]:

pd.crosstab(data.Gender,data.Handedness,margins=True)


# crosstab的前两个参数可以是数组、Series或数组列表

# In[228]:

pd.crosstab([tips.time,tips.day],tips.smoker,margins=True)


# ## 3，示例：2012联邦选举委员会数据库

# In[230]:

fec=pd.read_csv('D:/PythonDataAnalysis/ch09/P00000001-ALL.csv')


# In[231]:

fec


# In[232]:

fec.ix[123456]


# In[233]:

unique_cands=fec.cand_nm.unique()


# In[234]:

unique_cands


# In[235]:

unique_cands[2]


# In[236]:

parties={'Bachmann, Michelle':'Republican',
         'Romney, Mitt':'Republican', 
         'Obama, Barack':'Democrat',
         "Roemer, Charles E. 'Buddy' III":'Republican', 
         'Pawlenty, Timothy':'Republican',
         'Johnson, Gary Earl':'Republican', 
         'Paul, Ron':'Republican', 
         'Santorum, Rick':'Republican', 
         'Cain, Herman':'Republican',
         'Gingrich, Newt':'Republican',
         'McCotter, Thaddeus G':'Republican',
         'Huntsman, Jon':'Republican',
         'Perry, Rick':'Republican'}


# In[238]:

fec.cand_nm[123456:123461]


# In[240]:

fec.cand_nm[123456:123461].map(parties)


# In[242]:

fec['party']=fec.cand_nm.map(parties)


# In[244]:

fec['party'].value_counts()


# 需注意：该数据包既包括赞助也包括退款

# In[245]:

(fec.contb_receipt_amt>0).value_counts()


# In[246]:

fec=fec[fec.contb_receipt_amt>0]


# In[247]:

fec_mrbo=fec[fec.cand_nm.isin(['Obama, Barack','Romney, Mitt'])]


# In[248]:

fec_mrbo


# ### 根据职业和雇主统计赞助信息

# 首先，根据职业计算出总资源

# In[249]:

fec.contbr_occupation.value_counts()[:10]


# 下面清理一些数据（将一个职业信息映射到另一个）

# In[250]:

occ_mapping={
    'INFORMATION REQUESTED PER BEST EFFORTS':'NOT PROVIDED',
    'INFORMATION REQUESTED':'NOT PROVIDED',
    'INFORMATION REQUESTED (BEST EFFORTS)':'NOT PROVIDED',
    'C.E.O':'CEO'
}


# In[251]:

# 如果没有提供相关映射，则返回x


# In[252]:

f=lambda x:occ_mapping.get(x,x)


# In[253]:

fec.contbr_occupation=fec.contbr_occupation.map(f)


# 对雇主信息也进行同样处理

# In[254]:

emp_mapping={
    'INFORMATION REQUESTED PER BEST EFFORTS':'NOT PROVIDED',
    'INFORMATION REQUESTED':'NOT PROVIDED',
    'SELF':'SELF-EMPLOYED',
    'SELF EMPLOYED':'SELF-EMPLOYED',
}


# In[255]:

# 如果没有提供相关映射，则返回x


# In[256]:

f=lambda x:emp_mapping.get(x,x)


# In[257]:

fec.contbr_employer=fec.contbr_employer.map(f)


# 可以通过pivot_table根据党派和职业队数据进行聚合，然后过滤掉总出资源不足200万美元的数据

# In[259]:

by_occupation=fec.pivot_table('contb_receipt_amt',index='contbr_occupation',columns='party',aggfunc='sum')


# In[260]:

over_2mm=by_occupation[by_occupation.sum(1)>2000000]


# In[261]:

over_2mm


# In[263]:

over_2mm.plot(kind='barh')


# In[265]:

import matplotlib.pyplot as plt


# In[266]:

plt.show()


# 在计算出Obama和Rommney总出资额最高的职业和企业

# In[282]:

def get_top_amounts(group,key,n=5):
    totals=group.groupby(key)['contb_receipt_amt'].sum()
    # 根据key对totals进行降序排列
    return totals.sort_index(ascending=False)[n:]


# In[283]:

grouped=fec_mrbo.groupby('cand_nm')


# In[284]:

grouped.apply(get_top_amounts,'contbr_occupation',n=7)


# In[285]:

grouped.apply(get_top_amounts,'contbr_employer',n=7)


# ### 对出资额进行分组

# 利用cut函数根据出资额的大小将数据离散化到多个面元

# In[286]:

bins=np.array([0,1,10,100,1000,10000,100000,1000000,10000000])


# In[287]:

labels=pd.cut(fec_mrbo.contb_receipt_amt,bins)


# In[288]:

labels


# 根据候选人姓名以及面元标签对数据进行分组

# In[289]:

grouped=fec_mrbo.groupby(['cand_nm',labels])


# In[290]:

grouped.size().unstack()


# 对出资额求和并在面元内规格化，以便图形化显示两位候选人各种赞助额度的比例

# In[294]:

bucket_sums=grouped.contb_receipt_amt.sum().unstack(0)


# In[295]:

bucket_sums


# In[309]:

notmed_sums=bucket_sums.div(bucket_sums.sum(axis=1),axis=0)
# div除法


# In[298]:

notmed_sums


# In[301]:

notmed_sums[:-2].plot(kind='barh',stacked=True)


# In[302]:

plt.show()


# ### 根据州统计赞助信息

# In[303]:

grouped=fec_mrbo.groupby(['cand_nm','contbr_st'])


# In[304]:

totals=grouped.contb_receipt_amt.sum().unstack(0).fillna(0)


# In[305]:

totals=totals[totals.sum(1)>100000]


# In[306]:

totals[:10]


# In[307]:

percent=totals.div(totals.sum(1),axis=0)


# In[308]:

percent[:10]


# In[ ]:



