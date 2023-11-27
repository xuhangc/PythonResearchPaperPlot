
"""
编写时间：2022年4月30日 10：30

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
from colormaps import parula

from proplot import rc
rc["font.family"] = "Times New Roman"
rc["axes.labelsize"] = 15
rc["tick.labelsize"] = 10
rc["suptitle.size"] = 15
rc["title.size"] = 14


map_fig02 = gpd.read_file(r"\第6章 空间数据型图形的绘制\Virtual_Map1.shp")

type01 = map_fig02[map_fig02['country'].isin(["JACK","JAY"])]
type02 = map_fig02[map_fig02['country'].isin(["EELIN","RON"])]
type03 = map_fig02[~map_fig02['country'].isin(["JACK","JAY","EELIN","RON"])]

# a）类型地图绘制样式
colors = ["#458B74","#CDCD00","#F5DEB3"]
fig,ax = plt.subplots(figsize=(5,4.5),dpi=100,facecolor="w")
typology01 = type01.plot("country",legend=False,ec="k",lw=.5,color=colors[0],ax=ax)
typology02 = type02.plot("country",legend=False,ec="k",lw=.5,color=colors[1],ax=ax)
typology03 = type03.plot("country",legend=False,ec="k",lw=.5,color=colors[2],ax=ax)

# 单独绘制图例
labels = ["typology01","typology02","typology03"]
handles = [plt.Rectangle((0,0),.5,.5, color=color,ec="k") for color in colors]
bar_legend = ax.legend(handles, labels, loc='upper right', title='Typology Type',
                       fontsize=8,title_fontsize=9)
ax.grid(False)
ax.set_ylim((30, 60))
ax.set_xlim((100, 140))
ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)
ax.spines.left.set_position(("outward",10))
ax.spines.bottom.set_position(("outward",10))
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
fig.tight_layout()
fig.savefig('\第6章 空间数据型图形的绘制\图6-6-1 类型地图绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第6章 空间数据型图形的绘制\图6-6-1 类型地图绘制示例_a.png', 
            bbox_inches='tight',dpi=300)         
plt.show()

# b）类型地图文本添加绘制样式

colors = ["#458B74","#CDCD00","#F5DEB3"]
fig,ax = plt.subplots(figsize=(5,4.5),dpi=100,facecolor="w")
typology01 = type01.plot("country",legend=False,ec="k",lw=.5,color=colors[0],ax=ax)
typology02 = type02.plot("country",legend=False,ec="k",lw=.5,color=colors[1],ax=ax)
typology03 = type03.plot("country",legend=False,ec="k",lw=.5,color=colors[2],ax=ax)
# 添加文本信息
for loc,label in zip(type01.geometry.centroid,type01.country):
    text = ax.text(loc.x,loc.y,s=label,size=10,ha="center")
for loc,label in zip(type02.geometry.centroid,type02.country):
    text = ax.text(loc.x,loc.y,s=label,size=10,ha="center")
# 单独绘制图例
labels = ["typology01","typology02","typology03"]
handles = [plt.Rectangle((0,0),.5,.5, color=color,ec="k") for color in colors]
bar_legend = ax.legend(handles, labels, loc='upper right', title='Typology Type',
                       fontsize=8,title_fontsize=9)
ax.grid(False)
ax.set_ylim((30, 60))
ax.set_xlim((100, 140))
ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)
ax.spines.left.set_position(("outward",10))
ax.spines.bottom.set_position(("outward",10))
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
fig.tight_layout()
fig.savefig('\第6章 空间数据型图形的绘制\图6-6-1 类型地图绘制示例_b.pdf',bbox_inches='tight')
fig.savefig('\第6章 空间数据型图形的绘制\图6-6-1 类型地图绘制示例_b.png', 
            bbox_inches='tight',dpi=300)         
plt.show()

# c）类型地图注释文本阴影效果绘制样式一

# 添加文字阴影等效果
import matplotlib.patheffects as path_effects

colors = ["#458B74","#CDCD00","#F5DEB3"]
fig,ax = plt.subplots(figsize=(5,4.5),dpi=100,facecolor="w")
typology01 = type01.plot("country",legend=False,ec="k",lw=.5,color=colors[0],ax=ax)
typology02 = type02.plot("country",legend=False,ec="k",lw=.5,color=colors[1],ax=ax)
typology03 = type03.plot("country",legend=False,ec="k",lw=.5,color=colors[2],ax=ax)
# 添加文本信息
for loc,label in zip(type01.geometry.centroid,type01.country):
    ax.text(loc.x,loc.y,s=label,size=10,ha="center",va="center",weight="bold",
                   path_effects=[path_effects.withSimplePatchShadow()])
for loc,label in zip(type02.geometry.centroid,type02.country):
    ax.text(loc.x,loc.y,s=label,size=10,ha="center",va="center",weight="bold",
            path_effects=[path_effects.withSimplePatchShadow()])
# 单独绘制图例
labels = ["typology01","typology02","typology03"]
handles = [plt.Rectangle((0,0),.5,.5, color=color,ec="k") for color in colors]
bar_legend = ax.legend(handles, labels, loc='upper right', title='Typology Type',
                       fontsize=8,title_fontsize=9)
ax.grid(False)
ax.set_ylim((30, 60))
ax.set_xlim((100, 140))
ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)
ax.spines.left.set_position(("outward",10))
ax.spines.bottom.set_position(("outward",10))
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
fig.tight_layout()
fig.savefig('\第6章 空间数据型图形的绘制\图6-6-1 类型地图绘制示例_c.pdf',bbox_inches='tight')
fig.savefig('\第6章 空间数据型图形的绘制\图6-6-1 类型地图绘制示例_c.png', 
            bbox_inches='tight',dpi=300)         
plt.show()

# d）类型地图注释文本阴影效果绘制样式二
# 添加文字阴影等效果
import matplotlib.patheffects as path_effects

colors = ["#458B74","#CDCD00","#F5DEB3"]
fig,ax = plt.subplots(figsize=(5,4.5),dpi=100,facecolor="w")
typology01 = type01.plot("country",legend=False,ec="k",lw=.5,color=colors[0],ax=ax)
typology02 = type02.plot("country",legend=False,ec="k",lw=.5,color=colors[1],ax=ax)
typology03 = type03.plot("country",legend=False,ec="k",lw=.5,color=colors[2],ax=ax)
# 添加文本信息
for loc,label in zip(type01.geometry.centroid,type01.country):
    text = ax.text(loc.x,loc.y,s=label,size=10,ha="center",va="center",color="gray",weight="bold")
    text.set_path_effects([path_effects.Stroke(linewidth=3, foreground='black'),
                           path_effects.Normal()])
for loc,label in zip(type02.geometry.centroid,type02.country):
    text = ax.text(loc.x,loc.y,s=label,size=10,ha="center",va="center",color="gray",weight="bold")
    text.set_path_effects([path_effects.Stroke(linewidth=3, foreground='black'),
                           path_effects.Normal()])

# 单独绘制图例
labels = ["typology01","typology02","typology03"]
handles = [plt.Rectangle((0,0),.5,.5, color=color,ec="k") for color in colors]
bar_legend = ax.legend(handles, labels, loc='upper right', title='Typology Type',
                       fontsize=8,title_fontsize=9)
ax.grid(False)
ax.set_ylim((30, 60))
ax.set_xlim((100, 140))
ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)
ax.spines.left.set_position(("outward",10))
ax.spines.bottom.set_position(("outward",10))
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
fig.tight_layout()

fig.savefig('\第6章 空间数据型图形的绘制\图6-6-1 类型地图绘制示例_d.pdf',bbox_inches='tight')
fig.savefig('\第6章 空间数据型图形的绘制\图6-6-1 类型地图绘制示例_d.png', 
            bbox_inches='tight',dpi=300)         
plt.show()
