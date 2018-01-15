
# coding: utf-8

# 时间序列数据的的意义取决于具体的应用场景，主要有：
# + 时间戳，特定的时刻。
# + 固定时期，如2007年1月或2010年全年
# + 时间间隔，由起始和结束时间戳表示。时期可以被看做间隔特例。
# + 实验或过程时间，每个时间点都是相对于特定起始时间的一个度量。

# # 一、日期和时间数据类型及工具

# In[1]:

from datetime import datetime


# In[2]:

now=datetime.now()


# In[3]:

now


# In[4]:

now.year,now.month,now.day


# datetime.timedelta表示两个datetime对象之间的时间差

# In[5]:

dela=datetime(2011,1,7)-datetime(2008,6,24,8,15)


# In[6]:

dela


# In[7]:

dela.days


# In[8]:

dela.seconds


# 可以给datetime对象加上或减去一个或多个timedelta，这样会产生一个新对象

# In[9]:

from datetime import timedelta


# In[10]:

start=datetime(2011,1,7)


# In[11]:

start+timedelta(12)


# In[12]:

start-2*timedelta(12)


# **datetime模块中的数据类型**
# + date:以公历形式存储日历日期（年，月，日）
# + time:将时间存储为时，分，秒，毫秒
# + datetiem：存储日期和时间
# + timedelta：表示两个datetime值之间的差（日，秒，毫秒）

# ## 1、字符串和datetime的相互转换

# 利用str或strftime方法（传入一个格式化字符串），datetime对象和pandas的Timestamp对象可以被格式化为字符串

# In[13]:

stmp=datetime(2011,1,3)


# In[14]:

str(stmp)


# In[15]:

stmp.strftime('%Y-%m-%d')
# 注意只有y大写


# datetime.strptime也可以用这些格式化编码将字符串转换为日期

# In[16]:

value='2011-01-03'


# In[17]:

datetime.strptime(value,'%Y-%m-%d')


# In[18]:

datestrs=['7/6/2011','8/6/2011']


# In[19]:

[datetime.strptime(x,'%m/%d/%Y') for x in datestrs]


# In[20]:

from dateutil.parser import parse


# In[21]:

parse('2011-01-03')


# In[22]:

parse('Jan 31, 1997 10:45 PM')


# 国际上，日通常出现在月的前面，传入**dayfirst=True**即可解决

# In[23]:

parse('6/12/2011',dayfirst=True)


# to_datetime方法可以解析多种不同的日期表示形式

# In[24]:

datestrs


# In[25]:

import pandas as pd


# In[26]:

pd.to_datetime(datestrs)


# 它还可以处理缺失值（None，空字符串等）

# In[27]:

idx=pd.to_datetime(datestrs+[None])


# In[28]:

idx


# In[29]:

idx[2]


# In[30]:

pd.isnull(idx)


# **NaT(not a time)是pandas中时间戳的NA值

# **datetime格式定义**
# + %Y ：  4位数的年
# + %y ：  4位数的年
# + %m ：  两位数的月
# + %d ： 两位数的日
# + %H ： 时（24小时制）
# + %I ： 时（12小时制）
# + %M ：2位数的分
# + %S ：秒
# + %w ： 整数表示星期几
# + %U ： 每年的第几周
# + %z ： 以+HHMM或-HHMM表示的UTC时区偏移量
# + %F ： %Y-%m-%%d简写形式
# + %D ： %m/%d/%y简写形式

# # 二、时间序列基础

# In[31]:

dates=[datetime(2011,1,2),datetime(2011,1,5),datetime(2011,1,7),datetime(2011,1,8),datetime(2011,1,10),datetime(2011,1,12)]


# In[32]:

from pandas import Series,DataFrame
import numpy as np


# In[33]:

ts=Series(np.random.randn(6),index=dates)


# In[34]:

ts


# In[35]:

type(ts)


# In[36]:

ts.index


# 不同索引的时间序列之间的算术运算会自动按日期对齐

# In[37]:

ts+ts[::2]


# In[38]:

ts.index.dtype


# In[39]:

stamp=ts.index[0]


# In[40]:

stamp


# ## 1、索引、选取、子集的构造

# In[41]:

stmap=ts.index[2]


# In[42]:

ts[stamp]


# In[43]:

ts['1/10/2011']


# In[44]:

ts['20110110']


# In[45]:

longer_ts=Series(np.random.randn(1000),index=pd.date_range('1/1/2000',periods=1000))


