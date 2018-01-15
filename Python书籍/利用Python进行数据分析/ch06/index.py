
# coding: utf-8

# # 一，读写文本格式的数据

# ![_auto_0](attachment:_auto_0)

# ### 文本数据转换为DataFrame的一些技术

# + **索引**：将一个或多个列当做返回的DataFrame处理，以及是否从文件，用户获取列明。
# + **类型推断和数据转换**：包括用户定义值得转换，缺失值标记列表等
# + **日期解析**：包括组合功能，比如将分散在多个列中的日期时间信息组合成结果中的单个列
# + **迭代**：支持对大文件进行逐块迭代
# + **不规整数据问题**：跳过一些行，页脚，注释或其他一些不重要的东西

# In[1]:

from pandas import Series,DataFrame


# In[2]:

import pandas as pd


# In[3]:

import numpy as np


# In[4]:

df=pd.read_csv('D:\PythonDataAnalysis\ch6\ex1.csv')


# In[5]:

df


# In[6]:

pd.read_csv('D:\PythonDataAnalysis\ch6\ex1.csv',names=['a','b','c','d','message'])


# In[7]:

pd.read_csv('D:\PythonDataAnalysis\ch6\ex1.csv',names=['a','b','c','d','message'],index_col='message')


# In[9]:

parsed=pd.read_csv('D:\PythonDataAnalysis\ch6\ex2.csv',index_col=['key1','key2'])


# In[11]:

parsed


# In[12]:

list(open('D:\PythonDataAnalysis\ch6\ex3.txt'))


# In[13]:

result=pd.read_table('D:\PythonDataAnalysis\ch6\ex3.txt',sep='\s+')


# In[14]:

result


# In[16]:

pd.read_csv('D:\PythonDataAnalysis\ch6\ex4.csv',skiprows=[0,2,3])


# skiprows跳过某某行

# In[17]:

result=pd.read_csv('D:\PythonDataAnalysis\ch6\ex5.csv')


# In[18]:

result


# In[19]:

pd.isnull(result)


# na_values可以接受一组表示缺失值的字符串

# ![_auto_0](attachment:_auto_0)

# ![_auto_0](attachment:_auto_0)

# ![_auto_0](attachment:_auto_0)

# ## 1,逐块读取文本文件

# In[25]:

result=pd.read_csv('D:\PythonDataAnalysis\ch6\ex6.csv')


# In[26]:

result


# pd.read_csv('D:\PythonDataAnalysis\ch6\ex5.csv'，nrows=5)

# + chunker=pd.read_csv('D:\PythonDataAnalysis\ch6\ex5.csv'，chunkersize=1000)
# + tot=Series([])
# + for piece in chunker:
# +    tot=tot.add(piece['key'].value_counts(),fill_value=0)

# ## 2，将数据写出到文本格式

# In[55]:

result=pd.read_csv('D:\PythonDataAnalysis\ch6\ex5.csv')


# In[56]:

result


# In[57]:

result.to_csv('D:\PythonDataAnalysis\ch6\ex5_copy.csv')


# In[35]:

import sys


# In[37]:

result.to_csv(sys.stdout,sep='|')


# In[38]:

result.to_csv(sys.stdout,na_rep='NULL')


# In[39]:

result.to_csv(sys.stdout,index=False,header=False)


# result.to_csv(sys.stdout,index=False,cols=['a','b','c'])

# In[41]:

dates=pd.date_range('21/8/2017',periods=10)


# In[45]:

ts=Series(np.arange(10),index=dates)


# In[90]:

ts.to_csv('D:\PythonDataAnalysis\ch6\tseries.csv')


# In[91]:

Series.from_csv('D:\PythonDataAnalysis\ch6\tseries.csv',parse_dates=True)


# ## 3，手动处理分隔符格式 

# In[65]:

import csv


# In[66]:

f=open('D:\PythonDataAnalysis\ch6\ex7.csv')


# In[88]:

reader=csv.reader(f)


# In[68]:

reader


# In[70]:

for line in reader:
    print (line)


# 将任意已打开的文件或文件型的对象传给csv.reader,对这个csv.reader进行迭代将为每行产生一个元组，并移除所有引号

# In[72]:

lines=list(csv.reader(open('D:\PythonDataAnalysis\ch6\ex7.csv')))


# In[75]:

header,values=lines[0],lines[1:]


# In[77]:

data_dict={h:v for h,v in zip(header,zip(*values))}


# In[78]:

data_dict


# In[84]:

class my_dialect(csv.Dialect):
    lineminater='\n'
    delimiter=';'
    quotechar='"'


# reader=csv.reader(f,diaect=my_dialect)

# reader=reader.csv(f,delimiter='|')

# ![_auto_0](attachment:_auto_0)

# ## 4，JSON数据 

# In[96]:

obj="""
{"name":"xutao",
"place_lived":["changchun","tongling","shanghai"],
"pet":"heizi",
"sibling":[{"name":"xiaoran","age":23,"pet":"zuli"},
           {"name":"wangzhi","age":23,"pet":"zuul"}]
}
"""


