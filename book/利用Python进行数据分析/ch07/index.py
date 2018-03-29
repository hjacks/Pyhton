
# coding: utf-8

# # 一，合并数据集 

# + pandas.merge可以根据一个或多个键将不同DataFrame的行连接起来
# + pandas.concat可以沿着一个轴将多个对象堆叠到一起
# + combine.first可以将重复数据连接到一起，用一个对象的值填充另一个对象的缺失值

# ## 1，数据库风格的DataFrame合并

# In[3]:

import numpy as np


# In[4]:

import pandas as pd


# In[5]:

df1=pd.DataFrame({'key':['b','b','a','c','a','a','b'],'data1':range(7)})


# In[6]:

df2=pd.DataFrame({'key':['a','b','d'],'data2':range(3)})


# In[7]:

df1


# In[8]:

df2


# In[9]:

pd.merge(df1,df2,on='key')


# In[10]:

df3=pd.DataFrame({'lkey':['b','b','a','c','a','a','b'],'data1':range(7)})


# In[11]:

df4=pd.DataFrame({'rkey':['a','b','d'],'data2':range(3)})


# In[12]:

pd.merge(df3,df4,left_on='lkey',right_on='rkey')


# 默认情况下merge做的是“inner”连接；结果中的键是交集。其他方式还有“left”，“right”，“outer”。外连接做的是键的并集，组合了左连接和右连接的效果

# In[13]:

pd.merge(df1,df2,how='outer')


# 多对多连接产生的是行的笛卡尔积，如下：左面3个b，右边两个b，结果就有6个b行

# In[14]:

df1=pd.DataFrame({'key':['b','b','a','c','a','b'],'data1':range(6)})


# In[15]:

df2=pd.DataFrame({'key':['a','b','a','b','d'],'data2':range(5)})


# In[16]:

pd.merge(df1,df2,on='key',how='left')


# In[17]:

pd.merge(df1,df2,how='inner')


# 要根据多个键合并，传入一个由列名组成的列表就行了

# In[18]:

left=pd.DataFrame({'key1':['foo','foo','bar'],
                   'key2':['one','two','one'],
                   'lval':[1,2,3]})


# In[19]:

right=pd.DataFrame({'key1':['foo','foo','bar','bar'],
                   'key2':['one','two','one','two'],
                   'rval':[4,5,6,7]})


# In[20]:

pd.merge(left,right,on=['key1','key2'],how='outer')


# **Warning**:在进行列-列连接时，DataFrame中的索引会被丢弃

# 合并运算要考虑列名重复的问题，merge中的suffixes用于指定附加到左右2个DataFrame对象的重叠名上的字符串

# In[21]:

pd.merge(left,right,on='key1')


# In[22]:

# pd.merge(left,right,on='key1'，Suffixes=('_left','_right'))


# ![_auto_0](attachment:_auto_0)

# ![_auto_0](attachment:_auto_0)

# ## 2，索引上的合并

# 有时DataFrame中连接键位于其索引中，可以传入left_index=True和right_index=True以说明索引应该被用作连接键

# In[23]:

left1=pd.DataFrame({'key':['a','b','a','a','b','c'],
                 'value':range(6)})


# In[24]:

right1=pd.DataFrame({'group_val':[3.5,7]},index=['a','b'])


# In[25]:

left1


# In[26]:

right1


# In[27]:

pd.merge(left1,right1,left_on='key',right_index=True)


# In[28]:

pd.merge(left1,right1,left_on='key',right_index=True,how='outer')


# In[29]:

lefth=pd.DataFrame({'key1':['obio','obio','obio','nevada','nevada'],
                    'key2':[2000,2001,2002,2001,2002],
                    'data':np.arange(5.)})


# In[30]:

righth=pd.DataFrame(np.arange(12).reshape((6,2)),index=[['nevada','nevada','obio','obio','obio','obio'],[2001,2000,2000,2000,2001,2002]],columns=['event1','event2'])


# In[31]:

lefth


# In[32]:

righth


# In[33]:

pd.merge(lefth,righth,left_on=['key1','key2'],right_index=True)


# In[34]:

pd.merge(lefth,righth,left_on=['key1','key2'],right_index=True,how='outer')


# In[35]:

