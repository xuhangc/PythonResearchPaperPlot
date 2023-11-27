"""
编写时间：2022年4月18日 14：50

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

# a）连接线3D散点图绘制示例
x = [1, 2, 1.2, 1.5, 1.5]
y = [1, 1.2, 2, 1.5, 1.5]
z = [.5, .5, .5, 1.2, 2]

r = np.array(x)
s = np.array(y)
t = np.array(z) * 1.0

fig = plt.figure(figsize=(4,3.5),dpi=100,facecolor="w")
ax = fig.add_subplot(projection='3d')

ax.scatter(r,s,zs=t, s=200, color="#2FBE8F",ec="k",lw=1,alpha=1,
           label='True Position')
for x, y, z in zip(r, s, t):
    ax.plot3D([x, 1.5], [y, 1.5], [z, 1.2], 'k')

ax.xaxis._axinfo["color"] =(0.925, 0.125, 0.90, 0.25)
ax.xaxis.pane.set_color("none")
ax.yaxis.pane.set_color("none")
ax.zaxis.pane.set_color("none")
ax.xaxis._axinfo["grid"].update({"linewidth":.3, "color":"gray"})
ax.yaxis._axinfo["grid"].update({"linewidth":.3, "color":"gray"})
ax.zaxis._axinfo["grid"].update({"linewidth":.3, "color":"gray"})
#ax.grid(False)
ax.legend(markerscale=.8)
# 设置Z刻度轴位置
ax.zaxis._axinfo['juggled'] = (1,2,0)
ax.view_init(20)
#ax.invert_xaxis()
ax.set(xlabel='X', ylabel='Y', zlabel='Z')
fig.tight_layout()
fig.savefig('\第5章 多变量图形的绘制\图5-4-1 利用Matplotlib绘制的3D散点图示例_a.pdf',bbox_inches='tight')
fig.savefig('G\第5章 多变量图形的绘制\图5-4-1 利用Matplotlib绘制的3D散点图示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# b）气泡3D散点图绘制示例

np.random.seed(42)
ages = np.random.randint(low = 8, high = 30, size=35)
heights = np.random.randint(130, 195, 35)
weights = np.random.randint(30, 160, 35)
bmi = weights/((heights*0.01)**2)

fig = plt.figure(figsize=(4,3.5),dpi=100,facecolor="w")
ax = fig.add_subplot(projection='3d')
scatter = ax.scatter(xs = heights, ys = weights, zs = ages, ec="k",lw=.5,s=bmi*2,c=bmi,cmap=parula,alpha=1)
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
#ax.invert_xaxis()
# 添加大小图例
kw = dict(prop="sizes", num=5, color="k",mec="k",fmt="{x:.0f}",
          func=lambda s: s/2)
legend = ax.legend(*scatter.legend_elements(**kw),
                    loc="upper right", bbox_to_anchor=(1.18, .9),
                    title="Scatter Size",fontsize=9,title_fontsize=10,
                    handletextpad=.1,frameon=False)
cax = ax.inset_axes([1.0, 0.1, 0.06, 0.4], 
                    transform=ax.transAxes)
colorbar = fig.colorbar(scatter, cax=cax)
colorbar.ax.set_title("Cbar_values",fontsize=10,pad=5)
colorbar.ax.tick_params(left=True,direction="in",width=.5,labelsize=9)
#cbar = fig.colorbar(scatter,aspect=10,shrink=.6)
ax.set(xlabel='X', ylabel='Y', zlabel='Z')
fig.tight_layout()

fig.savefig('\第5章 多变量图形的绘制\图5-4-1 利用Matplotlib绘制的3D散点图示例_b.pdf',bbox_inches='tight')
fig.savefig('G\第5章 多变量图形的绘制\图5-4-1 利用Matplotlib绘制的3D散点图示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()
