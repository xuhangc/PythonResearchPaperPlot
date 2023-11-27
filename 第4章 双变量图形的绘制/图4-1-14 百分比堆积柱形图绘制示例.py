"""
编写时间：2022年4月11日 14：30

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

"""
此代码为使用Python-Prolot包进行学术风格图表绘制，绘图语法和Matplotlib有所不同，需注意。
"""

import pandas as pd
import numpy as np
import seaborn as sns
import proplot as pplt
import matplotlib.pyplot as plt

from proplot import rc
rc["font.family"] = "Times New Roman"
rc["axes.labelsize"] = 15
rc["tick.labelsize"] = 13
rc["suptitle.size"] = 15
rc["title.size"] = 14
rc["tick.minor"] = False


# a）百分比堆积柱形图绘制示例（灰色系）

from matplotlib import ticker

labels = ['one', 'two', 'three', 'four', 'five']
type01 = np.array([10, 8, 5, 10, 2])
type02 = np.array([13, 10,7, 4, 10])
type03 = np.array([5, 7, 10,6, 8])

all_data = [type01, type02, type03]
#将bottom_y元素都初始化为0
bottom_y = np.zeros(len(labels))
# 按列计算计算每组柱子的总和，计算百分
sums = np.sum(all_data, axis=0)

bar_color = ["#d0d0d0", "#a8a8a8","#808080"]
bar_label = ["type01","type02","type03"]
# 循环读取数据并进行可视化绘制
width = .6
fig,ax = plt.subplots(figsize=(5,4),dpi=100,facecolor="w")

for data,color,label in zip(all_data,bar_color,bar_label):
    y = data/sums
    ax.bar(labels,y,width,bottom=bottom_y,color=color,label=label,ec='k')
    bottom_y = y + bottom_y

ax.tick_params(which='major',direction='in',length=3,width=1.,bottom=False)
for spine in ["top","left","right"]:
    ax.spines[spine].set_visible(False)
ax.spines['bottom'].set_linewidth(2)

#设置刻度label
ax.set_xticklabels(labels)
ax.set_ylim(ymin = 0,ymax = 1.05)

# 设置百分比形式
ax.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1))
ax.legend(ncol=3,frameon=False,loc="upper center",
          bbox_to_anchor=(0.5, 1.08))      
# 添加label
for c in ax.containers:
    ax.bar_label(c, label_type='center',size=13,
                 labels=[str(round(i*100,1)) for i in c.datavalues],
                 color="k",fontweight="bold")

fig.savefig('\第4章 双变量图形的绘制\图4-1-14 百分比堆积柱形图绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-14 百分比堆积柱形图绘制示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# b）百分比堆积柱形图绘制示例（NEJM色系）

from matplotlib import ticker

labels = ['one', 'two', 'three', 'four', 'five']
type01 = np.array([10, 8, 5, 10, 2])
type02 = np.array([13, 10,7, 4, 10])
type03 = np.array([5, 7, 10,6, 8])

all_data = [type01, type02, type03]
#将bottom_y元素都初始化为0
bottom_y = np.zeros(len(labels))
# 按列计算计算每组柱子的总和，计算百分
sums = np.sum(all_data, axis=0)

bar_color = ["#BC3C29FF", "#0072B5FF","#E18727FF"]
bar_label = ["type01","type02","type03"]
# 循环读取数据并进行可视化绘制
width = .6
fig,ax = plt.subplots(figsize=(5,4),dpi=100,facecolor="w")

for data,color,label in zip(all_data,bar_color,bar_label):
    y = data/sums
    ax.bar(labels,y,width,bottom=bottom_y,color=color,label=label,ec='k')
    bottom_y = y + bottom_y

ax.tick_params(which='major',direction='in',length=3,width=1.,bottom=False)
for spine in ["top","left","right"]:
    ax.spines[spine].set_visible(False)
ax.spines['bottom'].set_linewidth(2)

#设置刻度label
ax.set_xticklabels(labels,size=12)
ax.set_ylim(ymin = 0,ymax = 1.05)

# 设置百分比形式
ax.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1))
ax.legend(ncol=3,frameon=False,loc="upper center",
          bbox_to_anchor=(0.5, 1.08))      
# 添加label
for c in ax.containers:
    ax.bar_label(c, label_type='center',size=13,
                 labels=[str(round(i*100,1)) for i in c.datavalues],
                 color="w",fontweight="bold")
                 
fig.savefig('\第4章 双变量图形的绘制\图4-1-14 百分比堆积柱形图绘制示例_b.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-14 百分比堆积柱形图绘制示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()