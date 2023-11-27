"""
编写时间：2022年4月17日 11：00

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

# a）Matplotlib 相关性散点图完善示例


from scipy import stats

x = scatter_data["values"]
y = scatter_data["pred values"]
z = scatter_data["3_value"].values
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
slope, intercept, r_value, p_value, std_err

#绘制最佳拟合线
best_line_x = np.linspace(-10,10)
best_line_y=best_line_x
#绘制拟合线
y3 = slope*x + intercept

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
scatter = ax.scatter(x=x,y=y,edgecolor=None, c='k', s=13,marker='s',label="Data")
bestline = ax.plot(best_line_x,best_line_y,color='k',linewidth=1.5,linestyle='--',label="1:1 Line")
linreg = ax.plot(x,y3,color='r',linewidth=1.5,linestyle='-',label="Fitted Line")
ax.set_xlim((-.1, 1.8))
ax.set_ylim((-.1, 1.8))
ax.set_xticks(np.arange(0, 2, step=0.2))
ax.set_yticks(np.arange(0, 2, step=0.2))

# 添加文本信息
fontdict = {"size":13,"fontstyle":"italic"}
ax.text(0.,1.6,r'$R=$'+str(round(r_value,2)),fontdict=fontdict)
ax.text(0.,1.4,"P < "+str(0.001),fontdict=fontdict)
ax.text(0.,1.2,r'$y=$'+str(round(slope,3))+'$x$'+" + "+str(round(intercept,3)),fontdict=fontdict)
ax.text(0.,1.0,r'$N=$'+ str(len(x)),fontdict=fontdict)

ax.set_xlabel("Variable 01")
ax.set_ylabel("Variable 02")
ax.legend(loc="lower right")

fig.savefig('\第4章 双变量图形的绘制\图4-2-11 相关性（误差）散点图完善绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-2-11 相关性（误差）散点图完善绘制示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()


# b）Matplotlib 相关性（误差）散点图绘制示例

data_err = pd.read_excel(r"\第4章 双变量图形的绘制\散点图样例数据2.xlsx",sheet_name="data02")
x = data_err["values"]
y = data_err["pred values"]
#绘制最佳拟合线
best_line_x = np.linspace(-10,10)
best_line_y=best_line_x
#绘制拟合线
y3 = slope*x + intercept

x = data_err["values"]
y = data_err["pred values"]
x_err = data_err["x_error"]
y_err = data_err["y_error"]
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)

#开始绘图
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
scatter = ax.scatter(x=x,y=y,edgecolor=None, c='k', s=18,label="Data")
bestline = ax.plot(best_line_x,best_line_y,color='k',linewidth=1.5,linestyle='--',label="1:1 Line")
linreg = ax.plot(x,y3,color='r',linewidth=1.5,linestyle='-',label="Fitted Line")
# 添加误差
errorbar = ax.errorbar(x,y,xerr=x_err,yerr=y_err,ecolor="k", elinewidth=.4,capsize=0,alpha=.7,
            linestyle="",mfc="none",mec="none",zorder=-1)

ax.set_xlim((-.1, 1.8))
ax.set_ylim((-.1, 1.8))
ax.set_xticks(np.arange(0, 2, step=0.2))
ax.set_yticks(np.arange(0, 2, step=0.2))

# 添加文本信息

fontdict = {"size":13,"fontstyle":"italic"}
ax.text(0.,1.6,r'$R=$'+str(round(r_value,2)),fontdict=fontdict)
ax.text(0.,1.4,"P < "+str(0.001),fontdict=fontdict)
ax.text(0.,1.2,r'$y=$'+str(round(slope,3))+'$x$'+" + "+str(round(intercept,3)),fontdict=fontdict)
ax.text(0.,1.0,r'$N=$'+ str(len(x)),fontdict=fontdict)

ax.set_xlabel("Variable 01")
ax.set_ylabel("Variable 02")
ax.legend(loc="lower right")

fig.savefig('\第4章 双变量图形的绘制\图4-2-11 相关性（误差）散点图完善绘制示例_b.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-2-11 相关性（误差）散点图完善绘制示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()


# c）SciencePlots 相关性散点图完善示例 # 需安装SciencePlots 包（pip install SciencePlots）,注意最新版本引用方式

from scipy import stats
import numpy as np
from sklearn.metrics import mean_squared_error

plt.style.use('science') # 设置全局绘图样式

x = scatter_data["values"]
y = scatter_data["pred values"]
z = scatter_data["3_value"].values
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
#绘制1：1线
best_line_x = np.linspace(-10,10)
best_line_y=best_line_x
# 拟合线
y3 = slope*x + intercept
# RMSE
rmse = round(np.sqrt(mean_squared_error(x,y)),3)

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
scatter = ax.scatter(x=x,y=y,edgecolor=None, c='k', s=13,marker='s',label="Data")
bestline = ax.plot(best_line_x,best_line_y,color='k',linewidth=1.5,linestyle='--',label="1:1 Line")
linreg = ax.plot(x,y3,color='r',linewidth=1.5,linestyle='-',label="Fitted Line")
ax.set_xlim((-.1, 1.8))
ax.set_ylim((-.1, 1.8))
ax.set_xticks(np.arange(0, 2, step=0.2))
ax.set_yticks(np.arange(0, 2, step=0.2))

# 添加文本信息
fontdict = {"size":13,"fontstyle":"italic"}
ax.text(0.,1.6,r'$R=$'+str(round(r_value,2)),fontdict=fontdict)
ax.text(0.,1.4,"$P <$ "+str(0.001),fontdict=fontdict)
ax.text(0.,1.2,r'$y=$'+str(round(slope,3))+'$x$'+" + "+str(round(intercept,3)),fontdict=fontdict)
ax.text(0.,1.0,r'$N=$'+ str(len(x)),fontdict=fontdict)

ax.set_xlabel("Variable 01")
ax.set_ylabel("Variable 02")
ax.legend(loc="lower right",frameon=True)

fig.savefig('\第4章 双变量图形的绘制\图4-2-11 相关性（误差）散点图完善绘制示例_c.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-2-11 相关性（误差）散点图完善绘制示例_c.png', 
            bbox_inches='tight',dpi=300)
plt.show()


# d）SciencePlots 相关性（误差）散点图绘制示例

plt.style.use('science') # 设置全局绘图样式

data_err = pd.read_excel(r"\第4章 双变量图形的绘制\散点图样例数据2.xlsx",sheet_name="data02")

x = data_err["values"]
y = data_err["pred values"]
x_err = data_err["x_error"]
y_err = data_err["y_error"]
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
rmse = np.sqrt(mean_squared_error(x,y))
#绘制1:1拟合线
best_line_x = np.linspace(-10,10)
best_line_y=best_line_x
#绘制拟合线
y3 = slope*x + intercept
#开始绘图
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
scatter = ax.scatter(x=x,y=y,edgecolor=None, c='k', s=18,label="Data")
bestline = ax.plot(best_line_x,best_line_y,color='k',linewidth=1.5,linestyle='--',label="1:1 Line")
linreg = ax.plot(x,y3,color='r',linewidth=1.5,linestyle='-',label="Fitted Line")
# 添加误差
errorbar = ax.errorbar(x,y,xerr=x_err,yerr=y_err,ecolor="k", elinewidth=.4,capsize=0,alpha=.7,
            linestyle="",mfc="none",mec="none",zorder=-1)
ax.set_xlim((-.1, 1.8))
ax.set_ylim((-.1, 1.8))
ax.set_xticks(np.arange(0, 2, step=0.2))
ax.set_yticks(np.arange(0, 2, step=0.2))
# 添加文本信息
fontdict = {"size":13,"fontstyle":"italic"}
ax.text(0.,1.6,r'$R=$'+str(round(r_value,2)),fontdict=fontdict)
ax.text(0.,1.4,"$P <$ "+str(0.001),fontdict=fontdict)
ax.text(0.,1.2,r'$y=$'+str(round(slope,3))+'$x$'+" + "+str(round(intercept,3)),fontdict=fontdict)
ax.text(0.,1.0,r'$N=$'+ str(len(x)),fontdict=fontdict)

ax.set_xlabel("Variable 01")
ax.set_ylabel("Variable 02")
ax.legend(loc="lower right",frameon=True)

fig.savefig('\第4章 双变量图形的绘制\图4-2-11 相关性（误差）散点图完善绘制示例_d.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-2-11 相关性（误差）散点图完善绘制示例_d.png', 
            bbox_inches='tight',dpi=300)
plt.show()



