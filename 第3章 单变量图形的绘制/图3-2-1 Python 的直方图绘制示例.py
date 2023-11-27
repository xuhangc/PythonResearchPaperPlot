"""
编写时间：2022年2月06日 09：20

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。

代码中Proplot包绘制的部分可能与Matplotlib绘制不同，需注意两者绘图语法的不同~~

"""
#注意：本案例中引入的SciencePlots库主题方式会随着SciencePlots版本的更新发生改变，读者还需参考其官网引入的正确方式。
#      建议按照官网引入方式进行操作和使用最新版本的ScienePlots。如引入方式发生改变，请关注微信公众号【DataCharm】进行实时获取代码更新。

import numpy as np
import pandas as pd

hist_data = pd.read_excel(r"第3章 单变量图形的绘制\柱形图绘制数.xlsx")

#(a) Matplotlib绘制的直方图
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["axes.linewidth"] = 1
plt.rcParams["axes.labelsize"] = 15
plt.rcParams["xtick.minor.visible"] = True
plt.rcParams["ytick.minor.visible"] = True
plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"
plt.rcParams["xtick.labelsize"] = 12
plt.rcParams["ytick.labelsize"] = 12
plt.rcParams["xtick.top"] = False
plt.rcParams["ytick.right"] = False

hist_x_data = hist_data["hist_data"].values
bins = np.arange(0.0,1.5,0.1)

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
hist = ax.hist(x=hist_x_data, bins=bins,color="#3F3F3F",
          edgecolor ='black',rwidth = 0.8)

ax.tick_params(axis="x",which="minor",top=False,bottom=False)
ax.set_xticks(np.arange(0,1.4,0.1))
ax.set_yticks(np.arange(0.,2500,400))
ax.set_xlim(-.05,1.3)
ax.set_ylim(0.0,2500)

ax.set_xlabel('Values', )
ax.set_ylabel('Frequency')

plt.savefig('\第3章 单变量图形的绘制\图3-2-1 Python 的直方图绘制示例_a.png', 
         bbox_inches='tight',dpi=600)
plt.savefig('\第3章 单变量图形的绘制\图3-2-1 Python 的直方图绘制示例_a.pdf', 
         bbox_inches='tight') 
plt.show()

#(b)ProPlot绘制的直方图

import proplot as pplt
from proplot import rc
rc["axes.labelsize"] = 15
rc['tick.labelsize'] = 12
rc["suptitle.size"] = 15

hist_x_data = hist_data["hist_data"].values
bins = np.arange(0.0,1.5,0.1)


fig = pplt.figure(figsize=(3.5,3))
ax = fig.subplot()
ax.format(abc='a.', abcloc='ur',abcsize=16,
          xlabel='Values', ylabel='Frequency',
          xlim = (-.05,1.3),ylim=(0,2500))
hist = ax.hist(x=hist_x_data, bins=bins,color="#3F3F3F",
               edgecolor ='black',rwidth = 0.8)


fig.savefig('\第3章 单变量图形的绘制\图3-2-1 Python 的直方图绘制示例_b.pdf')
fig.savefig('\第3章 单变量图形的绘制\图3-2-1 Python 的直方图绘制示例_b.png')
plt.show()

#(c)SciencePlots 绘制的直方图（已安装SciencePlots  pip install SciencePlots）

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

hist_x_data = hist_data["hist_data"].values
bins = np.arange(0.0,1.5,0.1)


with plt.style.context(['science']):
    fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
    hist = ax.hist(x=hist_x_data, bins=bins,color="#3F3F3F",
                   edgecolor ='black',rwidth = 0.8)
    ax.set_xlim(-.05,1.4)
    ax.set_ylim(0.0,2500)
    ax.set_xlabel('Values', )
    ax.set_ylabel('Frequency')
    fig.savefig('\第3章 单变量图形的绘制\图3-2-1 Python 的直方图绘制示例_c.pdf',bbox_inches='tight')
    fig.savefig('\第3章 单变量图形的绘制\图3-2-1 Python 的直方图绘制示例_c.png', 
                bbox_inches='tight',dpi=300)

plt.show()