# In[97]:

obj


# In[98]:

import json


# In[99]:

result=json.loads(obj)


# In[100]:

result


# json.loads()将json语句转换成python形式

# In[101]:

asjson=json.dumps(result)


# json.dumps()将python语句转换成json

# In[107]:

siblings=DataFrame(result['sibling'],columns=['name','age','pet'])


# In[108]:

siblings


# ## 5，XML和HTML:WEB信息收集

# In[109]:

from lxml.html import parse


# python3不需要安装urllib2，urllib和urllib2合成一个包，使用urllib.request调用urlopen

# In[117]:

from urllib.request import urlopen


# In[145]:

parsed=parse(urlopen('http://finance.sina.com.cn/stock/'))


# In[146]:

doc=parsed.getroot()


# In[147]:

links=doc.findall('.//a')


# In[148]:

links[13:30]


# In[149]:

lnk=links[28]


# In[150]:

lnk


# In[151]:

lnk.get('href')


# In[152]:

lnk.text_content()


# In[153]:

urls=[lnk.get('href') for lnk in links]


# In[154]:

urls[-10:]


# In[155]:

tables=doc.findall(".//table")


# In[165]:

calls=tables[2]


# In[166]:

puts=tables[4]


# In[156]:

rows=doc.findall('.//tr')


# In[157]:

def _unpack(row,kind="td"):
    elts=doc.findall(".//%s" % kind)
    return [val.text_content() for val in elts]


# In[158]:

_unpack(rows[0],kind='th')


# In[159]:

_unpack(rows[1],kind='td')


# In[160]:

from pandas.io.parsers import TextParser


# In[162]:

def parse_options_data(table):
    rows=table.findall('.//tr')
    header=_unpack(rows[0],kind='th')
    data=[_unpack(r) for r in rows[1:]]
    return TextParser(data,names=header).get_chunk()


# In[167]:

call_data=parse_options_data(calls)


# In[169]:

put_data=parse_options_data(puts)


# In[170]:

call_data[:10]


# In[171]:

put_data[:10]


# ## 6，利用lxml.objectify解析xml

# In[173]:

from lxml import objectify


# In[176]:

path='D:/PythonDataAnalysis/ch6/xml/Performance_MNR.xml'


# In[177]:

root=parsed.getroot()


# In[178]:

data=[]


# In[179]:

skip_fields=['PARENT_SEQ','INDICATOR_SEQ','DESIRED_SEQ','DECIMAL_SEQ']


# In[186]:

# for elt in root.indicator:
#    el_data={}
#    for child in elt.getchildren():
#        if child.tag in skip_fields:
#            continue
#        el_data[child.tag]=child.pyval
#    data.append(el_data)
# pref=DataFrame(data)


# In[191]:

# import StringIO


# ## 二，二进制数据格式

# In[192]:

frame=pd.read_csv('D:\PythonDataAnalysis\ch6\ex1.csv')


# In[193]:

frame


# ## 1，使用HDF5格式

# In[198]:

store=pd.HDFStore('mydata.h5')


# In[200]:

store['obj1']=frame


# In[201]:

store['obj1_col']=frame['a']


# In[202]:

store


# In[203]:

store['obj1']


# ## 2，读取Microsoft Excel文件

# In[208]:

# xls_file=pd.ExcelFile('D:\PythonDataAnalysis\ch6\data.xls')
# table=xls_file.parse('sheet1')


# # 三，使用HTML和WEB API

# In[2]:

import requests


# In[3]:

url='http://www.baidu.com/search.json?q=python%20pandas'


# In[4]:

resp=requests.get(url)


# In[5]:

resp


# In[6]:

import json


# In[7]:

# data=json.loads(resp.text)


# # 看书

# # 四，使用数据库

# In[26]:

import sqlite3


# In[27]:

query="""
CREATE TABLE test
(a VARCHAR(20),b VARCHAR(20),
 c REAL,       d INTEGER
 );"""


# In[28]:

con=sqlite3.connect(':memory:')


# In[29]:

con.execute(query)


# In[30]:

con.commit()


# In[31]:

data=[('xutao','tongling',1.25,6),
      ('xulei','tongling',2.6,3),
      ('liujianuo','hefei',1.7,5)]


# In[32]:

stmt='INSERT INTO test VALUES(?,?,?,?)'


# In[33]:

con.executemany(stmt,data)


# In[34]:

con.commit()


# In[35]:

corsur=con.execute('select * from test')


# In[36]:

rows=corsur.fetchall()


# In[37]:

rows


# In[41]:

import pandas as pd


# In[43]:

pd.DataFrame(rows,columns=['a','b','c','d'])


# In[44]:

import pandas.io.sql as sql


# In[45]:

sql.read_frame('select * from test',con)


# ## 1，存取MongoDB中的数据

# In[ ]:



