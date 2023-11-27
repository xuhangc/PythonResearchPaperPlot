
"""
编写时间：2022年4月10日 16：40

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

# a）利用seaborn 绘制的点带图（jitter= 0.1）

colors = ["#2FBE8F","#459DFF","#FF5B9B","#FFCC37"]
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
stripplot = sns.stripplot(x="day", y="total_bill", data=tips,palette=colors,size=6,edgecolor="k",
                         linewidth=.6)
ax.set_xlabel("Time")
ax.set_ylabel("Values")

fig.savefig('\第4章 双变量图形的绘制\图4-1-6 点带图、分簇散点图的绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-6 点带图、分簇散点图的绘制示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# b）利用seaborn绘制的点带图（jitter=0.2）

colors = ["#2FBE8F","#459DFF","#FF5B9B","#FFCC37"]
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
stripplot = sns.stripplot(x="day", y="total_bill", data=tips,palette=colors,size=6,edgecolor="k",
                         linewidth=.6,marker="s",jitter=.2)
ax.set_xlabel("Time")
ax.set_ylabel("Values")
fig.savefig('\第4章 双变量图形的绘制\图4-1-6 点带图、分簇散点图的绘制示例_b.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-6 点带图、分簇散点图的绘制示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# c）利用seaborn绘制的分簇散点图

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
ax = sns.swarmplot(x="day", y="total_bill", data=tips,palette=colors,edgecolor="k",
                   linewidth=.6,size=4)
ax.set_xlabel("Time")
ax.set_ylabel("Values")

fig.savefig('\第4章 双变量图形的绘制\图4-1-6 点带图、分簇散点图的绘制示例_c.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-6 点带图、分簇散点图的绘制示例_c.png', 
            bbox_inches='tight',dpi=300)
plt.show()
