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
models = ["LR","SVR","GBRT","DNN"] * 4
names = ["cropland","forest","grassland","savanna"] 
names_4 = [item for s in names for item in [s]*4]
makers = ['v','s','o','X'] * 4
label_list = ["("+i+")" for i in list(string.ascii_lowercase)[:16]]

rmse = np.sqrt(mean_squared_error(x,y))
fig,axs = plt.subplots(4,4,figsize=(6,6),dpi=100,sharex=True, sharey=True,
                       facecolor="w",constrained_layout=True)
for ax, row in zip(axs[:,0], names):
    ax.set_ylabel(row, rotation=90, size=10)

#for ax, (label, (x, y)) in zip(axs.flat, datasets.items())
for model,name,marker,ax,label in zip(models,names_4,makers,axs.flat,label_list):
        x = multiple_data[name+model+"_0"].dropna()
        y = multiple_data[name+model+"_1"].dropna()
        # 计算所需指标
        slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
        rmse = np.sqrt(mean_squared_error(x,y))
        #绘制最佳拟合线
        best_line_x = np.linspace(-10,90)
        best_line_y=best_line_x
        # 绘制散点
        scatter = ax.scatter(x,y,s=3,marker=marker,color="k",alpha=.2,label=model)
        bestline = ax.plot(best_line_x,best_line_y,color='k',linewidth=.6,alpha=.8,
                           linestyle='-',zorder=-1)
        regline = ax.plot(x, intercept + slope*x, 'r',linewidth=.8)
        ax.grid(False)
        # 添加文本信息
        ax.text(-5.,78,r'$y=$'+str(round(slope,3))+'$x$'+" + "+str(round(intercept,3)),fontsize=8)
        ax.text(-5, 68,r'$R^2=$'+str(round(r_value**2,2)),fontsize=8)
        ax.text(-5, 58,"RMSE="+str(round(rmse,2)),fontsize=8)
        ax.text(0.85, 0.95, label, transform=ax.transAxes,fontsize=10, fontweight='bold', va='top')
        ax.set(xlim=(-10, 90),ylim=(-10, 90),xticks=np.arange(-10, 100, step=20),
               yticks=np.arange(-10, 100, step=20))
        ax.legend(loc="lower right",markerscale=1.5,frameon=False,handletextpad=-.1)
fig.supxlabel('True Values',fontsize=15,fontweight="normal")
fig.supylabel('Estemate Values',fontsize=15,fontweight="normal")
fig.savefig('第8章 学术图绘制案例\图8-2-1 多子图相关性散点图绘制示例.pdf',bbox_inches='tight')
fig.savefig('第8章 学术图绘制案例\图8-2-1 多子图相关性散点图绘制示例.png', 
            bbox_inches='tight',dpi=300)
plt.show()



