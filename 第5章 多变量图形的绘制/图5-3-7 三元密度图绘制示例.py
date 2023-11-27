"""
编写时间：2022年4月16日 09：30

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

"""
此代码为使用Python-Prolot包进行学术风格图表绘制，绘图语法和Matplotlib有所不同，需注意。

"""
import scipy
import mpltern
import pandas as pd
import numpy as np
import proplot as pplt
import seaborn as sns
import matplotlib.pyplot as plt
from colormaps import parula

from proplot import rc
rc["font.family"] = "Times New Roman"
rc["axes.labelsize"] = 15
rc["tick.labelsize"] = 12
rc["suptitle.size"] = 15
rc["title.size"] = 14


ternary_den = pd.read_csv(r"\第5章 多变量图形的绘制\Ternary Density Scatter.csv")
trivar = ["SiO2", "MgO", "TiO2"]
tridat = ternary_den.loc[:, trivar]

t = tridat["SiO2"]
l = tridat["MgO"]
r = tridat["TiO2"]

# 计算高斯估计
den_data = tridat.to_numpy()
K2 = scipy.stats.gaussian_kde(den_data.T, bw_method=None)
zi2 = K2(den_data.T)
zi2 = zi2.reshape(den_data.shape[0])

# 获取数值大小排序
idx = zi2.argsort()
den_data_sort = den_data[idx]

t, l, r = den_data_sort[:,0],den_data_sort[:,1],den_data_sort[:,2]
zi2 = zi2[idx]


# 直接使用频数个数绘制
import mpltern
fig = plt.figure(figsize=(4, 3.5),dpi=100,facecolor="w")
ax = fig.add_subplot(projection='ternary')
ax.tick_params(length=8)
ax.grid(color="k",linewidth=0.5)
pc = ax.scatter(t, l, r,s=3,c=zi2,lw=.6,zorder=7,alpha=.9,cmap=parula)

ax.set_tlabel('SiO2')
ax.set_llabel('MgO')
ax.set_rlabel('TiO2')
cax = ax.inset_axes([1.01, 0.4, 0.05, 0.6], transform=ax.transAxes)
colorbar = fig.colorbar(pc, cax=cax,
                ticks=[int(min(zi2)), 50, 100, 150, 200, 250])
colorbar.ax.tick_params(labelsize=9,direction="in")
colorbar.ax.tick_params(which="minor",direction="in")
colorbar.set_label("Raletive point density \nfor ternary density plots",
             fontsize=9.5)
colorbar.ax.yaxis.set_ticklabels(
    [int(min(zi2)), 50, 100, 150, 200,250])
plt.tight_layout()                

# 转变成密度
zi_de = zi2 / np.nanmax(zi2)

# a）三元密度图绘制示例一

fig = plt.figure(figsize=(4, 3.5),dpi=100,facecolor="w")
ax = fig.add_subplot(projection='ternary')
ax.tick_params(length=8)
ax.grid(color="k",linewidth=0.5)
pc = ax.scatter(t, l, r,s=3,c=zi_de,lw=.6,zorder=7,alpha=.9,cmap=parula)

ax.set_tlabel('SiO2')
ax.set_llabel('MgO')
ax.set_rlabel('TiO2')
cax = ax.inset_axes([1.01, 0.4, 0.05, 0.6], transform=ax.transAxes)
colorbar = fig.colorbar(pc, cax=cax,
                ticks=[min(zi_de), 0.2, 0.40, 0.6, 0.8, 1.0])
colorbar.ax.tick_params(labelsize=9,direction="in")
colorbar.ax.tick_params(which="minor",direction="in")
colorbar.ax.yaxis.set_ticklabels(
    [0.0, 0.2, 0.40, 0.6, 0.8, 1.0])
colorbar.set_label("Raletive point density \nfor ternary density plots",
             fontsize=9.5)
plt.tight_layout()

plt.savefig(r'\第5章 多变量图形的绘制\图5-3-7 三元密度图绘制示例_a.pdf', bbox_inches='tight',)
plt.savefig(r'\第5章 多变量图形的绘制\图5-3-7 三元密度图绘制示例_a.png', 
            bbox_inches='tight',dpi=600)
plt.show()

# b）三元密度图绘制示例二

fig = plt.figure(figsize=(4.2, 4),dpi=100,facecolor="w")
ax = fig.add_subplot(projection='ternary')
ax.tick_params(length=8)
ax.grid(color="k",linewidth=0.5)
pc = ax.scatter(t, l, r,s=3,c=zi_de,lw=.6,zorder=7,alpha=.9,cmap=parula)

ax.set_tlabel('SiO2')
ax.set_llabel('MgO')
ax.set_rlabel('TiO2')
cax = ax.inset_axes([0.1, -0.25, 0.8, 0.05], transform=ax.transAxes)
colorbar = fig.colorbar(pc, cax=cax,orientation="horizontal",
                ticks=[min(zi_de), 0.2, 0.40, 0.6, 0.8, 1.0])
colorbar.ax.tick_params(labelsize=9,direction="in")
colorbar.ax.tick_params(which="minor",direction="in")
colorbar.ax.xaxis.set_ticklabels(
    [0.0, 0.2, 0.40, 0.6, 0.8, 1.0])
colorbar.set_label("Raletive point density for ternary density plots",
             fontsize=9.5)

plt.tight_layout()  

plt.savefig(r'\第5章 多变量图形的绘制\图5-3-7 三元密度图绘制示例_b.pdf', bbox_inches='tight',)
plt.savefig(r'\第5章 多变量图形的绘制\图5-3-7 三元密度图绘制示例_b.png', 
            bbox_inches='tight',dpi=600)
plt.show() 

