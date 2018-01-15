# 绘图显示中文
import matplotlib
zhfont1 = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc')
plt.xlabel('性别',fontproperties=zhfont1)
plt.ylabel('人数',fontproperties=zhfont1)
plt.title('直方图',fontproperties=zhfont1)

# Python绘制正态图
cishu=pd.read_csv('house_num.csv')
num=cishu.values
mean=num.mean()
std=num.std()

def normfun(x,mu, sigma):
    pdf = np.exp(-((x - mu)**2) / (2* sigma**2)) / (sigma * np.sqrt(2*np.pi))
    return pdf

# x的范围为1-27，以1为单位,需x根据范围调试
x = np.arange(1, 27,1)

# x数对应的概率密度
y = normfun(x, mean, std)

# 参数,颜色，线宽
plt.plot(x,y, color='g',linewidth = 3)

#数据，数组，颜色，颜色深浅，组宽，显示频率
plt.hist(num, bins =20, color = 'r',alpha=0.5,rwidth= 0.9, normed=True)

import matplotlib
zhfont1 = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc')

plt.title(u'次数',fontproperties=zhfont1)
plt.xlabel('num')
plt.ylabel('Probability')
plt.show()