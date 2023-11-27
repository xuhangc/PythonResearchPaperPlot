"""
编写时间：2022年4月15日 15：30

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

# a）利用Matplotlib绘制的矢量场图
X = np.arange(-10, 10, 1)
Y = np.arange(-10, 10, 1)
U, V = np.meshgrid(X, Y)
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
q = ax.quiver(X, Y, U, V)
ax.quiverkey(q, X=.33,Y=1.02, U=10,
             label='Quiver key, length = 10', labelpos='E')
ax.grid(False)
ax.set(xlabel='X Axis title', ylabel='Y Axis title')
fig.tight_layout()

fig.savefig('\第5章 多变量图形的绘制\图5-1-3 利用Matplotlib绘制的矢量场图和带矢量指示的等值线图示例_a.pdf',bbox_inches='tight')
fig.savefig('\第5章 多变量图形的绘制\图5-1-3 利用Matplotlib绘制的矢量场图和带矢量指示的等值线图示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# b）利用Matplotlib绘制的带矢量指示的等高线图
data = pd.read_excel(r"\第5章 多变量图形的绘制\coutour_data.xlsx",header=None)
x = np.arange(0,len(data), 1)
y = np.arange(0,len(data), 1)
X, Y = np.meshgrid(x, y)
Z = data.values

#Vector data
x = np.linspace(min(x), max(x), 10)
y = np.linspace(min(y), max(y), 10)
X2, Y2 = np.meshgrid(x, y)
U = X2 + Y2
V = Y2 - X2

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
ax.contour(X, Y, Z,linewidths=.6,linestyles="solid",colors="k")
Cf = ax.contourf(X, Y, Z,linewidths=1,cmap=parula)

q = ax.quiver(X2, Y2, U, V, color="k", angles='uv',
          scale_units='xy', scale=8, width=.005,headwidth=5,headlength=5)
ax.quiverkey(q, X=.55,Y=1.03, U=60,
             label='Quiver key, length = 60', labelpos='E')
ax.grid(False)
cbar = fig.colorbar(Cf)
cbar.ax.tick_params(direction="in",labelsize=10)
cbar.ax.minorticks_off()
ax.set(xlabel='X Axis title', ylabel='Y Axis title')
fig.tight_layout()
fig.savefig('\第5章 多变量图形的绘制\图5-1-3 利用Matplotlib绘制的矢量场图和带矢量指示的等值线图示例_b.pdf',bbox_inches='tight')
fig.savefig('\第5章 多变量图形的绘制\图5-1-3 利用Matplotlib绘制的矢量场图和带矢量指示的等值线图示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()