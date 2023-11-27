
"""
编写时间：2022年4月12日 19：30

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

"""
此代码为使用Python-Prolot包进行学术风格图表绘制，绘图语法和Matplotlib有所不同，需注意。
"""


import pandas as pd
import numpy as np
import seaborn as sns
from scipy import stats 
import matplotlib.pyplot as plt


plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["axes.linewidth"] = .8
plt.rcParams["axes.labelsize"] = 15
plt.rcParams["xtick.minor.visible"] = False
plt.rcParams["ytick.minor.visible"] = True
plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"
plt.rcParams["xtick.labelsize"] = 12
plt.rcParams["ytick.labelsize"] = 12
plt.rcParams["xtick.top"] = False
plt.rcParams["ytick.right"] = False

violin_data = pd.read_excel(r"\第4章 双变量图形的绘制\小提琴图数据.xlsx")
index = sorted(violin_data["class"].unique())
violin_data_pred = [violin_data[violin_data["class"] == index ]["values"].values for index in index]

# a）利用Matplotlib 绘制的基础“小提琴”图

colors = ["#2FBE8F","#459DFF","#FF5B9B"]
labels = ['cluster1', 'cluster2', 'cluster3']
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
violins = ax.violinplot(violin_data_pred,[0,1,2],widths=0.45,bw_method="silverman",
                        showmeans=False, showmedians=False,showextrema=False)
# 对每个小提琴图进行修改
for pc in (violins["bodies"]):
    pc.set_facecolor("#cccccc")
    pc.set_edgecolor("k")
    pc.set_linewidth(.7)
    pc.set_alpha(.8)
ax.set_xlabel("Class")
ax.set_ylabel("Values")
ax.set_xticks(np.arange(len(labels)))
ax.set_xticklabels(labels)

fig.savefig('\第4章 双变量图形的绘制\图4-1-30 不同样式“小提琴”图Matplotlib绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-30 不同样式“小提琴”图Matplotlib绘制示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# b）利用Matplotlib 绘制的误差“小提琴”图

labels = ['cluster1', 'cluster2', 'cluster3']
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
violins = ax.violinplot(violin_data_pred,[0,1,2],widths=0.45,bw_method="silverman",
                        showmeans=False, showmedians=False,showextrema=False)
# 对每个小提琴图进行修改
for pc in (violins["bodies"]):
    pc.set_facecolor("#cccccc")
    pc.set_edgecolor("k")
    pc.set_linewidth(.7)
    pc.set_alpha(.8)
# 添加误差
for x,y,err in zip(np.arange(len(means)),means,stds):
    ax.errorbar(x,y,err,fmt='o',ecolor="k",color="k",ms=8,
                linewidth=1.5,capsize=0,zorder=3)

ax.set_xlabel("Class")
ax.set_ylabel("Values")
ax.set_xticks(np.arange(len(labels)))
ax.set_xticklabels(labels)

fig.savefig('\第4章 双变量图形的绘制\图4-1-30 不同样式“小提琴”图Matplotlib绘制示例_b.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-30 不同样式“小提琴”图Matplotlib绘制示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# c）利用Matplotlib 绘制的箱线“小提琴”图

colors = ["#2FBE8F","#459DFF","#FF5B9B"]
labels = ['cluster1', 'cluster2', 'cluster3']
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
violins = ax.violinplot(violin_data_pred,[0,1,2],widths=0.45,bw_method="silverman",
                        showmeans=False, showmedians=False,showextrema=False)
# 对每个小提琴图进行修改
for pc in (violins["bodies"]):
    pc.set_facecolor("#cccccc")
    pc.set_edgecolor("k")
    pc.set_linewidth(.7)
    pc.set_alpha(.8)
# 添加boxplot
boxplot = ax.boxplot(violin_data_pred,positions=[0,1,2], showfliers = False, showcaps = False,   
                    boxprops={"linewidth":1.,"color":"gray"},
                    medianprops={"linewidth":1.5,"color":"k"},
                    whiskerprops={"linewidth":1.,"color":"gray"})
ax.set_xlabel("Class")
ax.set_ylabel("Values")
ax.set_xticks(np.arange(len(labels)))
ax.set_xticklabels(labels)

fig.savefig('\第4章 双变量图形的绘制\图4-1-30 不同样式“小提琴”图Matplotlib绘制示例_c.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-30 不同样式“小提琴”图Matplotlib绘制示例_c.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# d）利用Matplotlib绘制的箱线散点“小提琴”图

#自定义散点抖动
import scipy.stats as st

jitter = 0.04
x_data = [np.array([i] * len(d)) for i, d in enumerate(violin_data_pred)]
x_jittered = [x + st.t(df=6, scale=jitter).rvs(len(x)) for x in x_data]

colors = ["#2FBE8F","#459DFF","#FF5B9B"]
labels = ['cluster1', 'cluster2', 'cluster3']
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
violins = ax.violinplot(violin_data_pred,[0,1,2],widths=0.45,bw_method="silverman",
                        showmeans=False, showmedians=False,showextrema=False)
# 对每个小提琴图进行修改
for pc in (violins["bodies"]):
    pc.set_facecolor("#cccccc")
    pc.set_edgecolor("k")
    pc.set_linewidth(.7)
    pc.set_alpha(.8)
# 添加boxplot
boxplot = ax.boxplot(violin_data_pred,positions=[0,1,2], showfliers = False, showcaps = False,   
                    boxprops={"linewidth":1.,"color":"gray"},
                    medianprops={"linewidth":1.5,"color":"k"},
                    whiskerprops={"linewidth":1.,"color":"gray"})
# 手动添加抖动数据点
for x, y, in zip(x_jittered, violin_data_pred):
    ax.scatter(x, y, s = 20, color="yellow",ec="k",lw=.5,alpha=.7)
    
ax.set_xlabel("Class")
ax.set_ylabel("Values")
ax.set_xticks(np.arange(len(labels)))
ax.set_xticklabels(labels)

fig.savefig('\第4章 双变量图形的绘制\图4-1-30 不同样式“小提琴”图Matplotlib绘制示例_d.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-30 不同样式“小提琴”图Matplotlib绘制示例_d.png', 
            bbox_inches='tight',dpi=300)
plt.show()


