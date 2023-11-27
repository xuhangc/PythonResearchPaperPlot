
"""
编写时间：2022年4月11日 21：30

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


population_data = pd.read_excel(r"\第4章 双变量图形的绘制\人口金字塔图练习数据.xlsx")

label_list = [-20000000,-15000000,-10000000,-5000000,0,5000000,10000000,15000000,20000000]
tick_f = [str(int(i/1000000))+"m" for i in label_list]


fig,ax = plt.subplots(figsize=(5,4),dpi=100,facecolor="w")
group_col = 'Gender'
order_of_bars = population_data.Stage.unique()[::-1]
col_colors = ["black","gray"]

for color,group in zip(col_colors,population_data[group_col].unique()):
    sns.barplot(x='Users', y='Stage',data=population_data.loc[population_data[group_col]==group, :],
                order=order_of_bars, color=color, label=group,ax=ax)
# 定制化设置
ax.tick_params(which='major',direction='in',length=3,width=1.,labelsize=10,bottom=False)
for spine in ["top","left","right"]:
    ax.spines[spine].set_visible(False)
ax.grid(axis='y',ls='-',c='gray')
ax.set(xlabel="Users",ylabel="Stage",xticklabels=tick_f)
# 添加注释文本
ax.text(x=.8,y=-.1,s="(m = millions)",transform=ax.transAxes,size=12,style="italic")
#print(ax.get_xticks())
ax.legend()
plt.tight_layout()

fig.savefig('\第4章 双变量图形的绘制\图4-1-22 利用seaborn绘制的人口“金字塔”图示例.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-22 利用seaborn绘制的人口“金字塔”图示例.png', 
            bbox_inches='tight',dpi=300)
plt.show()