
"""
编写时间：2022年4月13日 21：50

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

"""
此代码为使用Python-Prolot包进行学术风格图表绘制，绘图语法和Matplotlib有所不同，需注意。
"""

import pandas as pd
import numpy as np
import ptitprince as pt # 需要单独安装
import seaborn as sns
from scipy import stats 
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["axes.linewidth"] = .8
plt.rcParams["axes.labelsize"] = 15
plt.rcParams["xtick.minor.visible"] = False
plt.rcParams["ytick.minor.visible"] = True
plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"
plt.rcParams["xtick.labelsize"] = 12
plt.rcParams["ytick.labelsize"] = 12
plt.rcParams["xtick.top"] = False
plt.rcParams["ytick.right"] = False


rain_data = sns.load_dataset("iris")
colors = ["#2FBE8F","#459DFF","#FF5B9B","#FFCC37","#751DFE"]


# a）PtitPrince云雨图基本样式一

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")

ax=pt.half_violinplot(x = "species", y ="sepal_width", data = rain_data, palette = colors[:3],
      bw=0.2, cut=2,scale = "area", width = 0.8, linewidth=1,inner="box",saturation=1)
ax.set_xlabel("Sepal")
ax.set_ylabel("Sepal\_width")

fig.savefig('\第4章 双变量图形的绘制\图4-1-35 不同样式云雨图绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-35 不同样式云雨图绘制示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()


# b）PtitPrince云雨图基本样式二

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
ax=pt.half_violinplot(x = "species", y ="sepal_width", data = rain_data, palette = colors[:3],
      bw=0.2, cut=2,scale = "area", width = 0.8, linewidth=1,inner="quartile",saturation=1)
ax.set_xlabel("Sepal")
ax.set_ylabel("Sepal\_width")
fig.savefig('\第4章 双变量图形的绘制\图4-1-35 不同样式云雨图绘制示例_b.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-35 不同样式云雨图绘制示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# c）PtitPrince云雨图基本样式三

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
ax=pt.half_violinplot(x = "species", y ="sepal_width", data = rain_data, palette = colors[:3],
      bw=0.2, cut=2,scale = "area", width = 0.8, linewidth=1,inner="box",saturation=1)

ax=sns.stripplot(x = "species", y ="sepal_width", data = rain_data, palette = colors[:3], 
                 edgecolor="k",linewidth=.4,size = 4, jitter = .08, zorder = 0,)
ax.set_xlabel("Sepal")
ax.set_ylabel("Sepal\_width")
fig.savefig('\第4章 双变量图形的绘制\图4-1-35 不同样式云雨图绘制示例_c.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-35 不同样式云雨图绘制示例_c.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# d）PtitPrince云雨图基本样式四
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
ax=pt.half_violinplot(x = "species", y ="sepal_width", data = rain_data, palette = colors[:3],
      bw=0.2, cut=2,scale = "area", width = 0.8, linewidth=1,inner=None,saturation=1)
ax=sns.stripplot(x = "species", y ="sepal_width", data = rain_data, palette = colors[:3], 
                 edgecolor="k",linewidth=.4,size = 4, jitter = .08, zorder = 5,)
ax=sns.boxplot(x = "species", y ="sepal_width", data = rain_data,width = .2,saturation = 1,
               boxprops = {'facecolor':'none', "zorder":2},
               medianprops={"color":"k","linewidth":1.5},showcaps=True,showfliers=False,zorder=0)
ax.set_xlabel("Sepal")
ax.set_ylabel("Sepal\_width")

fig.savefig('\第4章 双变量图形的绘制\图4-1-35 不同样式云雨图绘制示例_d.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-35 不同样式云雨图绘制示例_d.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# e）RainCloud()函数绘制的云雨图并排组合样式一
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
ax=pt.RainCloud(x = "species", y ="sepal_width", data = rain_data, palette = colors[:3],
                width_viol =.72,width_box=.2,move=.16,saturation = 1,linewidth=.5,box_showfliers=False,
                box_linewidth =1,point_size=4,ax=ax)
ax.set_xlabel("Sepal")
ax.set_ylabel("Sepal\_width")

fig.savefig('\第4章 双变量图形的绘制\图4-1-35 不同样式云雨图绘制示例_e.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-35 不同样式云雨图绘制示例_e.png', 
            bbox_inches='tight',dpi=300)
plt.show()

#  f）RainCloud()函数绘制的云雨图并排组合样式二

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
ax=pt.RainCloud(x = "species", y ="sepal_width", data = rain_data, palette = colors[:3],
                width_viol =.72,width_box=.2,move=.15,saturation = 1,linewidth=.5,box_showfliers=False,
                box_linewidth =1,point_size=4,pointplot = True,
                ax=ax)
ax.set_xlabel("Sepal")
ax.set_ylabel("Sepal\_width")

fig.savefig('\第4章 双变量图形的绘制\图4-1-35 不同样式云雨图绘制示例_f.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-35 不同样式云雨图绘制示例_f.png', 
            bbox_inches='tight',dpi=300)
plt.show()