left2=pd.DataFrame([[1,2],[3,4],[5,6]],index=['a','c','e'],columns=['ohio','nevada'])


# In[36]:

right2=pd.DataFrame([[7,8],[9,10],[11,12],[13,14]],index=['b','c','d','e'],columns=['missouri','alabama'])


# In[37]:

left2


# In[38]:

right2


# In[39]:

pd.merge(left2,right2,how='outer',left_index=True,right_index=True)


# DataFrame还有join实例方法，用于合并多个带有相同或相似索引的DataFrame对象，不管他们之间是否有重叠的列。

# In[40]:

left2.join(right2,how='outer')


# In[41]:

left1


# In[42]:

right1


# 在连接键上做左连接，他还支持索引和调用者的列之间的连接

# In[43]:

left1.join(right1,on='key')


# 还可以向join传入一个DataFrame

# In[44]:

another=pd.DataFrame([[7,8],[9,10],[11,12],[13,14]],index=['a','c','e','f'],columns=['newyork','tokyo'])


# In[45]:

left2.join([right2,another]) # warning []


# In[46]:

left2.join([right2,another],how='outer')


# ## 3，轴向连接

# NumPy有一个合并原始numpy数据的concatenation函数

# In[47]:

arr=np.arange(12).reshape(4,3)


# In[48]:

arr


# In[49]:

np.concatenate([arr,arr],axis=1)


# In[50]:

s1=pd.Series([1,2],index=['a','b'])


# In[51]:

s2=pd.Series([3,4,5],index=['c','d','e'])


# In[52]:

s3=pd.Series([6,7],index=['f','g'])


# In[53]:

pd.concat([s1,s2,s3]) # warning []


# concat可以将值和索引粘结在一起，默认下是axis=0，并产生一个新Series

# In[54]:

pd.concat([s1,s2,s3],axis=1)


# In[55]:

s4=pd.concat([s1*5,s3])


# In[56]:

pd.concat([s1,s4],axis=1)


# 传入join=inner就可得到交集

# In[57]:

pd.concat([s1,s4],axis=1,join='inner')


# 可通过join_axes指定在其他轴上使用的索引

# In[58]:

# pd.concat([s1,s4],axis=1,join='inner'，join_axes=[['a','b','c','d']])


# keys参数可以在连接轴上创建一个层次化索引

# In[59]:

result=pd.concat([s1,s1,s3],keys=['one','two','three'])


# In[60]:

result


# In[61]:

result.unstack()


# In[62]:

pd.concat([s1,s1,s3],axis=1,keys=['one','two','three'])


# In[63]:

df1=pd.DataFrame(np.arange(6).reshape(3,2),
                 index=['a','b','c'],
                 columns=['one','two'])


# In[64]:

df2=pd.DataFrame(np.arange(4).reshape(2,2)+5,
                 index=['a','c'],
                 columns=['three','four'])


# In[65]:

pd.concat([df1,df2],keys=['level1','level'])


# In[66]:

pd.concat([df1,df2],axis=1,keys=['level1','level'])


# 如果传入字典，字典的键就会当做keys的值

# In[67]:

pd.concat({'level1':df1,'level2':df2},axis=1)


# In[68]:

pd.concat([df1,df2],axis=1,keys=['level1','level'],names=['upper','lower'])


# 考虑和当前问题无关的行索引，这种情况下，传入ignore_index=True

# In[69]:

df1=pd.DataFrame(np.random.randn(3,4),columns=['a','b','c','d'])


# In[70]:

df2=pd.DataFrame(np.random.randn(2,3),columns=['b','d','a'])


# In[71]:

df1


# In[72]:

df2


# In[73]:

pd.concat([df1,df2],ignore_index=True)


# ![_auto_0](attachment:_auto_0)

# ## 4，合并重叠数据

# In[74]:

from pandas import DataFrame,Series


# In[75]:

a=Series([np.nan,1.5,np.nan,2.5,3.5,np.nan],
         index=['f','e','d','c','b','a'])


# In[76]:

b=Series(np.arange(len(a),dtype=float),
         index=['f','e','d','c','b','a'])


# In[77]:

b[-1]=np.nan


# In[78]:

a


# In[79]:

b


# In[80]:

np.where(pd.isnull(a),b,a)


# np.where相当于矢量化的if-else

# Series的combine_first方法实现的也是一样的功能

