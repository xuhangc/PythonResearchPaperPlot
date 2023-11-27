
"""
编写时间：2022年4月18日 22：30

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

"""
此代码为使用Python-Prolot包进行学术风格图表绘制，绘图语法和Matplotlib有所不同，需注意。
"""

import pandas as pd
import numpy as np
import proplot as pplt
import seaborn as sns
from scipy import interpolate
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from colormaps import parula

from proplot import rc
rc["axes.labelsize"] = 12
rc['tick.labelsize'] = 10
rc["suptitle.size"] = 15
rc["xtick.major.pad"] =.5
rc["xtick.minor.visible"] = False
rc["ytick.minor.visible"] = False
rc["font.family"] = "Times New Roman"

# a）3D组合图绘制示例（等高线图）
surface_data = pd.read_excel(r"\第5章 多变量图形的绘制\3D Surfaceplot.xlsx",skiprows=2)
x = surface_data["X"].values
y = surface_data.columns[1:]
X,Y = np.meshgrid(y,x)
Z = surface_data.iloc[0:,1:].values

fig = plt.figure(figsize=(4,3.5),dpi=100,facecolor="w")
ax = fig.add_subplot(projection='3d')
ax.plot_surface(X, Y, Z,rstride=2, cstride=2,cmap=parula, edgecolor='k', linewidth=0.1,
               alpha=.9)

# 添加等值线图
ax.contourf(X, Y, Z,linewidths=1,cmap=parula,offset=2500,alpha=.6)
ax.contour(X, Y, Z,linewidths=.6,linestyles="solid",colors="k",offset=2500,)
ax.xaxis._axinfo["color"] =(0.925, 0.125, 0.90, 0.25)
ax.xaxis.pane.set_color("none")
ax.yaxis.pane.set_color("none")
ax.zaxis.pane.set_color("none")
ax.xaxis._axinfo["grid"].update({"linewidth":.3, "color":"gray"})
ax.yaxis._axinfo["grid"].update({"linewidth":.3, "color":"gray"})
ax.zaxis._axinfo["grid"].update({"linewidth":.3, "color":"gray"})
# 设置Z刻度轴位置
ax.zaxis._axinfo['juggled'] = (1,2,0)
ax.view_init(30,-30)
ax.invert_xaxis()
ax.set(xlabel='X', ylabel='Y', zlabel='Z')
fig.tight_layout()

fig.savefig('\第5章 多变量图形的绘制\图5-4-7 3D组合图绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第5章 多变量图形的绘制\图5-4-7 3D组合图绘制示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()


# b）3D组合图绘制示例（曲面图）

mul_data = pd.read_excel(r"\第5章 多变量图形的绘制\Multiple Surfaces in Same Layer.xlsx",header=None)
x = np.arange(0,len(mul_data), 1)
y = np.arange(0,len(mul_data), 1)
X, Y = np.meshgrid(x, y)
Z = mul_data.values

fig = plt.figure(figsize=(4,3.5),dpi=100,facecolor="w")
ax = fig.add_subplot(projection='3d')
# surface
ax.plot_surface(X, Y, Z,rstride=2, cstride=2,cmap=parula, edgecolor='k', linewidth=0.1,
               alpha=1)
ax.contourf(X, Y, Z,linewidths=1,cmap=parula,offset=450)
ax.contour(X, Y, Z,linewidths=.4,linestyles="solid",colors="k",offset=450,)

ax.xaxis._axinfo["color"] =(0.925, 0.125, 0.90, 0.25)
ax.xaxis.pane.set_color("none")
ax.yaxis.pane.set_color("none")
ax.zaxis.pane.set_color("none")
ax.xaxis._axinfo["grid"].update({"linewidth":.3, "color":"gray"})
ax.yaxis._axinfo["grid"].update({"linewidth":.3, "color":"gray"})
ax.zaxis._axinfo["grid"].update({"linewidth":.3, "color":"gray"})
# 设置Z刻度轴位置
ax.zaxis._axinfo['juggled'] = (1,2,0)
ax.view_init(20)
ax.set(xlabel='X', ylabel='Y', zlabel='Z')
fig.tight_layout()
fig.savefig('\第5章 多变量图形的绘制\图5-4-7 3D组合图绘制示例_b.pdf',bbox_inches='tight')
fig.savefig('\第5章 多变量图形的绘制\图5-4-7 3D组合图绘制示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()

