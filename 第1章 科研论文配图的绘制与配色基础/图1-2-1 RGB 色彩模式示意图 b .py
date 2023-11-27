"""
编写时间：2022年2月04日 20：30

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。

代码中Proplot包绘制的部分可能与Matplotlib绘制不同，需注意两者绘图语法的不同~~

"""
import numpy as np
import pandas as pd
import seaborn as sns
import proplot as pplt
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from proplot import rc
rc["axes.labelsize"] = 12
rc['tick.labelsize'] = 10
rc["suptitle.size"] = 15
rc["xtick.major.pad"] =.5
rc["xtick.minor.visible"] = False
rc["ytick.minor.visible"] = False
rc["font.family"] = "Times New Roman"

def midpoints(x):
    sl = ()
    for i in range(x.ndim):
        x = (x[sl + np.index_exp[:-1]] + x[sl + np.index_exp[1:]]) / 2.0
        sl += np.index_exp[:]
    return x
# prepare some coordinates, and attach rgb values to each
r, g, b = np.indices((17, 17, 17)) / 16.0
rc = midpoints(r)
gc = midpoints(g)
bc = midpoints(b)
#
sphere = rc > -1
# combine the color components
colors = np.zeros(sphere.shape + (3,))
colors[..., 0] = rc
colors[..., 1] = gc
colors[..., 2] = bc

# and plot everything
fig = plt.figure(figsize=(5,4),dpi=100,facecolor="w")
ax = fig.add_subplot(projection='3d')
ax.voxels(r, g, b, sphere,
          facecolors=colors,
         # edgecolors=np.clip(colors-1, 0, 0),  # black
          edgecolors = "none",
          linewidth=0.3,
          shade=False)
ax.xaxis.pane.set_color("none")
ax.yaxis.pane.set_color("none")
ax.zaxis.pane.set_color("none")
ax.xaxis._axinfo["grid"].update({"linewidth":.3, "color" : "none"})
ax.yaxis._axinfo["grid"].update({"linewidth":.3, "color" : "none"})
ax.zaxis._axinfo["grid"].update({"linewidth":.3, "color" : "none"})
# 设置Z刻度轴位置
#ax.zaxis._axinfo['juggled'] = (1,2,0)
ax.view_init(elev=20,azim=20)
ax.set(xlabel='R', ylabel='G', zlabel='B')
ax.set_axis_off()
#ax.axis('off')
fig.tight_layout()

#fig.save(r"\第1章 科研论文配图的绘制与配色基础\\图1-2-1 RGB色彩模式示意图_b.svg")
#plt.save(r"\第1章 科研论文配图的绘制与配色基础\\图1-2-1 RGB色彩模式示意图_b.svg")
plt.show()