# In[81]:

b[:-2].combine_first(a[2:])


# In[82]:

df1=DataFrame({'a':[1.,np.nan,5.,np.nan],
               'b':[np.nan,2,np.nan,6],
               'c':range(2,18,4)})


# In[83]:

df2=DataFrame({'a':[5.,4.,np.nan,3.,7.],
               'b':[np.nan,3,4,6,8]})


# In[84]:

df1.combine_first(df2)


# # 二，重塑和轴向旋转

# ## 1，重塑层次化索引

# 层次化索引主要功能有二：

# + stack：将数据列“旋转”为行
# + unstack：将数据行“旋转”为列

# In[85]:

data=DataFrame(np.arange(6).reshape((2,3)),
               index=pd.Index(['Ohio','Colorado'],name='state'),
               columns=pd.Index(['one','two','three'],name='number'))


# In[86]:

data


# In[87]:

result=data.stack()


# In[88]:

result


# In[89]:

result.unstack()


# 传入分层级别的编号或名称即可对其他级别进行unstack操作

# In[90]:

result.unstack(0)


# In[91]:

result.unstack(1)


# In[92]:

result.unstack('state')


# In[93]:

result.unstack('number')


# In[94]:

s1=Series([0,1,2,3],index=['a','b','c','d'])


# In[95]:

s2=Series([4,5,6],index=['c','d','e'])


# In[96]:

data=pd.concat([s1,s2],keys=['one','two'])


# In[97]:

data


# In[98]:

data.unstack()


# In[99]:

data.unstack().stack()


# In[100]:

data.unstack().stack(dropna=False)


# In[101]:

result


# In[102]:

df=DataFrame({'left':result,'right':result+5},columns=pd.Index(['left','right'],name='side'))


# In[103]:

df


# In[104]:

df.unstack('state')


# In[105]:

df.unstack('state').stack('side')


# ## 2，将“长格式”旋转为“宽格式”

# In[110]:

ldata=pd.read_csv('D:\PythonDataAnalysis\ch07\ldata.csv')


# In[111]:

ldata


# DataFrame可以实现索引的转换

# In[114]:

pivoted=ldate.pivot('date','item','value')


# 前两个参数分别做行和列索引的列名，最后一个参数用于填充DataFrame的数据列的列名

# In[115]:

pivoted.head()


# In[118]:

ldata['value2']=np.random.randn(len(ldata))


# In[119]:

ldata


# 忽略最后一个参数就会得到带有层次化的DataFrame的列

# In[120]:

pivoted=ldata.pivot('date','item')


# In[121]:

pivoted


# In[122]:

pivoted['value']


# In[123]:

unstacked=ldata.set_index(['date','item'])


# In[124]:

unstacked


# In[125]:

unstacked.unstack()


# # 三，数据转换 

# ## 1，移除重复数据

# In[126]:

data=DataFrame({'k1':['one']*3+['two']*4,
                'k2':[1,1,2,3,3,4,4]})


# In[127]:

data


# DataFrame的duplicated方法返回一个布尔型Series，表示各行是否是重复行

# In[128]:

data.duplicated()


# drop_duplicates()返回一个移除重复行的DataFrame

# In[129]:

data.drop_duplicates()


# 该方法默认全列，也可以指定部分列进行重复项判断

# In[130]:

data['v1']=range(7)


# In[131]:

data


# In[133]:

data.drop_duplicates('k1')


# duplicated和drop_duplicates默认保留的是第一个出现的值的组合，传入take_last=True则保留最后一个

# In[136]:

# data.drop_duplicates(['k1','k2'],take_last=True)


# ## 2，利用函数或映射进行数据转换

# In[137]:

data=DataFrame({'food':['bacon','pulled pork','bacon','Pastrami','corned beef','Bacon','pastrami','honey ham','nova los'],
                'ounces':[4,3,12,6,7.5,8,3,5,6]})


# In[138]:

data


# 添加一列表示该肉类食物来源的动物类型

# In[145]:

meat_to_animal={
    'bacon':'pig',
    'pulled pork':'pig',
    'pastrami':'cow',
    'corned beef':'cow',
    'honey ham':'pig',
    'nova los':'salmon'
}


# In[146]:

data['animal']=data['food'].map(str.lower).map(meat_to_animal)


