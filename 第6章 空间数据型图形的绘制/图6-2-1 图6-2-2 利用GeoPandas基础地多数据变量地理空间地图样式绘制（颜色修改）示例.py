"""
编写时间：2022年4月28日 10：40

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

"""
此代码为使用Python-Prolot包进行学术风格图表绘制，绘图语法和Matplotlib有所不同，需注意。
"""

import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from proplot import rc
rc["font.family"] = "Times New Roman"
rc["axes.labelsize"] = 15
rc["tick.labelsize"] = 10
rc["suptitle.size"] = 15
rc["title.size"] = 14

file = r"\第6章 空间数据型图形的绘制\Virtual_Map0.shp"
map_fig01 = gpd.read_file(file)

#****************** 图6-2-1 利用GeoPandas绘制的基础地理空间底图样式（自定义颜色修）示例**************************

# a）地理空间地图基本样式
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
plot01 = map_fig01.plot("type",legend=True,ec="k",lw=.5,
                   legend_kwds=dict(loc="lower right",title="Type",title_fontsize=12),
                   ax=ax)
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
fig.tight_layout()

fig.savefig('\第6章 空间数据型图形的绘制\\图6-2-1 利用GeoPandas绘制的基础地理空间底图样式（自定义颜色修）示例_a.pdf',bbox_inches='tight')
fig.savefig('\第6章 空间数据型图形的绘制\\图6-2-1 利用GeoPandas绘制的基础地理空间底图样式（自定义颜色修）示例_a.png', 
            bbox_inches='tight',dpi=300)
            
plt.show()

# b）地理空间地图基本样式（自定义颜色）
from matplotlib.colors import ListedColormap
colors = ["#2FBE8F","#459DFF"]#,"#FF5B9B","#FFCC37","#751DFE"]
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
plot01 = map_fig01.plot("type",legend=True,ec="k",lw=.5,cmap=ListedColormap(colors),
                   legend_kwds=dict(loc="lower right",title="Type",title_fontsize=12),
                   ax=ax)
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
fig.tight_layout()   
fig.savefig('\第6章 空间数据型图形的绘制\\图6-2-1 利用GeoPandas绘制的基础地理空间底图样式（自定义颜色修）示例_b.pdf',bbox_inches='tight')
fig.savefig('\第6章 空间数据型图形的绘制\\图6-2-1 利用GeoPandas绘制的基础地理空间底图样式（自定义颜色修）示例_b.png', 
            bbox_inches='tight',dpi=300)
            
plt.show()

#****************** 图6-2-2 利用GeoPandas基础地多数据变量地理空间地图样式绘制（颜色修改）示例**************************
import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from proplot import rc
rc["font.family"] = "Times New Roman"
rc["axes.labelsize"] = 15
rc["tick.labelsize"] = 10
rc["suptitle.size"] = 15
rc["title.size"] = 14

file = r"\第6章 空间数据型图形的绘制\Virtual_Map0.shp"
map_fig01 = gpd.read_file(file)

# a）多数据变量填充地图绘制
fig,ax = plt.subplots(figsize=(4,3),dpi=100,facecolor="w")
plot01 = map_fig02.plot("country",legend=True,ec="k",lw=.5,
                   legend_kwds=dict(loc="upper right",title="Country",title_fontsize=12,
                                    bbox_to_anchor=((1.36, 1,)),
                                    markerscale=.8,frameon=True),
                    ax=ax)
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
fig.tight_layout()
fig.savefig('\第6章 空间数据型图形的绘制\图6-2-2 利用GeoPandas基础地多数据变量地理空间地图样式绘制（颜色修改）示例_a.pdf',bbox_inches='tight')
fig.savefig('\第6章 空间数据型图形的绘制\图6-2-2 利用GeoPandas基础地多数据变量地理空间地图样式绘制（颜色修改）示例_a.png', 
            bbox_inches='tight',dpi=300)
            
plt.show()

# b）多数据变量填充地图绘制（颜色修改）

from colormaps import parula
fig,ax = plt.subplots(figsize=(4,3),dpi=100,facecolor="w")
plot02 = map_fig02.plot("country",legend=True,ec="k",lw=.5,cmap=parula,
                   legend_kwds=dict(loc="upper right",title="Country",title_fontsize=12,
                                    bbox_to_anchor=((1.36, 1,)),
                                    markerscale=.8,frameon=True),
                    ax=ax)
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
fig.tight_layout()

fig.savefig('\第6章 空间数据型图形的绘制\图6-2-2 利用GeoPandas基础地多数据变量地理空间地图样式绘制（颜色修改）示例_b.pdf',bbox_inches='tight')
fig.savefig('\第6章 空间数据型图形的绘制\图6-2-2 利用GeoPandas基础地多数据变量地理空间地图样式绘制（颜色修改）示例_b.png', 
            bbox_inches='tight',dpi=300)
            
plt.show()

