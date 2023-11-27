
"""
编写时间：2022年4月30日 09：30

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


link_data = pd.read_excel(r"\第6章 空间数据型图形的绘制\Link_Map_data.xlsx")
map_fig02 = gpd.read_file(r"\第6章 空间数据型图形的绘制\Virtual_Map1.shp")

link_one_data = link_data[link_data["line class"]==1]
link_two_data = link_data[link_data["line class"]==2]

link_one_lon = link_one_data.loc[link_one_data["country"]=="Link Point1","long"]
link_one_lat = link_one_data.loc[link_one_data["country"]=="Link Point1","lat"]
link_two_lon = link_two_data.loc[link_two_data["country"]=="Link Point2","long"]
link_two_lat = link_two_data.loc[link_two_data["country"]=="Link Point2","lat"]

link_one_other = link_one_data.loc[link_one_data["country"]!="Link Point1",:]
link_two_other = link_two_data.loc[link_two_data["country"]!="Link Point2",:]


# a）多类别连接线地图绘制（直角连接线）
fig,ax = plt.subplots(figsize=(5,4.5),dpi=100,facecolor="w")
plot02 = map_fig02.plot("country",legend=False,ec="k",lw=.5,color="#9CCA9C",alpha=.8,
                       ax=ax)
for x,y,width in zip(link_one_other["long"],link_one_other["lat"],link_one_other["line width"]):
    ax.plot([link_one_lon,x],[link_one_lat,y],linewidth=width,color="k")

for x,y,width in zip(link_two_other["long"],link_two_other["lat"],link_two_other["line width"]):
    ax.plot([link_two_lon,x],[link_two_lat,y],linewidth=width,color="r")   
    
# 单独构建图例
Line1, = ax.plot([],[],color="k",linewidth=2,label="Line Class 1")
Line2, = ax.plot([],[],color="r",linewidth=2,label="Line Class 2")
legend1 = [Line1,Line2]
lab1 = [h.get_label() for h in legend1]
line_legend = ax.legend(legend1,lab1,title='Line Type',fontsize=8,title_fontsize=9,
                        loc='upper right')
ax.add_artist(line_legend)

legend2 = []
for value in legend_data:
    line, = ax.plot([],[],color="k",linewidth=value,label=str(value))
    legend2.append(line)
lab2 = [ h.get_label() for h in legend2]

ax.grid(False)
ax.set_ylim((30, 60))
ax.set_xlim((100, 140))
ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)
ax.spines.left.set_position(("outward",10))
ax.spines.bottom.set_position(("outward",10))
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")

line_width_legend = ax.legend(legend2,lab2,title='Line Width\n(class)',fontsize=8,title_fontsize=9,
                             loc="lower right")
# 设置标题文本居中
line_width_legend.get_title().set_horizontalalignment("center")
fig.tight_layout()

fig.savefig('\第6章 空间数据型图形的绘制\图6-5-2多类别连接线地图绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第6章 空间数据型图形的绘制\图6-5-2多类别连接线地图绘制示例_a.png', 
            bbox_inches='tight',dpi=300)         
plt.show()

# b）多类别连接线地图绘制（圆角连接线）

fig,ax = plt.subplots(figsize=(5,4.5),dpi=100,facecolor="w")
plot02 = map_fig02.plot("country",legend=False,ec="k",lw=.5,color="#9CCA9C",alpha=.8,
                       ax=ax)
for x,y,width in zip(link_one_other["long"],link_one_other["lat"],link_one_other["line width"]):
    ax.plot([link_one_lon,x],[link_one_lat,y],linewidth=width,color="k",solid_capstyle="round")

for x,y,width in zip(link_two_other["long"],link_two_other["lat"],link_two_other["line width"]):
    ax.plot([link_two_lon,x],[link_two_lat,y],linewidth=width,color="r",solid_capstyle="round")   
    
# 单独构建图例
Line1, = ax.plot([],[],color="k",linewidth=2,label="Line Class 1",solid_capstyle="round")
Line2, = ax.plot([],[],color="r",linewidth=2,label="Line Class 2",solid_capstyle="round")
legend1 = [Line1,Line2]
lab1 = [h.get_label() for h in legend1]
line_legend = ax.legend(legend1,lab1,title='Line Type',fontsize=8,title_fontsize=9,
                        loc='upper right')
ax.add_artist(line_legend)

legend2 = []
for value in legend_data:
    line, = ax.plot([],[],color="k",linewidth=value,label=str(value),solid_capstyle="round")
    legend2.append(line)
lab2 = [ h.get_label() for h in legend2]

ax.grid(False)
ax.set_ylim((30, 60))
ax.set_xlim((100, 140))
ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)
ax.spines.left.set_position(("outward",10))
ax.spines.bottom.set_position(("outward",10))
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")

line_width_legend = ax.legend(legend2,lab2,title='Line Width\n(class)',fontsize=8,title_fontsize=9,
                             loc="lower right")
# 设置标题文本居中
line_width_legend.get_title().set_horizontalalignment("center")
fig.tight_layout()

fig.savefig('\第6章 空间数据型图形的绘制\图6-5-2多类别连接线地图绘制示例_b.pdf',bbox_inches='tight')
fig.savefig('\第6章 空间数据型图形的绘制\图6-5-2多类别连接线地图绘制示例_b.png', 
            bbox_inches='tight',dpi=300)         
plt.show()