# In[46]:

longer_ts


# In[47]:

longer_ts['2001']


# In[48]:

longer_ts['2001-05']


# 通过日期进行切片的方式只对规则Series有效：

# In[49]:

ts[datetime(2011,1,7):]


# In[50]:

ts


# 可以用不存在于该时间序列中的时间戳对其进行切片（范围查询）

# In[51]:

ts['1/6/2011':'1/11/2011']


# 这里可以传入字符串日期，datetime或Timesstamp。注意，这样产生的是源时间序列的视图。此外，还有一个等价的实例方法可以截取两个日期之间的TimeSeries

# In[52]:

ts.truncate(after='1/9/2011')


# In[53]:

dates=pd.date_range('1/1/2000',periods=100,freq='W-WED')


# In[54]:

dates


# In[55]:

long_df=DataFrame(np.random.randn(100,4),index=dates,columns=['Colorado','Teaxs','New York','Ohio'])


# In[56]:

long_df


# ## 2,、带有重复索引的时间序列

# In[57]:

dates=pd.DatetimeIndex(['1/1/2000','1/2/2000','1/2/2000','1/2/2000','1/3/2000'])


# In[58]:

dup_ts=Series(np.arange(5),index=dates)


# In[59]:

dup_ts


# In[60]:

dup_ts.index.is_unique


# In[61]:

dup_ts['1/3/2000']


# In[62]:

dup_ts['1/2/2000']


# In[63]:

grouped=dup_ts.groupby(level=0)


# In[64]:

grouped.mean()


# In[65]:

grouped.count()


# # 三、日期的范围、频率以及移动

# pandas有一套标准时间序列以及用于重采样，频率推断，生成固定频率日期范围的工具

# 我们可以将之前那个时间序列转换为一个具有固定频率的时间序列

# In[66]:

ts


# In[67]:

ts.resample('D')


# ## 1、生成日期范围

# In[68]:

index=pd.date_range('4/1/2012','6/1/2012')


# In[69]:

index


# In[70]:

pd.date_range('4/1/2012',periods=20)


# In[71]:

pd.date_range(start='4/1/2012',periods=20)


# In[72]:

pd.date_range(end='4/1/2012',periods=20)


# 要生成每个月最后一天，传入“BM”频率

# In[73]:

pd.date_range('1/1/2000','12/1/2000',freq='BM')


# In[74]:

pd.date_range('5/2/2012 12:56:32', periods=7)


# normalize可以产生一组规范化到午夜的时间戳

# In[75]:

pd.date_range('5/1/2001',periods=5,normalize=True)


# ## 2、频率和日期偏移量

# pandas中的频率是由一个基础频率和一个乘数组成。基础频率通常以一个字符串别名表示。对于每个基础频率，都有一个被称为日期偏移量的对象与之对应

# In[76]:

from pandas.tseries.offsets import Hour,Minute


# In[77]:

hour=Hour()
# 按小时计算的频率可以用Hour类表示


# In[78]:

hour


# In[79]:

four_hours=Hour(4)


# In[80]:

four_hours


# In[81]:

pd.date_range('1/1/2000','1/3/2000 23:59',freq='4h')


# 大部分偏移量都可通过加法进行连接

# In[82]:

Hour(2)+Minute(30)


# In[83]:

pd.date_range('1/1/2000',periods=10,freq='1h30min')


# ![_auto_0](attachment:_auto_0)

# ![_auto_0](attachment:_auto_0)

# ![_auto_0](attachment:_auto_0)

# ### WOM日期

# WOM（week of month）以WOM开头，使你能获得诸如“每月第三个星期五”之类的日期

# In[84]:

rng=pd.date_range('1/1/2000','9/1/2000',freq='WOM-3FRI')


# In[85]:

list(rng)


# ## 3、移动（超前和滞后）数据

# 移动指的是沿着时间轴将数据前移或后移

# In[86]:

ts=Series(np.random.randn(4),
          index=pd.date_range('1/1/2000',periods=4,freq='M'))


# In[87]:

ts


# Series和DateFrame都有一个shift方法用于执行单纯的前移或后移操作，保持索引不变.shift通常用于计算一个时间序列或多个时间序列中的百分比变化

# In[88]:

ts/ts.shift(1)-1


# 因此，若频率已知，则将其传给shift以便实现对时间戳进行位移而不是对数据进行简单位移：

# In[89]:

ts.shift(2,freq="M")


# In[90]:

