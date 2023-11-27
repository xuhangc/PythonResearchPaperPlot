
"""
编写时间：2022年4月10日 15：50

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

"""
该运行代码为Seaborn绘制结果
"""

import pandas as pd
import numpy as np
import seaborn as sns
from numpy import mean
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["axes.linewidth"] = .8
plt.rcParams["axes.labelsize"] = 15
plt.rcParams["xtick.minor.visible"] = False
plt.rcParams["ytick.minor.visible"] = True
plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"
plt.rcParams["xtick.labelsize"] = 12
plt.rcParams["ytick.labelsize"] = 12
plt.rcParams["xtick.top"] = False
plt.rcParams["ytick.right"] = False


tips = sns.load_dataset("tips")
# a）基本线图示例

colors = ["#2FBE8F","#459DFF","#FF5B9B","#FFCC37"]
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
lineplot = sns.pointplot(x="day", y="total_bill", data=tips,scale=1.1,estimator=mean,ci=None,errwidth=1.5,
                        color='k',ax=ax,zorder=2)
ax.set_ylim(15,23)
ax.set_xlabel("Time")
ax.set_ylabel("Values")

fig.savefig('\第4章 双变量图形的绘制\图4-1-5 利用pointplot()函数绘制的类别折线图示例_a.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-5 利用pointplot()函数绘制的类别折线图示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# b）线图+SE估计

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
lineplot = sns.pointplot(x="day", y="total_bill", data=tips,siestimator=mean,ci=68,errwidth=1,
                         capsize=.2,color='k',ax=ax)
ax.set_xlabel("Time")
ax.set_ylabel("Values")
fig.savefig('\第4章 双变量图形的绘制\图4-1-5 利用pointplot()函数绘制的类别折线图示例_b.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-5 利用pointplot()函数绘制的类别折线图示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# c）线图+SD估计

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
lineplot = sns.pointplot(x="day", y="total_bill", data=tips,siestimator=mean,ci="sd",errwidth=1,
                         capsize=.2,color='k',ax=ax)
ax.set_xlabel("Time")
ax.set_ylabel("Values")
fig.savefig('\第4章 双变量图形的绘制\图4-1-5 利用pointplot()函数绘制的类别折线图示例_c.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-5 利用pointplot()函数绘制的类别折线图示例_c.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# d）线图+CI估计

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
lineplot = sns.pointplot(x="day", y="total_bill", data=tips,siestimator=mean,ci=95,errwidth=1,
                         capsize=.2,color='k',ax=ax)
ax.set_xlabel("Time")
ax.set_ylabel("Values")
fig.savefig('\第4章 双变量图形的绘制\图4-1-5 利用pointplot()函数绘制的类别折线图示例_d.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-5 利用pointplot()函数绘制的类别折线图示例_d.png', 
            bbox_inches='tight',dpi=300)
plt.show()