
"""
编写时间：2022年4月11日 19：30

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

group_data = pd.read_excel(r"\第4章 双变量图形的绘制\分组误差柱形图数据.xlsx")


# a）分组标准差误差柱形图

palette=['#0073C2FF','#EFC000FF']

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
ax = sns.barplot(x="order",y="value",hue="class",data=group_data,palette=palette,ci="sd",
                 capsize=.1,errwidth=1,errcolor="k",saturation=1,ax=ax,
                 **{"edgecolor":"k","linewidth":1})

ax.tick_params(which='major',direction='in',length=3,width=1.,bottom=False)
for spine in ["top","left","right"]:
    ax.spines[spine].set_visible(False)
ax.spines['bottom'].set_linewidth(1.5)
# 设置图例
ax.legend(title="Class")
plt.tight_layout()
fig.savefig('\第4章 双变量图形的绘制\图4-1-19 分组标准差、分组置信区间误差柱形图绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-19 分组标准差、分组置信区间误差柱形图绘制示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# b）分组置信区间误差柱形图

palette=['#0073C2FF','#EFC000FF']

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
ax = sns.barplot(x="order",y="value",hue="class",data=group_data,palette=palette,ci=95,
                 capsize=.1,errwidth=1,errcolor="k",saturation=1,ax=ax,
                 **{"edgecolor":"k","linewidth":1})

ax.tick_params(which='major',direction='in',length=3,width=1,bottom=False)
for spine in ["top","left","right"]:
    ax.spines[spine].set_visible(False)
ax.spines['bottom'].set_linewidth(1.5)
# 设置图例
ax.legend(title="Class")
plt.tight_layout()
fig.savefig('\第4章 双变量图形的绘制\图4-1-19 分组标准差、分组置信区间误差柱形图绘制示例_b.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-19 分组标准差、分组置信区间误差柱形图绘制示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()

