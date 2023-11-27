
"""
编写时间：2022年4月11日 09：50

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


# a）单数据柱形图绘制示例（升序）

name = ["A","B","C","D","E"]
value = [3,13,6,18,45]
bar_01 = pd.DataFrame(data={"name":name,"value":value})
# 对数据进行排序
bar_01 = bar_01.sort_values(['value'], ascending=True)
#构建图例
grey_color_palette = ["#d0d0d0","#a8a8a8","#808080","#484848","#181818"]
legend_label = [i for i in bar_01.name]
legend_dict = dict(zip(legend_label,grey_color_palette))

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
bar01 = ax.bar(bar_01.name,bar_01.value,color=grey_color_palette,ec='k',width=.7)
ax.bar_label(bar01,labels=bar_01.value,size=12,fontweight="bold")
ax.tick_params(which='major',direction='in',length=3,width=1.,labelsize=12,bottom=False)

for spine in ["top","left","right"]:
    ax.spines[spine].set_visible(False)
ax.spines['bottom'].set_linewidth(1.5)
ax.set(xlabel="Name",ylabel="Values",ylim=(0,50))
#单独添加图例
handles = [plt.Rectangle((0.5,.5),1,1, color=legend_dict[label],ec="k") \
           for label in legend_label]
ax.legend(handles, legend_label,handlelength=1.2,handleheight=1.2)
plt.tight_layout()

fig.savefig('\第4章 双变量图形的绘制\图4-1-11 单数据 系列柱形图示例（升降序样式）_a.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-11 单数据 系列柱形图示例（升降序样式）_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# b）单数据柱形图绘制示例（降序）
name = ["A","B","C","D","E"]
value = [3,13,6,18,45]
bar_01 = pd.DataFrame(data={"name":name,"value":value})
bar_01 = bar_01.sort_values(['value'], ascending=False)
#构建图例
grey_color_palette = ["#d0d0d0","#a8a8a8","#808080","#484848","#181818"]
grey_color_palette = grey_color_palette[::-1]
legend_label = [i for i in bar_01.name]
legend_dict = dict(zip(legend_label,grey_color_palette))

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
bar01 = ax.bar(bar_01.name,bar_01.value,color=grey_color_palette,ec='k',width=.7)
ax.bar_label(bar01,labels=bar_01.value,size=12,fontweight="bold")
ax.tick_params(which='major',direction='in',length=3,width=1.,labelsize=12,bottom=False)

for spine in ["top","left","right"]:
    ax.spines[spine].set_visible(False)
ax.spines['bottom'].set_linewidth(1.5)
ax.set(xlabel="Name",ylabel="Values",ylim=(0,50))
#单独添加图例
handles = [plt.Rectangle((0.5,.5),1,1, color=legend_dict[label],ec="k") \
           for label in legend_label]
ax.legend(handles, legend_label,handlelength=1.2,handleheight=1.2)
plt.tight_layout()
fig.savefig('\第4章 双变量图形的绘制\图4-1-11 单数据 系列柱形图示例（升降序样式）_b.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-11 单数据 系列柱形图示例（升降序样式）_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()
