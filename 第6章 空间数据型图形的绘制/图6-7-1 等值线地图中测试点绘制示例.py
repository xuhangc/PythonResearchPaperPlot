"""
编写时间：2022年4月30日 13：30

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
df_city = pd.read_csv(r"\第6章 空间数据型图形的绘制\Virtual_huouse.csv")

point_x = df_city["long"]
point_y = df_city["lat"]
point_value = df_city["value"]


# a）样例数据点位置分布（透明度设置）

fig,ax = plt.subplots(figsize=(5,4.5),dpi=100,facecolor="w")
plot02 = map_fig02.plot("country",legend=False,ec="k",lw=.5,color="#9CCA9C",alpha=.8,
                       ax=ax)
point = ax.scatter(x=point_x,y=point_y,s=9,color="k",alpha=.5)
# 构建图例
ax.scatter([],[],color="k",s=10,label="Test Point")
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

fig.savefig('\第6章 空间数据型图形的绘制\图6-7-1 等值线地图中测试点绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第6章 空间数据型图形的绘制\图6-7-1 等值线地图中测试点绘制示例_a.png', 
            bbox_inches='tight',dpi=300)         
plt.show()

# b）样例数据点位置分布（数值映射颜色）

fig,ax = plt.subplots(figsize=(5,4.5),dpi=100,facecolor="w")
plot02 = map_fig02.plot("country",legend=False,ec="k",lw=.5,color="#9CCA9C",alpha=.8,
                       ax=ax)
point = ax.scatter(x=point_x,y=point_y,s=9,c=point_value,cmap=parula)

# 添加colorbar
cbar = fig.colorbar(point,shrink=.4,aspect=10)
cbar.ax.set_ylabel(ylabel="Point Values",fontsize=11)
cbar.ax.set_title("Values",fontsize=12,pad=5)
cbar.ax.tick_params(left=True,direction="in",labelsize=10)
cbar.ax.tick_params(which="minor",right=False)
#添加图例
ax.scatter([],[],ec="k",fc="w",lw=.6,s=11,label="Test Point")
ax.grid(False)
ax.set_ylim((30, 60))
ax.set_xlim((100, 140))
ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)
ax.spines.left.set_position(("outward",10))
ax.spines.bottom.set_position(("outward",10))
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
ax.legend(handletextpad=.1)
fig.tight_layout()

fig.savefig('\第6章 空间数据型图形的绘制\图6-7-1 等值线地图中测试点绘制示例_b.pdf',bbox_inches='tight')
fig.savefig('\第6章 空间数据型图形的绘制\图6-7-1 等值线地图中测试点绘制示例_b.png', 
            bbox_inches='tight',dpi=300)         
plt.show()
