
"""
编写时间：2022年4月17日 17：30

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

"""
此代码为使用Python-Prolot包进行学术风格图表绘制，绘图语法和Matplotlib有所不同，需注意。
"""

import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats
import matplotlib.pyplot as plt
from colormaps import parula

# 需安装SciencePlots 包（pip install SciencePlots）,注意最新版本引用方式
plt.style.use('science') # 设置全局绘图样式

regre_data = pd.read_excel(r"\第4章 双变量图形的绘制\线性回归样例数据.xlsx")

from scipy import stats
import numpy as np
from sklearn.metrics import mean_squared_error

x = regre_data["values"]
y = regre_data["pred values"]
z = regre_data["3_value"].values
x_err = regre_data["x_error"]
y_err = regre_data["y_error"]
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)

#绘制最佳拟合线
best_line_x = np.linspace(-10,10)
best_line_y=best_line_x
#绘制拟合线
y3 = slope*x + intercept

# a）基本线性回归散点图示例
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
scatter = ax.scatter(x=x,y=y,edgecolor=None, c='k', marker="s",s=18,label="Data")
bestline = ax.plot(best_line_x,best_line_y,color='k',linewidth=1.5,linestyle='--',label="1:1 Line")
linreg = ax.plot(x,y3,color='r',linewidth=1.5,linestyle='-',label="Fitted Line")
ax.set_xlim((-.1, 1.8))
ax.set_ylim((-.1, 1.8))
ax.set_xticks(np.arange(0, 2, step=0.2))
ax.set_yticks(np.arange(0, 2, step=0.2))
ax.set_xlabel("Values")
ax.set_ylabel("Estimated Values")
ax.text(0.,1.6,'$R^2$ = '+str(round(r_value**2,2)),fontsize=12,fontstyle="italic")
ax.text(0.,1.4,r"$RMSE$ = "+str(rmse),fontsize=12,fontstyle="italic")
ax.text(0.,1.2,r'$y=$'+str(round(slope,3))+'$x$'+" + "+str(round(intercept,3)),fontsize=12,fontstyle="italic")
ax.text(0.,1.0,r'$N=$'+ str(len(x)),fontsize=12,fontstyle="italic")
ax.legend(loc="lower right",frameon=True)

fig.savefig('\第4章 双变量图形的绘制\图4-2-17 线性回归散点图的SciencePlots主题绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-2-17 线性回归散点图的SciencePlots主题绘制示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# b）基本线性回归误差散点图示例
x_err = regre_data["x_error"]
y_err = regre_data["y_error"]

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
scatter = ax.scatter(x=x,y=y,edgecolor=None, c='k',marker="s",s=18,label="Data")
# 添加误差
errorbar = ax.errorbar(x,y,xerr=x_err,yerr=y_err,ecolor="k", elinewidth=.4,capsize=0,alpha=.7,
            linestyle="",mfc="none",mec="none",zorder=-1,label="Error Line")

bestline = ax.plot(best_line_x,best_line_y,color='k',linewidth=1.5,linestyle='--',label="1:1 Line")
linreg = ax.plot(x,y3,color='r',linewidth=1.5,linestyle='-',label="Fitted Line")
ax.set_xlim((-.1, 1.8))
ax.set_ylim((-.1, 1.8))
ax.set_xticks(np.arange(0, 2, step=0.2))
ax.set_yticks(np.arange(0, 2, step=0.2))
ax.set_xlabel("Values")
ax.set_ylabel("Estimated Values")
ax.text(0.,1.6,'$R^2$ = '+str(round(r_value**2,2)),fontsize=12,fontstyle="italic")
ax.text(0.,1.4,r"$RMSE$ = "+str(rmse),fontsize=12,fontstyle="italic")
ax.text(0.,1.2,r'$y=$'+str(round(slope,3))+'$x$'+" + "+str(round(intercept,3)),fontsize=12,fontstyle="italic")
ax.text(0.,1.0,r'$N=$'+ str(len(x)),fontsize=12,fontstyle="italic")
ax.legend(loc="lower right",frameon=True)

fig.savefig('\第4章 双变量图形的绘制\图4-2-17 线性回归散点图的SciencePlots主题绘制示例_b.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-2-17 线性回归散点图的SciencePlots主题绘制示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# c）带置信区间和预测区间的线性回归散点图示例一

import statsmodels.api as sm
lm_fit = sm.OLS(y, x).fit()
dt = lm_fit.get_prediction(x).summary_frame(alpha = 0.05)
y_prd = dt['mean']
y_fit = dt['mean']
yprd_ci_lower = dt['obs_ci_lower']
yprd_ci_upper = dt['obs_ci_upper']
ym_ci_lower = dt['mean_ci_lower'] 
ym_ci_upper = dt['mean_ci_upper']

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
scatter = ax.scatter(x=x,y=y,edgecolor=None, c='k', s=12,marker='s',label="Data")
bestline = ax.plot(best_line_x,best_line_y,color='k',linewidth=1.5,linestyle='--',label="1:1 Line")
linreg = ax.plot(x,y3,color='r',linewidth=1.5,linestyle='-',label="Fit Curve")

ax.plot(x, yprd_ci_lower, color = "blue", linewidth=.8,linestyle = "--",label="95\% Prediction Interval")
ax.plot(x, yprd_ci_upper, color = "blue", linewidth=.8,linestyle = "--")
ax.plot(x, ym_ci_lower, color = "darkgreen", linewidth=.8,linestyle = "--", label = "95\% Confidence Interval")
ax.plot(x, ym_ci_upper, color = "darkgreen", linewidth=.8,linestyle = "--")

ax.set_xlim((-.1, 1.8))
ax.set_ylim((-.1, 1.8))
ax.set_xticks(np.arange(0, 2, step=0.2))
ax.set_yticks(np.arange(0, 2, step=0.2))
ax.set_xlabel("Values")
ax.set_ylabel("Estimated Values")
ax.text(1.1,0.2,'$R^2$ = '+str(round(r_value**2,2)),fontsize=11,fontstyle="italic")
ax.text(1.1,0.05,r"$RMSE$ = "+str(rmse),fontsize=11,fontstyle="italic")
ax.legend(loc="upper left",frameon=False,labelspacing=.4,handletextpad=.5,fontsize=9.5)

fig.savefig('\第4章 双变量图形的绘制\图4-2-17 线性回归散点图的SciencePlots主题绘制示例_c.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-2-17 线性回归散点图的SciencePlots主题绘制示例_c.png', 
            bbox_inches='tight',dpi=300)
plt.show()


# d）带置信区间和预测区间的线性回归散点图示例二

import statsmodels.api as sm
lm_fit = sm.OLS(y,x).fit()
# 计算95%置信区间
dt = lm_fit.get_prediction(x).summary_frame(alpha = 0.05)

y_fit = dt['mean']
yprd_ci_lower = dt['obs_ci_lower']
yprd_ci_upper = dt['obs_ci_upper']
ym_ci_lower = dt['mean_ci_lower'] 
ym_ci_upper = dt['mean_ci_upper']

#开始绘图
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
scatter = ax.scatter(x=x,y=y,edgecolor=None, c='k',marker="s",s=18,label="Data")
bestline = ax.plot(best_line_x,best_line_y,color='k',linewidth=1.5,linestyle='--',label="1:1 Line")
# 拟合线
linreg = ax.plot(x,y_fit,color='r',linewidth=1.5,linestyle='-',label="Regression Line")
#区间填充
ax.fill_between(x, yprd_ci_lower, yprd_ci_upper,color="gray",lw=.01,alpha=.1, label='95\% Prediction interval')
ax.fill_between(x, ym_ci_lower, ym_ci_upper, color="r",lw=.01,alpha=.2, label='95\% Confidence interval')
ax.set_xlim((-.1, 1.8))
ax.set_ylim((-.1, 1.8))
ax.set_xticks(np.arange(0, 2, step=0.2))
ax.set_yticks(np.arange(0, 2, step=0.2))
ax.set_xlabel("Values")
ax.set_ylabel("Estimated Values")
ax.text(1.1,0.2,'$R^2$ = '+str(round(r_value**2,2)),fontsize=11,fontstyle="italic")
ax.text(1.1,0.05,r"$RMSE$ = "+str(rmse),fontsize=11,fontstyle="italic")
ax.legend(loc="upper left",frameon=False,fontsize=9)

fig.savefig('\第4章 双变量图形的绘制\图4-2-17 线性回归散点图的SciencePlots主题绘制示例_d.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-2-17 线性回归散点图的SciencePlots主题绘制示例_d.png', 
            bbox_inches='tight',dpi=300)
plt.show()


