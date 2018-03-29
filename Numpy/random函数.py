
# coding: utf-8

# 在使用Python进行数据处理时，往往需要用到大量的随机数据，那如何构造这么多数据呢？Python的第三方库numpy库中提供了random函数来实现这个功能。 
# 本文将根据官方文档以及其他博友的博客一起来谈论常见的random函数以及使用

# 首先说下**numpy.random.seed()**与**numpy.random.RandomState()**这两个在数据处理中比较常用的函数，两者实现的作用是一样的，都是使每次随机生成数一样，具体可见下图

# In[1]:

import numpy as np


# In[5]:

np.random.seed(10)


# In[6]:

np.random.rand(8)


# In[7]:

np.random.seed(10)


# In[8]:

np.random.rand(8)


# In[9]:

rng=np.random.RandomState(10)


# In[10]:

rng.rand(8)


# In[11]:

rng=np.random.RandomState(10)


# In[12]:

rng.rand(8)


# ## 1.numpy.random.rand() 

# 官方文档中给出的用法是：numpy.random.rand(d0,d1,…dn) 以给定的形状创建一个数组，并在数组中加入在[0,1]之间均匀分布的随机样本。

# In[14]:

np.random.rand(2,3)


# ## 2.numpy.random.randn() 

# 官方文档中给出的用法是：numpy.random.rand(d0,d1,…dn) 
# 以给定的形状创建一个数组，数组元素来符合标准正态分布N(0,1) 
# 若要获得一般正态分布这里写图片描述则可用sigma * np.random.randn(…) + mu进行表示

# In[15]:

np.random.randn(2,3)


# ## 3.numpy.random.randint() 

# 官方文档中给出的用法是：numpy.random.randint(low,high=None,size=None,dtype) 生成在**半开半闭区间[low,high)**上离散均匀分布的整数值;若high=None，则取值区间变为[0,low) 

# In[16]:

np.random.randint(5,size=(2,3))


# In[22]:

np.random.randint(2,5,size=(3,2))


# ## 4.numpy.random.random_integers() 

# 官方文档中给出的用法是： numpy.random.random_integers(low,high=None,size=None) 生成**闭区间[low,high]**上离散均匀分布的整数值;若high=None，则取值区间变为[1,low] 
# 用法及实现 

# In[18]:

np.random.random_integers(5,size=(2,3))


# In[21]:

np.random.random_integers(2,5,size=(2,3))


# 此外，若要将【a,b】区间分成N等分，也可以用此函数实现 
# **a+(b-a)*(numpy.random.random_integers(N)-1)/(N-1)**

# ## 5.numpy.random_sample()

# 官方文档中给出的用法是： numpy.random.random_sample(size=None) 以给定形状返回[0,1)之间的随机浮点数 

# In[23]:

np.random.random_sample(size=(2,3))


# In[24]:

np.random.random_sample()


# 其他函数，numpy.random.random() ;numpy.random.ranf() numpy.random.sample()用法及实现都与它相同

# ## 6.numpy.random.choice() 

# 官方文档中给出的用法： numpy.random.choice(a,size=None,replace=True,p=None) 若a为数组，则从a中选取元素；若a为单个int类型数，则选取range(a)中的数 replace是bool类型，为True，则选取的元素会出现重复；反之不会出现重复 p为数组，里面存放选到每个数的可能性，即概率 

# In[25]:

np.random.choice(5,size=4,replace=True,p=[0.1,0.1,0.3,0.4,0.1])


# In[26]:

np.random.choice(5,size=4,replace=False,p=[0.1,0.1,0.3,0.4,0.1])


# In[ ]:



