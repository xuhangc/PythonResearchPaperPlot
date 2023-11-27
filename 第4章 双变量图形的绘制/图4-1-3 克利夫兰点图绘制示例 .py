
"""
编写时间：2022年4月10日 14：30

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

"""
此代码为使用Python-Prolot包进行学术风格图表绘制，绘图语法和Matplotlib有所不同，需注意。
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from proplot import rc
rc["font.family"] = "Times New Roman"
rc["axes.labelsize"] = 15
rc["tick.labelsize"] = 12
rc["suptitle.size"] = 15
rc["title.size"] = 14

# a）利用ProPlot绘制的单组克利夫兰点图
values = [2,3.5,4.2,5,6.8,7.5]
labels = ['a','b','c','d','e',"f"]
index = np.arange(len(labels))

fig = pplt.figure(figsize=(3.5,3))
ax = fig.subplot()
ax.format(abc='a.', abcloc='ul',abcsize=16,
          xlabel='Values', ylabel='Class',
          xlim=(0, 9),ylim=(-1,6))
for x,y in zip(values,index):
    ax.scatter(x=x,y=y,s=100,color="gray",ec="k")
ax.set_yticks(index)
ax.set_yticklabels(labels)

fig.savefig('\第4章 双变量图形的绘制\图4-1-3 克利夫兰点图绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-3 克利夫兰点图绘制示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# b）利用ProPlot绘制的多组克利夫兰点图

values1 = [2,3.7,4.1,5,6.8,7.5]
values2 = [1.1,3,4.9,5.7,6,7]
labels = ['a','b','c','d','e',"f"]
index = np.arange(len(labels))
fig = pplt.figure(figsize=(3.5,3))
ax = fig.subplot()
ax.format(abc='a.', abcloc='ur',abcsize=16,
          xlabel='Values', ylabel='Class',
          xlim=(0, 9),ylim=(-1,6))
for x1,x2,y in zip(values1,values2,index):
    ax.scatter(x=x1,y=y,s=100,color="#459DFF",ec="k",zorder=2)
    ax.scatter(x=x2,y=y,s=100,color="#FF5B9B",ec="k",zorder=2)
ax.set_yticks(index)
ax.set_yticklabels(labels)
#单独添加图例
ax.scatter([],[],color="#459DFF",ec="k",label="values1")
ax.scatter([],[],color="#FF5B9B",ec="k",label="values2")
ax.legend(ncol=1,loc="ul")
fig.savefig('\第4章 双变量图形的绘制\图4-1-3 克利夫兰点图绘制示例_b.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-3 克利夫兰点图绘制示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# c）利用seaborn绘制的多组克利夫兰点图
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["axes.linewidth"] = .8
plt.rcParams["axes.labelsize"] = 15
plt.rcParams["xtick.minor.visible"] = True
plt.rcParams["ytick.minor.visible"] = True
plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"
plt.rcParams["xtick.labelsize"] = 12
plt.rcParams["ytick.labelsize"] = 12
plt.rcParams["xtick.top"] = True
plt.rcParams["ytick.right"] = True

values1 = [2,3.7,4.1,5,6.8,7.5]
values2 = [1.1,3,4.9,5.7,6,7]
variable = ["values1"]*len(values1)+["values2"]*len(values2)
labels = ['a','b','c','d','e',"f"]
group_data = pd.DataFrame({"Values":values1+values2,
                          "Class":labels*2,
                          "Variable":variable})
                          
palette = ["#459DFF","#FF5B9B"]
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
sns.stripplot(x="Values",y="Class",hue="Variable",data=group_data,size=10,palette=palette,
              edgecolor="k",linewidth=1,jitter=False,ax=ax)
ax.grid(axis="y",ls="--",lw=.6)
ax.set(xlim=(0, 9),ylim=(-1,6))
fig.savefig('\第4章 双变量图形的绘制\图4-1-3 克利夫兰点图绘制示例_c.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-3 克利夫兰点图绘制示例_c.png', 
            bbox_inches='tight',dpi=300)
plt.show()


                          



