"""
编写时间：2022年4月16日 10：30

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
from mpltern.ternary.datasets import get_shanon_entropie
from colormaps import parula

from proplot import rc
rc["font.family"] = "Times New Roman"
rc["axes.labelsize"] = 15
rc["tick.labelsize"] = 12
rc["suptitle.size"] = 15
rc["title.size"] = 14


from mpltern.ternary.datasets import get_shanon_entropies
t, l, r, v = get_shanon_entropies()

# a）矩阵三元相等值线图绘制示例
vmin = 0.0
vmax = 1.2
levels = np.linspace(vmin, vmax, 8)

fig = plt.figure(figsize=(4.5, 4),dpi=100,facecolor="w")
ax = fig.add_subplot(projection='ternary')
cs = ax.tricontour(t, l, r, v, levels=levels,colors="k",linewidths=1)
ax.clabel(cs)
ax.tick_params(length=8)
#ax.grid(color="k",linewidth=0.5)
ax.text(-0.2,0.7,0.5,s="Variable 1",fontsize=16, fontweight="bold")
ax.text(0.2,0.4,-.1,s="Variable 2",fontsize=16, fontweight="bold",rotation="60")
ax.text(0.2,-.02,0.35,s="Variable 3",fontsize=16, fontweight="bold",rotation="-60")

plt.savefig(r'\第5章 多变量图形的绘制\图5-3-8 矩阵三元相等值线图和带颜色填充的三元相等值线图绘制示例_a.pdf', bbox_inches='tight',)
plt.savefig(r'\第5章 多变量图形的绘制\图5-3-8 矩阵三元相等值线图和带颜色填充的三元相等值线图绘制示例_a.png', 
            bbox_inches='tight',dpi=600)
plt.show()


# b）带颜色填充的三元相等值线图绘制示例
vmin = 0.0
vmax = 1.2
levels = np.linspace(vmin, vmax, 7)

fig = plt.figure(figsize=(4.5, 4),dpi=100,facecolor="w")
ax = fig.add_subplot(projection='ternary')
cs = ax.tricontour(t, l, r, v, levels=levels,colors="k",linewidths=1)
ax.clabel(cs)
ax.tick_params(length=8)
cs = ax.tricontourf(t, l, r, v, levels=levels,cmap=parula)
ax.tick_params(length=8)
#ax.grid(color="k",linewidth=0.5)
ax.text(-0.2,0.7,0.5,s="Variable 1",fontsize=16, fontweight="bold")
ax.text(0.2,0.4,-.1,s="Variable 2",fontsize=16, fontweight="bold",rotation="60")
ax.text(0.2,-.02,0.35,s="Variable 3",fontsize=16, fontweight="bold",rotation="-60")
cax = ax.inset_axes([1.12, 0.1, 0.08, 0.8], transform=ax.transAxes)
colorbar = fig.colorbar(cs, cax=cax)
colorbar.set_label('Cbar_values', rotation=270, va='baseline')
colorbar.ax.tick_params(left=True,direction="in",width=.5,labelsize=12)
colorbar.outline.set_linewidth(.5)
plt.savefig(r'\第5章 多变量图形的绘制\图5-3-8 矩阵三元相等值线图和带颜色填充的三元相等值线图绘制示例_b.pdf', bbox_inches='tight',)
plt.savefig(r'\第5章 多变量图形的绘制\图5-3-8 矩阵三元相等值线图和带颜色填充的三元相等值线图绘制示例_b.png', 
            bbox_inches='tight',dpi=600)
plt.show()

