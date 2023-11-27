
"""
编写时间：2022年5月10日 17：50

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。

代码中Proplot包绘制的部分可能与Matplotlib绘制不同，需注意两者绘图语法的不同~~

"""
#注意：本案例中引入的SciencePlots库主题方式会随着SciencePlots版本的更新发生改变，读者还需参考其官网引入的正确方式。

import numpy as np
import pandas as pd
import proplot as pplt
import matplotlib.pyplot as plt

from proplot import rc
rc["font.family"] = "Times New Roman"
rc["axes.labelsize"] = 14
rc["tick.labelsize"] = 11
rc["suptitle.size"] = 15
rc["title.size"] = 14
rc["font.weight"] = "bold"
rc["axes.labelweight"] = "bold"
rc["axes.titleweight"] = "bold"
rc["tick.minor"] = False
rc['figure.constrained_layout.use'] = True #调整子图显示不全等问题

scatter_data = pd.read_excel(r"第8章 学术图绘制案例\scatter_data.xlsx")

bins = np.arange(-5,90,10)
obser = scatter_data.obser_all
dnn = scatter_data.DNN_all
lr = scatter_data.LR_all
svm = scatter_data.SVM_all


# a）ET观测值直方图
fig,ax = plt.subplots(figsize=(4,3.3),dpi=100,facecolor="w",)
ax.hist(x=obser, bins=bins,color="#3F3F3F",alpha=0.85,
        edgecolor ='black',rwidth = 0.8)
ax.grid(False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set(xlabel="ET Values",ylabel="Number of Cases",
      xlim=(-7,85),ylim=(0,6000),xticks=np.arange(-5,90,10))
fig.savefig('第8章 学术图绘制案例\图8-1-1 ET观测值与3种模型估算值直方图绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('第8章 学术图绘制案例\图8-1-1 ET观测值与3种模型估算值直方图绘制示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# b）DNN模型估算值直方图 
fig,ax = plt.subplots(figsize=(4,3.3),dpi=100,facecolor="w",)
ax.hist(x=dnn, bins=bins,color="#3F3F3F",alpha=0.85,
        edgecolor ='black',rwidth = 0.8)
ax.grid(False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set(xlabel="ET Values",ylabel="Number of Cases",
      xlim=(-7,85),ylim=(0,6000),xticks=np.arange(-5,90,10))
fig.savefig('第8章 学术图绘制案例\图8-1-1 ET观测值与3种模型估算值直方图绘制示例_b.pdf',bbox_inches='tight')
fig.savefig('第8章 学术图绘制案例\图8-1-1 ET观测值与3种模型估算值直方图绘制示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# c）LR模型估算值直方图

fig,ax = plt.subplots(figsize=(4,3.3),dpi=100,facecolor="w",)
ax.hist(x=lr, bins=bins,color="#3F3F3F",alpha=0.85,
        edgecolor ='black',rwidth = 0.8)
ax.grid(False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set(xlabel="ET Values",ylabel="Number of Cases",
      xlim=(-7,85),ylim=(0,6000),xticks=np.arange(-5,90,10))

fig.savefig('第8章 学术图绘制案例\图8-1-1 ET观测值与3种模型估算值直方图绘制示例_c.pdf',bbox_inches='tight')
fig.savefig('第8章 学术图绘制案例\图8-1-1 ET观测值与3种模型估算值直方图绘制示例_c.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# d）SVR模型估算值直方图

fig,ax = plt.subplots(figsize=(4,3.3),dpi=100,facecolor="w",)
ax.hist(x=svm, bins=bins,color="#3F3F3F",alpha=0.85,
        edgecolor ='black',rwidth = 0.8)
ax.grid(False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set(xlabel="ET Values",ylabel="Number of Cases",
      xlim=(-7,85),ylim=(0,6000),xticks=np.arange(-5,90,10))
fig.savefig('第8章 学术图绘制案例\图8-1-1 ET观测值与3种模型估算值直方图绘制示例_d.pdf',bbox_inches='tight')
fig.savefig('第8章 学术图绘制案例\图8-1-1 ET观测值与3种模型估算值直方图绘制示例_d.png', 
            bbox_inches='tight',dpi=300)
plt.show()
