"""
编写时间：2022年4月14日 09：50

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

"""
此代码为使用Python-Prolot包进行学术风格图表绘制，绘图语法和Matplotlib有所不同，需注意。
"""

import pandas as pd
import numpy as np
import seaborn as sns
import proplot as pplt
from scipy import stats 
import matplotlib.pyplot as plt

from proplot import rc
rc["font.family"] = "Times New Roman"
rc["axes.labelsize"] = 15
rc["tick.labelsize"] = 12
rc["suptitle.size"] = 15
rc["title.size"] = 14


data = [18, 2, 25, 10,5,40]
labels = ['A','B','C','D',"E",'F']
recipe = ["{:.1%}".format(i/100) for i in data]
colors = plt.cm.gray(np.linspace(0.2,1,len(labels)))

fig,ax = plt.subplots(figsize=(5,3.5),dpi=100,facecolor="w")
wedges, texts = ax.pie(data, startangle=-40,colors=colors,
                       wedgeprops=dict(width=0.5,linewidth=.8, 
                                       edgecolor="k"))

bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.5)
kw = dict(arrowprops=dict(arrowstyle="-"),
          bbox=bbox_props, zorder=0, va="center")
for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1)/2. + p.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    connectionstyle = "angle,angleA=0,angleB={}".format(ang)
    kw["arrowprops"].update({"connectionstyle": connectionstyle})
    ax.annotate(recipe[i], xy=(x, y), xytext=(1.5*np.sign(x), 1.5*y),
                horizontalalignment=horizontalalignment, **kw)
ax.legend(labels,ncol=3,loc ='lower right',fontsize=9,
          bbox_to_anchor=(.7, -.1, 0.5, 1))
plt.tight_layout()

fig.savefig('\第4章 双变量图形的绘制\图4-1-38 利用  Matplotlib绘制环形图时添加引线式文本信息示.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-38 利用  Matplotlib绘制环形图时添加引线式文本信息示.png', 
            bbox_inches='tight',dpi=300)
plt.show()