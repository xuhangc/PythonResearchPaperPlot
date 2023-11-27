
"""
编写时间：2022年2月06日 11：20

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。

代码中Proplot包绘制的部分可能与Matplotlib绘制不同，需注意两者绘图语法的不同~~

"""
#注意：本案例中引入的SciencePlots库主题方式会随着SciencePlots版本的更新发生改变，读者还需参考其官网引入的正确方式。
#      建议按照官网引入方式进行操作和使用最新版本的ScienePlots。如引入方式发生改变，请关注微信公众号【DataCharm】进行实时获取代码更新。



# a）Matplotlib中经验分布函数图的属性添加示例
import numpy as np
import pandas as pd
import seaborn as sns
from statsmodels.distributions.empirical_distribution import ECDF

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

# fit a ecdf
ecdf = ECDF(ecdf_data)
fig,ax = plt.subplots(figsize=(4.5,3.5),dpi=100,facecolor="w")
ax.plot(ecdf.x, ecdf.y,color="#2FBE8F",lw=1.5,label="ECDF")
#第二条ecdf线
ecdf_full = ECDF(np.random.normal(loc = ecdf_data.mean(), 
                                        scale = ecdf_data.std(), 
                                        size = 100000))
ax.plot(ecdf_full.x,ecdf_full.y,"k",lw=1)

xs = ecdf.x
ys = ecdf.y
percent_values = [.25,.50,.75]
# 循环绘制
for p in percent_values:
    value = xs[np.where(ys > p)[0][0] - 1]
    pvalue = ys[np.where(ys > p)[0][0] - 1]
    ax.scatter(value,pvalue,s=30,color="#2FBE8F",ec="k",zorder=3)
    ax.hlines(y=p, xmin=0, xmax = value,color="r",ls="--",lw=1)
    ax.text(x=value/3,y=pvalue+.05,s=f'{int(100*p)}%',color="r",va="center")
    ax.vlines(x=value, ymin=0, ymax = pvalue,color="r",ls="--",lw=1)
    ax.text(x = value+.5, y = 0.02,s = f'{value:.1f}',color="r",ha="left")

ax.scatter(value,pvalue,color="#2FBE8F",ec="k",label="Test Point")
ax.set_xlim(0,max(ecdf_data)+2)
ax.set_ylim(0,1.05)
ax.set_ylabel('Percentile')
ax.set_xlabel('Normal Distribution Values')
ax.set_title('ECDF of Normal Distribution',fontsize=16)
ax.legend(fontsize=9)
fig.savefig('\第3章 单变量图形的绘制\图3-2-18 正态分布数据的经验分布函数图属性添加绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第3章 单变量图形的绘制\图3-2-18 正态分布数据的经验分布函数图属性添加绘制示例_a.png', 
            bbox_inches='tight',dpi=300) 
plt.show() 
            
           
#b）ProPlot中经验分布函数图的属性添加示例          

import numpy as np
import pandas as pd
import seaborn as sns
import statsmodels.api as sm
import proplot as pplt
from statsmodels.distributions.empirical_distribution import ECDF

from proplot import rc
rc["axes.labelsize"] = 11
rc['tick.labelsize'] = 10
rc["suptitle.size"] = 12


#生成数据
data1 = np.random.normal(loc=20, scale=5, size=400)
data2 = np.random.normal(loc=40, scale=5, size=800)
ecdf_data = np.hstack((data1, data2))


ecdf = ECDF(ecdf_data)
#第二条ecdf线
ecdf_full = ECDF(np.random.normal(loc = ecdf_data.mean(), 
                                        scale = ecdf_data.std(), 
                                        size = 100000))
                                        
                                        
fig = pplt.figure(figsize=(3.5,3))
ax = fig.subplot()
ax.format(abc='a.', abcloc='ur',abcsize=16,xlim=(0,55),
          xlabel='Normal Distribution Values', ylabel='Percentile',
          suptitle='ECDF of Normal Distribution')
ax.plot(ecdf.x, ecdf.y,color="#2FBE8F",lw=1.5,label="ECDF")
ax.plot(ecdf_full.x,ecdf_full.y,"k",lw=1)

xs = ecdf.x
ys = ecdf.y
percent_values = [.25,.50,.75]
# 循环绘制
for p in percent_values:
    value = xs[np.where(ys > p)[0][0] - 1]
    pvalue = ys[np.where(ys > p)[0][0] - 1]
    ax.scatter(value,pvalue,s=30,color="#2FBE8F",ec="k",zorder=3)
    ax.hlines(y=p, x1=0, x2=value,color="r",ls="--",lw=1)
    ax.text(x=value/3,y=pvalue+.05,s=f'{int(100*p)}%',color="r",va="center")
    ax.vlines(x=value, y1=0, y2=pvalue,color="r",ls="--",lw=1)
    ax.text(x = value+.5, y = 0.02,s = f'{value:.1f}',color="r",ha="left")
ax.scatter(value,pvalue,color="#2FBE8F",ec="k",label="Test Point")
ax.legend(ncols=1,loc='ul')

fig.savefig('\第3章 单变量图形的绘制\图3-2-18 正态分布数据的经验分布函数图属性添加绘制示例_b.pdf',bbox_inches='tight')
fig.savefig('\第3章 单变量图形的绘制\图3-2-18 正态分布数据的经验分布函数图属性添加绘制示例_b.png', 
            bbox_inches='tight',dpi=300) 
plt.show() 

