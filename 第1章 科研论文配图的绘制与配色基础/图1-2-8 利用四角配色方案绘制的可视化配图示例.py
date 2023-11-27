"""
编写时间：2022年2月04日 21：30

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
rc["axes.labelsize"] = 15
rc['tick.labelsize'] = 13
rc["suptitle.size"] = 15

#图1-2-8 利用四角配色方案绘制的可视化配图示例_a
menMeans  = (5, 15, 30, 40)
menStd   = (2, 3, 4, 5)
ind  = np.arange(4)   
labels = ('A', 'B', 'C', 'D')
colors=["#1826B0","#4C10AE","#FFE200","#FFBA00"]
fig,ax = plt.subplots(figsize=(4,3),dpi=100,facecolor="w")
for name,value,err,label,color in zip(labels,menMeans,menStd,labels,colors):
    ax.bar(name,value,yerr=err,label=label,color=color,ec="k",lw=.8,
          capsize=5,error_kw={'linewidth':1})
for spine in ["top","right"]:
    ax.spines[spine].set_visible(False)
ax.grid(False)
ax.set_ylim(0,50)
ax.legend(frameon=False,handlelength=1.5,handleheight=1.5)
plt.savefig(r'r"\第1章 科研论文配图的绘制与配色基础\图1-2-8 利用四角配色方案绘制的可视化配图示例_a.pdf',bbox_inches='tight')
plt.savefig(r'r"\第1章 科研论文配图的绘制与配色基础\图1-2-8 利用四角配色方案绘制的可视化配图示例_a.png', 
             bbox_inches='tight',dpi=300)
plt.show()
             
             
#图1-2-8 利用四角配色方案绘制的可视化配图示例_b             
sizes = [20, 40, 25, 15]
labels = ['A','B','C','D',]
colors=["#1826B0","#4C10AE","#FFE200","#FFBA00"]

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
explode = (0, 0., 0,0)  
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
       shadow=False, startangle=90,colors=colors,
       wedgeprops={'linewidth':.8, 'edgecolor': 'k'},
       textprops={'size': 12,"color":"w"})
ax.legend(labels,loc ='upper left',fontsize=9,handlelength=1.2,handleheight=1.2)
plt.tight_layout()
plt.savefig(r'r"\第1章 科研论文配图的绘制与配色基础\图1-2-8 利用四角配色方案绘制的可视化配图示例_b.pdf',bbox_inches='tight')
plt.savefig(r'r"\第1章 科研论文配图的绘制与配色基础\图1-2-8 利用四角配色方案绘制的可视化配图示例_b.png', 
             bbox_inches='tight',dpi=300)
plt.show()