# In[147]:

data


# In[148]:

data['food'].map(lambda x: meat_to_animal[x.lower()])


# ## 3，替换值

# replace可以替换值

# In[149]:

data=Series([1.,-999.,2.,-999.,-1000.,3.])


# In[150]:

data


# In[151]:

data.replace(-999,np.nan)


# In[152]:

data.replace([-999,-1000],np.nan)


# In[153]:

data.replace([-999,-1000],[np.nan,0])


# In[154]:

data.replace({-999:np.nan,-1000:0})


# ## 4，重命名轴索引

# In[155]:

data=DataFrame(np.arange(12).reshape((3,4)),
               index=['Ohio','Colorado','New York'],
               columns=['one','two','three','four'])


# In[156]:

data


# In[157]:

data.index.map(str.upper)


# In[159]:

data.index=data.index.map(str.upper)


# In[160]:

data


# In[162]:

data.rename(index=str.title,columns=str.upper)


# tiltl函数：所有单词首字母大写，其余小写

# rename还可以实现部分轴标签的更新

# In[163]:

data.rename(index={'OHIO':'INDINA'},
            columns={'three':'peekaboo'})


# In[164]:

data


# 要实现就地修改，传入inplace=True

# In[165]:

_=data.rename(index={'OHIO':'INDIANA'},inplace=True)


# In[166]:

data


# ## 5，离散化和面元划分

# 为了便于分析，连续数据常常被离散化或拆分为“面元”

# In[168]:

ages=[20,22,25,27,21,23,37,31,61,45,41,32]


# 将ages划分为“18到25”，“26到35”，“35到60”以及“60以上”,使用pandas的cut函数

# In[170]:

bins=[18,25,35,60,100]


# In[171]:

cats=pd.cut(ages,bins)


# In[172]:

cats


# pandas返回的是一个特殊的Categorical对象，可看做是一组表示面元名称的字符串.它含有一个表示不同分类名称的levels数组以及一个为年龄数据进行标号的labels属性

# In[174]:

cats.labels


# In[178]:

# cats.levels


# In[179]:

pd.value_counts(cats)


# 圆括号开端，方括号闭端，哪边是闭端可以用right=False进行修改

# In[180]:

pd.cut(ages,[18,26,36,61,100],right=False)


# 可以设置面元名称，将labels选项设置为一个列表或数组即可

# In[181]:

group_names=['Youth','YoungAdult','MiddleAged','Senior']


# In[182]:

pd.cut(ages,bins,labels=group_names)


# 若向cut传入的是面积的数量而不是确切的面元边界，则它会根据数据的最小值和最大值计算等长面元

# In[185]:

data=np.random.rand(20)


# In[186]:

data


# In[188]:

pd.cut(data,4,precision=2)


# qcut函数根据样本分位数对数据进行面元划分,得到大小相等的面元

# In[189]:

data=np.random.randn(1000)


# In[191]:

cats=pd.qcut(data,4)


# In[192]:

cats


# In[193]:

pd.value_counts(cats)


# qcut还可以设置自定义的分位数（0到1之间的数值，包含端点）

# In[194]:

pd.qcut(data,[0,0.1,0.5,0.9,1])


# ## 6，检测和过滤异常值

# In[195]:

np.random.seed(12345)


# In[196]:

data=DataFrame(np.random.randn(1000,4))


# In[197]:

data


# In[198]:

data.describe()


# In[199]:

col=data[3]


# In[200]:

col[np.abs(col)>3]


# In[201]:

data[(np.abs(data)>3).any(1)]


# In[202]:

data[np.abs(data)>3]=np.sign(data)*3


# In[203]:

data.describe()


# np.sign()返回的是一个由1和-1组成的数组，表示原始值得符号

# ## 7，排列和随机采样

# 通过需要排列的轴的长度调用np.random.permutation，可产生一个表示新顺序的整数数组（随机重排序）

# In[209]:

df=DataFrame(np.arange(5*4).reshape(5,4))


# In[210]:

df


# In[211]:

sampler=np.random.permutation(5)


# In[212]:

sampler


# In[213]:

df.take(sampler)


# 非替换方式采样

# In[215]:

df.take(np.random.permutation(len(df))[:3])


# In[216]:

bag=np.array([5,7,-1,6,4])


