"""
编写时间：2022年2月05日 17：20

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。

代码中Proplot包绘制的部分可能与Matplotlib绘制不同，需注意两者绘图语法的不同~~

"""

import pandas as pd
import numpy as np
import proplot as pplt
import seaborn as sns
import matplotlib.pyplot as plt


from proplot import rc
rc["font.family"] = "Times New Roman"
rc["axes.labelsize"] = 15
rc['tick.labelsize'] = 13

data = pd.read_excel(r"\第2章 绘制工具及其重要特征\分组误差线图构建.xlsx")

#(a)paper值对应的缩放效果

sns.set_context("paper")
selsect = ["A","B","C","D"]
colors = ["#2FBE8F","#459DFF","#FF5B9B","#FFCC37"]

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
for index,color in zip(selsect,colors):
    data_selcet = data.loc[data['type']==index,:]
    ax.errorbar(x=data_selcet["time"],y=data_selcet["mean"],yerr=data_selcet["sd"],color="k",
                linewidth=1.5,marker='o',ms=10,mew=2,mfc=color,mec='k',capsize=5,label=index)
  
ax.set_ylim(-8,30)
ax.set_xlim(-2,40)
ax.set_xlabel("Day")
ax.set_ylabel("Values Change")
ax.legend()

plt.savefig(r'\第2章 绘制工具及其重要特征\图2-2-5 context参数4种值对应的缩放效果_a.pdf',bbox_inches='tight')
plt.savefig(r'\第2章 绘制工具及其重要特征\图2-2-5 context参数4种值对应的缩放效果_a.png', 
            bbox_inches='tight',dpi=300)       
plt.show()

#(b) notebook值对应的缩放效果
sns.set_context("notebook")
selsect = ["A","B","C","D"]
colors = ["#2FBE8F","#459DFF","#FF5B9B","#FFCC37"]

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
for index,color in zip(selsect,colors):
    data_selcet = data.loc[data['type']==index,:]
    ax.errorbar(x=data_selcet["time"],y=data_selcet["mean"],yerr=data_selcet["sd"],color="k",
                linewidth=1.5,marker='o',ms=10,mew=2,mfc=color,mec='k',capsize=5,label=index)
  
ax.set_ylim(-8,30)
ax.set_xlim(-2,40)
ax.set_xlabel("Day")
ax.set_ylabel("Values Change")
ax.legend()

plt.savefig(r'\第2章 绘制工具及其重要特征\图2-2-5 context参数4种值对应的缩放效果_b.pdf',bbox_inches='tight')
plt.savefig(r'\第2章 绘制工具及其重要特征\图2-2-5 context参数4种值对应的缩放效果_b.png', 
            bbox_inches='tight',dpi=300)       
plt.show()

#(c) talk值对应的缩放效果
sns.set_context("talk")
selsect = ["A","B","C","D"]
colors = ["#2FBE8F","#459DFF","#FF5B9B","#FFCC37"]

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
for index,color in zip(selsect,colors):
    data_selcet = data.loc[data['type']==index,:]
    ax.errorbar(x=data_selcet["time"],y=data_selcet["mean"],yerr=data_selcet["sd"],color="k",
                linewidth=1.5,marker='o',ms=10,mew=2,mfc=color,mec='k',capsize=5,label=index)
  
ax.set_ylim(-8,30)
ax.set_xlim(-2,40)
ax.set_xlabel("Day")
ax.set_ylabel("Values Change")
ax.legend()
#plt.tight_layout()
plt.savefig(r'\第2章 绘制工具及其重要特征\图2-2-5 context参数4种值对应的缩放效果_c.pdf',bbox_inches='tight')
plt.savefig(r'\第2章 绘制工具及其重要特征\图2-2-5 context参数4种值对应的缩放效果_c.png', 
            bbox_inches='tight',dpi=300)       
plt.show()

#(d) poster值对应的缩放效果

sns.set_context("poster")
selsect = ["A","B","C","D"]
colors = ["#2FBE8F","#459DFF","#FF5B9B","#FFCC37"]

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
for index,color in zip(selsect,colors):
    data_selcet = data.loc[data['type']==index,:]
    ax.errorbar(x=data_selcet["time"],y=data_selcet["mean"],yerr=data_selcet["sd"],color="k",
                linewidth=1.5,marker='o',ms=10,mew=2,mfc=color,mec='k',capsize=5,label=index)
  
ax.set_ylim(-8,30)
ax.set_xlim(-2,40)
ax.set_xlabel("Day")
ax.set_ylabel("Values Change")
ax.legend()
#plt.tight_layout()
plt.savefig(r'\第2章 绘制工具及其重要特征\图2-2-5 context参数4种值对应的缩放效果_d.pdf',bbox_inches='tight')
plt.savefig(r'\第2章 绘制工具及其重要特征\图2-2-5 context参数4种值对应的缩放效果_d.png', 
            bbox_inches='tight',dpi=300)       
plt.show()