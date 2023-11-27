
"""
编写时间：2022年4月16日 15：30

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

"""
此代码为使用Python-Prolot包进行学术风格图表绘制，绘图语法和Matplotlib有所不同，需注意。
"""

import numpy as np
import pandas as pd
from scipy import interpolate
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


area_data2 = pd.read_excel(r"\第4章 双变量图形的绘制\交叉面积图构建.xlsx")

day = area_data2["day"].values
#计算插值
x,a,b = day,area_data2["Area_a"].values,area_data2["Area_b"].values
f_a = interpolate.interp1d(x, a,kind="quadratic")
f_b = interpolate.interp1d(x, b,kind="quadratic")
xnew = np.linspace(min(x),max(x),101)
a_new = f_a(xnew)
b_new = f_b(xnew)

# 可视化绘制
fig,ax = plt.subplots(figsize=(5,3.5),dpi=100,facecolor="w")
ax.plot(xnew,a_new,color="#868686",lw=.5,ls="--",label="Area_a")
ax.plot(xnew,b_new,color="#CD534C",lw=.5,label="Area_b")
ax.fill_between(xnew,a_new,b_new,where=(a_new > b_new),
                color="#868686",hatch="///",alpha=.3,label="Area_a is Better")
ax.fill_between(xnew,a_new,b_new,where=(a_new <= b_new),
                color="#CD534C",hatch="///",alpha=.3,label="Area_b is Better")

ax.set_xlabel("Day")
ax.set_ylabel("Interpolated Values")
ax.set_ylim(0,10)
ax.set_ylim(0,40)
ax.legend(frameon=False,loc="upper left")

fig.savefig('\第4章 双变量图形的绘制\图4-2-6 利用Matplotlib绘制的交叉面积图示例.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-2-6 利用Matplotlib绘制的交叉面积图示例.png', 
            bbox_inches='tight',dpi=300)
plt.show()