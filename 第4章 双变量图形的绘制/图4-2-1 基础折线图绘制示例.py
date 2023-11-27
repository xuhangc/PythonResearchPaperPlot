"""
编写时间：2022年4月16日 09：50

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

"""
此代码为使用Python-Prolot包进行学术风格图表绘制，绘图语法和Matplotlib有所不同，需注意。
"""

import numpy as np
import pandas as pd
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

line_data = pd.read_excel(r"第4章 双变量图形的绘制\折线图数据.xlsx")


# a）Matplotlib绘制折线图示例

data_select = ["one","two","three"]
colors = ["#2FBE8F","#459DFF","#FFCC37"]
#colors = ["#2FBE8F","#459DFF","#FF5B9B","#FFCC37"]
day = line_data["day"].values

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
for select,color in zip(data_select,colors):
    ax.plot(day,line_data[select].values,color=color,lw=4,label=select)
    ax.grid(which="major",ls="--",lw=.8,zorder=0)
    ax.set_xlabel("Day")
    ax.set_ylabel("Values")
    ax.legend(ncol=1,frameon=False)
    
fig.savefig('\第4章 双变量图形的绘制\图4-2-1 基础折线图绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-2-1 基础折线图绘制示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# b）ProPlot绘制折线图示例
import proplot as pplt
from proplot import rc
rc["axes.labelsize"] = 15
rc['tick.labelsize'] = 12
rc["suptitle.size"] = 15

data_select = ["one","two","three"]
colors = ["#2FBE8F","#459DFF","#FFCC37"]
day = line_data["day"].values

fig = pplt.figure(figsize=(3.5,3))
ax = fig.subplot()
ax.format(abc='a.', abcloc='ul',abcsize=16,
          xlabel='Day', ylabel='Values',
          xlim=(-2,40),ylim=(-7,32))

for select,color in zip(data_select,colors):
    ax.plot(day,line_data[select].values,color=color,lw=4,label=select)
ax.legend(frame=False,loc='t')

fig.savefig('\第4章 双变量图形的绘制\图4-2-1 基础折线图绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-2-1 基础折线图绘制示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# c）SciencePlots绘制折线图示例 # 许安装SciencePlots 包（pip installl SciencePlots）,注意最新版本引用方式
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

plt.style.use('science') # 设置全局绘图样式

data_select = ["one","two","three"]
colors = ["#2FBE8F","#459DFF","#FFCC37"]
day = line_data["day"].values
    
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
  for select,color in zip(data_select,colors):
      ax.plot(day,line_data[select].values,color=color,lw=4,label=select)
      ax.grid(which="major",ls="--",lw=.8,zorder=0)
      ax.set_xlabel("Day")
      ax.set_ylabel("Values")
      ax.legend(ncol=1,frameon=False)
      
fig.savefig('\第4章 双变量图形的绘制\图4-2-1 基础折线图绘制示例_c.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-2-1 基础折线图绘制示例_c.png', 
            bbox_inches='tight',dpi=300)
plt.show()


