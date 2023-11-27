
"""
编写时间：2022年4月17日 10：00

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

"""
此代码为使用Python-Prolot包进行学术风格图表绘制，绘图语法和Matplotlib有所不同，需注意。
"""


import numpy as np
import pandas as pd
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

scatter_data = pd.read_excel(r"\第4章 双变量图形的绘制\散点图样例数据2.xlsx")

# a）Matplotlib 正相关散点图绘制示例
x = scatter_data["values"]
y = scatter_data["pred values"]
best_line_x = np.linspace(-10,10)
best_line_y=best_line_x

# 计算统计信息
from scipy import stats
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
scatter = ax.scatter(x=x,y=y,s=30,c="k",ec="k",label="Original Data")
ax.plot(x, intercept + slope*x, 'r', label='Fitted Line')
ax.set_xlim((-.1, 1.8))
ax.set_ylim((-.1, 1.8))
ax.set_xticks(np.arange(0, 2, step=0.2))
ax.set_yticks(np.arange(0, 2, step=0.2))
ax.set_xlabel("Variable 01")
ax.set_ylabel("Variable 02")
ax.text(0.,1.6,'R = '+str(round(r_value,2)),fontsize=12,fontstyle="italic")
ax.text(0.,1.4,"P < "+str(0.001),fontsize=12,fontstyle="italic")
ax.legend(loc="lower right")

fig.savefig('\第4章 双变量图形的绘制\4-2-10 正、负相关散点图绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\4-2-10 正、负相关散点图绘制示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# b）Matplotlib 负相关散点图绘制示例
from scipy import stats
mtcars = pd.read_excel(r"\第4章 双变量图形的绘制\mtcars.xlsx")
x2 = mtcars["wt"]
y2 = mtcars["mpg"]
slope, intercept, r_value, p_value, std_err = stats.linregress(x2,y2)

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
scatter = ax.scatter(x=x2,y=y2,s=30,c="k",ec="k",label="Original Data")
ax.plot(x2, intercept + slope*x2, 'r', label='Fitted Line')
ax.set_xlabel("Variable 01")
ax.set_ylabel("Variable 02")
ax.text(4,28,'R = '+str(round(r_value,2)),fontsize=11,fontstyle="italic")
ax.text(4,25,"P < "+str(0.001),fontsize=11,fontstyle="italic")
ax.legend(loc="upper right",frameon=False)

fig.savefig('\第4章 双变量图形的绘制\4-2-10 正、负相关散点图绘制示例_b.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\4-2-10 正、负相关散点图绘制示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# c）SciencePlots 正相关散点图绘制示例 # 需安装SciencePlots 包（pip install SciencePlots）,注意最新版本引用方式

import numpy as np
import pandas as pd
# 计算统计信息
from scipy import stats
import matplotlib.pyplot as plt
plt.style.use('science') # 设置全局绘图样式

scatter_data = scatter_data = pd.read_excel(r"\第4章 双变量图形的绘制\散点图样例数据2.xlsx")
x = scatter_data["values"]
y = scatter_data["pred values"]
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
# 可视化绘制
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
scatter = ax.scatter(x=x,y=y,s=30,c="k",ec="k",marker='s',label="Original Data")
ax.plot(x, intercept + slope*x, 'r', label='Fitted Line')
ax.set_xlim((-.1, 1.8))
ax.set_ylim((-.1, 1.8))
ax.set_xticks(np.arange(0, 2, step=0.2))
ax.set_yticks(np.arange(0, 2, step=0.2))
ax.set_xlabel("Variable 01")
ax.set_ylabel("Variable 02")
ax.text(0.,1.6,'R = '+str(round(r_value,2)),fontsize=12,fontstyle="italic")
ax.text(0.,1.4,r"$p < $"+str( 0.001),fontsize=12,fontstyle="italic")
ax.legend(loc="lower right",frameon=True)

fig.savefig('\第4章 双变量图形的绘制\4-2-10 正、负相关散点图绘制示例_c.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\4-2-10 正、负相关散点图绘制示例_c.png', 
            bbox_inches='tight',dpi=300)
plt.show()


# d）SciencePlots 负相关散点图绘制示例 # 需安装SciencePlots 包（pip install SciencePlots）,注意最新版本引用方式

import numpy as np
import pandas as pd
# 计算统计信息
from scipy import stats
import matplotlib.pyplot as plt
plt.style.use('science') # 设置全局绘图样式

mtcars = pd.read_excel(r"\第4章 双变量图形的绘制\mtcars.xlsx")

x2 = mtcars["wt"]
y2 = mtcars["mpg"]
slope, intercept, r_value, p_value, std_err = stats.linregress(x2,y2)
# 可视化绘图
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
scatter = ax.scatter(x=x2,y=y2,s=30,c="k",ec="k",marker='s',label="Original Data")
ax.plot(x2, intercept + slope*x2, 'r', label='Fitted Line')
ax.set_xlabel("Variable 01")
ax.set_ylabel("Variable 02")
ax.text(4,28,'R = '+str(round(r_value,2)),fontsize=11,fontstyle="italic")
ax.text(4,25,r"$p < $"+str(0.001),fontsize=11,fontstyle="italic")
ax.legend(loc="upper right",frameon=False)

fig.savefig('\第4章 双变量图形的绘制\4-2-10 正、负相关散点图绘制示例_d.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\4-2-10 正、负相关散点图绘制示例_d.png', 
            bbox_inches='tight',dpi=300)
plt.show()