ts.shift(1,freq='90T')


# 通过偏移量对日期进行位移

# In[91]:

from pandas.tseries.offsets import Day,MonthEnd


# In[92]:

now=datetime(2011,11,17)


# In[93]:

now+3*Day()


# 若加的是锚点位移量（如MonthEnd），第一次增量会将原日期向前滚动到符合频率规则的下一个日期：

# In[94]:

now+MonthEnd()


# In[95]:

now+MonthEnd(2)


# 通过锚点位移量的rollforward和rollback方法，可显式地将日期向前或向后“滚动”：

# In[96]:

offset=MonthEnd()


# In[97]:

offset.rollforward(now)


# In[98]:

offset.rollback(now)


# 日期偏移量还可结合groupby使用这两个“滚动”方法：

# In[99]:

ts=Series(np.random.randn(20),index=pd.date_range('1/15/2000',periods=20,freq='4d'))


# In[100]:

ts


# In[101]:

ts.groupby(offset.rollforward).mean()


# In[102]:

ts.resample('M',how='mean')
# 稍后进行详述


# # 四、时区处理

# python中，时区信息来自第三方库pytz

# In[103]:

import pytz


# In[104]:

pytz.common_timezones[-5:]


# 使用pytz.timezone即可获取时区对象

# In[105]:

tz=pytz.timezone('US/Eastern')


# In[106]:

tz


# ## 1、本地化和转换

# 默认下，pandas中的时间序列是单纯(naive)的时区

# In[107]:

rng=pd.date_range('3/9/2012 9:30',periods=6,freq="D")


# In[108]:

rng


# In[109]:

ts=Series(np.random.randn(len(rng)),index=rng)


# 其索引的tz字段为none

# In[110]:

print(ts.index.tz)


# 在生成日期范围得时候还可以加上一个时区集

# In[111]:

pd.date_range('3/9/2012 9:30',periods=10,freq="D",tz='UTC')


# 从单纯到本地化的转换是通过tz_localize方法处理的

# In[112]:

ts_utc=ts.tz_localize('UTC')


# In[113]:

ts_utc


# In[114]:

ts_utc.index


# 一旦时间序列被本地化到某个特定时区，就可以用tz_convert将其转换到别的时区了

# In[115]:

ts_utc.tz_convert('US/Eastern')


# 对于上面，我们可以将其本地化到EST，然后转换为UTC或柏林时间

# In[116]:

ts_eastern=ts.tz_localize("US/Eastern")


# In[117]:

ts_eastern


# In[118]:

ts_eastern.tz_convert('UTC')


# In[119]:

ts_eastern.tz_convert('Europe/Berlin')


# tz_localize和tz_convert也是DateTimeIndex的实例方法

# ## 2、操作时区意识型Timestamp对象

# Timestamp对象也能从单纯型本地化为时区意识型，并从一个时区转换到另一个时区

# In[120]:

stamp=pd.Timestamp('2011-03-12 04:00')


# In[121]:

stamp


# In[122]:

stamp_utc=stamp.tz_localize('utc')


# In[123]:

stamp_utc


# In[124]:

stamp_utc.tz_convert('US/Eastern')


# In[125]:

stamp_moscow=pd.Timestamp('2011-03-12 04:00',tz='Europe/Moscow')


# In[126]:

stamp_moscow


# 时区意识型Timestamp对象在内部保存了一个UTC时间戳值（自UNIX纪元（1970年1月1日）算起的纳秒数）。这个UTC值在时区转换过程中是不变的

# In[127]:

stamp_utc.value


# In[128]:

stamp_utc.tz_convert('US/Eastern').value


# 当使用pandas的DateOffset对象执行时间算术运算时，运算过程会自动关注是否存在夏令时转变期

# In[129]:

from pandas.tseries.offsets import Hour


# In[130]:

stamp=pd.Timestamp('2012-03-12 01:30',tz='US/Eastern')


# In[131]:

stamp


# In[132]:

stamp+Hour()


# In[133]:

stamp+2*Hour()


# ## 3、不同时区之间的运算

# In[134]:

rng=pd.date_range('3/6/2012 9:40',periods=10,freq='B')


# In[135]:

rng


# In[136]:

ts=Series(np.random.randn(len(rng)),index=rng)


# In[137]:

ts


# In[138]:

ts1=ts[:7].tz_localize('Europe/London')


# In[139]:

ts2=ts1[2:].tz_convert('Europe/Moscow')


# In[140]:

