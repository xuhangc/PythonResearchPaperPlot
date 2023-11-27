"""
编写时间：2022年4月15日 20：50

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

"""
此代码为使用Python-Prolot包进行学术风格图表绘制，绘图语法和Matplotlib有所不同，需注意。

"""
import mpltern
import pandas as pd
import numpy as np
import proplot as pplt
import seaborn as sns
import matplotlib.pyplot as plt
from colormaps import parula
from proplot import rc
rc["font.family"] = "Times New Roman"
rc["axes.labelsize"] = 15
rc["tick.labelsize"] = 12
rc["suptitle.size"] = 15
rc["title.size"] = 14

scatter_data = pd.read_excel(r"\第5章 多变量图形的绘制\ternary_scatter.xlsx")

t, l, r = scatter_data["Variable 1"],scatter_data["Variable 2"],scatter_data["Variable 3"]
cbar_values = scatter_data["Size"]

# a）三元相气泡图绘制示例一
fig = plt.figure(figsize=(4.5, 4),dpi=100,facecolor="w")
ax = fig.add_subplot(projection='ternary')
ax.tick_params(length=8)
ax.grid(color="k",linewidth=0.5)
scatter = ax.scatter(t, l, r,s=cbar_values*100,color="#459DFF",ec="k",lw=.6,zorder=7)

kw = dict(prop="sizes", num=5, color="#459DFF",mec="k",fmt="{x:.2f}",
          func=lambda s: s/100)
legend2 = ax.legend(*scatter.legend_elements(**kw),
                    loc="upper right", bbox_to_anchor=(1.1, 1.2),
                    title="Z Values",fontsize=13,handletextpad=.1,
                    title_fontsize=14,frameon=False)
ax.set_tlabel('Top')
ax.set_llabel('Left')
ax.set_rlabel('Right')
#ax.set_llabel("Variable 1",fontsize=15, fontweight="bold")
ax.text(-0.2,0.7,0.5,s="Variable 1",fontsize=16, fontweight="bold")
ax.text(0.2,0.4,-.1,s="Variable 2",fontsize=16, fontweight="bold",rotation="60")
ax.text(0.2,-.02,0.35,s="Variable 3",fontsize=16, fontweight="bold",rotation="-60")

plt.savefig(r'\第5章 多变量图形的绘制\图5-3-4 三元相气泡图绘制示例_a.pdf', bbox_inches='tight',)
plt.savefig(r'\第5章 多变量图形的绘制\图5-3-4 三元相气泡图绘制示例_a.png', 
            bbox_inches='tight',dpi=600)
plt.show()

# b）三元相气泡图绘制示例二

scatter_size = scatter_data["Size"].values
legend_size = np.linspace(min(scatter_size),max(scatter_size),5)*100

fig = plt.figure(figsize=(4.5, 4),dpi=100,facecolor="w")
ax = fig.add_subplot(projection='ternary')
ax.tick_params(length=8)
ax.grid(color="k",linewidth=0.5)
scatter = ax.scatter(t, l, r,s=cbar_values*100,color="#FFCC37",ec="k",lw=.6,zorder=7)
# 添加气泡图例
# 添加图例属性
for s in legend_size:
    #tax.scatter(point,color="#459DFF",ec="k",s=s,label=str(round(s,2)))
    ax.scatter([],[],[],color="#FFCC37",ec="k",lw=.6,s=s,label=str(round(s/100,2)))
ax.legend(loc="upper right", frameon=False,bbox_to_anchor=(1.1, 1.12),title="Z Values")
ax.set_tlabel('Top')
ax.set_llabel('Left')
ax.set_rlabel('Right')
ax.text(-0.2,0.7,0.5,s="Variable 1",fontsize=16, fontweight="bold")
ax.text(0.2,0.4,-.1,s="Variable 2",fontsize=16, fontweight="bold",rotation="60")
ax.text(0.2,-.02,0.35,s="Variable 3",fontsize=16, fontweight="bold",rotation="-60")

plt.savefig(r'\第5章 多变量图形的绘制\图5-3-4 三元相气泡图绘制示例_b.pdf', bbox_inches='tight',)
plt.savefig(r'\第5章 多变量图形的绘制\图5-3-4 三元相气泡图绘制示例_b.png', 
            bbox_inches='tight',dpi=600)
plt.show()
