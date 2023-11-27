"""
编写时间：2022年4月28日 11：20

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


# a）默认空间地图绘制样式（ProPlot）

fig,ax = plt.subplots(figsize=(5,4.5),dpi=100,facecolor="w")
plot01 = map_fig02.plot("type",ec="k",lw=.5,color="#9CCA9C",alpha=.8,ax=ax),
ax.grid(False)
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
fig.tight_layout()
fig.savefig('\第6章 空间数据型图形的绘制\图6-2-3 不同坐标系样式空间地图绘制示例对比_a.pdf',bbox_inches='tight')
fig.savefig('\第6章 空间数据型图形的绘制\图6-2-3 不同坐标系样式空间地图绘制示例对比_a.png', 
            bbox_inches='tight',dpi=300)
            
plt.show()

# b）修改轴脊样式空间地图绘制（ProPlot）
fig,ax = plt.subplots(figsize=(5,4.5),dpi=100,facecolor="w")
plot01 = map_fig02.plot("type",ec="k",lw=.5,color="#9CCA9C",alpha=.8,ax=ax),
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
fig.savefig('\第6章 空间数据型图形的绘制\图6-2-3 不同坐标系样式空间地图绘制示例对比_b.pdf',bbox_inches='tight')
fig.savefig('\第6章 空间数据型图形的绘制\图6-2-3 不同坐标系样式空间地图绘制示例对比_b.png', 
            bbox_inches='tight',dpi=300)
            
plt.show()
