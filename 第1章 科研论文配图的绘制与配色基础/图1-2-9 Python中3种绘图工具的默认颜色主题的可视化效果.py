"""
编写时间：2022年2月04日 22：00

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。

代码中Proplot包绘制的部分可能与Matplotlib绘制不同，需注意两者绘图语法的不同~~

"""

import numpy as np
import pandas as pd
import seaborn as sns
import proplot as pplt
import matplotlib.pyplot as plt

from proplot import rc
rc["font.family"] = "Times New Roman"
rc["axes.labelsize"] = 13
rc['tick.labelsize'] = 11
rc["suptitle.size"] = 15

tips = sns.load_dataset("tips")


# a）Matplotlib的默认颜色主题
matplotlib_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

fig,ax = plt.subplots(figsize=(3,3.2),dpi=100,facecolor="w")
ax = sns.violinplot(x="day", y="total_bill", data=tips,
                    palette=matplotlib_colors,
                    saturation=1)
for spine in ["top","right"]:
    ax.spines[spine].set_visible(False)
ax.grid(False)
ax.set_ylim(-10,60)
ax.set_xlabel("Class")
ax.set_ylabel("Value")
plt.tight_layout()
plt.savefig(r'r"\第1章 科研论文配图的绘制与配色基础\图1-2-9 Python中3种绘图工具的默认颜色主题的可视化效果_a.pdf',bbox_inches='tight')
plt.savefig(r'r"\第1章 科研论文配图的绘制与配色基础\图1-2-9 Python中3种绘图工具的默认颜色主题的可视化效果_a.png', 
             bbox_inches='tight',dpi=300)
plt.show()

# b)Seaborn的默认颜色主题
fig,ax = plt.subplots(figsize=(3,3.2),dpi=100,facecolor="w")
ax = sns.violinplot(x="day", y="total_bill", data=tips,saturation=1)
for spine in ["top","right"]:
    ax.spines[spine].set_visible(False)
ax.grid(False)
ax.set_ylim(-10,60)
ax.set_xlabel("Class")
ax.set_ylabel("Value")
plt.tight_layout() 
plt.savefig(r'r"\第1章 科研论文配图的绘制与配色基础\图1-2-9 Python中3种绘图工具的默认颜色主题的可视化效果_b.pdf',bbox_inches='tight')
plt.savefig(r'r"\第1章 科研论文配图的绘制与配色基础\图1-2-9 Python中3种绘图工具的默认颜色主题的可视化效果_b.png', 
             bbox_inches='tight',dpi=300)
plt.show()          

# c）SciencePlots的默认颜色主题（需安装Scienceplots包(pip install SciencePlots)，不同版本引用方式有所不同，请注意！）
with plt.style.context(['science']):
    from proplot import rc
    rc["xtick.minor.visible"] = False
    rc["ytick.minor.visible"] = False
    rc["xtick.major.pad"] =5
    fig,ax = plt.subplots(figsize=(3,3.2),dpi=100,facecolor="w")
    ax = sns.violinplot(x="day", y="total_bill", data=tips,saturation=1)
    for spine in ["top","right"]:
        ax.spines[spine].set_visible(False)
    ax.tick_params(top=False,right=False)
    ax.grid(False)
    ax.set_ylim(-10,60)
    ax.set_xlabel("Class")
    ax.set_ylabel("Value")
    plt.tight_layout()
    plt.savefig(r'r"\第1章 科研论文配图的绘制与配色基础\图1-2-9 Python中3种绘图工具的默认颜色主题的可视化效果_c.pdf',bbox_inches='tight')
    plt.savefig(r'r"\第1章 科研论文配图的绘制与配色基础\图1-2-9 Python中3种绘图工具的默认颜色主题的可视化效果_c.png', 
             bbox_inches='tight',dpi=300)
plt.show() 