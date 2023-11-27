
"""
编写时间：2022年4月16日 14：30

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

"""
此代码为使用Python-Prolot包进行学术风格图表绘制，绘图语法和Matplotlib有所不同，需注意。
"""


import numpy as np
import pandas as pd
from scipy import interpolate
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

error_dot_line = pd.read_excel(r"\第4章 双变量图形的绘制\分组误差线图构建.xlsx")

# a）Matplotlib误差折线图示例

selsect = ["A","B","C","D"]
colors = ["#2FBE8F","#459DFF","#FF5B9B","#FFCC37"]
data = error_dot_line

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
for index,color in zip(selsect,colors):
    data_selcet = data.loc[data['type']==index,:]
    ax.errorbar(x=data_selcet["time"],y=data_selcet["mean"],yerr=data_selcet["sd"],color="k",
                linewidth=1.5,marker='o',ms=10,mew=2,mfc=color,mec='k',capsize=5,label=index)
ax.set_ylim(-8,30)
ax.set_xlim(-2,40)
ax.set_xlabel("Day")
ax.set_ylabel("Values Change")
ax.legend(ncol=2,frameon=False)
ax.set_axisbelow(True)

fig.savefig('\第4章 双变量图形的绘制\图4-2-4 误差折线图绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-2-4 误差折线图绘制示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# b）ProPlot误差折线图示例
import proplot as pplt
from proplot import rc
rc["axes.labelsize"] = 15
rc['tick.labelsize'] = 12
rc["suptitle.size"] = 15

data = error_dot_line

fig,ax = pplt.subplots(figsize=(3.5,3))
ax.format(abc='a.', abcloc='ul',abcsize=16,
          xlabel='Day', ylabel='Values Change',
          xlim=(-2,40),ylim=(-8,30))
selsect = ["A","B","C","D"]
colors = ["#2FBE8F","#459DFF","#FF5B9B","#FFCC37"]
for index,color in zip(selsect,colors):
    data_selcet = data.loc[data['type']==index,:]
    #ax.plot(data_selcet["time"].values,data_selcet["mean"].values,linewidth=5,color=color)
    ax.errorbar(x=data_selcet["time"],y=data_selcet["mean"],yerr=data_selcet["sd"],color="k",
                linewidth=1.5,marker='o',ms=10,mew=2,mfc=color,mec='k',capsize=5,label=index)
ax.legend(ncols=4, frame=False,loc='t')

fig.savefig('\第4章 双变量图形的绘制\图4-2-4 误差折线图绘制示例_b.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-2-4 误差折线图绘制示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()


# c）SciencePlots误差折线图示例 需安装SciencePlots 包（pip install SciencePlots）,注意最新版本引用方式

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = error_dot_line

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

fig.savefig('\第4章 双变量图形的绘制\图4-2-4 误差折线图绘制示例_c.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-2-4 误差折线图绘制示例_c.png', 
            bbox_inches='tight',dpi=300)
plt.show()





