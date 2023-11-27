"""
编写时间：2022年4月15日 19：50

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

"""
此代码为使用Python-Prolot包进行学术风格图表绘制，绘图语法和Matplotlib有所不同，需注意。

"""
import mpltern
import pandas as pd
import numpy as np
import proplot as pplt
import seaborn as sns
import matplotlib.pyplot as plt
from colormaps import parula
from proplot import rc
rc["font.family"] = "Times New Roman"
rc["axes.labelsize"] = 15
rc["tick.labelsize"] = 12
rc["suptitle.size"] = 15
rc["title.size"] = 14

scatter_data = pd.read_excel(r"\第5章 多变量图形的绘制\ternary_scatter.xlsx")
t, l, r = scatter_data["Variable 1"],scatter_data["Variable 2"],scatter_data["Variable 3"]


# a）三元相散点图示例

fig = plt.figure(figsize=(4.5, 4),dpi=100,facecolor="w")
ax = fig.add_subplot(projection='ternary')
ax.tick_params(length=8)
ax.grid(color="k",linewidth=0.5)
ax.scatter(t, l, r,s=65,color="#459DFF",ec="k",lw=.6,zorder=7,label="Test Data")
ax.set_tlabel('Top')
ax.set_llabel('Left')
ax.set_rlabel('Right')
# 添加label
ax.text(-0.2,0.7,0.5,s="Variable 1",fontsize=16, fontweight="bold")
ax.text(0.2,0.4,-.1,s="Variable 2",fontsize=16, fontweight="bold",rotation="60")
ax.text(0.2,-.02,0.35,s="Variable 3",fontsize=16, fontweight="bold",rotation="-60")
ax.legend(fontsize=12,handletextpad=.1)
plt.savefig(r'\第5章 多变量图形的绘制\图5-3-3  使用mpltern绘制的三元相散点图示例_a.pdf', bbox_inches='tight',)
plt.savefig(r'\第5章 多变量图形的绘制\图5-3-3  使用mpltern绘制的三元相散点图示例_a.png', 
            bbox_inches='tight',dpi=600)
plt.show()


# b）三元相散点图（SciencePlots主题）:需安装SciencePlots包，导入方式随版本更新有所不同，读者可查看最新版本引用方式
import mpltern
import matplotlib.pyplot as plt
plt.rcParams["axes.linewidth"] = 1.5
plt.rcParams["axes.labelsize"] = 15
plt.rcParams["xtick.labelsize"] = 14
plt.rcParams["ytick.labelsize"] = 14

scatter_data = pd.read_excel(r"\第5章 多变量图形的绘制\ternary_scatter.xlsx")
l = scatter["Variable 1"].values
t = scatter["Variable 2"].values
r = scatter["Variable 3"].values

#引用SciencePlots主题
plt.style.use('science')
fig = plt.figure(figsize=(4.5, 4),dpi=100,facecolor="w")
ax = fig.add_subplot(projection='ternary')
ax.tick_params(length=8)
ax.grid(color="k",linewidth=0.5)
ax.scatter(t, l, r,s=65,color="#459DFF",ec="k",lw=.6,zorder=7,label="Test Data")
ax.set_tlabel('Top')
ax.set_llabel('Left')
ax.set_rlabel('Right')
# 添加label
ax.text(-0.2,0.7,0.5,s="Variable 1",fontsize=16, fontweight="bold")
ax.text(0.2,0.4,-.1,s="Variable 2",fontsize=16, fontweight="bold",rotation="60")
ax.text(0.2,-.02,0.35,s="Variable 3",fontsize=16, fontweight="bold",rotation="-60")
ax.legend(fontsize=12,handletextpad=.1)

plt.savefig(r'\第5章 多变量图形的绘制\图5-3-3  使用mpltern绘制的三元相散点图示例_b.pdf', bbox_inches='tight',)
plt.savefig(r'\第5章 多变量图形的绘制\图5-3-3  使用mpltern绘制的三元相散点图示例_b.png', 
            bbox_inches='tight',dpi=600)
plt.show()
