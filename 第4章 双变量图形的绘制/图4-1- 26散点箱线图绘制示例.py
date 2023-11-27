
"""
编写时间：2022年4月12日 15：30

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

"""
此代码为使用Python-Prolot包进行学术风格图表绘制，绘图语法和Matplotlib有所不同，需注意。
"""


import pandas as pd
import numpy as np
import seaborn as sns
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


scatterbox = pd.read_excel(r"第4章 双变量图形的绘制\scatterbox_data.xlsx")

# a）seaborn散点箱线图绘制（stripplot()）

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
boxplot = sns.boxplot(x="group", y="values",data=scatterbox,palette=colors,saturation=1,
                      width=.7,linewidth=1.2,whis=np.inf,showcaps=False,ax=ax)
point = sns.stripplot(x="group", y="values",data=scatterbox,size=8,jitter=.15,palette=colors,
                      edgecolor="k",linewidth=.8,ax=ax)
ax.set_xlabel("Group")
ax.set_ylabel("Values")
ax.set(ylim=(0,25))

fig.savefig('\第4章 双变量图形的绘制\图4-1-26散点箱线图绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-26散点箱线图绘制示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()


# b）seaborn散点箱线图绘制（swarmplot()）

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
boxplot = sns.boxplot(x="group", y="values",data=scatterbox,palette=colors,saturation=1,
                      width=.7,linewidth=1.2,whis=np.inf,showcaps=False,ax=ax)
point = sns.swarmplot(x="group", y="values",data=scatterbox,size=8,palette=colors,
                      edgecolor="k",linewidth=.8,ax=ax)
ax.set_xlabel("Group")
ax.set_ylabel("Values")
ax.set(ylim=(0,25))

fig.savefig('\第4章 双变量图形的绘制\图4-1-26散点箱线图绘制示例_b.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-26散点箱线图绘制示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()



