
"""
编写时间：2022年4月28日 21：30

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
stats_map = map_fig02[map_fig02["country"].isin(["PETER","JACK","EELIN","RON"])]
stats_map = stats_map.drop_duplicates(subset=["country"],keep="first")

# a）带柱形图的地图示例

def map_bar3(height,x_pos,y_pos,adjust,ax_width,ax_height,main_ax):
    x = np.arange(1,len(height)+1)
    ax_bar = main_ax.inset_axes([x_pos-adjust,y_pos-adjust,ax_width,ax_height],
                                transform=main_ax.transData)
    ax_bar.bar(x, height,width=1,ec="k",lw=.3,color=colors[:3])
    ax_bar.set_facecolor("none")
    ax_bar.grid(False)
    ax_bar.tick_params(which="both",labelleft=False,left=False,bottom=False,labelbottom=False)
    for spine in ["left","top","right"]:
        ax_bar.spines[spine].set_visible(False)
    return ax_bar
    
    
heights = [[1,2,3],[2,1,4],[3,2,5],[3,1,6]]
colors = ["#2FBE8F","#459DFF","#FF5B9B"]
fig,main_ax = plt.subplots(figsize=(5,4.5),dpi=100,facecolor="w")
map_fig02.plot("country",legend=False,ec="k",lw=.5,color="#9CCA9C",alpha=.8,
                ax=main_ax)
# 绘制柱形图
for x, y, height in zip(stats_map.centroid.x,stats_map.centroid.y,heights):
    height = height
    adjust = 1.5
    map_bar = map_bar3(height,x_pos=x,y_pos=y,adjust=adjust,ax_width=2.5,ax_height=3,
                       main_ax=main_ax)
# 绘制构建的柱形图图例
labels = ["One","Two","Three"]
handles = [plt.Rectangle((0,0),.5,.5, color=color,ec="k") for color in colors]
bar_legend = main_ax.legend(handles, labels, loc='upper right', title='Type',
                        fontsize=10,title_fontsize=11,handlelength=1,handleheight=1)

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

fig.savefig('\第6章 空间数据型图形的绘制\图6-4-1 带统计信息的地图绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第6章 空间数据型图形的绘制\图6-4-1 带统计信息的地图绘制示例_a.png', 
            bbox_inches='tight',dpi=300)         
plt.show()

# b）带饼图的地图示例

def map_pie(value,x_pos,y_pos,adjust,ax_width,ax_height,main_ax,colors):
    ax_pie = main_ax.inset_axes([x_pos-adjust,y_pos-adjust,ax_width,ax_height],
                                transform=main_ax.transData)
    ax_pie.pie(value,shadow=False,colors=colors,
               wedgeprops={"lw": .5, "edgecolor": "k"})
    ax_pie.set_facecolor("none")
    ax_pie.grid(False)
    ax_pie.tick_params(which="both",labelleft=False,left=False,bottom=False,labelbottom=False)
    for spine in ["left","top","right"]:
        ax_pie.spines[spine].set_visible(False)
    return ax_pie
    
values = [[15, 10, 45, 30],[15, 30, 45, 10],
          [25, 30, 15, 30],[35, 10, 35, 20]]
colors = ["#2FBE8F","#459DFF","#FF5B9B","#FFCC37"]
labels = ['One', 'Two','Three','Four']
fig,main_ax = plt.subplots(figsize=(5,4.5),dpi=100,facecolor="w")
map_fig02.plot("country",legend=False,ec="k",lw=.5,color="#9CCA9C",alpha=.8,
               ax=main_ax)
# 绘制饼图
for x, y, value in zip(stats_map.centroid.x,stats_map.centroid.y,values):
    height = height
    adjust = 1.5
    map_bar = map_pie(value,colors=colors,x_pos=x,y_pos=y,adjust=adjust,ax_width=4,ax_height=4,
                       main_ax=main_ax)
# 绘制构建的柱形图图例
handles = [plt.Rectangle((0,0),.5,.5, color=color,ec="k") for color in colors]
bar_legend = main_ax.legend(handles, labels, loc='upper right', title='Type',
                        fontsize=10,title_fontsize=11,handlelength=1,handleheight=1)

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

fig.savefig('\第6章 空间数据型图形的绘制\图6-4-1 带统计信息的地图绘制示例_b.pdf',bbox_inches='tight')
fig.savefig('\第6章 空间数据型图形的绘制\图6-4-1 带统计信息的地图绘制示例_b.png', 
            bbox_inches='tight',dpi=300)         
plt.show()


