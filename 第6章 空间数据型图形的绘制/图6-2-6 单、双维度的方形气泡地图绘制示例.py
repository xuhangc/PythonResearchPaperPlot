"""
编写时间：2022年4月28日 16：30

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

"""
此代码为使用Python-Prolot包进行学术风格图表绘制，绘图语法和Matplotlib有所不同，需注意。
"""

import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from colormaps import parula

from proplot import rc
rc["font.family"] = "Times New Roman"
rc["axes.labelsize"] = 15
rc["tick.labelsize"] = 10
rc["suptitle.size"] = 15
rc["title.size"] = 14

file = r"\第6章 空间数据型图形的绘制\Virtual_Map0.shp"
map_fig01 = gpd.read_file(file)
values01 = pd.read_csv(r"第6章 空间数据型图形的绘制\Virtual_City.csv")
#合并数据
merger01 = pd.merge(left=map_fig02,right=values01,on="country",how="right")

square_data = merger01[["lat","long","orange"]]
square_data = square_data.drop_duplicates()

square_x = square_data["long"]
square_y = square_data["lat"]
square_s = square_data["orange"]

# a）方形气泡地图的单维度数值映射（方形大小）
fig,ax = plt.subplots(figsize=(5,4.5),dpi=100,facecolor="w")
map_01 = merger01.plot("type",legend=False,ec="k",lw=.5,color="#9CCA9C",alpha=.8,ax=ax)

square_plot = ax.scatter(square_x,square_y,square_s*20,marker="s",color="#BC3C29",ec="w")
# 添加图例
kw = dict(prop="sizes", num=5, color="#BC3C29",mec="k",
          func=lambda s: s/20)
legend = ax.legend(*square_plot.legend_elements(**kw),
                    loc="upper right", bbox_to_anchor=(1, 1),
                    title="Orange",fontsize=9,handletextpad=.1,
                    title_fontsize=10)
ax.grid(False)
ax.set_ylim((30, 60))
ax.set_xlim((100, 140))
ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)
ax.spines.left.set_position(("outward",10))
ax.spines.bottom.set_position(("outward",10))
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
plt.tight_layout()
fig.savefig('\第6章 空间数据型图形的绘制\图6-2-6 单、双维度的方形气泡地图绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第6章 空间数据型图形的绘制\图6-2-6 单、双维度的方形气泡地图绘制示例_a.png', 
            bbox_inches='tight',dpi=300)         
plt.show()

# b）方形气泡地图的双维度数值映射（方形大小、数据类别）
merger_square = merger01.drop_duplicates(subset="country")

def color_set(x):
    if x in ["JACK","JAY"]:
        color = "#BC3C29"
    elif x in ["EELIN","RON"]:
        color = "#0072B5"
    else:
        color = "#E18727"
    return color
    
merger_square["square_color"] = merger_square["country"].map(lambda x :color_set(x))
color = merger_square.square_color
fig,ax = plt.subplots(figsize=(5,4.5),dpi=100,facecolor="w")
map_01 = merger01.plot("type",legend=False,ec="k",lw=.5,color="#9CCA9C",alpha=.8,ax=ax)
square_plot = ax.scatter(square_x,square_y,square_s*20,marker="s",color=color,ec="k")

# 单独类别图例
colors = ["#BC3C29","#0072B5","#E18727"]
square1, = ax.plot([],[],marker="s",ls="",ms=8,mec="k",mew=.6,color=colors[0],label="Typology 1")
square2, = ax.plot([],[],marker="s",ls="",ms=8,mec="k",mew=.6,color=colors[1],label="Typology 2")
square3, = ax.plot([],[],marker="s",ls="",ms=8,mec="k",mew=.6,color=colors[2],label="Typology 3")
legend1 = [square1,square2,square3]
lab1 = [h.get_label() for h in legend1]
square_legend = ax.legend(legend1,lab1,title='Typology Class',fontsize=8,title_fontsize=9,
                          loc='lower right',handletextpad=.1)
ax.add_artist(square_legend)
# 构建大小映射图例
handles, labels = square_plot.legend_elements(prop="sizes", num=5, color="gray",
                                              mec="k",func=lambda s: s/20)
legend2 = ax.legend(handles, labels, loc="upper right", bbox_to_anchor=(1, 1),
                    title="Orange",fontsize=9,handletextpad=.1,
                    title_fontsize=10)

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
fig.savefig('\第6章 空间数据型图形的绘制\图6-2-6 单、双维度的方形气泡地图绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第6章 空间数据型图形的绘制\图6-2-6 单、双维度的方形气泡地图绘制示例_a.png', 
            bbox_inches='tight',dpi=300)         
plt.show()




