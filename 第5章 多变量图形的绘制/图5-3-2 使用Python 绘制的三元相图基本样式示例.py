"""
编写时间：2022年4月15日 19：30

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

"""
此代码为使用Python-Prolot包进行学术风格图表绘制，绘图语法和Matplotlib有所不同，需注意。

"""
import ternary
import pandas as pd
import numpy as np
import proplot as pplt
import seaborn as sns
import matplotlib.pyplot as plt
from mpltern.ternary.datasets import get_triangular_grid
from colormaps import parula
from proplot import rc
rc["font.family"] = "Times New Roman"
rc["axes.labelsize"] = 15
rc["tick.labelsize"] = 12
rc["suptitle.size"] = 15
rc["title.size"] = 14

# a）三元相图样式一

from mpltern.ternary.datasets import get_triangular_grid
t, l, r = get_triangular_grid()
fig = plt.figure(figsize=(4.5, 4),dpi=100,facecolor="w")
ax = fig.add_subplot(projection='ternary')
ax.tick_params(length=8)
ax.triplot(t, l, r,color="k",lw=.5,alpha=.5)
ax.set_tlabel('Top')
ax.set_llabel('Left')
ax.set_rlabel('Right')

ax.text(-0.2,0.7,0.5,s="Variable 1",fontsize=16, fontweight="bold")
ax.text(0.2,0.4,-.1,s="Variable 2",fontsize=16, fontweight="bold",rotation="60")
ax.text(0.2,-.02,0.35,s="Variable 3",fontsize=16, fontweight="bold",rotation="-60")

plt.savefig(r'\第5章 多变量图形的绘制\图5-3-2 使用Python 绘制的三元相图基本样式示例_a.pdf', bbox_inches='tight',)
plt.savefig(r'\第5章 多变量图形的绘制\图5-3-2 使用Python 绘制的三元相图基本样式示例_a.png', 
            bbox_inches='tight',dpi=600)
plt.show()


# b）三元相图样式二
colors = ["#2FBE8F","#459DFF","#FF5B9B","#FFCC37","#751DFE"]

fig = plt.figure(figsize=(4.5, 4),dpi=100,facecolor="w")
ax = fig.add_subplot(projection='ternary')
ax.set_tlabel('Top')
ax.set_llabel('Left')
ax.set_rlabel('Right')
ax.grid()

# Color ticks, grids, tick-labels
ax.taxis.set_tick_params(tick2On=True, colors=colors[0], grid_color=colors[0])
ax.laxis.set_tick_params(tick2On=True, colors=colors[1], grid_color=colors[1])
ax.raxis.set_tick_params(tick2On=True, colors=colors[2], grid_color=colors[2])
# Color labels
ax.taxis.label.set_color(colors[0])
ax.laxis.label.set_color(colors[1])
ax.raxis.label.set_color(colors[2])
# Color spines
ax.spines['tside'].set_color(colors[0])
ax.spines['lside'].set_color(colors[1])
ax.spines['rside'].set_color(colors[2])
ax.text(-0.2,0.7,0.5,s="Variable 1",fontsize=16, fontweight="bold")
ax.text(0.2,0.4,-.1,s="Variable 2",fontsize=16, fontweight="bold",rotation="60")
ax.text(0.2,-.02,0.35,s="Variable 3",fontsize=16, fontweight="bold",rotation="-60")
plt.savefig(r'\第5章 多变量图形的绘制\图5-3-2 使用Python 绘制的三元相图基本样式示例_b.pdf', bbox_inches='tight',)
plt.savefig(r'\第5章 多变量图形的绘制\图5-3-2 使用Python 绘制的三元相图基本样式示例_b.png', 
            bbox_inches='tight',dpi=600)
plt.show()

# c）三元相图样式三
import ternary

scale = 10
aux = dict({(i,j,k): k for i, j, k in  ternary.helpers.simplex_iterator(scale)})
ax = ternary.heatmap(aux, scale,cmap=parula,colorbar=False,permutation="012", style="t")
tax = ternary.TernaryAxesSubplot(ax=ax, scale=scale)
tax.boundary(linewidth=1.5)
tax.gridlines(color="k", multiple=6)
tax.gridlines(color="k", multiple=2, linewidth=0.5,linestyle="-")
# 刻度位置
tax.ticks(axis='lbr', linewidth=1, multiple=2,offset=0.03,tick_formats="%.1f",fontsize=13)
# 刻度标签和标题
fontsize = 15
offset = 0.14
#tax.set_title("A Basic Example\n", fontsize=16,fontweight="bold")
tax.left_axis_label("Variable 2", fontsize=fontsize, fontweight="bold",offset=offset)
tax.right_axis_label("Variable 3", fontsize=fontsize, fontweight="bold",offset=offset)
tax.bottom_axis_label("Variable 1", fontsize=fontsize, fontweight="bold",offset=offset)
tax.right_corner_label("Right", fontsize=fontsize)
tax.top_corner_label("Top", fontsize=fontsize)
tax.left_corner_label("Left", fontsize=fontsize)
tax.clear_matplotlib_ticks()
tax.get_axes().axis('off')

plt.savefig(r'\第5章 多变量图形的绘制\图5-3-2 使用Python 绘制的三元相图基本样式示例_c.pdf', bbox_inches='tight',)
plt.savefig(r'\第5章 多变量图形的绘制\图5-3-2 使用Python 绘制的三元相图基本样式示例_c.png', 
            bbox_inches='tight',dpi=600)
plt.show()