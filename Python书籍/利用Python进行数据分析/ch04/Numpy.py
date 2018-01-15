
# coding: utf-8

# # numpy

# # 一，NumPy的ndarry：一种多维数组对象

# ## 1，创建ndarray

# In[15]:

import numpy as np
data1=[1,3,6,7,8]
arr1=np.array(data1)
arr1


# In[16]:

data2=[[1,6,7,9],[2,6,8,3]]
arr2=np.array(data2)
arr2


# In[17]:

arr2.ndim
#维数


# In[18]:

arr2.shape
#形状，几行几列


# In[19]:

arr1.dtype
#数据类型


# In[20]:

arr2.dtype


# In[21]:

np.zeros(10)
#生成多少0的数组


# In[22]:

np.ones(10)
#生成多少1的数组


# In[23]:

np.zeros((3,6))


# In[24]:

np.empty((2,3))


# In[25]:

np.arange(10)


# In[26]:

np.eye(10)


# In[27]:

np.identity(4)


# ## 2，ndarray数据类型

# In[28]:

arr3=np.array([1,3,3,4],dtype=np.float64)


# In[29]:

arr3


# In[30]:

arr3.dtype


# In[31]:

arr=np.array([3.43,2.56,-1.74,6.89])
arr


# In[32]:

arr.astype(np.int32)


# In[33]:

arr.dtype


# In[34]:

int_array=np.arange(10)


# In[35]:

calib=np.array([.22,.44,.46,.854,.56],dtype=np.float64)
int_array.astype(calib.dtype)
int_array


# ## 3，数组和标量之间的运算

# **大小相等的数组运算会作用到元素级，不同大小的运算称为广播**

# In[36]:

arr=np.array([[1,3.,5.],[2.,6.,8.]])


# In[37]:

arr


# In[38]:

arr*arr


# In[39]:

arr-arr


# In[40]:

1/arr


# In[41]:

arr**3


# ## 4，基本的索引和切片

# In[42]:

arr=np.arange(10)


# In[43]:

arr


# In[44]:

arr[5]


# In[45]:

arr[5:8]


# In[46]:

arr[5:8]=12


# In[47]:

arr


# **数据切片是原始数组的视图，视图的任何修改都会反映在原始数组上**

# In[48]:

arr_slice=arr[5:8]


# In[49]:

arr_slice[1]=12345


# In[50]:

arr


# In[51]:

arr_slice[:]=456


# In[52]:

arr


# In[53]:

arr2d=np.array([[1,2,3],[4,5,6],[7,8,9]])


# In[54]:

arr2d[2]


# In[55]:

arr2d[0][2]
arr2d[0,2]
#两者等价


# In[56]:

arr3d=np.array([[[1,2,3],[4,4,6]],[[7,8,9],[10,11,12]]])


# In[57]:

arr3d


# In[58]:

arr3d[0]


# In[59]:

old_values=arr3d[0].copy()
#复制


# In[60]:

arr3d[0]=34


# In[61]:

arr3d[0]


# In[62]:

arr3d


# In[63]:

arr3d[0]=old_values


# In[64]:

arr3d


# In[65]:

arr3d[1,0]


# In[66]:

arr


# ## 5，切片索引

# In[67]:

arr[1:6]


# In[68]:

arr2d


# In[69]:

arr2d[:2]


# In[70]:

arr2d[:2,1:]


# In[71]:

arr2d[1,:2]


# In[72]:

arr2d[2,1:]


# In[73]:

arr2d[:,:2]


# In[74]:

arr2d[:2,1:]=1


# In[75]:

arr2d


# ## 6，布尔型索引

# In[76]:

names=np.array(['xutao','jack','tom','xutao','tom','jack','jack'])


# In[77]:

data=np.random.randn(7,4)
#注意不是双括号


# In[78]:

names


# In[79]:

data


# In[80]:

names=='jack'


# In[81]:

data[names=='jack']


# In[82]:

data[names=='jack',2:]


# In[83]:

data[names=='jack',3]


# In[84]:

names!='jack'


