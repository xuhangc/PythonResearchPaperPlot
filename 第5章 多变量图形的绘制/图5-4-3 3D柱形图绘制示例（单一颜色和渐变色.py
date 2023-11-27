"""
编写时间：2022年4月18日 16：30

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

"""
此代码为使用Python-Prolot包进行学术风格图表绘制，绘图语法和Matplotlib有所不同，需注意。
"""

import pandas as pd
import numpy as np
import proplot as pplt
import seaborn as sns
import matplotlib.pyplot as plt
from colormaps import parula

from proplot import rc
rc["axes.labelsize"] = 12
rc['tick.labelsize'] = 10
rc["suptitle.size"] = 15
rc["xtick.major.pad"] =.5
rc["xtick.minor.visible"] = False
rc["ytick.minor.visible"] = False
rc["font.family"] = "Times New Roman"



# a）单一颜色3D柱形图绘制示例
# Fixing random state for reproducibility
np.random.seed(19680801)

fig = plt.figure(figsize=(5,4.5),dpi=100,facecolor="w")
ax = fig.add_subplot(projection='3d')
x, y = np.random.rand(2, 100) * 4
hist, xedges, yedges = np.histogram2d(x, y, bins=4, range=[[0, 4], [0, 4]])

# Construct arrays for the anchor positions of the 16 bars.
xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25, indexing="ij")
xpos = xpos.ravel()
ypos = ypos.ravel()
zpos = 0

# Construct arrays with the dimensions for the 16 bars.
dx = dy = 0.5 * np.ones_like(zpos)
dz = hist.ravel()

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, zsort='average',
         color="#2796EC", edgecolor="black",lw=.5,shade=False)
ax.xaxis.pane.set_color("none")
ax.yaxis.pane.set_color("none")
ax.zaxis.pane.set_color("none")
ax.xaxis._axinfo["grid"].update({"linewidth":.3, "color" : "gray"})
ax.yaxis._axinfo["grid"].update({"linewidth":.3, "color" : "gray"})
ax.zaxis._axinfo["grid"].update({"linewidth":.3, "color" : "gray"})
# 设置Z刻度轴位置
ax.zaxis._axinfo['juggled'] = (1,2,0)
ax.view_init(20)
ax.invert_xaxis()
ax.set(xlabel='X', ylabel='Y', zlabel='Z')
fig.tight_layout()
fig.savefig('\第5章 多变量图形的绘制\图5-4-3 3D柱形图绘制示例（单一颜色和渐变色）_a.pdf',bbox_inches='tight')
fig.savefig('G\第5章 多变量图形的绘制\图5-4-3 3D柱形图绘制示例（单一颜色和渐变色）_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# b）渐变色3D柱形图绘制示例
from matplotlib import cm
from matplotlib.colors import Normalize

# Fixing random state for reproducibility
np.random.seed(19680801)

fig = plt.figure(figsize=(5,4.5),dpi=100,facecolor="w")
ax = fig.add_subplot(projection='3d')

x, y = np.random.rand(2, 100) * 4
hist, xedges, yedges = np.histogram2d(x, y, bins=4, range=[[0, 4], [0, 4]])
# Construct arrays for the anchor positions of the 16 bars.
xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25, indexing="ij")
xpos = xpos.ravel()
ypos = ypos.ravel()
zpos = 0

# Construct arrays with the dimensions for the 16 bars.
dx = dy = 0.5 * np.ones_like(zpos)
dz = hist.ravel()

cmap = parula
norm = Normalize(vmin=min(dz), vmax=max(dz))
colors = cmap(norm(dz))

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, zsort='average',
         color=colors, edgecolor="black",lw=.5,shade=False)
ax.xaxis.pane.set_color("none")
ax.yaxis.pane.set_color("none")
ax.zaxis.pane.set_color("none")
ax.xaxis._axinfo["grid"].update({"linewidth":.3, "color" : "gray"})
ax.yaxis._axinfo["grid"].update({"linewidth":.3, "color" : "gray"})
ax.zaxis._axinfo["grid"].update({"linewidth":.3, "color" : "gray"})
# 设置Z刻度轴位置
ax.zaxis._axinfo['juggled'] = (1,2,0)
ax.view_init(20)
ax.invert_xaxis()
# 添加colorbar
sc = cm.ScalarMappable(cmap=cmap,norm=norm)
colorbar = fig.colorbar(sc,shrink=0.4,aspect=10)
colorbar.ax.tick_params(left=True,direction="in",width=.5,labelsize=12)
ax.set(xlabel='X', ylabel='Y', zlabel='Z')
fig.tight_layout()
fig.savefig('\第5章 多变量图形的绘制\图5-4-3 3D柱形图绘制示例（单一颜色和渐变色）_b.pdf',bbox_inches='tight')
fig.savefig('G\第5章 多变量图形的绘制\图5-4-3 3D柱形图绘制示例（单一颜色和渐变色）_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()
