"""
编写时间：2022年4月18日 21：30

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

x = np.linspace(-2, 0, 20)
y = np.linspace(0, 2, 20)
[X, Y] = np.meshgrid(x,y)
# Define the function Z = f(X,Y)
Z = 2./np.exp((X-.5)**2+Y**2)-2./np.exp((X+.5)**2+Y**2)

# a）未插值计算的3D曲面图绘制示例

fig = plt.figure(figsize=(4,3.5),dpi=100,facecolor="w")
ax = fig.add_subplot(projection='3d')
cmap = parula

surf = ax.plot_surface(X, Y, Z,ec="k",lw=.2,cmap=cmap)
ax.xaxis._axinfo["color"] =(0.925, 0.125, 0.90, 0.25)
ax.xaxis.pane.set_color("none")
ax.yaxis.pane.set_color("none")
ax.zaxis.pane.set_color("none")
ax.xaxis._axinfo["grid"].update({"linewidth":.3, "color":"gray"})
ax.yaxis._axinfo["grid"].update({"linewidth":.3, "color":"gray"})
ax.zaxis._axinfo["grid"].update({"linewidth":.3, "color":"gray"})
ax.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
ax.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.1f'))
# 设置Z刻度轴位置
ax.zaxis._axinfo['juggled'] = (1,2,0)
ax.view_init(20)
#ax.view_init(30, 45)
colorbar = fig.colorbar(surf, shrink=0.5, aspect=8)
colorbar.ax.tick_params(width=.5,labelsize=8)
colorbar.ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
ax.set(xlabel='X', ylabel='Y', zlabel='Z')
fig.tight_layout()

fig.savefig('\第5章 多变量图形的绘制\图5-4-6 插值计算前后的3D曲面图绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第5章 多变量图形的绘制\图5-4-6 插值计算前后的3D曲面图绘制示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()


# b）使用interp2d()函数进行插值计算后的3D曲面图绘制示例

xnew, ynew = np.linspace(-2, 0, 1000),np.linspace(0, 2, 1000)

# 插值处理
f = interpolate.interp2d(x, y, Z, kind='cubic')
znew = f(xnew, ynew)
[Xnew,Ynew] = np.meshgrid(xnew, ynew)

fig = plt.figure(figsize=(4,3.5),dpi=100,facecolor="w")
ax = fig.add_subplot(projection='3d')
cmap = parula
surf_inter = ax.plot_surface(Xnew, Ynew, znew,cmap=cmap,linewidth=0)
#surf = ax.plot_surface(X, Y, Z,ec="k",lw=.1,cmap=cmap)
ax.xaxis._axinfo["color"] =(0.925, 0.125, 0.90, 0.25)
ax.xaxis.pane.set_color("none")
ax.yaxis.pane.set_color("none")
ax.zaxis.pane.set_color("none")
ax.xaxis._axinfo["grid"].update({"linewidth":.3, "color":"gray"})
ax.yaxis._axinfo["grid"].update({"linewidth":.3, "color":"gray"})
ax.zaxis._axinfo["grid"].update({"linewidth":.3, "color":"gray"})
ax.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
ax.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.1f'))
# 设置Z刻度轴位置
ax.zaxis._axinfo['juggled'] = (1,2,0)
ax.view_init(20)
colorbar = fig.colorbar(surf_inter, shrink=0.5, aspect=8)
colorbar.ax.tick_params(width=.5,labelsize=8)
colorbar.ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
ax.set(xlabel='X', ylabel='Y', zlabel='Z')
fig.tight_layout()

fig.savefig('\第5章 多变量图形的绘制\图5-4-6 插值计算前后的3D曲面图绘制示例_b.pdf',bbox_inches='tight')
fig.savefig('\第5章 多变量图形的绘制\图5-4-6 插值计算前后的3D曲面图绘制示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()