# In[85]:

data[-(names=='jack')]


# In[86]:

mask=(names=='jack')|(names=='xutao')


# In[87]:

mask


# In[88]:

data[data<0]=0


# In[89]:

data


# In[90]:

data[names!='jack']=7


# In[91]:

data


# ## 7，花式索引

# ***好好理解***

# In[92]:

arr=np.empty((8,4))


# In[93]:

for i in np.arange(8):
    arr[i]=i


# In[94]:

arr


# In[95]:

arr[[4,3,1,5]]


# In[96]:

arr[[-3,-4,-2]]


# In[97]:

arr=np.arange(32).reshape(8,4)


# In[98]:

arr


# In[99]:

arr[[1,5,7,2],[0,3,1,2]]


# In[100]:

arr[[1,5,7,2]][:,[0,3,1,2]]


# In[101]:

arr[np.ix_([1,5,7,2],[0,3,1,2])]


# ## 8，数组转置和轴对换

# In[102]:

arr=np.arange(15).reshape(3,5)


# In[103]:

arr


# In[104]:

arr.T


# In[105]:

arr=np.random.randn(6,3)


# In[106]:

np.dot(arr.T,arr)


# In[107]:

arr=np.arange(16).reshape((2,2,4))


# In[108]:

arr


# In[109]:

arr.transpose((1,0,2))


# In[110]:

arr


# In[111]:

arr.swapaxes(1,2)


# **swapaxes也是返回原数组的视图**

# # 二，通用数组：快速的元素级数组函数

# In[112]:

arr=np.arange(10)


# In[113]:

np.sqrt(arr)


# In[114]:

np.exp(arr)


# In[115]:

x=np.random.randn(8)


# In[116]:

y=np.random.randn(8)


# In[117]:

x


# In[118]:

y


# In[119]:

np.maximum(x,y)


# In[120]:

arr=np.random.randn(7)*5


# In[121]:

arr


# In[122]:

np.modf(arr)
#将数组的小数，整数部分以两个数组表示出来


# In[123]:

np.abs(-1+i)


# In[124]:

np.fabs(-44)


# In[125]:

np.log1p(9)
#等于log(1+x)


# In[126]:

np.log(10)
#自然对数（以e为底）


# In[127]:

np.log10(10)


# In[128]:

np.log2(10)


# In[129]:

np.sign(1)
#计算元素正负号


# In[130]:

np.sign(0)


# In[131]:

np.sign(-33)


# In[132]:

np.ceil(9.5555)


# In[133]:

np.floor(9.555)


# In[134]:

np.rint(4.5)


# In[135]:

np.rint(4.4)


# In[136]:

a=np.array([1,2,3,4,5])


# In[137]:

b=np.array([-1,-4,7,-9,8])


# In[138]:

np.add(a,b)


# In[139]:

np.subtract(a,b)


# In[140]:

np.multiply(a,b)


# In[141]:

np.divide(a,b)


# In[142]:

np.power(a,np.abs(b))


# In[143]:

np.copysign(a,b)


# In[144]:

np.greater(a,b)
#大于


# In[145]:

np.greater_equal(a,b)
#大于等于


# In[146]:

np.less(a,b)
#小于


# In[147]:

np.less_equal(a,b)
#小于等于


# In[148]:

np.equal(a,b)


# In[149]:

np.not_equal(a,b)


# In[150]:

np.logical_not(a)


# In[151]:

np.logical_and(a,b)


# In[152]:

np.logical_or(a,b)


# In[153]:

np.logical_xor(a,b)


# # 三，利用数组进行数据处理

# In[154]:

points=np.arange(-5,5,0.01)


# In[155]:

xs,ys=np.meshgrid(points,points)


# In[156]:

ys


# In[157]:

import matplotlib.pyplot as plt


# In[158]:

z=np.sqrt(xs**2+ys**2)


# In[159]:

z


# In[160]:

plt.imshow(z,cmap=plt.cm.gray);plt.colorbar()


# In[161]:

plt.title("Image plot of $\sqrt{x^2+y^2}$ for a grid values")


