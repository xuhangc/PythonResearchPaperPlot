
"""
编写时间：2022年4月16日 16：00

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

"""
此代码为使用Python-Prolot包进行学术风格图表绘制，绘图语法和Matplotlib有所不同，需注意。
"""


#**********************图4-2-7 利用ProPlot绘制的面积图系列*****************************
import numpy as np
import pandas as pd
import proplot as pplt
from scipy import interpolate
import matplotlib.pyplot as plt

from proplot import rc
rc["axes.labelsize"] = 15
rc['tick.labelsize'] = 12
rc["suptitle.size"] = 15

area_data = pd.read_excel(r"\第4章 双变量图形的绘制\面积图构建.xlsx")
area_data2 = pd.read_excel(r"\第4章 双变量图形的绘制\交叉面积图构建.xlsx")


# a）面积图
time = area_data["day"].values
area_a = area_data["Area_a"].values
area_b = area_data["Area_b"].values

fig,ax = pplt.subplots(figsize=(3.5,3))
ax.format(xlabel='Day', ylabel='Values',
          xlim=(-2,40),ylim=(0,10))

ax.plot(time,area_a,color="#868686",lw=.5,)
ax.fill_between(time,area_a,color="#868686",hatch="///",alpha=.3,label ="Area_a")
ax.plot(time,area_b,color="#CD534C",lw=.5,)
ax.fill_between(time,area_b,color="#CD534C",hatch="///",alpha=.3,label ="Area_b")
ax.set_xlabel("Day")
ax.set_ylabel("Values")
ax.set_ylim(0,10)
ax.legend(ncols=1,frameon=False,loc='ul')

fig.savefig('\第4章 双变量图形的绘制\图4-2-7 利用ProPlot绘制的面积图系列_a.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-2-7 利用ProPlot绘制的面积图系列_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# b）插值后的面积图

from scipy import interpolate
data_select = ["Area_a","Area_b"]
colors = ["#868686","#CD534C"]
day = area_data["day"].values

fig,ax = pplt.subplots(figsize=(3.5,3))
ax.format(xlabel='Day', ylabel='Interpolated Values',
          xlim=(-2,40),ylim=(0,10))
for select,color in zip(data_select,colors):
    #计算插值
    x,y = day,area_data[select].values
    f = interpolate.interp1d(x, y,kind="quadratic")
    xnew = np.linspace(min(x),max(x),101)
    ynew = f(xnew)
    # 可视化绘制
    ax.plot(xnew,ynew,color=color,lw=.5)
    ax.fill_between(xnew,ynew,color=color,hatch="///",alpha=.3,label="Interpolated "+select)
    ax.legend(ncols=1,frameon=False,loc="ul")
    
fig.savefig('\第4章 双变量图形的绘制\图4-2-7 利用ProPlot绘制的面积图系列_b.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-2-7 利用ProPlot绘制的面积图系列_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()   


# c）交叉面积图

from scipy import interpolate
day = area_data2["day"].values
#计算插值(两组)
x,a,b = day,area_data2["Area_a"].values,area_data2["Area_b"].values
f_a = interpolate.interp1d(x, a,kind="quadratic")
f_b = interpolate.interp1d(x, b,kind="quadratic")
xnew = np.linspace(min(x),max(x),101)
a_new = f_a(xnew)
b_new = f_b(xnew)

fig,ax = pplt.subplots(figsize=(3.5,3))
ax.format(xlabel='Day', ylabel='Interpolated Values',
          xlim=(0,11),ylim=(0,40))

ax.plot(xnew,a_new,color="#868686",lw=.5,ls="--",label="Area_a")
ax.plot(xnew,b_new,color="#CD534C",lw=.5,label="Area_b")
ax.fill_between(xnew,a_new,b_new,where=(a_new > b_new),
                color="#868686",hatch="///",alpha=.3,label="Area_a is Better")
ax.fill_between(xnew,a_new,b_new,where=(a_new <= b_new),
                color="#CD534C",hatch="///",alpha=.3,label="Area_b is Better")
ax.legend(ncols=1,frameon=False,loc="ul")
fig.savefig('\第4章 双变量图形的绘制\图4-2-7 利用ProPlot绘制的面积图系列_c.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-2-7 利用ProPlot绘制的面积图系列_c.png', 
            bbox_inches='tight',dpi=300)
plt.show() 

#**********************图4-2-8 利用SciencePlots绘制的面积图系列*****************************
# 需安装SciencePlots 包（pip install SciencePlots）,注意最新版本引用方式

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('science') # 设置全局绘图样式

# a）面积图

time = area_data["day"].values
area_a = area_data["Area_a"].values
area_b = area_data["Area_b"].values
    
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
ax.plot(time,area_a,color="#868686",lw=.5,)
ax.fill_between(time,area_a,color="#868686",hatch="///",alpha=.3,label ="Area a")
ax.plot(time,area_b,color="#CD534C",lw=.5,)
ax.fill_between(time,area_b,color="#CD534C",hatch="///",alpha=.3,label ="Area b")
ax.set_xlabel("Day")
ax.set_ylabel("Values")
ax.set_ylim(0,10)
ax.legend(frameon=False,loc="upper left")

fig.savefig('\第4章 双变量图形的绘制\图4-2-8 利用SciencePlots绘制的面积图系列_a.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-2-8 利用SciencePlots绘制的面积图系列_a.png', 
            bbox_inches='tight',dpi=300)
plt.show() 


# b）插值后的面积图插值
from scipy import interpolate

data_select = ["Area_a","Area_b"]
colors = ["#868686","#CD534C"]
day = area_data["day"].values

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
for select,color in zip(data_select,colors):
     #计算插值
     x,y = day,area_data[select].values
     f = interpolate.interp1d(x, y,kind="quadratic")
     xnew = np.linspace(min(x),max(x),101)
     ynew = f(xnew)
     # 可视化绘制
     ax.plot(xnew,ynew,color=color,lw=.5)
     ax.fill_between(xnew,ynew,color=color,hatch="///",alpha=.3,
                     label="Interpolated "+select.split("_")[-1])
     ax.set_xlabel("Day")
     ax.set_ylabel("Interpolated Values")
     ax.set_ylim(0,10)
     ax.legend(frameon=False,loc="upper left")
fig.savefig('\第4章 双变量图形的绘制\图4-2-8 利用SciencePlots绘制的面积图系列_b.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-2-8 利用SciencePlots绘制的面积图系列_b.png', 
            bbox_inches='tight',dpi=300)
plt.show() 


#  c）交叉面积图

#计算插值
x,a,b = day,area_data2["Area_a"].values,area_data2["Area_b"].values
f_a = interpolate.interp1d(x, a,kind="quadratic")
f_b = interpolate.interp1d(x, b,kind="quadratic")
xnew = np.linspace(min(x),max(x),101)
a_new = f_a(xnew)
b_new = f_b(xnew)

# 可视化绘制
fig,ax = plt.subplots(figsize=(5,3.5),dpi=100,facecolor="w")
ax.plot(xnew,a_new,color="#868686",lw=.5,ls="--",label="Area a")
ax.plot(xnew,b_new,color="#CD534C",lw=.5,label="Area b")
ax.fill_between(xnew,a_new,b_new,where=(a_new > b_new),
                color="#868686",hatch="///",alpha=.3,label="Area a is Better")
ax.fill_between(xnew,a_new,b_new,where=(a_new <= b_new),
                color="#CD534C",hatch="///",alpha=.3,label="Area b is Better")
ax.set_ylim(0,40)
ax.set_xlabel("Day")
ax.set_ylabel("Interpolated Values")
ax.legend(frameon=False,loc="upper left")

fig.savefig('\第4章 双变量图形的绘制\图4-2-8 利用SciencePlots绘制的面积图系列_c.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-2-8 利用SciencePlots绘制的面积图系列_c.png', 
            bbox_inches='tight',dpi=300)
plt.show() 





