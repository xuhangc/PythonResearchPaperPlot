
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
from scipy import stats
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from colormaps import parula

from proplot import rc
rc["font.family"] = "Times New Roman"
rc["axes.labelsize"] = 15
rc["tick.labelsize"] = 12
rc["suptitle.size"] = 15
rc["title.size"] = 14

cor_line = pd.read_excel(r"\第5章 多变量图形的绘制\散点图样例数据2.xlsx",sheet_name="data02")
x = cor_line["values"]
y = cor_line["pred values"]
z = cor_line["3_value"]
xerr = cor_line["x_error"]
yerr = cor_line["y_error"]


slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
slope, intercept, r_value, p_value, std_err
r2 = round(r_value**2,2)
#绘制最佳拟合线
best_line_x = np.linspace(-10,10)
best_line_y=best_line_x
#绘制拟合线
y3 = slope*x + intercept
rmse = np.sqrt(mean_squared_error(x,y))

# a）未添加注释文本的多变量相关性散点图绘制示例
ticks=np.arange(0,max(z),20)

fig,ax = plt.subplots(figsize=(4.2,3.5),dpi=100,facecolor="w")
scatter = ax.scatter(x=x,y=y,c=z,s=50,ec="k",lw=.8,cmap = parula,vmin=min(z),vmax=max(z))
bestline = ax.plot(best_line_x,best_line_y,color='k',linewidth=1.5,linestyle='--',label="1:1 Line",zorder=-1)
linreg = ax.plot(x,y3,color='r',linewidth=1.5,linestyle='-',label="Fit Curve")
errorbar = ax.errorbar(x,y,xerr=xerr,yerr=yerr,ecolor="k", elinewidth=.4,capsize=0,alpha=.7,
            linestyle="",mfc="none",mec="none",zorder=-1)
ax.grid(False)
cbar = fig.colorbar(scatter,ticks=ticks,aspect=17)
cbar.set_label(label="Colorbar Label",fontsize=12)
cbar.ax.tick_params(left=True,direction="in",width=.4,labelsize=11)
cbar.ax.tick_params(which="minor",right=False)
cbar.ax.yaxis.set_ticklabels(ticklabels=ticks) 
cbar.outline.set_linewidth(.4)

ax.set(xlim=(-.1, 1.8),ylim=(-.1, 1.8),xlabel="X Axis Title",ylabel="T Axis Title",
       xticks=np.arange(0, 2, step=0.2),yticks=np.arange(0, 2, step=0.2))

ax.legend(loc="upper left")
fig.tight_layout()

fig.savefig('\第5章 多变量图形的绘制\图5-2-1 利用Matplotlib绘制的多变量相关性散点图（添加注释文本前后）示例_a.pdf',bbox_inches='tight')
fig.savefig('\第5章 多变量图形的绘制\图5-2-1 利用Matplotlib绘制的多变量相关性散点图（添加注释文本前后）示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# b）添加注释文本的多变量相关性散点图绘制示例
ticks=np.arange(0,max(z),20)

fig,ax = plt.subplots(figsize=(4.2,3.5),dpi=100,facecolor="w")
scatter = ax.scatter(x=x,y=y,c=z,s=50,ec="k",lw=.8,cmap = parula,vmin=min(z),vmax=max(z))
bestline = ax.plot(best_line_x,best_line_y,color='k',linewidth=1.5,linestyle='--',label="1:1 Line",zorder=-1)
linreg = ax.plot(x,y3,color='r',linewidth=1.5,linestyle='-',label="Fit Curve")
errorbar = ax.errorbar(x,y,xerr=xerr,yerr=yerr,ecolor="k", elinewidth=.4,capsize=0,alpha=.7,
            linestyle="",mfc="none",mec="none",zorder=-1)
ax.grid(False)
cbar = fig.colorbar(scatter,ticks=ticks,aspect=17)
cbar.set_label(label="Colorbar Label",fontsize=12)
cbar.ax.tick_params(left=True,direction="in",width=.4,labelsize=11)
cbar.ax.tick_params(which="minor",right=False)
cbar.ax.yaxis.set_ticklabels(ticklabels=ticks) 
cbar.outline.set_linewidth(.4)

# 添加文本信息
fontdict = {"size":12,"fontstyle":"italic","fontweight":"bold"}
ax.text(0.,1.6,r'$R^2=$'+str(round(r_value**2,2)),fontdict=fontdict)
ax.text(0.,1.4,"RMSE="+str(round(rmse,3)),fontdict=fontdict)
ax.text(0.,1.2,r'$y=$'+str(round(slope,3))+'$x$'+" + "+str(round(intercept,3)),fontdict=fontdict)
ax.text(0.,1.0,r'$N=$'+ str(len(x)),fontdict=fontdict)

ax.set(xlim=(-.1, 1.8),ylim=(-.1, 1.8),xlabel="X Axis Title",ylabel="T Axis Title",
       xticks=np.arange(0, 2, step=0.2),yticks=np.arange(0, 2, step=0.2))

#ax.legend(loc="lower right",frameon=False)
ax.legend(loc="lower right")
fig.tight_layout()

fig.savefig('\第5章 多变量图形的绘制\图5-2-1 利用Matplotlib绘制的多变量相关性散点图（添加注释文本前后）示例_b.pdf',bbox_inches='tight')
fig.savefig('\第5章 多变量图形的绘制\图5-2-1 利用Matplotlib绘制的多变量相关性散点图（添加注释文本前后）示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()

