
"""
编写时间：2022年2月05日 13：50

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。

代码中Proplot包绘制的部分可能与Matplotlib绘制不同，需注意两者绘图语法的不同~~

"""

import pandas as pd
import numpy as np
import proplot as pplt
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from proplot import rc
rc["font.family"] = "Times New Roman"
rc['tick.labelsize'] = 12
rc["suptitle.size"] = 15

#(a) 三维直角坐标系中的散点图绘制示例
fig = plt.figure(figsize=(5,4.5),dpi=110,facecolor="w")
ax = fig.add_subplot(projection='3d')

np.random.seed(42)
xs = np.random.random(100)*10+20
ys = np.random.random(100)*5+7
zs = np.random.random(100)*15+50

ax.scatter(xs, ys, zs, c='#459DFF',s=50)
ax.xaxis.pane.set_color("none")
ax.yaxis.pane.set_color("none")
ax.zaxis.pane.set_color("none")
ax.xaxis._axinfo["grid"].update({"linewidth":.3, "color" : "gray"})
ax.yaxis._axinfo["grid"].update({"linewidth":.3, "color" : "gray"})
ax.zaxis._axinfo["grid"].update({"linewidth":.3, "color" : "gray"})
ax.view_init(25, 40)

plt.savefig(r'\第2章 绘制工具及其重要特征\图2-1-8 Matplotlib中三维直角坐标系的绘图示例_a.pdf',bbox_inches='tight')
plt.savefig(r'\第2章 绘制工具及其重要特征\图2-1-8 Matplotlib中三维直角坐标系的绘图示例_a.png', 
            bbox_inches='tight',dpi=300)       
plt.show()


#(b) 三维直角坐标系中的柱形图绘制示例

np.random.seed(19680801)

fig = plt.figure(figsize=(5,4.5),dpi=110,facecolor="w")
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
ax.view_init(20, 40)
plt.savefig(r'\第2章 绘制工具及其重要特征\图2-1-8 Matplotlib中三维直角坐标系的绘图示例_b.pdf',bbox_inches='tight')
plt.savefig(r'\第2章 绘制工具及其重要特征\图2-1-8 Matplotlib中三维直角坐标系的绘图示例_b.png', 
            bbox_inches='tight',dpi=300)       
plt.show()

