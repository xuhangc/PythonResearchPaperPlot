"""
编写时间：2022年2月04日 22：40

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。

代码中Proplot包绘制的部分可能与Matplotlib绘制不同，需注意两者绘图语法的不同~~

"""

import numpy as np
import pandas as pd
import seaborn as sns
import proplot as pplt
import matplotlib.pyplot as plt
from matplotlib import cm
from colorspacious import cspace_converter

from proplot import rc
rc["font.family"] = "Times New Roman"
rc["axes.labelsize"] = 13
rc['tick.labelsize'] = 11
rc["suptitle.size"] = 15


tips = sns.load_dataset("tips")

#使用Scienceplots包绘图主题绘制（需安装Scienceplots包(pip install SciencePlots)，不同版本引用方式有所不同，请注意！）

# a）单色系可视化绘制示例
with plt.style.context(['science']):
    from proplot import rc
    rc["xtick.minor.visible"] = False
    rc["ytick.minor.visible"] = False
    rc["xtick.major.pad"] =5
    
    fig,ax = plt.subplots(figsize=(3,3.2),dpi=100,facecolor="w")
    scatter = ax.scatter(x="total_bill",y="tip",c="tip",data=tips,ec="k",
               cmap="YlGnBu")
    for spine in ["top","right"]:
        ax.spines[spine].set_visible(False)
    ax.tick_params(top=False,right=False)
    cax = ax.inset_axes([0.1, .85, 0.6, 0.05], transform=ax.transAxes)
    colorbar = fig.colorbar(scatter, ax=scatter, cax=cax,
                            orientation="horizontal")

    colorbar.ax.tick_params(bottom=True,direction="in",labelsize=8,pad=3)
    colorbar.ax.xaxis.set_ticks_position('top')
    colorbar.outline.set_linewidth(.4)
    ax.grid(False)
    ax.set_ylim(0,12)
    ax.set_xlabel("X Label")
    ax.set_ylabel("Y Label")
    plt.tight_layout()
    plt.savefig(r'r"\第1章 科研论文配图的绘制与配色基础\图1-2-14 使用seaborn库中Tips数据集绘制的单色系、双色渐变色系和多色系可视化配图示例_a.pdf',bbox_inches='tight')
    plt.savefig(r'r"\第1章 科研论文配图的绘制与配色基础\图1-2-14 使用seaborn库中Tips数据集绘制的单色系、双色渐变色系和多色系可视化配图示例_a.png', 
             bbox_inches='tight',dpi=300)
plt.show()

# b）双色渐变色系可视化绘制示例 

with plt.style.context(['science']):
    from proplot import rc
    rc["xtick.minor.visible"] = False
    rc["ytick.minor.visible"] = False
    rc["xtick.major.pad"] =5
    
    fig,ax = plt.subplots(figsize=(3,3.2),dpi=100,facecolor="w")
    scatter = ax.scatter(x="total_bill",y="tip",c="tip",data=tips,ec="k",
               cmap="seismic")
    for spine in ["top","right"]:
        ax.spines[spine].set_visible(False)
    ax.tick_params(top=False,right=False)
    cax = ax.inset_axes([0.1, .85, 0.6, 0.05], transform=ax.transAxes)
    colorbar = fig.colorbar(scatter, ax=scatter, cax=cax,
                            orientation="horizontal")

    colorbar.ax.tick_params(bottom=True,direction="in",labelsize=8,pad=3)
    colorbar.ax.xaxis.set_ticks_position('top')
    colorbar.outline.set_linewidth(.4)
    ax.grid(False)
    ax.set_ylim(0,12)
    ax.set_xlabel("X Label")
    ax.set_ylabel("Y Label")
    plt.tight_layout()
    plt.savefig(r'r"\第1章 科研论文配图的绘制与配色基础\图1-2-14 使用seaborn库中Tips数据集绘制的单色系、双色渐变色系和多色系可视化配图示例_b.pdf',bbox_inches='tight')
    plt.savefig(r'r"\第1章 科研论文配图的绘制与配色基础\图1-2-14 使用seaborn库中Tips数据集绘制的单色系、双色渐变色系和多色系可视化配图示例_b.png', 
             bbox_inches='tight',dpi=300)
plt.show()

# c）多色系可视化绘制示例

with plt.style.context(['science']):
    from proplot import rc
    rc["xtick.minor.visible"] = False
    rc["ytick.minor.visible"] = False
    rc["xtick.major.pad"] =5
    
    fig,ax = plt.subplots(figsize=(3,3.2),dpi=100,facecolor="w")
    scatter = ax.scatter(x="total_bill",y="tip",c="tip",data=tips,ec="k",
               cmap="Set1")
    for spine in ["top","right"]:
        ax.spines[spine].set_visible(False)
    ax.tick_params(top=False,right=False)
    cax = ax.inset_axes([0.1, .85, 0.6, 0.05], transform=ax.transAxes)
    colorbar = fig.colorbar(scatter, ax=scatter, cax=cax,
                            orientation="horizontal")

    colorbar.ax.tick_params(bottom=True,direction="in",labelsize=8,pad=3)
    colorbar.ax.xaxis.set_ticks_position('top')
    colorbar.outline.set_linewidth(.4)
    ax.grid(False)
    ax.set_ylim(0,12)
    ax.set_xlabel("X Label")
    ax.set_ylabel("Y Label")
    plt.tight_layout()
    plt.savefig(r'r"\第1章 科研论文配图的绘制与配色基础\图1-2-14 使用seaborn库中Tips数据集绘制的单色系、双色渐变色系和多色系可视化配图示例_c.pdf',bbox_inches='tight')
    plt.savefig(r'r"\第1章 科研论文配图的绘制与配色基础\图1-2-14 使用seaborn库中Tips数据集绘制的单色系、双色渐变色系和多色系可视化配图示例_c.png', 
             bbox_inches='tight',dpi=300)
plt.show()