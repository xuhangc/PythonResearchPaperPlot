
"""
编写时间：2022年4月16日 15：30

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

"""
此代码为使用Python-Prolot包进行学术风格图表绘制，绘图语法和Matplotlib有所不同，需注意。
"""

import numpy as np
import pandas as pd
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

area_data = pd.read_excel(r"\第4章 双变量图形的绘制\面积图构建.xlsx")
time = area_data["day"].values
area_a = area_data["Area_a"].values
area_b = area_data["Area_b"].values


# a）Matplotlib 面积图绘制示例

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
ax.plot(time,area_a,color="#868686",lw=.5,)
ax.fill_between(time,area_a,color="#868686",hatch="///",alpha=.3,label ="Area_a")
ax.plot(time,area_b,color="#CD534C",lw=.5,)
ax.fill_between(time,area_b,color="#CD534C",hatch="///",alpha=.3,label ="Area_b")
ax.set_xlabel("Day")
ax.set_ylabel("Values")
ax.set_ylim(0,10)
ax.legend(frameon=False,loc="upper left")

fig.savefig('\第4章 双变量图形的绘制\图4-2-5 面积图插值前后绘制示例对比_a.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-2-5 面积图插值前后绘制示例对比_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()


# b）Matplotlib 面积图（插值）绘制示例
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
    ax.fill_between(xnew,ynew,color=color,hatch="///",alpha=.3,label="Interpolated "+select)
    
    #ax.grid(which="major",ls="--",lw=.8,zorder=0)
    ax.set_xlabel("Day")
    ax.set_ylabel("Interpolated Values")
    ax.set_ylim(0,10)
    ax.legend(frameon=False,loc="upper left")

fig.savefig('\第4章 双变量图形的绘制\图4-2-5 面积图插值前后绘制示例对比_b.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-2-5 面积图插值前后绘制示例对比_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()
