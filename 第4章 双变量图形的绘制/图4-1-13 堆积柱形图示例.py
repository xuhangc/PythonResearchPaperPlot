
"""
编写时间：2022年4月11日 11：30

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

# a）灰色系堆积柱形图绘制示例
labels = ['one', 'two', 'three', 'four', 'five']
type01 = np.array([10, 8, 5, 10, 2])
type02 = np.array([13, 10,7, 4, 10])
type03 = np.array([5, 7, 10,6, 8])
width = .7
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
bar_a = ax.bar(labels, type01, width,label='type01',color="#d0d0d0",ec='k')
bar_b = ax.bar(labels, type02, width,bottom= type01,label='type02',color="#a8a8a8",ec='k')
bar_c = ax.bar(labels, type03, width,bottom = type01+type02,label='type03',color="#808080",ec='k')
ax.tick_params(which='major',direction='in',length=3,width=1.,labelsize=13,bottom=False)

for spine in ["top","left","right"]:
    ax.spines[spine].set_visible(False)
ax.spines['bottom'].set_linewidth(1.5)
ax.set(xlabel="Name",ylabel="Values",xticklabels=labels,
       ylim=(0,30))
# 添加label
for c in ax.containers:
    ax.bar_label(c, label_type='center',size=12,fontweight="bold")
ax.legend(ncol=3,frameon=False)  
plt.tight_layout()

fig.savefig('\第4章 双变量图形的绘制\图4-1-13 堆积柱形图示例_a.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-13 堆积柱形图示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()


# b）NEJM色系堆积柱形图绘制示例

labels = ['one', 'two', 'three', 'four', 'five']
type01 = np.array([10, 8, 5, 10, 2])
type02 = np.array([13, 10,7, 4, 10])
type03 = np.array([5, 7, 10,6, 8])
width = .7

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
bar_a = ax.bar(labels, type01, width,label='type01',color="#BC3C29FF",ec='k')
bar_b = ax.bar(labels, type02, width,bottom= type01,label='type02',color="#0072B5FF",ec='k')
bar_c = ax.bar(labels, type03, width,bottom = type01+type02,label='type03',color="#E18727FF",ec='k')
ax.tick_params(which='major',direction='in',length=3,width=1.,bottom=False)

for spine in ["top","left","right"]:
    ax.spines[spine].set_visible(False)
ax.spines['bottom'].set_linewidth(1.5)
ax.set(xlabel="Name",ylabel="Values",xticklabels=labels,
       ylim=(0,30))
# 添加label
for c in ax.containers:
    ax.bar_label(c, label_type='center',size=12,fontweight="bold")
ax.legend(ncol=3,frameon=False)  
plt.tight_layout()

fig.savefig('\第4章 双变量图形的绘制\图4-1-13 堆积柱形图示例_b.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-13 堆积柱形图示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()


