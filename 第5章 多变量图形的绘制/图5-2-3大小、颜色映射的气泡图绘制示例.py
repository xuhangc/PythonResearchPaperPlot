"""
编写时间：2022年4月15日 17：40

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

rc["font.family"] = "Times New Roman"
rc["axes.labelsize"] = 15
rc["tick.labelsize"] = 12
rc["suptitle.size"] = 15
rc["title.size"] = 14

pubble_data = pd.read_excel(r"\第5章 多变量图形的绘制\散点图样例数据2.xlsx",sheet_name="data03")

# a）气泡图数值大小映射绘制示例
x = pubble_data.x
y = pubble_data.y
values = pubble_data["values"]
values02 = pubble_data["values02"]

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
pubble = ax.scatter(x=x,y=y,s=values*20,color="#459DFF",ec="k",lw=.5,alpha=.8)
# 绘制图例
handles, labels = pubble.legend_elements(prop="sizes", alpha=0.6,
                                        num=5, color="gray",mec="k",fmt="{x:.0f}",
                                        func=lambda s: s/20)
legend = ax.legend(handles, labels, loc="upper right", title="Values", bbox_to_anchor=(1.25, 1.),
                   fontsize=11,title_fontsize=12,handletextpad=.1,frameon=False)
ax.set(xlim=(10, 40),ylim=(0, 45),
       xticks=np.arange(5, 50, step=5),yticks=np.arange(0, 50, step=5),
       xlabel="X Axis Title",ylabel="T Axis Title")
fig.tight_layout()
fig.savefig('\第5章 多变量图形的绘制\图5-2-3大小、颜色映射的气泡图绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第5章 多变量图形的绘制\图5-2-3大小、颜色映射的气泡图绘制示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# b）气泡图数值大小、颜色映射绘制示例
x = pubble_data.x
y = pubble_data.y
values = pubble_data["values"]
values02 = pubble_data["values02"]

fig,ax = plt.subplots(figsize=(4.2,3.5),dpi=100,facecolor="w")
pubble = ax.scatter(x=x,y=y,s=values*20,c=values02,ec="k",lw=.5,cmap = parula,vmin=min(values02),
                     vmax=max(values02))
#ax.grid(False)
#添加图例
kw = dict(prop="sizes", num=5, color="k",mec="k",fmt="{x:.0f}",
          func=lambda s: s/20)
legend = ax.legend(*pubble.legend_elements(**kw),
                    loc="upper right", bbox_to_anchor=(1.28, 1.),
                    title="Values",fontsize=10,title_fontsize=11,
                    handletextpad=.1,frameon=False)
cax = ax.inset_axes([1.1, 0.01, 0.08, 0.4], 
                    transform=ax.transAxes)
cbar = fig.colorbar(pubble, cax=cax)
cbar.ax.set_title("Values 02",fontsize=11,pad=5)
cbar.ax.tick_params(left=True,direction="in",width=.5,labelsize=10)
cbar.ax.tick_params(which="minor",right=False)
cbar.outline.set_linewidth(.5)

ax.set(xlim=(10, 40),ylim=(0, 45),
       xticks=np.arange(5, 50, step=5),yticks=np.arange(0, 50, step=5),
       xlabel="X Axis Title",ylabel="T Axis Title")

fig.tight_layout()
fig.savefig('\第5章 多变量图形的绘制\图5-2-3大小、颜色映射的气泡图绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第5章 多变量图形的绘制\图5-2-3大小、颜色映射的气泡图绘制示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()