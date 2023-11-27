"""
编写时间：2022年2月06日 09：30

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。

代码中Proplot包绘制的部分可能与Matplotlib绘制不同，需注意两者绘图语法的不同~~

"""
#注意：本案例中引入的SciencePlots库主题方式会随着SciencePlots版本的更新发生改变，读者还需参考其官网引入的正确方式。
#      建议按照官网引入方式进行操作和使用最新版本的ScienePlots。如引入方式发生改变，请关注微信公众号【DataCharm】进行实时获取代码更新。


import numpy as np
import pandas as pd

hist_data = pd.read_csv(r"第3章 单变量图形的绘制\直方图绘制02.xlsx")

hist_x_data = hist_data02["hist_data"].values
X_mean = np.mean(hist_x_data)


# 图3-2-2 带统计信息的直方图绘制示例
from scipy.stats import norm
import matplotlib.pyplot as plt

bins=15
hist_x_data = hist_data02["hist_data"].values

Median = np.median(hist_x_data)

mu, std = norm.fit(hist_x_data)

fig,ax = plt.subplots(figsize=(5,3.5),dpi=100,facecolor="w")
hist = ax.hist(x=hist_x_data, bins=bins,color="gray",
               edgecolor ='black',lw=.5)
# Plot the PDF.
xmin, xmax = min(hist_x_data),max(hist_x_data)
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)
N = len(hist_x_data)
bin_width = (x.max() - x.min()) / bins
ax.plot(x, p*N*bin_width,linewidth=1,color="r",label="Normal Distribution Curve")

# 添加平均值线
ax.axvline(x=Median,ls="--",lw=1.2,color="b",label="Median Line")
ax.set_xlabel('Values')
ax.set_ylabel('Count')
ax.legend(frameon=False)

plt.savefig('\第3章 单变量图形的绘制\图3-2-2 带统计信息的直方图绘制示例.png', 
         bbox_inches='tight',dpi=600)
plt.savefig('\第3章 单变量图形的绘制\图3-2-2 带统计信息的直方图绘制示例.pdf', 
         bbox_inches='tight') 
plt.show()

# 图3-2-3 使用ProPlot和SciencePlots绘制的带统计信息的直方图示例

# (a)使用ProPlot绘制的带统计信息的直方图示例
from scipy.stats import norm
from proplot import rc

rc["axes.labelsize"] = 15
rc['tick.labelsize'] = 12
rc["suptitle.size"] = 15


bins=15
hist_x_data = hist_data["hist_data"].values
Median = np.median(hist_x_data)
mu, std = norm.fit(hist_x_data)

fig = pplt.figure(figsize=(3.5,3))
ax = fig.subplot()
ax.format(abc='a.', abcloc='ur',abcsize=16,
          xlabel='Values', ylabel='Count')

hist = ax.hist(x=hist_x_data, bins=bins,color="gray",
               edgecolor ='black',lw=.5)
# Plot the PDF.
xmin, xmax = min(hist_x_data),max(hist_x_data)
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)
N = len(hist_x_data)
bin_width = (x.max() - x.min()) / bins
ax.plot(x, p*N*bin_width,linewidth=1,color="r",label="Normal Distribution Curve")
# 添加平均值线
ax.axvline(x=Median,ls="--",lw=1.2,color="b",label="Median Line")
ax.legend(ncols=1,frameon=False,loc="ur")
fig.savefig('\第3章 单变量图形的绘制\图3-2-3 使用ProPlot和SciencePlots绘制的带统计信息的直方图示例_a.pdf')
fig.savefig('\第3章 单变量图形的绘制\图3-2-3 使用ProPlot和SciencePlots绘制的带统计信息的直方图示例_a.png')
plt.show()

# (b)使用SciencePlots 绘制的带统计信息的直方图示例

from scipy.stats import norm

bins=15
hist_x_data = hist_data["hist_data"].values
Median = np.median(hist_x_data)
mu, std = norm.fit(hist_x_data)
xmin, xmax = min(hist_x_data),max(hist_x_data)
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)
N = len(hist_x_data)
bin_width = (x.max() - x.min()) / bins

with plt.style.context(['science']):
    fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
    hist = ax.hist(x=hist_x_data, bins=bins,color="gray",
                   edgecolor ='black',lw=.5)
    ax.plot(x, p*N*bin_width,linewidth=1,color="r",label="Normal Distribution Curve")

    # 添加平均值线
    ax.axvline(x=Median,ls="--",lw=1.2,color="b",label="Median Line")
    ax.set_xlabel('Values')
    ax.set_ylabel('Count')
    ax.legend(frameon=False)
    fig.savefig('\第3章 单变量图形的绘制\图3-2-3 使用ProPlot和SciencePlots绘制的带统计信息的直方图示例_b.pdf',bbox_inches='tight')
    fig.savefig('\第3章 单变量图形的绘制\图3-2-3 使用ProPlot和SciencePlots绘制的带统计信息的直方图示例_b.png', 
                 bbox_inches='tight',dpi=300)

plt.show()