# In[217]:

bag


# 替换方式采样

# In[219]:

sampler=np.random.randint(0,len(bag),size=10)


# In[220]:

sampler


# In[221]:

draws=bag.take(sampler)


# In[222]:

draws


# ## 8，计算指标、哑变量

# In[223]:

df=DataFrame({'key':['b','b','a','c','a','b'],
              'data1':range(6)})


# In[224]:

df


# 若DataFrame某列含有k个不同的值，则可以派生出一个k列矩阵或DataFrame（其值全为0或1）。pd有个get_dummies可实现该功能

# In[225]:

pd.get_dummies(df['key'])


# In[226]:

pd.get_dummies(df['data1'])


# get_dummies的prefix参数可实现给指标的列加上一个前缀

# In[227]:

dummies=pd.get_dummies(df['key'],prefix='key')


# In[228]:

dummies


# In[229]:

mnames=['movie_id','title','genres']


# In[231]:

movies=pd.read_table('D:\PythonDataAnalysis\ch07\movies.dat',sep='::',header=None,names=mnames)


# In[232]:

movies[:10]


# In[233]:

genre_iter=(set(x.split('|')) for x in movies.genres)


# In[234]:

genres=sorted(set.union(*genre_iter))


# In[235]:

genres


# In[236]:

dummies=DataFrame(np.zeros((len(movies),len(genres))),columns=genres)


# In[238]:

for i,gen in enumerate(movies.genres):
    dummies.ix[i,gen.split('|')]=1


# In[239]:

movies_windic=movies.join(dummies.add_prefix('Genre_'))


# In[241]:

movies_windic.ix[0]


# In[242]:

values=np.random.rand(10)


# In[243]:

values


# In[244]:

bins=[0,0.2,0.4,0.6,0.8,1]


# In[245]:

pd.get_dummies(pd.cut(values,bins))


# # 四，字符串操作

# ## 1，字符串对象方法

# In[248]:

val='a,b,  guidp'


# In[249]:

val.split(',')


# strip用于修改空白符（包括换行符）

# In[250]:

pieces=[x.strip() for x in val.split(',')]


# In[251]:

pieces


# In[252]:

first,second,three=pieces


# In[253]:

first+'::'+second+'::'+'three'


# In[254]:

'::'.join(pieces)


# In[255]:

'guidp' in pieces


# In[256]:

val.index(',')


# In[257]:

val.find(':')


# 找不到字符串，index会引发一个异常

# In[258]:

val.index(';')


# In[259]:

val.count(',')


# In[261]:

val.replace(',','::')


# In[262]:

val.replace(',','')


# ![_auto_0](attachment:_auto_0)

# ![_auto_0](attachment:_auto_0)

# ## 2，正则表达式

# python内置的re模块负责对字符串应用正则表达式

# re模块的函数分为模式匹配，替换和拆分

# 描述一个或多个空白符(制表符、空格、换行符等）的regex是** \s+ **

# In[263]:

import re


# In[264]:

text='foo bar\t baz \tqux'


# In[265]:

text


# In[266]:

re.split('\s+',text)


# 用re.compile编译regex以得到一个可重用的regex对象

# In[269]:

regex=re.compile('\s+')


# In[270]:

regex.split(text)


# findall可以得到匹配regex的所有模式

# In[271]:

regex.findall(text)


# search返回第一个匹配项

# match只匹配字符串首部

# In[273]:

text="""
Dave dave@google.com
Steve steve@mail.com
Rob rob@mail.com
Ryan ryan@yahoo.com
"""


# In[274]:

pattern=r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}'


# In[275]:

regex=re.compile(pattern,flags=re.IGNORECASE)


# In[276]:

regex.findall(text)


# In[277]:

m=regex.search(text)


# In[278]:

m


# In[280]:

text[m.start():m.end()]


# In[281]:

print (regex.match(text))


# sub将匹配到的模式替换为指定字符串

# In[283]:

print(regex.sub('REDACTED',text))


# 若想将电子邮件地址分为用户名，域名以及域名后缀，只需将分段模式的各部分用圆括号包起来

# In[284]:

pattern=r'([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})'


# In[287]:

regex=re.compile(pattern,flags=re.IGNORECASE)


# 通过groups方法返回一个由模式各段组成的元组

