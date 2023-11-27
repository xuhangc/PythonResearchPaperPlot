
"""
编写时间：2022年5月11日 19：50

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。

代码中Proplot包绘制的部分可能与Matplotlib绘制不同，需注意两者绘图语法的不同~~

"""
#注意：本案例中引入的SciencePlots库主题方式会随着SciencePlots版本的更新发生改变，读者还需参考其官网引入的正确方式。

import random,string
import numpy as np
import pandas as pd
import seaborn as sns
import proplot as pplt
from scipy import stats
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid
from sklearn.metrics import mean_squared_error

from proplot import rc
rc["font.family"] = "Times New Roman"
rc["axes.labelsize"] = 14
rc["tick.labelsize"] = 11
rc["suptitle.size"] = 15
rc["title.size"] = 14
rc["font.weight"] = "bold"
rc["axes.labelweight"] = "bold"
rc["axes.titleweight"] = "bold"
rc["tick.minor"] = False
rc['figure.constrained_layout.use'] = True #调整子图显示不全等问题

multiple_data = pd.read_excel(r"第8章 学术图绘制案例\multiple_data.xlsx")

fig = plt.figure(figsize=(6, 6.2))

models = ["LR","SVR","GBRT","DNN"] * 4
names = ["cropland","forest","grassland","savanna"] 
names_4 = [item for s in names for item in [s]*4]
makers = ['v','s','o','X'] * 4
label_list = ["("+i+")" for i in list(string.ascii_lowercase)[:16]]
rmse = np.sqrt(mean_squared_error(x,y))

grid = ImageGrid(fig, 111,  # similar to subplot(111)
                 nrows_ncols=(4, 4),  # creates 2x2 grid of axes
                 axes_pad=0.15,  # pad between axes in inch.
                 cbar_mode="single",
                 cbar_location="right")
for ax, row in zip(grid.axes_column[0], names):
    ax.set_ylabel(row, rotation=90, size=10)
cols = ["LR","SVR","GBRT","DNN"]
for ax, col in zip(grid.axes_row[0], cols,):
    ax.set_title(col,size=10)

for model,name,marker,ax,label in zip(models,names_4,makers,grid,label_list):
    x = multiple_data[name+model+"_0"].dropna()
    y = multiple_data[name+model+"_1"].dropna()
    # 计算所需指标
    slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
    rmse = np.sqrt(mean_squared_error(x,y))
    #绘制最佳拟合线
    best_line_x = np.linspace(-10,90)
    best_line_y=best_line_x
    # 绘制散点
    #scatter = ax.scatter(x,y,s=3,marker=marker,color="k",alpha=.2,label=model)
    hist2d = ax.hist2d(x=x,y=y,bins=50,cmap=parula,cmin=.0001)
    bestline = ax.plot(best_line_x,best_line_y,color='k',linewidth=.8,alpha=.8,
                       linestyle='-',zorder=-1)
    regline = ax.plot(x, intercept + slope*x, 'r',linewidth=.8)
    ax.grid(False)
    # 添加文本信息
    ax.text(-5.,78,r'$y=$'+str(round(slope,3))+'$x$'+" + "+str(round(intercept,3)),fontsize=8)
    ax.text(-5, 68,r'$R^2=$'+str(round(r_value**2,2)),fontsize=8)
    ax.text(-5, 58,"RMSE="+str(round(rmse,2)),fontsize=8)
    ax.text(0.8, 0.15, label, transform=ax.transAxes,fontsize=10, fontweight='bold', va='top')
    ax.set(xlim=(-10, 90),ylim=(-10, 90),xticks=np.arange(-10, 100, step=20),
           yticks=np.arange(-10, 100, step=20))

    
fig.supxlabel('True Values',y=0.05,fontsize=15,fontweight="normal")
fig.supylabel('Estemate Values',x=.01,fontsize=15,fontweight="normal")

cbar = fig.colorbar(hist2d[3], cax=grid.cbar_axes[0], orientation='vertical')
cbar.set_label(label="Number Of Point",fontsize=11)
cbar.ax.tick_params(left=True,labelright=True,direction="in",width=.4,labelsize=10)
cbar.ax.tick_params(which="minor",right=False)
cbar.ax.set_title("Counts",fontsize=11)
cbar.outline.set_linewidth(.4)

