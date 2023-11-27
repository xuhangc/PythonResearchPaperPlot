
"""
编写时间：2022年4月19日 11：30

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

# a）3D填充要素图绘制示例
from mpl_toolkits.mplot3d import Axes3D

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
fig = plt.figure(figsize=(4,3.5),dpi=100,facecolor="w")
ax = fig.add_subplot(projection='3d')
ax.voxels(r, g, b, sphere,
          facecolors=colors,
         # edgecolors=np.clip(colors-1, 0, 0),  # black
          edgecolors = "k",
          linewidth=0.2,
          shade=False)
ax.xaxis.pane.set_color("none")
ax.yaxis.pane.set_color("none")
ax.zaxis.pane.set_color("none")
ax.xaxis._axinfo["grid"].update({"linewidth":.3, "color" : "gray"})
ax.yaxis._axinfo["grid"].update({"linewidth":.3, "color" : "gray"})
ax.zaxis._axinfo["grid"].update({"linewidth":.3, "color" : "gray"})
# 设置Z刻度轴位置
#ax.zaxis._axinfo['juggled'] = (1,2,0)

ax.set(xlabel='R', ylabel='G', zlabel='B')
fig.tight_layout()
fig.savefig('\第5章 多变量图形的绘制\图5-4-9 利用Matplotlib绘制的3D填充要素图示例_a.pdf',bbox_inches='tight')
fig.savefig('\第5章 多变量图形的绘制\图5-4-9 利用Matplotlib绘制的3D填充要素图示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()



# b）散点样式的3D填充要素图绘制示例
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(4,3.5),dpi=100,facecolor="w")
ax = fig.add_subplot(projection='3d')
x=range(0,255,15)
for i in x:
    for j in x:
        for k in x:
            ax.plot([i],[j],[k],color=(i/255.,j/255.,k/255.),markersize=4,marker='o',mec="k",mew=.1)
            ax.xaxis.pane.set_color("none")
            ax.yaxis.pane.set_color("none")
            ax.zaxis.pane.set_color("none")
            ax.xaxis._axinfo["grid"].update({"linewidth":.3, "color" : "gray"})
            ax.yaxis._axinfo["grid"].update({"linewidth":.3, "color" : "gray"})
            ax.zaxis._axinfo["grid"].update({"linewidth":.3, "color" : "gray"})
            ax.set(xlabel='R', ylabel='G', zlabel='B')
fig.tight_layout()

fig.savefig('\第5章 多变量图形的绘制\图5-4-9 利用Matplotlib绘制的3D填充要素图示例_b.pdf',bbox_inches='tight')
fig.savefig('\第5章 多变量图形的绘制\图5-4-9 利用Matplotlib绘制的3D填充要素图示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()


