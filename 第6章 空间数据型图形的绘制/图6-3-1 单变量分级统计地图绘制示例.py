"""
编写时间：2022年4月28日 19：30

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

values01 = pd.read_csv(r"\第6章 空间数据型图形的绘制\Virtual_City.csv")
map_fig = gpd.read_file(r"\第6章 空间数据型图形的绘制\Virtual_Map1.shp")
# 拼接数据
merger01 = map_fig0.merge(values01,on="country")


# a）单变量分级统计地图的单色系渐变映射
fig,ax = plt.subplots(figsize=(5,4.5),dpi=100,facecolor="w")
choropleth_map01 = merger01.plot(column="orange",ec="k",lw=.6,cmap=parula,legend=True,
                                 legend_kwds=dict(label="Orange",aspect=11,shrink=0.4),
                                 ax=ax)
# 添加文本信息
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
plt.tight_layout()

fig.savefig('\第6章 空间数据型图形的绘制\图6-3-1 单变量分级统计地图绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第6章 空间数据型图形的绘制\图6-3-1 单变量分级统计地图绘制示例_a.png', 
            bbox_inches='tight',dpi=300)         
plt.show()


# b）单变量分级统计地图的双色系渐变映射

fig,ax = plt.subplots(figsize=(5,4.5),dpi=100,facecolor="w")
choropleth_map01 = merger01.plot(column="orange",ec="k",lw=.6,cmap="div",legend=True,
                                 legend_kwds=dict(label="Orange",aspect=11,shrink=0.4),
                                 ax=ax)
# 添加文本信息
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
plt.tight_layout()

fig.savefig('\第6章 空间数据型图形的绘制\图6-3-1 单变量分级统计地图绘制示例_b.pdf',bbox_inches='tight')
fig.savefig('\第6章 空间数据型图形的绘制\图6-3-1 单变量分级统计地图绘制示例_b.png', 
            bbox_inches='tight',dpi=300)         
plt.show()





