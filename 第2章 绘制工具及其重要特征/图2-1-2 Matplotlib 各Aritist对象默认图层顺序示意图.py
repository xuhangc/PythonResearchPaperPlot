"""
编写时间：2022年2月05日 09：50

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。

代码中Proplot包绘制的部分可能与Matplotlib绘制不同，需注意两者绘图语法的不同~~

"""


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.text import TextPath
from matplotlib.transforms import Affine2D
import mpl_toolkits.mplot3d.art3d as art3d
from matplotlib.patches import Rectangle, PathPatch

plt.rcParams["font.family"] = "Times New Roman"



colors = ["#2FBE8F","#459DFF","#FF5B9B","#FFCC37","#751DFE","#0057FF"]

def text3d(ax, xyz, s, zdir="z", size=None,angle=0, **kwargs):
    x, y, z = xyz
    if zdir == "y":
        x, y, z = x, z, y
    elif zdir == "x":
        x, y, z = y, z, x
    else:
        x, y, z = x, y, z
    text_path = TextPath((0, 0), s, size=size)
    trans = Affine2D().rotate(angle).translate(x, y)
    p = PathPatch(trans.transform_path(text_path), **kwargs)
    ax.add_patch(p)
    art3d.pathpatch_2d_to_3d(p, z=z, zdir=zdir)
    
fig = plt.figure(figsize=(8, 5),dpi=100,facecolor="w")
ax = fig.add_subplot(111, projection="3d", xticks=[], yticks=[], zticks=[])
ax.set_axis_off()
ax.set_xlim(0, 10), ax.set_ylim(0, 10), ax.set_zlim(0, 10)

figs = ["Figure (background)",
        "Images(zorder=0)",
        "Patches (zorder=1)",
        "Lines (zorder=2)",
        "Text (zorder=3)",
        "Inset axes & legend (zorder=5)",
    ]
for i, text,color in zip(np.arange(len(figs)),figs,colors):

    #p = Rectangle((0, 0), 10, 10, edgecolor="None", facecolor="white", alpha=0.5)
    p = Rectangle((0, 0), 10, 10, edgecolor="None", facecolor=color, alpha=0.5)
    ax.add_patch(p)
    art3d.pathpatch_2d_to_3d(p, z=i, zdir="z")

    p = Rectangle((0, 0), 10, 10, edgecolor="black", facecolor="None",lw=.6)
    ax.add_patch(p)
    art3d.pathpatch_2d_to_3d(p, z=i, zdir="z")

    text3d(
        ax,
        (-0.25, 0.25, i),
        text,
        zdir="z",
        size=0.6,
        angle=np.pi / 2,
        ec="none",
        fc=color,
    )

plt.tight_layout()
plt.savefig(r'\第2章 绘制工具及其重要特征\图2-1-2 Matplotlib 各Aritist对象默认图层顺序示意图.pdf',bbox_inches='tight')
plt.savefig(r'\第2章 绘制工具及其重要特征\图2-1-2 Matplotlib 各Aritist对象默认图层顺序示意图.png', 
            bbox_inches='tight',dpi=300)
            
plt.show()

