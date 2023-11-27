
"""
编写时间：2022年5月11日 17：50

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。

代码中Proplot包绘制的部分可能与Matplotlib绘制不同，需注意两者绘图语法的不同~~

"""
#注意：本案例中引入的SciencePlots库主题方式会随着SciencePlots版本的更新发生改变，读者还需参考其官网引入的正确方式。

import numpy as np
import pandas as pd
import seaborn as sns
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
obser = scatter_data.obser_all
dnn = scatter_data.DNN_all
gbrt = scatter_data.GBRT_all
lr = scatter_data.LR_all
svm = scatter_data.SVM_all

colors = ["#2FBE8F","#459DFF","#FF5B9B","#FFCC37","#751DFE"]
labels = scatter_data.columns.to_list()
all_data = [obser,dnn,gbrt,lr,svm]

# a）不同模型估算值箱线图绘制（Matplotlib）
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
bplot = ax.boxplot(all_data,vert=True, patch_artist=True,labels=labels,widths=.7,
                  medianprops={"color":"k"}) 
ax.grid(False)
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)
ax.set_xlabel("Model")
ax.set_ylabel("ET Values")

fig.savefig('第8章 学术图绘制案例\图8-1-2 观测值与不同模型估算值箱线图绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('第8章 学术图绘制案例\图8-1-2 观测值与不同模型估算值箱线图绘制示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# b）不同模型估算值箱线图绘制（seaborn）

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
box = sns.boxplot(data=scatter_data, palette=colors,
                  saturation=1,width=.7,linewidth=1.2)
ax.grid(False)
ax.set_xlabel("Model")
ax.set_ylabel("ET Values")

fig.savefig('第8章 学术图绘制案例\图8-1-2 观测值与不同模型估算值箱线图绘制示例_b.pdf',bbox_inches='tight')
fig.savefig('第8章 学术图绘制案例\图8-1-2 观测值与不同模型估算值箱线图绘制示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()