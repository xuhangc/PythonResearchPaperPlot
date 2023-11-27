"""
编写时间：2022年4月15日 16：50

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

"""
此代码为使用Python-Prolot包进行学术风格图表绘制，绘图语法和Matplotlib有所不同，需注意。

"""

import numpy as np
import pandas as pd
import seaborn as sns
import proplot as pplt
from scipy import stats
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from colormaps import parula

from proplot import rc
rc["font.family"] = "Times New Roman"
rc["axes.labelsize"] = 15
rc["tick.labelsize"] = 12
rc["suptitle.size"] = 15
rc["title.size"] = 14

cor_df_01 = pd.read_excel(r"\第5章 多变量图形的绘制\散点图样例数据2.xlsx",sheet_name="data03")

x = cor_df_01["x"]
y = cor_df_01["y"]
values = cor_df_01["values"]
xerr=cor_df_01["x_err"]
yerr=cor_df_01["y_err"]

slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
slope, intercept, r_value, p_value, std_err

#绘制最佳拟合线
best_line_x = np.linspace(-40,40)
best_line_y=best_line_x


#a）较少数据默认多变量相关性散点图绘制示例
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
scatter = ax.scatter(x=x,y=y,c=values,s=70,ec="k",lw=1,cmap = parula,vmin=min(values),vmax=max(values))
errorbar = ax.errorbar(x,y,xerr=xerr,yerr=yerr,ecolor="k", elinewidth=.4,capsize=0,alpha=.7,
            linestyle="",mfc="none",mec="none",zorder=-1)

bestline = ax.plot(best_line_x,best_line_y,color='k',linewidth=1.5,linestyle='--',label="1:1 Line")
# 添加colorbar
cbar = fig.colorbar(scatter,aspect=17)
cbar.set_label(label="Z Values",fontsize=12)
cbar.ax.tick_params(left=True,direction="in",width=.4,labelsize=11)
cbar.ax.tick_params(which="minor",right=False)
cbar.outline.set_linewidth(.4)

ax.grid(False)
ax.set(xlim=(0, 40),ylim=(0, 60),xlabel="X Axis Title",ylabel="T Axis Title")
ax.legend(loc="upper left")
fig.tight_layout()

fig.savefig('\第5章 多变量图形的绘制\图5-2-2 涉及较少数据时绘制的默认布局和调整之后的colorbar可视化布局_a.pdf',bbox_inches='tight')
fig.savefig('\第5章 多变量图形的绘制\图5-2-2 涉及较少数据时绘制的默认布局和调整之后的colorbar可视化布局_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# b）较少数据多变量相关性散点图图层调整绘制示例
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
scatter = ax.scatter(x=x,y=y,c=values,s=70,ec="k",lw=1,cmap = parula,vmin=min(values),vmax=max(values))
errorbar = ax.errorbar(x,y,xerr=xerr,yerr=yerr,ecolor="k", elinewidth=.4,capsize=0,alpha=.7,
            linestyle="",mfc="none",mec="none",zorder=-1)

bestline = ax.plot(best_line_x,best_line_y,color='k',linewidth=1.5,linestyle='--',label="1:1 Line")

# 添加调整位置colorbar
axins = inset_axes(ax,
                    width="7%",  
                    height="60%",
                    loc='upper left',
                    bbox_transform=ax.transAxes,
                    bbox_to_anchor=(0, 0., 1, 1),
                    borderpad=3)

cbar = fig.colorbar(scatter,cax=axins)
cbar.set_label(label="Colorbar Label",fontsize=12)
cbar.ax.tick_params(left=True,labelleft=True,labelright=False,direction="in",width=.4,labelsize=11)
cbar.ax.tick_params(which="minor",right=False)
cbar.ax.set_title("Z Values",fontsize=11)
cbar.outline.set_linewidth(.4)

ax.grid(False)
ax.set(xlim=(0, 40),ylim=(0, 60),xlabel="X Axis Title",ylabel="T Axis Title")
ax.legend()
fig.tight_layout()

fig.savefig('\第5章 多变量图形的绘制\图5-2-2 涉及较少数据时绘制的默认布局和调整之后的colorbar可视化布局_b.pdf',bbox_inches='tight')
fig.savefig('\第5章 多变量图形的绘制\图5-2-2 涉及较少数据时绘制的默认布局和调整之后的colorbar可视化布局_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()

