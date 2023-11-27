"""
编写时间：2022年2月05日 20：20

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。

代码中Proplot包绘制的部分可能与Matplotlib绘制不同，需注意两者绘图语法的不同~~

"""
#注意：本案例中引入的SciencePlots库主题方式会随着SciencePlots版本的更新发生改变，读者还需参考其官网引入的正确方式。
#      建议按照官网引入方式进行操作和使用最新版本的ScienePlots。如引入方式发生改变，请关注微信公众号【DataCharm】进行实时获取代码更新。
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_excel(r"\第2章 绘制工具及其重要特征\分组误差线图构建.xlsx")

#(a)Matplotlib的默认颜色主题和绘图风格
selsect = ["A","B","C","D"]
colors = ["#2FBE8F","#459DFF","#FF5B9B","#FFCC37"]
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")

for index,color in zip(selsect,colors):
    data_selcet = data.loc[data['type']==index,:]
    ax.errorbar(x=data_selcet["time"],y=data_selcet["mean"],yerr=data_selcet["sd"],
                linewidth=1,marker='o',ms=10,mew=1,mec='k',capsize=5,label=index)
    ax.legend()
    ax.set(xlabel='Time', ylabel='Values',
           xlim=(-2,40),ylim=(-8,30))

plt.savefig('\第2章 绘制工具及其重要特征\图2-3-8 ScienecePlots_matplotlib.png', 
         bbox_inches='tight',dpi=600)
plt.savefig('\第2章 绘制工具及其重要特征\图2-3-8 ScienecePlots_matplotlib.pdf', 
         bbox_inches='tight') 
plt.show()

#(b)Science系列期刊风格绘制结果

selsect = ["A","B","C","D"]
colors = ["#2FBE8F","#459DFF","#FF5B9B","#FFCC37"]
plt.style.use('science')
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
for index,color in zip(selsect,colors):
    data_selcet = data.loc[data['type']==index,:]
    ax.errorbar(x=data_selcet["time"],y=data_selcet["mean"],yerr=data_selcet["sd"],
                linewidth=1,marker='o',ms=10,mew=1,mec='k',capsize=5,label=index)
    ax.legend()
    ax.set(xlabel='Time', ylabel='Values',
           xlim=(-2,40),ylim=(-8,30))
plt.savefig('\第2章 绘制工具及其重要特征\图2-3-8 SciencePlots_science.png', 
         bbox_inches='tight',dpi=600)
plt.savefig('\第2章 绘制工具及其重要特征\图2-3-8 SciencePlots_science.pdf', 
         bbox_inches='tight') 
plt.show()

#(c)IEEE期刊风格绘制结果
selsect = ["A","B","C","D"]
colors = ["#2FBE8F","#459DFF","#FF5B9B","#FFCC37"]
plt.style.use(['science','ieee'])
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
for index,color in zip(selsect,colors):
    data_selcet = data.loc[data['type']==index,:]
    ax.errorbar(x=data_selcet["time"],y=data_selcet["mean"],yerr=data_selcet["sd"],
                linewidth=1,marker='o',ms=10,mew=1,mec='k',capsize=5,label=index)
    ax.legend()
    ax.set(xlabel='Time', ylabel='Values',
           xlim=(-2,40),ylim=(-8,30))
plt.savefig('\第2章 绘制工具及其重要特征\图2-3-8 SciencePlots_ieee.png', 
         bbox_inches='tight',dpi=600)
plt.savefig('\第2章 绘制工具及其重要特征\图2-3-8 SciencePlots_ieee.pdf', 
         bbox_inches='tight') 
plt.show()

#(d)Nature期刊风格绘制结果
colors = ["#2FBE8F","#459DFF","#FF5B9B","#FFCC37"]
selsect = ["A","B","C","D"]
plt.style.use(['science','nature'])
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
for index,color in zip(selsect,colors):
    data_selcet = data.loc[data['type']==index,:]
    ax.errorbar(x=data_selcet["time"],y=data_selcet["mean"],yerr=data_selcet["sd"],
                linewidth=1,marker='o',ms=10,mew=1,mec='k',capsize=5,label=index)
    ax.legend()
    ax.set(xlabel='Time', ylabel='Values',
           xlim=(-2,40),ylim=(-8,30))

plt.savefig('\第2章 绘制工具及其重要特征\图2-3-8 SciencePlots_nature.png', 
         bbox_inches='tight',dpi=600)
plt.savefig('\第2章 绘制工具及其重要特征\图2-3-8 SciencePlots_nature.pdf', 
         bbox_inches='tight') 
plt.show()

#(e)使用了vibrant 颜色主题的Science期刊绘图风格
selsect = ["A","B","C","D"]
plt.style.use(['science','vibrant'])
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
for index,color in zip(selsect,colors):
    data_selcet = data.loc[data['type']==index,:]
    ax.errorbar(x=data_selcet["time"],y=data_selcet["mean"],yerr=data_selcet["sd"],
                linewidth=1,marker='o',ms=10,mew=1,mec='k',capsize=5,label=index)
    ax.legend()
    ax.set(xlabel='Time', ylabel='Values',
           xlim=(-2,40),ylim=(-8,30))

plt.savefig('\第2章 绘制工具及其重要特征\图2-3-8 SciencePlots_vibrant.png', 
         bbox_inches='tight',dpi=600)
plt.savefig('\第2章 绘制工具及其重要特征\图2-3-8 SciencePlots_vibrant.pdf', 
         bbox_inches='tight') 
plt.show()

#(f)使用了bright颜色主题的Science期刊绘图风格
selsect = ["A","B","C","D"]
plt.style.use(['science','bright'])
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
for index,color in zip(selsect,colors):
    data_selcet = data.loc[data['type']==index,:]
    ax.errorbar(x=data_selcet["time"],y=data_selcet["mean"],yerr=data_selcet["sd"],
                linewidth=1,marker='o',ms=10,mew=1,mec='k',capsize=5,label=index)
    ax.legend()
    ax.set(xlabel='Time', ylabel='Values',
           xlim=(-2,40),ylim=(-8,30))
           
plt.savefig('\第2章 绘制工具及其重要特征\图2-3-8 SciencePlots_bright.png', 
         bbox_inches='tight',dpi=600)
plt.savefig('\第2章 绘制工具及其重要特征\图2-3-8 SciencePlots_bright.pdf', 
         bbox_inches='tight') 
plt.show()