"""
编写时间：2022年4月15日 16：30

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

"""
此代码为使用Python-Prolot包进行学术风格图表绘制，绘图语法和Matplotlib有所不同，需注意。

"""

import numpy as np
import pandas as pd
import seaborn as sns
import proplot as pplt
import matplotlib.pyplot as plt
from colormaps import parula

from proplot import rc
rc["tick.minor"] = False
rc["font.family"] = "Times New Roman"
rc["axes.labelsize"] = 15
rc["tick.labelsize"] = 12
rc["suptitle.size"] = 15
rc["title.size"] = 14


matrix = pd.read_excel(r"\第5章 多变量图形的绘制\矩阵气泡图数据.xlsx")
matrix_melt = pd.melt(matrix,id_vars="columns")
matrix_melt.columns = ['x', 'y', 'value']

x=matrix_melt['x']
y=matrix_melt['y']
size=matrix_melt["value"]

# a）矩阵气泡图绘制示例（圆点）
fig,ax = plt.subplots(figsize=(4,3.3),dpi=100,facecolor="w")
matrix_pubble = ax.scatter(x,y,s=size,c=size,cmap="jet",ec="k",lw=.3)
# 绘制图例
handles, labels = matrix_pubble.legend_elements(prop="sizes", alpha=0.6,
                                        num=5, color="gray",mec="k",fmt="{x:.0f}",
                                        )
legend = ax.legend(handles, labels, loc="upper right", title="Sizes", bbox_to_anchor=(1.25, 1.),
                   fontsize=11,title_fontsize=12,handletextpad=.1,frameon=False)
cax = ax.inset_axes([1.05, 0.01, 0.06, 0.4], 
                    transform=ax.transAxes)
cbar = fig.colorbar(matrix_pubble, cax=cax,
                   ticks=[min(size), 75, 100, 125, 150])
cbar.ax.tick_params(left=True,direction="in",width=.5,labelsize=10)
#cbar.ax.tick_params(which="minor",right=False)
cbar.outline.set_linewidth(.5)
plt.tight_layout()

fig.savefig('\第5章 多变量图形的绘制\图5-2-4 矩阵气泡图绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第5章 多变量图形的绘制\图5-2-4 矩阵气泡图绘制示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# b）矩阵气泡图绘制示例（方块）
fig,ax = plt.subplots(figsize=(4,3.3),dpi=100,facecolor="w")
matrix_pubble = ax.scatter(x,y,s=size,c=size,cmap=parula,marker="s",ec="k",lw=.5)
# 绘制图例
handles, labels = matrix_pubble.legend_elements(prop="sizes", alpha=0.6,
                                        num=5, color="gray",mec="k",fmt="{x:.0f}",
                                        )
legend = ax.legend(handles, labels, loc="upper right", title="Sizes", bbox_to_anchor=(1.25, 1.),
                   fontsize=11,title_fontsize=12,handletextpad=.1,frameon=False)
cax = ax.inset_axes([1.05, 0.01, 0.06, 0.4], 
                    transform=ax.transAxes)
cbar = fig.colorbar(matrix_pubble, cax=cax,
                   ticks=[min(size), 75, 100, 125, 150])
cbar.ax.tick_params(left=True,direction="in",width=.5,labelsize=10)
cbar.ax.tick_params(which="minor",right=False)
cbar.outline.set_linewidth(.5)
plt.tight_layout()

fig.savefig('\第5章 多变量图形的绘制\图5-2-4 矩阵气泡图绘制示例_b.pdf',bbox_inches='tight')
fig.savefig('\第5章 多变量图形的绘制\图5-2-4 矩阵气泡图绘制示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()



