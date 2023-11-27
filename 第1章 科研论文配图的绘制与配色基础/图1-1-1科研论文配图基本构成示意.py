"""
编写时间：2022年2月04日 20：00

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

plt.style.use('science') #需安装Scienceplots 库（pip install SciencePlots），注意版本不同，引用方式可能有所改变


#data = pd.read_excel(r"\第1章 科研论文配图的绘制与配色基础\基本构成示意绘图数据.xlsx")
data = pd.read_excel(r"基本构成示意绘图数据.xlsx")

#proplot 方法绘制
fig = pplt.figure(figsize=(4.5,3.5))
ax = fig.subplot()
ax.format(abc='(a.)', abcloc='ul',abcsize=20,
          xlabel='Time', ylabel='Values',
          xlim=(-2,40),ylim=(-8,30))
selsect = ["A","B","C","D"]
colors = ["#2FBE8F","#459DFF","#FF5B9B","#FFCC37"]
for index,color in zip(selsect,colors):
    data_selcet = data.loc[data['type']==index,:]
    ax.errorbar(x=data_selcet["time"],y=data_selcet["mean"],yerr=data_selcet["sd"],color="k",
                linewidth=1,marker='o',ms=10,mew=1,mec='k',mfc=color,capsize=5,label=index)
ax.legend(ncols=4, frame=True,loc='t')
#fig.save(r"\第1章 科研论文配图的绘制与配色基础\\图1-1-1 科研论文配图基本构成示意图.svg")
plt.show()


