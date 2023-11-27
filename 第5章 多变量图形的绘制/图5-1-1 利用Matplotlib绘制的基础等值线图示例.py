"""
编写时间：2022年4月15日 14：00

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

"""
此代码为使用Python-Prolot包进行学术风格图表绘制，绘图语法和Matplotlib有所不同，需注意。

"""
import numpy as np
import pandas as pd
import seaborn as sns
import proplot as pplt
import matplotlib.pyplot as plt
from colormaps import parula

from proplot import rc
rc["font.family"] = "Times New Roman"
rc["axes.labelsize"] = 15
rc["tick.labelsize"] = 12
rc["suptitle.size"] = 15
rc["title.size"] = 14

data = pd.read_excel(r"\第5章 多变量图形的绘制\coutour_data.xlsx",header=None)
x = np.arange(0,len(data), 1)
y = np.arange(0,len(data), 1)
X, Y = np.meshgrid(x, y)
Z = data.values

# a）Matplotlib中的Axes.contour()函数绘制示例
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
CS = ax.contour(X, Y, Z,linewidths=1,cmap=parula)
ax.clabel(CS, inline=True, fontsize=10)
ax.set(xlabel='X Axis Title', ylabel='Y Axis Title')
ax.grid(False)
fig.tight_layout()

fig.savefig('\第5章 多变量图形的绘制\图5-1-1 利用Matplotlib绘制的基础等值线图示例_a.pdf',bbox_inches='tight')
fig.savefig('\第5章 多变量图形的绘制\图5-1-1 利用Matplotlib绘制的基础等值线图示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# b）Matplotlib中的Axes.contourf()函数绘制示例
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
ax.contour(X, Y, Z,linewidths=.6,linestyles="solid",colors="k")
Cf = ax.contourf(X, Y, Z,linewidths=1,cmap=parula)
ax.clabel(Cf,inline=False, colors="k",fontsize=10)
ax.set(xlabel='X Axis title', ylabel='Y Axis title', )
ax.grid(False)
cbar = fig.colorbar(Cf)
cbar.ax.tick_params(direction="in",labelsize=10)
cbar.ax.minorticks_off()
fig.tight_layout()
fig.savefig('\第5章 多变量图形的绘制\图5-1-1 利用Matplotlib绘制的基础等值线图示例_b.pdf',bbox_inches='tight')
fig.savefig('\第5章 多变量图形的绘制\图5-1-1 利用Matplotlib绘制的基础等值线图示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()