# In[288]:

m=regex.match('wesm@bright.net')


# In[290]:

m.groups()


# In[291]:

regex.findall(text)


# sub还能通过诸如\1,\2之类的特殊符号访问各匹配项中的分组

# In[292]:

print(regex.sub(r'Username: \1,Domain: \2,Suffix: \3',text))


# In[293]:

regex=re.compile(r"""
(?P<username>[A-Z0-9._%+-]+)
@
(?P<domain>[A-Z0-9.-]+)
\.
(?P<suffix>[A-Z]{2,4})
""",flags=re.IGNORECASE|re.VERBOSE)


# In[295]:

m=regex.match('wesm@bright.com')


# In[296]:

m.groupdict()


# ![_auto_0](attachment:_auto_0)

# ## 3,pandas中矢量化的字符串函数

# In[297]:

data={'Dave':'dave@google.com','Steve':'steve@mail.com','Rob':'rob@mail.com','Wes':np.nan}


# In[299]:

data=Series(data)


# In[300]:

data


# In[301]:

data.isnull()


# 通过data.map,所有字符串和正则表达式都能被应用于各个值，但是存在NA就会报错。但Series有一些能够跳过NA值得字符串操作方法。通过Series的str属性即可访问这些方法

# In[303]:

data.str.contains('mail')


# In[304]:

pattern


# In[305]:

data.str.findall(pattern,flags=re.IGNORECASE)


# 实现矢量化的元素获取操作：1，使用str.get,2,在str属性上使用索引

# In[318]:

matches=data.str.match(pattern,flags=re.IGNORECASE)


# In[319]:

matches


# In[320]:

matches.str.get(1)


# In[321]:

matches.str[0]


# In[322]:

data.str[:5]


# ![_auto_0](attachment:_auto_0)

# ![_auto_0](attachment:_auto_0)

# # 示例：USDA食品数据库

# In[370]:

import json
import matplotlib.pyplot as plt


# In[371]:

db=json.load(open('D:/PythonDataAnalysis/ch07/foods-2011-10-03.json'))


# In[372]:

len(db)


# In[373]:

db[1].keys()


# In[374]:

db[0]['nutrients'][0]


# In[375]:

nutrients=DataFrame(db[0]['nutrients'])


# In[376]:

nutrients[:7]


# In[377]:

info_keys=['description','group','id','manufacturer']


# In[378]:

info=DataFrame(db,columns=info_keys)


# In[379]:

info[:10]


# In[380]:

info


# In[381]:

pd.value_counts(info.group)


# In[382]:

nutrients=[]


# In[383]:

for rec in db:
    fnuts=DataFrame(rec['nutrients'])
    fnuts['id']=rec['id']
    nutrients.append(fnuts)


# In[384]:

nutrients=pd.concat(nutrients,ignore_index=True)


# In[385]:

nutrients


# In[386]:

nutrients.duplicated().sum()


# In[387]:

nutrients=nutrients.drop_duplicates()


# 两个DataFrame对象中都有“group”和“description”，需重新命名以便分辨

# In[388]:

col_mapping={'description':'food',
             'group':'fgroup'}


# In[389]:

info=info.rename(columns=col_mapping,copy=False)


# In[390]:

info


# In[391]:

col_mapping={'description':'nutrient',
             'group':'nutgroup'}


# In[392]:

nutrients=nutrients.rename(columns=col_mapping,copy=False)


# In[393]:

nutrients


# In[394]:

ndata=pd.merge(nutrients,info,on='id',how='outer')


# In[395]:

ndata


# In[396]:

ndata.ix[30000]


# In[397]:

result=ndata.groupby(['nutrient','fgroup'])['value'].quantile(0.5)


# In[399]:

# result['Zinc,Zn'].order().plot(kind='barh')


# In[400]:

by_nutrient=ndata.groupby(['nutgroup','nutrient'])


# In[401]:

get_maximum=lambda x:x.xs(x.value.idxmax())


# In[402]:

get_minimum=lambda x:x.xs(x.value.idxmin())


# In[404]:

max_foods=by_nutrient.apply(get_maximum)[['value','food']]


# In[406]:

max_foods.food=max_foods.food.str[:50]


# In[407]:

max_foods.ix['Amino Acids']['food']


# In[ ]:



