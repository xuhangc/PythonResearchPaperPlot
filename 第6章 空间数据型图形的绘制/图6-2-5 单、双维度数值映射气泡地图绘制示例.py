"""
编写时间：2022年4月28日 16：20

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

bubble_data = merger01[["lat","long","orange"]]
bubble_data = bubble_data.drop_duplicates()


# a）气泡地图的单维度数值映射（气泡大小）

bubble_x = bubble_data["long"]
bubble_y = bubble_data["lat"]
bubble_s = bubble_data["orange"]

fig,ax = plt.subplots(figsize=(5,4.5),dpi=100,facecolor="w")
map_01 = merger01.plot("type",legend=True,ec="k",lw=.5,color="#9CCA9C",alpha=.8,ax=ax)
bubble_plot = ax.scatter(bubble_x,bubble_y,bubble_s*20,color="#F7D826",ec="k")
# 添加图例
kw = dict(prop="sizes", num=5, color="#F7D826",mec="k",
          func=lambda s: s/20)
legend2 = ax.legend(*bubble_plot.legend_elements(**kw),
                    loc="upper right", bbox_to_anchor=(1, 1.1),
                    title="Orange",fontsize=13,handletextpad=.1,
                    title_fontsize=14)
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

fig.savefig('\第6章 空间数据型图形的绘制\图6-2-5 单、双维度数值映射气泡地图绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第6章 空间数据型图形的绘制\图6-2-5 单、双维度数值映射气泡地图绘制示例_a.png', 
            bbox_inches='tight',dpi=300)         
plt.show()

# b）气泡地图的双维度数值映射（气泡大小、颜色）

bubble_x = bubble_data["long"]
bubble_y = bubble_data["lat"]
bubble_s = bubble_data["orange"]

fig,ax = plt.subplots(figsize=(5,4.5),dpi=100,facecolor="w")
map_01 = merger01.plot("type",legend=True,ec="k",lw=.5,color="#9CCA9C",alpha=.8,ax=ax)
bubble_plot = ax.scatter(bubble_x,bubble_y,bubble_s*20,c=bubble_s,cmap=parula,ec="k")
# 添加图例
kw = dict(prop="sizes", num=5, color="none",mec="k",
          func=lambda s: s/20)
legend = ax.legend(*bubble_plot.legend_elements(**kw),
                    loc="upper right", bbox_to_anchor=(1.05, 1.),
                    title="Orange",fontsize=11,handletextpad=.1,
                    title_fontsize=12,frameon=False)
cax = ax.inset_axes([.94, 0.02, 0.05, 0.5], 
                    transform=ax.transAxes)
colorbar = fig.colorbar(bubble_plot, cax=cax)
colorbar.ax.set_title("Orange",fontsize=12,pad=5)
#colorbar.set_label('Cbar_values', rotation=270, va='baseline')
colorbar.ax.tick_params(which="both",direction="in",labelsize=11)
#colorbar.ax.tick_params()
colorbar.outline.set_linewidth(.5)
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

fig.savefig('\第6章 空间数据型图形的绘制\图6-2-5 单、双维度数值映射气泡地图绘制示例_b.pdf',bbox_inches='tight')
fig.savefig('\第6章 空间数据型图形的绘制\图6-2-5 单、双维度数值映射气泡地图绘制示例_b.png', 
            bbox_inches='tight',dpi=300)         
plt.show()

