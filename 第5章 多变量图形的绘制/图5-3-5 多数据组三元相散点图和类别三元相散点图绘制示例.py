"""
编写时间：2022年4月15日 21：50

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

"""
此代码为使用Python-Prolot包进行学术风格图表绘制，绘图语法和Matplotlib有所不同，需注意。

"""
import mpltern
import pandas as pd
import numpy as np
import proplot as pplt
import seaborn as sns
import matplotlib.pyplot as plt
from colormaps import parula
from proplot import rc
rc["font.family"] = "Times New Roman"
rc["axes.labelsize"] = 15
rc["tick.labelsize"] = 12
rc["suptitle.size"] = 15
rc["title.size"] = 14



# a）多数据组三元相散点图示例

combine_data = pd.read_excel(r"\第5章 多变量图形的绘制\ternary_scatter.xlsx",sheet_name="data02")
l = combine_data["Variable 1"].values
t = combine_data["Variable 2"].values
r = combine_data["Variable 3"].values
l1 = combine_data["Variable 1-1"].values
t1 = combine_data["Variable 2-1"].values
r1 = combine_data["Variable 3-1"].values

fig = plt.figure(figsize=(4.5, 4),dpi=100,facecolor="w")
ax = fig.add_subplot(projection='ternary')
ax.tick_params(length=8)
ax.grid(color="k",linewidth=0.5)
scatter01 = ax.scatter(t, l, r,s=120,c="#459DFF",ec="k",lw=.6,zorder=3,label="Test 01")
scatter02 = ax.scatter(t1, l1, r1,s=120,c="#FF5B9B",marker="^",ec="k",lw=.6,zorder=3,label="Test 02")
ax.set_tlabel('Top')
ax.set_llabel('Left')
ax.set_rlabel('Right')
# 添加label
ax.text(-0.2,0.7,0.5,s="Variable 1",fontsize=16, fontweight="bold")
ax.text(0.2,0.4,-.1,s="Variable 2",fontsize=16, fontweight="bold",rotation="60")
ax.text(0.2,-.02,0.35,s="Variable 3",fontsize=16, fontweight="bold",rotation="-60")
ax.legend(loc="upper right", bbox_to_anchor=(1.1, 1.2),
                    title="Type",fontsize=13,handletextpad=.1,
                    title_fontsize=14,frameon=False)

plt.savefig(r'\第5章 多变量图形的绘制\图5-3-5 多数据组三元相散点图和类别三元相散点图绘制示例_a.pdf', bbox_inches='tight',)
plt.savefig(r'\第5章 多变量图形的绘制\图5-3-5 多数据组三元相散点图和类别三元相散点图绘制示例_a.png', 
            bbox_inches='tight',dpi=600)
plt.show()

# b）类别三元相散点图示例

scatter_data = pd.read_excel(r"\第5章 多变量图形的绘制\ternary_scatter.xlsx")

t, l, r = scatter_data["Variable 1"],scatter_data["Variable 2"],scatter_data["Variable 3"]
cbar_values = scatter_data["Size"]

colors = ["#2FBE8F","#459DFF","#FF5B9B","#FFCC37","#751DFE"]

def scatter_color(value):
    if 0<=value<=0.2:
        color = "#2FBE8F"
    elif 0.2<=value<=0.4:
        color = "#459DFF"
    elif 0.4<=value<=0.6:
        color = "#FF5B9B"
    elif 0.6<=value<=0.8:
        color = "#FFCC37"
    else:
        color = "#751DFE"
    return color

scatter_data["data_color"] = scatter_data["Size"].map(lambda x :scatter_color(x))


data_color = scatter_data["data_color"].values
legend_colors = ["#2FBE8F","#459DFF","#FF5B9B","#FFCC37","#751DFE"]
legend_text = ["0.0~0.2","0.2~0.4","0.4~0.6","0.6~0.8","0.8~1.0"]
fig = plt.figure(figsize=(4.5, 4),dpi=100,facecolor="w")
ax = fig.add_subplot(projection='ternary')
ax.tick_params(length=8)
ax.grid(color="k",linewidth=0.5)
ax.scatter(t, l, r,s=80,color=data_color,ec="k",lw=.6,zorder=2)
ax.set_tlabel('Top')
ax.set_llabel('Left')
ax.set_rlabel('Right')
# 添加label
ax.text(-0.2,0.7,0.5,s="Variable 1",fontsize=16, fontweight="bold")
ax.text(0.2,0.4,-.1,s="Variable 2",fontsize=16, fontweight="bold",rotation="60")
ax.text(0.2,-.02,0.35,s="Variable 3",fontsize=16, fontweight="bold",rotation="-60")
#单独添加legend
for color,text in zip(legend_colors,legend_text):
    ax.scatter([],[],[],color=color,ec="k",lw=.8,s=80,label=text)
ax.legend(loc="upper right", frameon=False,bbox_to_anchor=(1.15, 1.25),title="Size Value",
          handletextpad=.1,title_fontsize=14,fontsize=13)

plt.savefig(r'\第5章 多变量图形的绘制\图5-3-5 多数据组三元相散点图和类别三元相散点图绘制示例_b.pdf', bbox_inches='tight',)
plt.savefig(r'\第5章 多变量图形的绘制\图5-3-5 多数据组三元相散点图和类别三元相散点图绘制示例_b.png', 
            bbox_inches='tight',dpi=600)
plt.show()