result=ts1+ts2


# In[141]:

result.index


# # 五、时期及其算术运算

# 时期（period）表示的是时间区间，比如数日，数月，数季，数年等。Period类所表示的就是这种数据类型，其构造函数需要用到一个字符串或整数

# In[142]:

p=pd.Period(2007,freq='A-DEC')


# In[143]:

p


# In[144]:

p+5


# In[145]:

p-2


# In[146]:

pd.Period('2013',freq='A-DEC')-p


# period_range函数可用于创建规则的时期范围

# In[147]:

rng=pd.period_range('1/1/2000','6/30/2000',freq='M')


# In[148]:

rng


# PeriodIndex保存了一组Period，它可以在任何pandas数据结构中被用作轴索引

# In[149]:

Series(np.random.randn(6),index=rng)


# PeriodIndex类构造的函数还允许直接使用一组字符串

# In[150]:

values=['2001Q3','2002Q2','2003Q1']


# In[151]:

index=pd.PeriodIndex(values,freq="Q-DEC")


# In[152]:

index


# ##  1、时期的频率转换

# Period和PeriodIndex对象都可以通过其asfreq方法被转换成别的频率

# In[153]:

p=pd.Period('2007',freq='A-DEC')


# In[154]:

p.asfreq('M',how='start')


# In[155]:

p.asfreq('M',how='end')


# In[156]:

p=pd.Period('2007',freq='A-JUN')


# In[157]:

p


# In[158]:

p.asfreq('M',how='start')


# In[159]:

p.asfreq('M',how='end')


# 在将高频率转换为低频率时，超时期是由子时期所属的位置决定的

# In[160]:

p=pd.Period('2007-08','M')


# In[161]:

p.asfreq('A-JUN')


# PeriodIndex或TimeSeries的频率转换方式也是如此

# In[162]:

rng=pd.period_range('2006','2009',freq='A-DEC')


# In[163]:

rng


# In[164]:

ts=Series(np.random.randn(len(rng)),index=rng)


# In[165]:

ts


# In[166]:

ts.asfreq('M',how='start')


# In[167]:

ts.asfreq('M',how='end')


# ![_auto_0](attachment:_auto_0)

# ## 2、按季度计算的时期频率

# 许多季度型数据都会涉及“财年末”的概念。通常是一年12个月中某月的最后一个日历日或工作日。因此，“2012Q4”根据财年末的不同会有不同含义。pandas支持12钟可能的季度型频率

# In[168]:

p=pd.Period('2012Q4',freq='Q-JAN')


# In[169]:

p


# In[170]:

p.asfreq('D','start')


# In[171]:

p.asfreq('D','end')


# 获取该季度倒数第二个工作日下午4点的时间戳

# In[172]:

p4pm=(p.asfreq('B','e')-1).asfreq('T','S')+16*60


# In[173]:

p4pm


# In[174]:

p4pm.to_timestamp()


# ![_auto_0](attachment:_auto_0)

# period_range还可用于生成季度型范围。

# In[175]:

rng=pd.period_range('2011Q3','2012Q4',freq='Q-JAN')


# In[176]:

rng


# In[177]:

ts=Series(np.arange(len(rng)),index=rng)


# In[178]:

ts


# ## 3、将Timestamp转换为Period（及其反向过程）

# to_period方法可以将时间戳索引的Series和DataFrame对象转换为以是时期索引：

# In[179]:

rng=pd.date_range('1/1/2000',periods=3,freq='M')


# In[180]:

rng


# In[181]:

ts=Series(np.random.randn(3),index=rng)


# In[182]:

ts


# In[183]:

pts=ts.to_period()


# In[184]:

pts


# 时期指的是非重叠区间，因此对于给定的频率，一个时间戳只能属于一个时期

# In[185]:

rng=pd.date_range('1/29/2000',periods=6,freq='D')


# In[186]:

rng


# In[187]:

ts2=Series(np.random.randn(6),index=rng)


# In[188]:

ts2.to_period('M')


# In[189]:

pts.to_timestamp(how='end')


# ## 4、通过数组创建PeriodIndex

# 固定频率的数据通常会将时间信息分开存放在多个列中

# In[190]:

data=pd.read_csv('D:/PythonDataAnalysis/ch10/macrodata.csv')


# In[191]:

data


# In[192]:

data.year


# In[193]:

data.quarter


# In[194]:

index=pd.PeriodIndex(year=data.year,quarter=data.quarter,freq='Q-DEC')


