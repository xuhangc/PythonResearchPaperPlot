"""
编写时间：2022年4月11日 18：30

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

"""
此代码为使用Python-Prolot包进行学术风格图表绘制，绘图语法和Matplotlib有所不同，需注意。
"""

import pandas as pd
import numpy as np
import seaborn as sns
import proplot as pplt
import matplotlib.pyplot as plt

from proplot import rc
rc["font.family"] = "Times New Roman"
rc["axes.labelsize"] = 15
rc["tick.labelsize"] = 13
rc["suptitle.size"] = 15
rc["title.size"] = 14
rc["tick.minor"] = False

error_bar = sns.load_dataset("iris")
data = error_bar[["sepal_length","species"]]


#计算置信区间
import numpy as np
import scipy.stats
def mean_confidence_interval(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    ci = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return ci

data_select = data[data["species"]=="versicolor"]["sepal_length"]
#计算误差
versicolor_mean = data[data["species"]=="versicolor"]["sepal_length"].mean()
versicolor_sd = data[data["species"]=="versicolor"]["sepal_length"].std()
versicolor_se = versicolor_sd / np.sqrt(len(data_select))
versicolor_ci = mean_confidence_interval(data_select)

data_select = data[data["species"]=="virginica"]["sepal_length"]
virginica_mean = data[data["species"]=="virginica"]["sepal_length"].mean()
virginica_sd = data[data["species"]=="virginica"]["sepal_length"].std()
virginica_se = virginica_sd / np.sqrt(len(data_select))
virginica_ci = mean_confidence_interval(data_select)

data_select = data[data["species"]=="setosa"]["sepal_length"]
setosa_mean = data[data["species"]=="setosa"]["sepal_length"].mean()
setosa_sd = data[data["species"]=="setosa"]["sepal_length"].std()
setosa_se = setosa_sd / np.sqrt(len(data_select))
setosa_ci = mean_confidence_interval(data_select)

# a）SE误差柱形图
names = ["setosa","versicolor","virginica"]
colors = ['#0073C2FF','#EFC000FF','#868686FF']
means = [setosa_mean,versicolor_mean,virginica_mean]
se = [setosa_se,versicolor_se,virginica_se]

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
ax.bar(x=names, height=means, width=.5,color=colors,edgecolor="k",yerr=se, capsize=4) 
ax.tick_params(which='major',direction='in',length=3,width=1.,bottom=False)
for spine in ["top","left","right"]:
    ax.spines[spine].set_visible(False)
ax.spines['bottom'].set_linewidth(1.5)
ax.set(xlabel="Name",ylabel="Values",
       xticklabels=names,ylim=(0,8))
plt.tight_layout()

fig.savefig('\第4章 双变量图形的绘制\图4-1-18 使用Matplotlib绘制的基于自定义方法的不同类别误差柱形图示例_a.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-18 使用Matplotlib绘制的基于自定义方法的不同类别误差柱形图示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()


# b）SD误差柱形图
names = ["setosa","versicolor","virginica"]
colors = ['#0073C2FF','#EFC000FF','#868686FF']
means = [setosa_mean,versicolor_mean,virginica_mean]
sd = [setosa_sd,versicolor_sd,virginica_sd]
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
ax.bar(x=names, height=means, width=.5,color=colors,edgecolor="k",
       yerr=sd, capsize=4) 

ax.tick_params(which='major',direction='in',length=3,width=1.,bottom=False)
for spine in ["top","left","right"]:
    ax.spines[spine].set_visible(False)
ax.spines['bottom'].set_linewidth(2)
ax.set(xlabel="Name",ylabel="Values",
       xticklabels=names,ylim=(0,8))
plt.tight_layout()
fig.savefig('\第4章 双变量图形的绘制\图4-1-18 使用Matplotlib绘制的基于自定义方法的不同类别误差柱形图示例_b.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-18 使用Matplotlib绘制的基于自定义方法的不同类别误差柱形图示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# c）CI误差柱形图
names = ["setosa","versicolor","virginica"]
colors = ['#0073C2FF','#EFC000FF','#868686FF']
means = [setosa_mean,versicolor_mean,virginica_mean]
ci = [setosa_ci,versicolor_ci,virginica_ci]

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
ax.bar(x=names, height=means, width=.5,color=colors,edgecolor="k",yerr=ci, capsize=4) 
ax.tick_params(which='major',direction='in',length=3,width=1.,bottom=False)
for spine in ["top","left","right"]:
    ax.spines[spine].set_visible(False)
ax.spines['bottom'].set_linewidth(1.5)
ax.set(xlabel="Name",ylabel="Values",
       xticklabels=names,ylim=(0,8))
plt.tight_layout()
fig.savefig('\第4章 双变量图形的绘制\图4-1-18 使用Matplotlib绘制的基于自定义方法的不同类别误差柱形图示例_c.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-18 使用Matplotlib绘制的基于自定义方法的不同类别误差柱形图示例_c.png', 
            bbox_inches='tight',dpi=300)
plt.show()
