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

group_data_point = pd.read_excel(r"\第4章 双变量图形的绘制\分组误差柱形图数据.xlsx")

# a）seaborn数据点误差柱形图（SD）
palette=['white','black']
palette_point=['white','white']
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
plot = sns.barplot(x="order",y="value",hue="class",data=group_data_point,palette=palette,ci="sd",
                 capsize=.1,errwidth=1,errcolor="k",ax=ax,saturation=1,
                 **{"edgecolor":"k","linewidth":1})
# 添加单独数据点
sns.stripplot(x="order",y="value",hue="class",data=group_data_point,dodge=True,palette=palette_point,
              edgecolor="black",linewidth=.75)
# 对图例操作
handles, labels = ax.get_legend_handles_labels()
l = plt.legend(handles[2:], labels[2:],loc="upper left",title="Class")
# 定制化设置
ax.tick_params(which='major',direction='in',length=3,width=1.,bottom=False)
for spine in ["top","left","right"]:
    ax.spines[spine].set_visible(False)
ax.spines['bottom'].set_linewidth(1.5)
plt.tight_layout()
fig.savefig('\第4章 双变量图形的绘制\图4-1-21 seaborn分组误差柱形图单独数据点绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-21 seaborn分组误差柱形图单独数据点绘制示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# b）seaborn数据点误差柱形图（CI）

palette=["#BC3C29FF","#0072B5FF"]
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
plot = sns.barplot(x="order",y="value",hue="class",data=group_data_point,palette=palette,ci=95,
                 capsize=.1,errwidth=1,errcolor="k",ax=ax,saturation=1,
                 **{"edgecolor":"k","linewidth":1})
# 添加单独数据点
sns.stripplot(x="order",y="value",hue="class",data=group_data_point,dodge=True,palette=palette,
              edgecolor="black",linewidth=.75)
# 对图例操作
handles, labels = ax.get_legend_handles_labels()
l = plt.legend(handles[2:], labels[2:],loc="upper left",title="Class")
# 定制化设置
ax.tick_params(which='major',direction='in',length=3,width=1.,labelsize=14,bottom=False)
for spine in ["top","left","right"]:
    ax.spines[spine].set_visible(False)
ax.spines['bottom'].set_linewidth(1.5)
plt.tight_layout()

fig.savefig('\第4章 双变量图形的绘制\图4-1-21 seaborn分组误差柱形图单独数据点绘制示例_b.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-21 seaborn分组误差柱形图单独数据点绘制示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()



