
"""
编写时间：2022年4月17日 13：30

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

Class_data = pd.read_excel(r"\第4章 双变量图形的绘制\分类相关性散点图.xlsx")

# a）Matplotlib 多类别相关性（误差）散点图绘制

data01_x = Class_data.loc[Class_data["type"]=="class 01","Variable 01"]
data01_y = Class_data.loc[Class_data["type"]=="class 01","Variable 02"]
data02_x = Class_data.loc[Class_data["type"]=="class 02","Variable 01"]
data02_y = Class_data.loc[Class_data["type"]=="class 02","Variable 02"]
data01_err_x = Class_data.loc[Class_data["type"]=="class 01","x_error"]
data01_err_y = Class_data.loc[Class_data["type"]=="class 01","y_error"]
data02_err_x = Class_data.loc[Class_data["type"]=="class 02","x_error"]
data02_err_y = Class_data.loc[Class_data["type"]=="class 02","y_error"]

linregress01 = stats.linregress(data01_x,data01_y)
linregress02 = stats.linregress(data02_x,data02_y)

r_value_01,intercept01,slope01 = linregress01.rvalue,linregress01.intercept,linregress01.slope
r_value_02,intercept02,slope02 = linregress02.rvalue,linregress02.intercept,linregress02.slope

rmse01 = np.sqrt(mean_squared_error(data01_x,data01_y))
rmse02 = np.sqrt(mean_squared_error(data02_x,data02_y))

#绘制1:1 线
best_line_x = np.linspace(-10,10)

#开始绘图
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")

scatter01 = ax.scatter(x=data01_x,y=data01_y,edgecolor="k", c='#459DFF', lw=.8,s=50,label="Data One")
scatter02 = ax.scatter(x=data02_x,y=data02_y,edgecolor="k", c='#FFCC37', lw=.8,s=50,label="Data Two")

bestline = ax.plot(best_line_x,best_line_y,color='gray',linewidth=1,linestyle='--',label="1:1 Line")
# 添加误差
errorbar_one = ax.errorbar(data01_x,data01_y,xerr=data01_err_x,yerr=data01_err_y,ecolor="#459DFF", 
                           elinewidth=.4,capsize=0,alpha=.8,linestyle="",mfc="none",mec="none",zorder=-1)
errorbar_one = ax.errorbar(data02_x,data02_y,xerr=data02_err_x,yerr=data02_err_y,ecolor="#FFCC37", 
                           elinewidth=.4,capsize=0,alpha=.8,linestyle="",mfc="none",mec="none",zorder=-1)
ax.set_xlim((-.1, 1.8))
ax.set_ylim((-.1, 1.8))
ax.set_xticks(np.arange(0, 2, step=0.2))
ax.set_yticks(np.arange(0, 2, step=0.2))

# 添加文本信息
fontdict = {"size":12,"fontstyle":"italic","weight":"bold"}
ax.text(0.0,1.6,r'$R_1=$'+str(round(r_value_01,2)),c="#459DFF",fontdict=fontdict)
ax.text(0.0,1.4,r'$R_2=$'+str(round(r_value_02,2)),c="#FFCC37",fontdict=fontdict)
ax.text(0.0,1.2,r'$y_1=$'+str(round(slope01,3))+'$x_1$'+"+"+str(round(intercept01,3)),c="#459DFF",
        fontdict=fontdict)
ax.text(0.,1.,r'$y_2=$'+str(round(slope02,3))+'$x_2$'+"+"+str(round(intercept02,3)),c="#FFCC37",
        fontdict=fontdict)
ax.set_xlabel("Variable 01")
ax.set_ylabel("Variable 02")

fig.savefig('\第4章 双变量图形的绘制\图4-2-12 多类别相关性（误差）散点图绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-2-12 多类别相关性（误差）散点图绘制示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# b）ScienePlots 多类别相关性（误差）散点图绘制 # 需安装SciencePlots 包（pip install SciencePlots）,注意最新版本引用方式

plt.style.use('science') # 设置全局绘图样式

Class_data = pd.read_excel(r"G:\书籍编写\Python-学术图表手册\双变量图表绘制\分类相关性散点图.xlsx")
data01_x = Class_data.loc[Class_data["type"]=="class 01","Variable 01"]
data01_y = Class_data.loc[Class_data["type"]=="class 01","Variable 02"]
data02_x = Class_data.loc[Class_data["type"]=="class 02","Variable 01"]
data02_y = Class_data.loc[Class_data["type"]=="class 02","Variable 02"]
data01_err_x = Class_data.loc[Class_data["type"]=="class 01","x_error"]
data01_err_y = Class_data.loc[Class_data["type"]=="class 01","y_error"]
data02_err_x = Class_data.loc[Class_data["type"]=="class 02","x_error"]
data02_err_y = Class_data.loc[Class_data["type"]=="class 02","y_error"]

linregress01 = stats.linregress(data01_x,data01_y)
linregress02 = stats.linregress(data02_x,data02_y)

r_value_01,intercept01,slope01 = linregress01.rvalue,linregress01.intercept,linregress01.slope
r_value_02,intercept02,slope02 = linregress02.rvalue,linregress02.intercept,linregress02.slope

rmse01 = np.sqrt(mean_squared_error(data01_x,data01_y))
rmse02 = np.sqrt(mean_squared_error(data02_x,data02_y))
#绘制1:1 线
best_line_x = np.linspace(-10,10)
best_line_y=best_line_x

#开始绘图
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")

scatter01 = ax.scatter(x=data01_x,y=data01_y,edgecolor="k", c='#459DFF', lw=.8,s=50,label="Data One")
scatter02 = ax.scatter(x=data02_x,y=data02_y,edgecolor="k", c='#FFCC37', lw=.8,s=50,label="Data Two")

bestline = ax.plot(best_line_x,best_line_y,color='gray',linewidth=1,linestyle='--',label="1:1 Line")
# 添加误差
errorbar_one = ax.errorbar(data01_x,data01_y,xerr=data01_err_x,yerr=data01_err_y,ecolor="#459DFF", 
                           elinewidth=.4,capsize=0,alpha=.8,linestyle="",mfc="none",mec="none",zorder=-1)
errorbar_one = ax.errorbar(data02_x,data02_y,xerr=data02_err_x,yerr=data02_err_y,ecolor="#FFCC37", 
                           elinewidth=.4,capsize=0,alpha=.8,linestyle="",mfc="none",mec="none",zorder=-1)
ax.set_xlim((-.1, 1.8))
ax.set_ylim((-.1, 1.8))
ax.set_xticks(np.arange(0, 2, step=0.2))
ax.set_yticks(np.arange(0, 2, step=0.2))

# 添加文本信息
fontdict = {"size":12,"fontstyle":"italic","weight":"bold"}
ax.text(0.0,1.6,r'$R_1=$'+str(round(r_value_01,2)),c="#459DFF",fontdict=fontdict)
ax.text(0.0,1.4,r'$R_2=$'+str(round(r_value_02,2)),c="#FFCC37",fontdict=fontdict)
ax.text(0.0,1.2,r'$y_1=$'+str(round(slope01,3))+'$x_1$'+"+"+str(round(intercept01,3)),c="#459DFF",
        fontdict=fontdict)
ax.text(0.,1.,r'$y_2=$'+str(round(slope02,3))+'$x_2$'+"+"+str(round(intercept02,3)),c="#FFCC37",
        fontdict=fontdict)
ax.set_xlabel("Variable 01")
ax.set_ylabel("Variable 02")

fig.savefig('\第4章 双变量图形的绘制\图4-2-12 多类别相关性（误差）散点图绘制示例_b.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-2-12 多类别相关性（误差）散点图绘制示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()


