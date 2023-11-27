"""
编写时间：2022年4月15日 22：30

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
cbar_values = scatter_data["Size"]
scatter_legend = scatter_data["Size02"]
t, l, r = scatter_data["Variable 1"],scatter_data["Variable 2"],scatter_data["Variable 3"]

# a）三元相散点图颜色映射绘制

fig = plt.figure(figsize=(4.5, 4),dpi=100,facecolor="w")
ax = fig.add_subplot(projection='ternary')
ax.tick_params(length=8)
ax.grid(color="k",linewidth=0.5)
pc = ax.scatter(t, l, r,s=100,c=cbar_values,ec="k",cmap=parula,lw=.7,
                zorder=3,vmin=min(cbar_values),vmax=max(cbar_values))
ax.set_tlabel('Top')
ax.set_llabel('Left')
ax.set_rlabel('Right')
#ax.set_llabel("Variable 1",fontsize=15, fontweight="bold")
ax.text(-0.2,0.7,0.5,s="Variable 1",fontsize=16, fontweight="bold")
ax.text(0.2,0.4,-.1,s="Variable 2",fontsize=16, fontweight="bold",rotation="60")
ax.text(0.2,-.02,0.35,s="Variable 3",fontsize=16, fontweight="bold",rotation="-60")
#ax.legend(fontsize=12,handletextpad=.1)
cax = ax.inset_axes([1.15, 0.1, 0.08, 0.8], 
                    transform=ax.transAxes)
colorbar = fig.colorbar(pc, cax=cax,)
colorbar.set_label('Colorbar_Values', rotation=270, va='baseline')
colorbar.ax.set_title("Z-Values",fontsize=14,pad=10)
colorbar.ax.tick_params(left=True,direction="in",width=.5,labelsize=12)
colorbar.outline.set_linewidth(.5)

plt.savefig(r'\第5章 多变量图形的绘制\图5-3-6 颜色、散点大小映射的三元相散点图绘制示例_a.pdf', bbox_inches='tight',)
plt.savefig(r'\第5章 多变量图形的绘制\图5-3-6 颜色、散点大小映射的三元相散点图绘制示例_a.png', 
            bbox_inches='tight',dpi=600)
plt.show()


# b）三元相散点图颜色、散点大小映射绘制

scatter_legend = scatter_data["Size"]
cbar_values = scatter_data["Size02"]

fig = plt.figure(figsize=(4.5, 4),dpi=100,facecolor="w")
ax = fig.add_subplot(projection='ternary')
ax.tick_params(length=8)
ax.grid(color="k",linewidth=0.5)
scatter = ax.scatter(t, l, r,s=scatter_legend*120,c=cbar_values,ec="k",cmap="jet",lw=.7,
                zorder=3,vmin=min(cbar_values),vmax=max(cbar_values))
ax.set_tlabel('Top')
ax.set_llabel('Left')
ax.set_rlabel('Right')

kw = dict(prop="sizes", num=5, color="k",mec="k",fmt="{x:.2f}",
          func=lambda s: s/120)
legend = ax.legend(*scatter.legend_elements(**kw),
                    loc="upper right", bbox_to_anchor=(1.35, 1.2),
                    title="Mark Size",fontsize=13,title_fontsize=14,
                    handletextpad=.1,frameon=False)
cax = ax.inset_axes([1.15, 0.1, 0.08, 0.5], 
                    transform=ax.transAxes)
colorbar = fig.colorbar(scatter, cax=cax)
colorbar.ax.set_title("Colorbar_values",fontsize=14,pad=10)
#colorbar.set_label('Cbar_values', rotation=270, va='baseline')
colorbar.ax.tick_params(left=True,direction="in",width=.5,labelsize=12)
colorbar.outline.set_linewidth(.5)

#ax.set_llabel("Variable 1",fontsize=15, fontweight="bold")
ax.text(-0.2,0.7,0.5,s="Variable 1",fontsize=16, fontweight="bold")
ax.text(0.2,0.4,-.1,s="Variable 2",fontsize=16, fontweight="bold",rotation="60")
ax.text(0.2,-.02,0.35,s="Variable 3",fontsize=16, fontweight="bold",rotation="-60")

plt.savefig(r'\第5章 多变量图形的绘制\图5-3-6 颜色、散点大小映射的三元相散点图绘制示例_b.pdf', bbox_inches='tight',)
plt.savefig(r'\第5章 多变量图形的绘制\图5-3-6 颜色、散点大小映射的三元相散点图绘制示例_b.png', 
            bbox_inches='tight',dpi=600)
plt.show()

