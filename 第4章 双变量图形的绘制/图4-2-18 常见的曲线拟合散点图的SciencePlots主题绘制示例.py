
"""
编写时间：2022年4月17日 19：30

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

cure_data = pd.read_excel(r"\第4章 双变量图形的绘制\Curve_Fitting_Methods.xlsx")


# a）LOWESS回归拟合曲线
from moepy import lowess #需要安装moepy库

xdata = cure_data["x"].values
ydata = cure_data["y"].values

# Model fitting
lowess_model = lowess.Lowess()
lowess_model.fit(xdata, ydata)
new_data = np.linspace(min(xdata), max(xdata), 60)
y_pred = lowess_model.predict(new_data)

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
scatter = ax.scatter(xdata,ydata,s=30,c="k",ec="k",label="Original Data")
# 拟合线
lowessreg = ax.plot(new_data,y_pred,color='r',linewidth=1.5,linestyle='-',
                 label=str.upper("LOWESS"))
ax.set_xlabel("Values")
ax.set_ylabel("Estimated Values")
ax.legend(loc="upper left",frameon=True,fontsize=9)

fig.savefig('\第4章 双变量图形的绘制\图4-2-18 常见的曲线拟合散点图的SciencePlots主题绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-2-18 常见的曲线拟合散点图的SciencePlots主题绘制示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# b）Quadratic回归拟合曲线

import scipy.stats as stats
xdata = cure_data["x"].values
ydata = cure_data["y"].values

#polynomial fit with degree = 2
model = np.poly1d(np.polyfit(xdata, ydata, 2))
#add fitted polynomial line to scatterplot
polyline = np.linspace(min(xdata), max(xdata), 60)

#开始绘图
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
scatter = ax.scatter(xdata,ydata,s=30,c="k",ec="k",label="Original Data")
# 拟合线
linreg = ax.plot(polyline,model(polyline),color='r',linewidth=1.5,linestyle='-',label=str.upper("quadratic"))
ax.set_xlabel("Values")
ax.set_ylabel("Estimated Values")
ax.legend(loc="upper left",frameon=True,fontsize=9)

fig.savefig('\第4章 双变量图形的绘制\图4-2-18 常见的曲线拟合散点图的SciencePlots主题绘制示例_b.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-2-18 常见的曲线拟合散点图的SciencePlots主题绘制示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()


# c）Logarithmic回归拟合曲线

xdata = cure_data["x"].values
ydata = cure_data["y"].values

#fit the model
fit_logari = np.polyfit(np.log(xdata), ydata, 1)
#开始绘图
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
scatter = ax.scatter(xdata,ydata,s=30,c="k",ec="k",label="Original Data")
# 拟合线
linreg = ax.plot(polyline,polyline_data,color='r',linewidth=1.5,linestyle='-',
                 label=str.upper("Logarithmic"))
ax.set_xlabel("Values")
ax.set_ylabel("Estimated Values")
ax.legend(loc="upper left",frameon=True,fontsize=9)

fig.savefig('\第4章 双变量图形的绘制\图4-2-18 常见的曲线拟合散点图的SciencePlots主题绘制示例_c.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-2-18 常见的曲线拟合散点图的SciencePlots主题绘制示例_c.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# d）Exponential回归拟合曲线

import lmfit  #需安装lmfit库
import scipy.stats as stats
xdata = cure_data["x"].values
ydata = cure_data["y"].values

#fit the model
expon_fit = np.polyfit(xdata, np.log(ydata), 1)
polyline = np.linspace(min(xdata), max(xdata), 60)
polyline_data = np.exp(expon_fit[0] * polyline + expon_fit[1]

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
scatter = ax.scatter(xdata,ydata,s=30,c="k",ec="k",label="Original Data")
# 拟合线
linreg = ax.plot(polyline,polyline_data,color='r',linewidth=1.5,linestyle='-',
                 label=str.upper("exponential"))
ax.set_xlabel("Values")
ax.set_ylabel("Estimated Values")
ax.legend(loc="upper left",frameon=True,fontsize=9)

fig.savefig('\第4章 双变量图形的绘制\图4-2-18 常见的曲线拟合散点图的SciencePlots主题绘制示例_d.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-2-18 常见的曲线拟合散点图的SciencePlots主题绘制示例_d.png', 
            bbox_inches='tight',dpi=300)
plt.show()


