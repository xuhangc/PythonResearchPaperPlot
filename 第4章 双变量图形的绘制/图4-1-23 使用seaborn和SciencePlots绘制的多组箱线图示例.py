
"""
编写时间：2022年4月12日 09：30

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

# a）使用seaborn绘制的一般多组箱线图

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
boxplot = sns.boxplot(x="day", y="total_bill",data=tips,palette=colors,saturation=1,
                      width=.7,linewidth=1.2)
ax.set_xlabel("Time")
ax.set_ylabel("Values")

fig.savefig('\第4章 双变量图形的绘制\图4-1-23 使用seaborn和SciencePlots绘制的多组箱线图示例_a.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-23 使用seaborn和SciencePlots绘制的多组箱线图示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()


# b）使用seaborn绘制的多组缺口箱线图

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
boxplot = sns.boxplot(x="day", y="total_bill",data=tips,palette=colors,saturation=1,
                      width=.7,linewidth=1.2,notch=True)
ax.set_xlabel("Time")
ax.set_ylabel("Values")

fig.savefig('\第4章 双变量图形的绘制\图4-1-23 使用seaborn和SciencePlots绘制的多组箱线图示例_b.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-23 使用seaborn和SciencePlots绘制的多组箱线图示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# c）使用SciencePlots主题库绘制的多组箱线图
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

plt.style.use('science')  # 需安装SciencePlots  读者需注意其最新的引用方式

tips = sns.load_dataset("tips")

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
boxplot = sns.boxplot(x="day", y="total_bill",data=tips,palette=colors,saturation=1,
                      width=.7,linewidth=1.2)
ax.set_xlabel("Time")
ax.set_ylabel("Values")

fig.savefig('\第4章 双变量图形的绘制\图4-1-23 使用seaborn和SciencePlots绘制的多组箱线图示例_c.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-23 使用seaborn和SciencePlots绘制的多组箱线图示例_c.png', 
            bbox_inches='tight',dpi=300)
plt.show()


