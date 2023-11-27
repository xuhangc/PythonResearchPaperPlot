"""
编写时间：2022年4月28日 14：20

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

# a）多面中心坐标点绘制示例
fig,ax = plt.subplots(figsize=(5,4.5),dpi=100,facecolor="w")
plot02 = map_fig02.plot("country",legend=False,ec="k",lw=.5,color="#9CCA9C",alpha=.8,
                       ax=ax)
for loc in map_fig02.geometry.centroid:
    ax.scatter(loc.x,loc.y,s=18,fc="w",ec="k",lw=1)
# 构建图例
ax.scatter([],[],fc="w",ec="k",lw=1,label="Test Point")
ax.grid(False)
ax.set_ylim((30, 60))
ax.set_xlim((100, 140))
ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)
ax.spines.left.set_position(("outward",10))
ax.spines.bottom.set_position(("outward",10))
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
ax.legend()
fig.tight_layout()
fig.savefig('\第6章 空间数据型图形的绘制\6-2-4 常见基础地理空间地图类型绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第6章 空间数据型图形的绘制\6-2-4 常见基础地理空间地图类型绘制示例_a.png', 
            bbox_inches='tight',dpi=300)         
plt.show()


values01 = pd.read_csv(r"第6章 空间数据型图形的绘制\Virtual_City.csv")
#合并数据
merger01 = pd.merge(left=map_fig02,right=values01,on="country",how="right")

# b）多面中心坐标文本添加示例

fig,ax = plt.subplots(figsize=(5,4.5),dpi=100,facecolor="w")
plot02 = map_fig02.plot("country",legend=False,ec="k",lw=.5,color="#9CCA9C",alpha=.8,
                       ax=ax)
for x, y,label in zip(merger01.long,merger01.lat,merger01.country):
    ax.text(x,y,label,size=6,color="k",bbox=dict(boxstyle="round", fc="w"))
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
fig.savefig('\第6章 空间数据型图形的绘制\6-2-4 常见基础地理空间地图类型绘制示例_b.pdf',bbox_inches='tight')
fig.savefig('\第6章 空间数据型图形的绘制\6-2-4 常见基础地理空间地图类型绘制示例_b.png', 
            bbox_inches='tight',dpi=300)         
plt.show()



point_data = pd.read_excel(r"\第6章 空间数据型图形的绘制\地图监测点数据.xlsx")
single = point_data[point_data['type']==1]
point_x = single["lon"]
point_y = single["lat"]

point_x2 = single2["lon"]
point_y2 = single2["lat"]

# c）单系列虚拟监测站点绘制示例


fig,ax = plt.subplots(figsize=(5,4.5),dpi=100,facecolor="w")
plot01 = map_fig02.plot("type",ec="k",lw=.5,color="#9CCA9C",alpha=.8,ax=ax)
# 添加监测站点信息
ax.scatter(x=point_x,y=point_y,s=15,color="k",label="Monitoring Points")
ax.grid(False)
ax.set_ylim((30, 60))
ax.set_xlim((100, 140))
ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)
ax.spines.left.set_position(("outward",10))
ax.spines.bottom.set_position(("outward",10))
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
ax.legend()
fig.tight_layout()
fig.savefig('\第6章 空间数据型图形的绘制\6-2-4 常见基础地理空间地图类型绘制示例_c.pdf',bbox_inches='tight')
fig.savefig('\第6章 空间数据型图形的绘制\6-2-4 常见基础地理空间地图类型绘制示例_c.png', 
            bbox_inches='tight',dpi=300)         
plt.show()

# d）多系列虚拟监测站点绘制示例

fig,ax = plt.subplots(figsize=(5,4.5),dpi=100,facecolor="w")
plot01 = map_fig02.plot("type",ec="k",lw=.5,color="#9CCA9C",alpha=.8,ax=ax)
# 添加监测站点信息
ax.scatter(x=point_x,y=point_y,s=15,color="k",label="Monitoring Points One")
ax.scatter(x=point_x2,y=point_y2,s=15,marker="v",color="r",label="Monitoring Points Two")
ax.grid(False)
ax.set_ylim((30, 60))
ax.set_xlim((100, 140))
ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)
ax.spines.left.set_position(("outward",10))
ax.spines.bottom.set_position(("outward",10))
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
ax.legend()
fig.tight_layout()
fig.savefig('\第6章 空间数据型图形的绘制\6-2-4 常见基础地理空间地图类型绘制示例_d.pdf',bbox_inches='tight')
fig.savefig('\第6章 空间数据型图形的绘制\6-2-4 常见基础地理空间地图类型绘制示例_d.png', 
            bbox_inches='tight',dpi=300)         
plt.show()

# e）研究区域、注释信息绘制示例
test_point_x = [111,121,121]
test_point_y = [44.5,37.5,51.5]

fig,ax = plt.subplots(figsize=(5,4.5),dpi=100,facecolor="w")
plot01 = map_fig02.plot("type",legend=True,ec="k",lw=.5,color="#9CCA9C",alpha=.8,ax=ax)
ploygon_fig =ploygon_df.plot(ax=ax,facecolor="none",ec="#F8A202",lw=.8)
for x,y in zip(test_point_x,test_point_y):
    ax.scatter(x,y,s=20,color="k")
ax.annotate(text="Test Point 01",xy=(111.5,44.5),xytext=(105,35),
            ha="center",fontsize=8,
            bbox=dict(boxstyle="round", fc="w"),
            arrowprops=dict(arrowstyle="->", color="k",
                                shrinkA=5, shrinkB=5,
                                patchA=None, patchB=None,
                                connectionstyle="angle3,angleA=90,angleB=30",
                                ))
ax.annotate(text="Test Point 02",xy=(120,37.5),xytext=(128.5,30),
            ha="center",fontsize=8,
            bbox=dict(fc="w"),
            arrowprops=dict(arrowstyle="-", color="k",
                                shrinkA=5, shrinkB=5,
                                patchA=None, patchB=None,
                                connectionstyle="arc,angleA=50,angleB=0,armA=0,armB=90,rad=10",
                                ))
ax.annotate(text="Test Point 03",xy=(120.5,51.2),xytext=(132,57),
            ha="center",fontsize=8,
            arrowprops=dict(arrowstyle="-", color="k",
                                shrinkA=5, shrinkB=5,
                                patchA=None, patchB=None,
                                connectionstyle="arc3,rad=0",
                                ))
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
fig.savefig('\第6章 空间数据型图形的绘制\6-2-4 常见基础地理空间地图类型绘制示例_e.pdf',bbox_inches='tight')
fig.savefig('\第6章 空间数据型图形的绘制\6-2-4 常见基础地理空间地图类型绘制示例_e.png', 
            bbox_inches='tight',dpi=300)         
plt.show()

# f）单系列监测站点数值映射绘制示例

from palettable import colorbrewer,cartocolors
cmap = colorbrewer.sequential.GnBu_9.mpl_colormap

point_data = pd.read_excel(r"\第6章 空间数据型图形的绘制\地图监测点数据.xlsx")
point_x = single["lon"]
point_y = single["lat"]
aes_values = single["values"]

fig,ax = plt.subplots(figsize=(5,4.5),dpi=100,facecolor="w")
plot01 = map_fig02.plot("type",ec="k",lw=.5,color="#9CCA9C",alpha=.8,ax=ax)
# 添加监测站点信息
aes_scatter = ax.scatter(x=point_x,y=point_y,s=30,c=aes_values,ec="k",lw=.5,cmap = cmap,
           label="Monitoring Points")
# 添加colorbar
cbar = fig.colorbar(aes_scatter,shrink=.4,aspect=10)
cbar.ax.set_ylabel(ylabel="Aes Values",fontsize=11)
cbar.ax.set_title("Values",fontsize=12,pad=5)
cbar.ax.tick_params(left=True,direction="in",labelsize=10)
cbar.ax.tick_params(which="minor",right=False)
ax.grid(False)
ax.set_ylim((30, 60))
ax.set_xlim((100, 140))
ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)
ax.spines.left.set_position(("outward",10))
ax.spines.bottom.set_position(("outward",10))
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
ax.legend()
fig.tight_layout()
fig.savefig('\第6章 空间数据型图形的绘制\6-2-4 常见基础地理空间地图类型绘制示例_f.pdf',bbox_inches='tight')
fig.savefig('\第6章 空间数据型图形的绘制\6-2-4 常见基础地理空间地图类型绘制示例_f.png', 
            bbox_inches='tight',dpi=300)         
plt.show()