# ## 1，将条件逻辑转换为数组运算

# In[162]:

xarr=np.array([1.1,1.2,1.3,1.4,1.5])


# In[163]:

yarr=np.array([2.1,2.2,2.3,2.4,2.5])


# In[164]:

cond=np.array([True,False,True,True,False])


# In[165]:

result=np.where(cond,xarr,yarr)
#是x if condition else y 的矢量化版本


# In[166]:

result


# In[167]:

arr=np.random.randn(4,4)
#返回标准正态分布的随机数，括号中代表维度


# In[168]:

arr


# In[169]:

np.where(arr>0,2,-2)


# In[170]:

result=[]


# In[171]:

conda1=[1,3,0,8,0,0]
conda2=[0,2,3,3,0,1]


# In[172]:

np.where(conda1 and conda2,0,
        np.where(conda1,1,
                np.where(conda2,2,3)))


# ## 2，数学和统计方法

# In[173]:

arr=np.random.randn(5,4)
arr


# In[174]:

arr.mean()


# In[175]:

np.mean(arr)


# In[176]:

arr.sum()


# In[177]:

arr.mean(axis=0)
#行压缩


# In[178]:

arr.mean(axis=1)
#列压缩


# In[179]:

arr=np.array([[0,1,5],[2,3,7],[6,7,3]])
arr


# In[180]:

arr.cumsum(0)
#行相加，第二行等于前两行相加，第三行等于前三行相加


# In[181]:

arr.cumsum(1)
#列相加，第二列等于前两列相加，第三列等于前三列相加


# In[182]:

arr.cumprod(0)
#行相乘


# In[183]:

arr.cumprod(1)
#列相乘


# In[184]:

arr.std()
#标准差，自由度可调（默认n）


# In[185]:

arr.var()
#方差，自由度可调（默认n）


# In[186]:

arr.min()


# In[187]:

arr.max()


# In[188]:

arr.argmin()
#最小值索引


# In[189]:

arr.argmax()
#最大值索引


# ## 3，用于布尔型数组的方法

# **上面方法中布尔值会被强制转换为0或1，因此sum经常用来对布尔型数组的True值进行计算**

# In[190]:

arr=np.random.randn(100)


# In[191]:

(arr>0).sum()


# In[192]:

bools=np.array([True,True,False,False])


# In[193]:

bools.any()
#是否有一个或多个True


# In[194]:

bools.all()
#是否全为True


# ## 4，排序

# In[195]:

arr=np.random.randn(8)


# In[196]:

arr


# In[197]:

arr.sort()


# In[198]:

arr


# In[199]:

arr=np.random.randn(5,3)


# In[200]:

arr


# In[201]:

arr.sort(1)
#列排序


# In[202]:

arr


# In[203]:

arr.sort(0)
#行排序


# In[204]:

arr


# In[205]:

large_arr=np.random.randn(1000)


# In[206]:

large_arr.sort()


# In[207]:

large_arr[int(0.05*len(large_arr))]
#  %5分位数


# ## 5，唯一化以及其他的集合逻辑

# In[208]:

names=['bob','joe','will','bob','will','joe','joe']


# In[209]:

np.unique(names)
#返回唯一值


# In[210]:

values=np.array([8,4,5,4,0,0,4,3])


# In[211]:

np.in1d(values,[4,3,2])
#用来测试一个数组的值在另一个数组的成员资格


# In[212]:

x=np.array([1,4,5,7,2,2])


# In[213]:

y=np.array([2,5,6,9,2,1])


# In[214]:

np.intersect1d(x,y)
#返回两个数组共有的元素（有序）


# In[215]:

np.union1d(x,y)
#返回两个数组并集（有序）


# In[216]:

np.setdiff1d(x,y)
#数组的差，即元素在x中不在y中


# In[217]:

np.setxor1d(x,y)
#数组的对称差，即在一个数组中不在两个数组中


# # 四，用于数组的文件输入输出

# ## 1，将数组以二进制格式保存到磁盘

# **np.save和np.load是读取磁盘数组数据的两个主要函数**

