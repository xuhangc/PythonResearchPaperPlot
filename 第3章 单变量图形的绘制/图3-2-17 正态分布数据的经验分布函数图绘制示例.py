
"""
编写时间：2022年2月06日 11：20

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。

代码中Proplot包绘制的部分可能与Matplotlib绘制不同，需注意两者绘图语法的不同~~

"""
#注意：本案例中引入的SciencePlots库主题方式会随着SciencePlots版本的更新发生改变，读者还需参考其官网引入的正确方式。
#      建议按照官网引入方式进行操作和使用最新版本的ScienePlots。如引入方式发生改变，请关注微信公众号【DataCharm】进行实时获取代码更新。


import numpy as np
import pandas as pd
import seaborn as sns
import statsmodels.api as sm
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["axes.linewidth"] = 1
plt.rcParams["axes.labelsize"] = 15
plt.rcParams["xtick.minor.visible"] = True
plt.rcParams["ytick.minor.visible"] = True
plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"
plt.rcParams["xtick.labelsize"] = 12
plt.rcParams["ytick.labelsize"] = 12
plt.rcParams["xtick.top"] = True
plt.rcParams["ytick.right"] = True

#生成数据
data1 = np.random.normal(loc=20, scale=5, size=400)
data2 = np.random.normal(loc=40, scale=5, size=800)
ecdf_data = np.hstack((data1, data2))

# a）双峰正态分布直方图
ecdf_data_df = pd.Series(ecdf_data)

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
ecdf_data_df.plot.kde(ax=ax, color="r",lw=1,legend=False)
ecdf_data_df.plot.hist(density=True,color="#2FBE8F",ec="k",lw=.5,bins=20,ax=ax)
ax.set_ylabel('Frequency')
ax.set_xlabel('Values')
fig.savefig('\第3章 单变量图形的绘制\图3-2-17 正态分布数据的经验分布函数图绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第3章 单变量图形的绘制\图3-2-17 正态分布数据的经验分布函数图绘制示例_a.png', 
            bbox_inches='tight',dpi=300) 
plt.show() 

# b）利用seaborn库中的ecdfplot()函数绘制的经验分布函数图

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
sns.ecdfplot(x=ecdf_data,color="#2FBE8F",ax=ax)
ax.set_xlabel('Normal Distribution Values')
ax.set_ylim(-.05,1.05)
fig.savefig('\第3章 单变量图形的绘制\图3-2-17 正态分布数据的经验分布函数图绘制示例_b.pdf',bbox_inches='tight')
fig.savefig('\第3章 单变量图形的绘制\图3-2-17 正态分布数据的经验分布函数图绘制示例_b.png', 
            bbox_inches='tight',dpi=300) 
plt.show() 

# c）利用statsmodels库中的ECDF()函数绘制的经验分布函数图

from statsmodels.distributions.empirical_distribution import ECDF
# fit a cdf
ecdf = ECDF(ecdf_data)
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
ax.plot(ecdf.x, ecdf.y,color="#2FBE8F",lw=1.5)
ax.set_ylabel('Percentile')
ax.set_xlabel('Normal Distribution Values')
fig.savefig('\第3章 单变量图形的绘制\图3-2-17 正态分布数据的经验分布函数图绘制示例_c.pdf',bbox_inches='tight')
fig.savefig('\第3章 单变量图形的绘制\图3-2-17 正态分布数据的经验分布函数图绘制示例_c.png', 
            bbox_inches='tight',dpi=300) 
plt.show() 

