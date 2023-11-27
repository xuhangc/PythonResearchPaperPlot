
"""
编写时间：2022年4月12日 13：30

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

tips = sns.load_dataset("tips")

# a）利用seaborn绘制的字母值箱线图
colors = ["#2FBE8F","#459DFF","#FF5B9B","#FFCC37"]
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
ax = sns.boxenplot(x="day", y="total_bill", data=tips,palette=colors,saturation=1,
                      width=.7,linewidth=1.2,ax=ax)
ax.set_xlabel("Time")
ax.set_ylabel("Values")

fig.savefig('\第4章 双变量图形的绘制\图4-1-25 单/分组 字母值箱线图绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-25 单/分组 字母值箱线图绘制示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# b）利用SciencePlots主题库绘制的字母值箱线图
plt.style.use('science')  # 需安装SciencePlots  读者需注意其最新的引用方式

colors = ["#2FBE8F","#459DFF","#FF5B9B","#FFCC37"]
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
ax = sns.boxenplot(x="day", y="total_bill", data=tips,palette=colors,saturation=1,
                      width=.7,linewidth=1.2,ax=ax)
ax.set_xlabel("Time")
ax.set_ylabel("Values")
fig.savefig('\第4章 双变量图形的绘制\图4-1-25 单/分组 字母值箱线图绘制示例_b.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-25 单/分组 字母值箱线图绘制示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# c）利用seaborn绘制的分组字母值箱线图
colors = ["#459DFF","#FF5B9B"]
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
ax = sns.boxenplot(x="day", y="total_bill", hue="smoker",data=tips,palette=colors,saturation=1,
                      width=.7,linewidth=1.2,ax=ax)
ax.set_xlabel("Time")
ax.set_ylabel("Values")

fig.savefig('\第4章 双变量图形的绘制\图4-1-25 单/分组 字母值箱线图绘制示例_c.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-25 单/分组 字母值箱线图绘制示例_c.png', 
            bbox_inches='tight',dpi=300)
plt.show()
# d）利用SciencePlots 主题库绘制的分组字母值箱线图
plt.style.use('science')  # 需安装SciencePlots  读者需注意其最新的引用方式

colors = ["#459DFF","#FF5B9B"]
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
ax = sns.boxenplot(x="day", y="total_bill", hue="smoker",data=tips,palette=colors,saturation=1,
                      width=.7,linewidth=1.2,ax=ax)
ax.set_xlabel("Time")
ax.set_ylabel("Values")

fig.savefig('\第4章 双变量图形的绘制\图4-1-25 单/分组 字母值箱线图绘制示例_d.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-25 单/分组 字母值箱线图绘制示例_d.png', 
            bbox_inches='tight',dpi=300)
plt.show()



