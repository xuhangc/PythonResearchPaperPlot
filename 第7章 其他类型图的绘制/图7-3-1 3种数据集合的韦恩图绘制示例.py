"""
编写时间：2022年5月06日 14：50

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。

代码中Proplot包绘制的部分可能与Matplotlib绘制不同，需注意两者绘图语法的不同~~

"""
#注意：本案例中引入的SciencePlots库主题方式会随着SciencePlots版本的更新发生改变，读者还需参考其官网引入的正确方式。
# 
import scipy
import numpy as np
import pandas as pd
from venn import venn
import matplotlib.pyplot as plt
from proplot import rc
rc["xtick.minor.visible"] = False
rc["ytick.minor.visible"] = False
from colormaps import parula

venn_data = pd.read_table(r"\第7章 其他类型图的绘制\data2.txt")

# a）3个数据集合的韦恩图绘制
venn_dict3 = dict(Set1={i for i in venn_data["Set1"].values},
                 Set2={i for i in venn_data["Set2"].values},
                 Set3={i for i in venn_data["Set3"].values})
            
fig,ax = plt.subplots(figsize=(5,4),dpi=100,facecolor="w")
venn(venn_dict3,cmap=parula,ax=ax,legend_loc=2,fontsize=8,alpha=.6)
fig.tight_layout()

fig.savefig('\第7章 其他类型图的绘制\图7-3-1 3种数据集合的韦恩图绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第7章 其他类型图的绘制\图7-3-1 3种数据集合的韦恩图绘制示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# b）4个数据集合的韦恩图绘制

venn_dict4 = dict(Set1={i for i in venn_data["Set1"].values},
                 Set2={i for i in venn_data["Set2"].values},
                 Set3={i for i in venn_data["Set3"].values},
                 Set4={i for i in venn_data["Set4"].values})
                 
fig,ax = plt.subplots(figsize=(5,4),dpi=100,facecolor="w")
venn(venn_dict4,cmap=parula,ax=ax,legend_loc=2,fontsize=11,alpha=.6)
fig.tight_layout()    

fig.savefig('\第7章 其他类型图的绘制\图7-3-1 3种数据集合的韦恩图绘制示例_b.pdf',bbox_inches='tight')
fig.savefig('\第7章 其他类型图的绘制\图7-3-1 3种数据集合的韦恩图绘制示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()            

# c）5个数据集合的韦恩图绘制

venn_dict5 = dict(Set1={i for i in venn_data["Set1"].values},
                 Set2={i for i in venn_data["Set2"].values},
                 Set3={i for i in venn_data["Set3"].values},
                 Set4={i for i in venn_data["Set4"].values},
                 Set5={i for i in venn_data["Set5"].values},)
                 
fig,ax = plt.subplots(figsize=(5,4),dpi=100,facecolor="w")
venn(venn_dict5,cmap=parula,ax=ax,legend_loc=2,fontsize=11,alpha=.6)
fig.tight_layout()

fig.savefig('\第7章 其他类型图的绘制\图7-3-1 3种数据集合的韦恩图绘制示例_c.pdf',bbox_inches='tight')
fig.savefig('\第7章 其他类型图的绘制\图7-3-1 3种数据集合的韦恩图绘制示例_c.png', 
            bbox_inches='tight',dpi=300)
plt.show()   