# In[218]:

arr=np.arange(10)


# In[219]:

arr


# In[220]:

np.save('some_arr',arr)


# In[221]:

np.load('some_arr.npy')
#文件名格式为npy


# **np.savez()可以将多个数组保存到一个压缩文件中，将数组以关键字形式传入即可**

# In[222]:

np.savez('arr_arch.npz',a=arr,b=arr)


# In[223]:

arch=np.load('arr_arch.npz')
#文件名格式为npz


# In[224]:

arch['a']


# In[225]:

arch['b']


# ## 2，存取文本文件

# **参考后面内容**

# # 五，线性代数

# In[226]:

import numpy as np


# In[227]:

x=np.array([[1.,2.,3.],[4.,5.,6.]])


# In[228]:

y=np.array([[6.,23.],[-1.,7],[8.,9]])


# In[229]:

x


# In[230]:

y


# In[231]:

x.dot(y)
#点乘


# In[232]:

np.dot(x,y)
#点乘


# In[233]:

np.dot(x,np.ones(3))


# In[234]:

from numpy.linalg import inv,qr


# In[235]:

x=np.array([[1,2,3,4],[2,3,4,5],[3,-4,5,-6],[5,-6,-7,8]])


# In[236]:

x


# In[237]:

x.T
#转置


# In[238]:

inv(x)
#计算矩阵的逆


# In[239]:

x.dot(inv(x))


# In[240]:

q,r=qr(x)


# In[241]:

q


# In[242]:

r


# ### 常用的numpy.linalg函数

# + diag：以一维数组形式返回方阵的对角线元素，或者将一维数组转换为方阵（非对角线元素为0）
# + dot：矩阵点乘
# + det：计算矩阵行列式
# + eig：计算方阵的本征值和本征向量
# + inv：计算方阵的逆
# + pinv：计算矩阵的Moore-Penrose伪逆
# + qr：计算QR分解
# + svd：计算奇异值分解（SVD）
# + solve：解线性方程组Ax=b，A为一个方阵
# + lstsq：计算Ax=b的最小二乘解

# In[243]:

import numpy as np
from numpy.linalg import *
np.linalg.det([[1,2],[2,3]])


# In[244]:

x=np.array([[1,3,2],[2,3,4],[6,8,4]])
x


# In[245]:

np.linalg.eig(x)


# # 六，随机数生成

# In[246]:

samples=np.random.randn(4,4)


# In[247]:

samples


# In[248]:

samples=np.random.normal(3)


# In[249]:

samples


# In[250]:

np.random.randint(0,2)
#从给定的上下限范围内选取随机整数，不包括后者


# In[251]:

np.random.rand(5)
#产生均匀分布的样本


# In[252]:

np.random.binomial(4,0.5)
#产生二项分布的样本值，第二个参数为概率


# In[253]:

np.random.uniform()
#产生[0,1)均匀分布的样本值


# # 七，范例：随机漫步

# In[254]:

#纯Python方式实现1000步漫步
positions=0
walk=[positions]
steps=1000
for i in np.arange(steps):
    step=1 if np.random.randint(0,2) else -1
    positions += step
    walk.append(positions)


# In[255]:

#随机数实现
nstep=1000
draw=np.random.randint(0,2,size=nstep)
steps=np.where(draw>0,1,-1)
walk=steps.cumsum()


# In[256]:

walk.min()


# In[257]:

walk.max()


# In[258]:

#计算多久到距离初始点（0）10步远
(np.abs(walk>=10)).argmax()


# ## 一次模拟多个随机漫步

# In[259]:

mwalks=5000
msteps=1000
draws=np.random.randint(0,2,size=(msteps,mwalks))
steps=np.where(draws>0,1,-1)
walks=steps.cumsum(1)


# In[260]:

walks


# In[261]:

walks.max()


# In[262]:

walks.min()


# In[263]:

#计算30,或-30的穿越时间
his30=(np.abs(walks)>=30).any(0)


# In[264]:

his30


# In[265]:

his30.sum()