# In[195]:

index


# In[196]:

data.index=index


# In[197]:

data.infl


# # 六、重采样及频率转换

# 重采样指的是将时间序列从一个序列转换到另一个频率的处理过程。高频率数据聚合到低频率称为降采样，反之称为升采样。但并不都是这两种。pandas对象的resample方法是各种频率转换工作的主力函数

# In[198]:

rng=pd.date_range('1/1/2000',periods=100,freq='D')


# In[199]:

ts=Series(np.random.randn(100),index=rng)


# In[200]:

ts


# In[201]:

ts.resample('M',how='mean')


# In[202]:

ts.resample('M',how='mean',kind='period')


# ![_auto_0](attachment:_auto_0)

# ![_auto_0](attachment:_auto_0)

# ## 1、降采样

# 降采样时考虑：
# + 各区间哪边是聚合的
# + 如何标记各个聚合面元，用区间的开头还是末尾

# In[203]:

rng=pd.date_range('1/1/2000',periods=12,freq='T')


# In[204]:

ts=Series(np.arange(12),index=rng)


# In[205]:

ts


# In[206]:

ts.resample('5min',how='sum',closed='right')


# In[207]:

ts.resample('5min',how='sum',closed='left')


# In[208]:

ts.resample('5min',how='sum',closed='left',label='left')


# ![_auto_0](attachment:_auto_0)

# In[209]:

ts.resample('5min',how='sum',loffset='-1s')


# ## 2、OHLC采样（open，high，low，close）

# In[210]:

ts


# In[211]:

ts.resample('5min',how='ohlc')


# ## 3、通过groupby进行重采样

# In[212]:

rng=pd.date_range('1/1/2000',periods=100,freq='D')


# In[213]:

ts=Series(np.arange(100),index=rng)


# In[214]:

ts


# In[215]:

ts.groupby(lambda x: x.month).mean()


# In[216]:

ts.groupby(lambda x: x.weekday).mean()


# ## 4、升采样和插值

# In[217]:

frame=DataFrame(np.random.randn(2,4),
                index=pd.date_range('1/1/2000',periods=2,freq='W-WED'),
                columns=['Colorado','Texas','New York','Ohio'])


# In[218]:

frame


# In[219]:

df_daily=frame.resample('D')


# In[220]:

df_daily


# In[221]:

frame.resample('D',fill_method='ffill')


# In[222]:

frame.resample('D',fill_method='ffill',limit=2)


# In[223]:

frame.resample('W-THU',fill_method='ffill')


# ## 5、通过时期进行重采样

# In[224]:

frame=DataFrame(np.random.randn(24,4),
                index=pd.period_range('1-2000','12-2001',freq='M'),
                columns=['Colorado','Texas','New York','Ohio'])


# In[225]:

frame


# In[226]:

annual_frame=frame.resample('A-DEC',how='mean')


# In[227]:

annual_frame


# In[228]:

# Q-DEC:季度型（每年以12月结束）
annual_frame.resample('Q-DEC',fill_method='ffill')


# In[229]:

# Q-DEC:季度型（每年以12月结束）
annual_frame.resample('Q-DEC',fill_method='ffill',convention='start')
#convention默认参数是end


# + 降采样中，目标频率是源频率的子时期
# + 升采样中，目标频率是源频率的超时期

# In[230]:

annual_frame.resample('Q-MAR',fill_method='ffill')


# # 七、时间序列绘图

# In[231]:

close_px_all=pd.read_csv('D:/PythonDataAnalysis/ch10/stock_px.csv',parse_dates=True,index_col=0)


# In[232]:

close_px_all


# In[233]:

close_px=close_px_all[['AAPL','MSFT','XOM']]


# In[234]:

close_px=close_px.resample('B',fill_method='ffill')


# In[235]:

close_px


# In[236]:

close_px['AAPL'].plot()


# In[237]:

import matplotlib.pyplot as plt


# In[238]:

plt.show()


# In[239]:

close_px.ix['2009'].plot()


# In[240]:

plt.show()


# In[241]:

close_px['AAPL'].ix['01-2011':'03-2011'].plot()


# In[242]:

plt.show()


# In[243]:

appl_q=close_px['AAPL'].resample('Q-DEC',fill_method='ffill')


# In[244]:

appl_q.ix['2009':].plot()


# In[245]:

plt.show()


# # 八、移动窗口函数