fig.savefig('第8章 学术图绘制案例\图8-2-2 多子图相关性散点图添加colorbar绘制示例（位置属性为right).pdf',bbox_inches='tight')
fig.savefig('第8章 学术图绘制案例\图8-2-2 多子图相关性散点图添加colorbar绘制示例（位置属性为right).png', 
            bbox_inches='tight',dpi=300)
plt.show()

#**********************图8-2-3 多子图相关性散点图添加colorbar绘制示例（位置属性为top）*************

from mpl_toolkits.axes_grid1 import ImageGrid

fig = plt.figure(figsize=(6, 6))

models = ["LR","SVR","GBRT","DNN"] * 4
names = ["cropland","forest","grassland","savanna"] 
names_4 = [item for s in names for item in [s]*4]
makers = ['v','s','o','X'] * 4
label_list = ["("+i+")" for i in list(string.ascii_lowercase)[:16]]
rmse = np.sqrt(mean_squared_error(x,y))

grid = ImageGrid(fig, 111,  # similar to subplot(111)
                 nrows_ncols=(4, 4),  # creates 2x2 grid of axes
                 axes_pad=0.15,  # pad between axes in inch.
                 cbar_mode="single",
                 cbar_location="top")
for ax, row in zip(grid.axes_column[0], names):
    ax.set_ylabel(row, rotation=90, size=10)
cols = ["LR","SVR","GBRT","DNN"]
for ax, col in zip(grid.axes_row[-1], cols,):
    ax.set_xlabel(col,size=10)

for model,name,marker,ax,label in zip(models,names_4,makers,grid,label_list):
    x = multiple_data[name+model+"_0"].dropna()
    y = multiple_data[name+model+"_1"].dropna()
    # 计算所需指标
    slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
    rmse = np.sqrt(mean_squared_error(x,y))
    #绘制最佳拟合线
    best_line_x = np.linspace(-10,90)
    best_line_y=best_line_x
    # 绘制散点
    #scatter = ax.scatter(x,y,s=3,marker=marker,color="k",alpha=.2,label=model)
    hist2d = ax.hist2d(x=x,y=y,bins=50,cmap=parula,cmin=.0001)
    bestline = ax.plot(best_line_x,best_line_y,color='k',linewidth=.8,alpha=.8,
                       linestyle='-',zorder=-1)
    regline = ax.plot(x, intercept + slope*x, 'r',linewidth=.8)
    ax.grid(False)
    # 添加文本信息
    ax.text(-5.,78,r'$y=$'+str(round(slope,3))+'$x$'+" + "+str(round(intercept,3)),fontsize=8)
    ax.text(-5, 68,r'$R^2=$'+str(round(r_value**2,2)),fontsize=8)
    ax.text(-5, 58,"RMSE="+str(round(rmse,2)),fontsize=8)
    ax.text(0.8, 0.15, label, transform=ax.transAxes,fontsize=10, fontweight='bold', va='top')
    ax.set(xlim=(-10, 90),ylim=(-10, 90),xticks=np.arange(-10, 100, step=20),
           yticks=np.arange(-10, 100, step=20))

    
fig.supxlabel('True Values',y=0.01,fontsize=15,fontweight="normal")
fig.supylabel('Estemate Values',x=.01,fontsize=15,fontweight="normal")

cbar = fig.colorbar(hist2d[3], cax=grid.cbar_axes[0], orientation='horizontal')
cbar.ax.tick_params(left=True,labelright=True,direction="in",width=.4,labelsize=10)
cbar.ax.tick_params(which="minor",direction="in",right=False)
cbar.ax.set_title("Number Of Point",fontsize=11)
cbar.ax.xaxis.set_ticks_position('top')
cbar.outline.set_linewidth(.4)
fig.savefig('第8章 学术图绘制案例\图8-2-3 多子图相关性散点图添加colorbar绘制示例（位置属性为top）.pdf',bbox_inches='tight')
fig.savefig('第8章 学术图绘制案例\图8-2-3 多子图相关性散点图添加colorbar绘制示例（位置属性为top）.png', 
            bbox_inches='tight',dpi=300)
plt.show()

