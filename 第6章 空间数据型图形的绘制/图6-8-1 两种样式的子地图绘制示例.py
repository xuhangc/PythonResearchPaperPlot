"""
编写时间：2022年4月30日 16：30

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

"""
此代码为使用Python-Prolot包进行学术风格图表绘制，绘图语法和Matplotlib有所不同，需注意。
"""

import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pykrige.kriging_tools as kt
from pykrige.ok import OrdinaryKriging
from colormaps import parula

from proplot import rc
rc["font.family"] = "Times New Roman"
rc["axes.labelsize"] = 15
rc["tick.labelsize"] = 10
rc["suptitle.size"] = 15
rc["title.size"] = 14


map_fig02 = gpd.read_file(r"\第6章 空间数据型图形的绘制\Virtual_Map1.shp")

jay = map_fig02[map_fig02["country"]=="JAY"]

# a）子地图绘制样式一
fig,main_ax = plt.subplots(figsize=(5,4.5),dpi=100,facecolor="w")
plot02 = map_fig02.plot("country",legend=False,ec="k",lw=.5,color="#9CCA9C",alpha=.8,
                       ax=main_ax)
jay.plot("country",color="r",ax=main_ax)
sub_map = main_ax.inset_axes([0.7, 0.01, 0.3, 0.3],transform=main_ax.transAxes)
sub_map.grid(False)
sub_map.tick_params(which="both",labelleft=False,left=False,bottom=False,labelbottom=False)
inset_map = jay.plot("country",color="r",ec="k",lw=.5,ax=sub_map)

# 绘制指示线
main_ax.annotate("",xy=(jay.centroid.x,jay.centroid.y),xytext=(131,35),
            arrowprops=dict(arrowstyle="-", color="k",
                                shrinkA=5, shrinkB=5,
                                patchA=None, patchB=None,
                                connectionstyle="arc,angleA=50,angleB=-80,armA=0,armB=90,rad=20",
                                ))
main_ax.grid(False)
main_ax.set_ylim((30, 60))
main_ax.set_xlim((100, 140))
main_ax.spines.right.set_visible(False)
main_ax.spines.top.set_visible(False)
main_ax.spines.left.set_position(("outward",10))
main_ax.spines.bottom.set_position(("outward",10))
main_ax.set_xlabel("Longitude")
main_ax.set_ylabel("Latitude")
fig.tight_layout()

fig.savefig('\第6章 空间数据型图形的绘制\图6-8-1 两种样式的子地图绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第6章 空间数据型图形的绘制\图6-8-1 两种样式的子地图绘制示例_a.png', 
            bbox_inches='tight',dpi=300)         
plt.show()


# b）子地图绘制样式二

fig,main_ax = plt.subplots(figsize=(5,4.5),dpi=100,facecolor="w")
plot02 = map_fig02.plot("country",legend=False,ec="k",lw=.5,color="#9CCA9C",alpha=.8,
                       ax=main_ax)
jay.plot("country",color="r",ax=main_ax)
sub_map = main_ax.inset_axes([0.7, 0.01, 0.3, 0.35],transform=main_ax.transAxes)
sub_map.grid(False)
sub_map.tick_params(which="both",labelleft=False,left=False,bottom=False,labelbottom=False)
inset_map = jay.plot("country",color="r",ec="k",lw=.5,ax=sub_map)
#main_ax.indicate_inset_zoom(sub_map)
main_ax.indicate_inset_zoom(sub_map,edgecolor="black",lw=.8)

main_ax.grid(False)
main_ax.set_ylim((30, 60))
main_ax.set_xlim((100, 140))
main_ax.spines.right.set_visible(False)
main_ax.spines.top.set_visible(False)
main_ax.spines.left.set_position(("outward",10))
main_ax.spines.bottom.set_position(("outward",10))
main_ax.set_xlabel("Longitude")
main_ax.set_ylabel("Latitude")
fig.tight_layout()

fig.savefig('\第6章 空间数据型图形的绘制\图6-8-1 两种样式的子地图绘制示例_b.pdf',bbox_inches='tight')
fig.savefig('\第6章 空间数据型图形的绘制\图6-8-1 两种样式的子地图绘制示例_b.png', 
            bbox_inches='tight',dpi=300)         
plt.show()