# 在移动窗口（可带有指数衰减权数）上计算的各种统计函数也是一类常见于时间序列的数组变换。将其称为移动窗口函数，还包括那些窗口不定长的函数。移动窗口函数会自动排除缺失值

# In[246]:

close_px.AAPL.plot()


# In[247]:

plt.show()


# rolling_mean是其中最简单的一个，接受一个TimeSeries或DataFrame以及一个window（表示期数）

# In[248]:

pd.rolling_mean(close_px.AAPL,250).plot()


# In[249]:

plt.show()


# In[250]:

appl_std250=pd.rolling_std(close_px.AAPL,250,min_periods=10)


# In[251]:

appl_std250[5:12]


# In[252]:

appl_std250.plot()


# In[253]:

plt.show()


# 计算扩展窗口平均，可将扩展窗口看做是一个特殊的窗口，其长度与时间序列一样，但只需一期或多期即可计算一个值

# In[254]:

expanding_mean=lambda x:rolling_mean(x,len(x),min_periods=1)


# In[255]:

pd.rolling_mean(close_px,60).plot(logy=True)


# In[256]:

plt.show()


# ![_auto_0](attachment:_auto_0)

# ## 1、指数加权函数

# 另一种使用固定大小窗口及相等权数观测值得方法是，定义一个衰减因子常量，以便是近期的观测值拥有更大的权数

# In[257]:

fig,axes=plt.subplots(nrows=2,ncols=1,sharex=True,sharey=True,figsize=(12,7))


# In[258]:

aapl_px=close_px.AAPL['2005':'2009']


# In[259]:

ma60=pd.rolling_mean(aapl_px,60,min_periods=50)


# In[260]:

ewma60=pd.ewma(aapl_px,span=60)


# In[261]:

aapl_px.plot(style='k-',ax=axes[0])


# In[262]:

ma60.plot(style='k--',ax=axes[0])


# In[263]:

ewma60.plot(style='k-',ax=axes[1])


# In[264]:

aapl_px.plot(style='k--',ax=axes[1])


# In[265]:

axes[0].set_title('Simple MA')


# In[266]:

axes[1].set_title('Exponentially-weighted MA')


# In[267]:

plt.show()


# ## 2、二元移动窗口函数

# In[268]:

spx_px=close_px_all['SPX']


# In[269]:

spx_rets=spx_px/spx_px.shift(1)-1


# In[270]:

returns=close_px.pct_change()


# In[271]:

corr=pd.rolling_corr(returns.AAPL,spx_rets,125,min_periods=100)


# In[272]:

corr.plot()


# In[273]:

plt.show()


# In[274]:

corr=pd.rolling_corr(returns,spx_rets,125,min_periods=100)


# In[275]:

corr.plot()


# In[276]:

plt.show()


# ## 3、用户定义的移动窗口函数

# rolling_apply函数能使你在移动窗口上应用自己设计的数组函数，该函数要能从数组的各个片段中产生单个值（即约简）

# In[277]:

from scipy.stats import percentileofscore


# In[278]:

score_at_2percent=lambda x:percentileofscore(x,0.02)


# In[279]:

result=pd.rolling_apply(returns.AAPL,250,score_at_2percent)


# In[280]:

result.plot()


# In[281]:

plt.show()


# # 九、性能和内存使用方面的注意事项

# pandas会尽量在多个时间序列之间共享索引，所以创建现有时间序列的视图不会占用更多内存。此外，低频率索引（日以上）会被存放在一个中心缓存中，所以任何固定频率的索引都是该日期缓存的视图

# 性能方面，pandas对数据对齐和重采样运算进行了高度优化。下面例子将一亿个数据点聚合为OHLC：

# In[282]:

rng=pd.date_range('1/1/2000',periods=10000,freq='10ms')


# In[283]:

ts=Series(np.random.randn(len(rng)),index=rng)


# In[284]:

ts


# In[285]:

ts.resample('10s',how='ohlc')


# In[287]:

get_ipython().magic("timeit ts.resample('10s',how='ohlc')")


# 运行时间跟聚合结果的相对大小有一定关系，越高频率的聚合所耗费的时间越多

# In[288]:

rng=pd.date_range('1/1/2000',periods=10000,freq='1s')


# In[289]:

ts=Series(np.random.randn(len(rng)),index=rng)


# In[292]:

ts.resample('10ms',how='ohlc')


# In[293]:

get_ipython().magic("timeit ts.resample('10ms',how='ohlc')")


# In[ ]:



