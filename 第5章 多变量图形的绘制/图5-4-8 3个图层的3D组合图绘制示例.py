"""
编写时间：2022年4月19日 10：30

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

multile_surdata = pd.read_excel(r"\第5章 多变量图形的绘制\multiple_surface.xlsx",header=None)
x = np.arange(0,len(multile_surdata), 1)
y = np.arange(0,len(multile_surdata), 1)
X, Y = np.meshgrid(x, y)
Z1 = multile_surdata.values
Z1 = Z1-200
Z2 = Z1 +200
Z3 = Z1 + 400
Z4 = Z1 + 600

fig = plt.figure(figsize=(4,3.5),dpi=100,facecolor="w")
ax = fig.add_subplot(projection='3d')
# surface
ax.plot_surface(X, Y, Z1, cmap="copper",edgecolor='none', linewidth=0.1,alpha=1)
ax.contourf(X, Y, Z1, zdir='z', offset=0,cmap=parula)
ax.contour(X, Y, Z2,zdir='z',offset=0,colors="k",linewidths=.3,linestyles="solid",)
ax.plot_surface(X, Y, Z3,edgecolor='k', linewidth=0.1,alpha=0)

ax.set_zlim(bottom=0,top=1000)
# ax.contourf(X, Y, A2, 100, zdir='z', offset=0.5,cmap=cmap)
# ax.contourf(X, Y, A3, 100, zdir='z', offset=1,cmap=cmap)

ax.xaxis._axinfo["color"] =(0.925, 0.125, 0.90, 0.25)
ax.xaxis.pane.set_color("none")
ax.yaxis.pane.set_color("none")
ax.zaxis.pane.set_color("none")
ax.xaxis._axinfo["grid"].update({"linewidth":.3, "color":"gray"})
ax.yaxis._axinfo["grid"].update({"linewidth":.3, "color":"gray"})
ax.zaxis._axinfo["grid"].update({"linewidth":.3, "color":"gray"})
# 设置Z刻度轴位置
#ax.zaxis._axinfo['juggled'] = (1,2,0)
#ax.view_init(25)
ax.view_init(25, 45)
ax.set(xlabel='X', ylabel='Y', zlabel='Z')
fig.tight_layout()

fig.savefig('\第5章 多变量图形的绘制\图5-4-8 3个图层的3D组合图绘制示例.pdf',bbox_inches='tight')
fig.savefig('\第5章 多变量图形的绘制\图5-4-8 3个图层的3D组合图绘制示例.png', 
            bbox_inches='tight',dpi=300)
plt.show()