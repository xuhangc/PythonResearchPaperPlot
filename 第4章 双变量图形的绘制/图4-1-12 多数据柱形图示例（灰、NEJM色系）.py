
"""
编写时间：2022年4月11日 10：30

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

# 构建数据
labels = ['one', 'two', 'three', 'four', 'five']
type01 = [10, 8, 5, 10, 2]
type02 = [13, 10,7, 4, 10]
type03 = [5, 7, 10,6, 8]

# a）多数据柱形图示例（灰色系）
#设置x刻度位置
x = np.arange(len(labels))
width = .25
#plots
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
bar_a = ax.bar(x-width/2, type01,width,label='type01',color="#808080",ec='k')
bar_b = ax.bar(x+width/2, type02, width,label='type02',color="#484848",ec='k')
bar_c = ax.bar(x+width*3/2, type03,width,label='type03',color="#181818",ec='k')
ax.tick_params(which='major',direction='in',length=3,width=1,bottom=False)
for spine in ["top","left","right"]:
    ax.spines[spine].set_visible(False)
ax.spines['bottom'].set_linewidth(1.5)

ax.set(xlabel="Name",ylabel="Values",xticklabels=labels,
       yticks=np.arange(0, 15, step=2),xticks=x+.1,ylim=(0,14))
ax.legend(ncol=3,frameon=False)    
plt.tight_layout()

fig.savefig('\第4章 双变量图形的绘制\图4-1-12 多数据柱形图示例（灰、NEJM色系）_a.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-12 多数据柱形图示例（灰、NEJM色系）_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# b）多数据柱形图示例（NEJM色系）

#设置x刻度位置
x = np.arange(len(labels))
width = .25
#plots
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
bar_a = ax.bar(x-width/2, type01,width,label='type01',color="#BC3C29FF",ec='k')
bar_b = ax.bar(x+width/2, type02, width,label='type02',color="#0072B5FF",ec='k')
bar_c = ax.bar(x+width*3/2, type03,width,label='type03',color="#E18727FF",ec='k')
ax.tick_params(which='major',direction='in',length=3,width=1,bottom=False)
for spine in ["top","left","right"]:
    ax.spines[spine].set_visible(False)
ax.spines['bottom'].set_linewidth(1.5)

ax.set(xlabel="Name",ylabel="Values",xticklabels=labels,
       yticks=np.arange(0, 15, step=2),xticks=x+.1,ylim=(0,14))
ax.legend(ncol=3,frameon=False)    
plt.tight_layout()
fig.savefig('\第4章 双变量图形的绘制\图4-1-12 多数据柱形图示例（灰、NEJM色系）_b.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-12 多数据柱形图示例（灰、NEJM色系）_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()


