"""
编写时间：2022年2月06日 10：20

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。

代码中Proplot包绘制的部分可能与Matplotlib绘制不同，需注意两者绘图语法的不同~~

"""
#注意：本案例中引入的SciencePlots库主题方式会随着SciencePlots版本的更新发生改变，读者还需参考其官网引入的正确方式。
#      建议按照官网引入方式进行操作和使用最新版本的ScienePlots。如引入方式发生改变，请关注微信公众号【DataCharm】进行实时获取代码更新。

import numpy as np
import pandas as pd
from KDEpy import FFTKDE
from colormaps import parula

#构建数据集
data_01 = [5.1,5.2,5.3,5.4,5.5,6.0,6.2,6.3,6.4,6.5,
           7.0,7.5,8.0,8.5,8.8,8.9,9.0,9.5,10,11,
           11.5,12,13,14,14.5,15,15.5,16,16.5,17]
           
           
#(a)利用Matplotlib绘制的带渐变颜色填充的密度图           
import matplotlib.pyplot as plt
from matplotlib.axes import Axes

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["axes.linewidth"] = 1
plt.rcParams["axes.labelsize"] = 15
plt.rcParams["xtick.minor.visible"] = True
plt.rcParams["ytick.minor.visible"] = True
plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"
plt.rcParams["xtick.labelsize"] = 12
plt.rcParams["ytick.labelsize"] = 12
plt.rcParams["xtick.top"] = False
plt.rcParams["ytick.right"] = False

x, y = FFTKDE(kernel="gaussian", bw=2).fit(data_01).evaluate()
img_data = x.reshape(1, -1)

cmap = parula
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
ax.plot(x,y, lw=1,color="k")
# 添加单独数据、
ax.plot(data_01, [0.005]*len(data_01), '|', color='k',lw=1)
#ax.tick_params(which="both",direction='in')
ax.set_xlabel("Values")
ax.set_ylabel("Density")
ax.set_title("Gaussian Kernel",size=15)

extent=[*ax.get_xlim(), *ax.get_ylim()]
im = Axes.imshow(ax, img_data, aspect='auto',cmap=cmap,extent=extent)
fill_line,= ax.fill(x, y,facecolor='none')
im.set_clip_path(fill_line)
colorbar = fig.colorbar(im,ax=ax,aspect=12,label="Values")
#colorbar.ax.tick_params(which="both",direction='in')
#colorbar.ax.set_title("Values",fontsize=10)
fig.savefig('\第3章 单变量图形的绘制\图3-2-8 带渐变颜色填充的密度图_a.pdf',bbox_inches='tight')
fig.savefig('\第3章 单变量图形的绘制\图3-2-8 带渐变颜色填充的密度图_a.png', 
            bbox_inches='tight',dpi=300) 
plt.show()   

#(b)利用ProPlot绘制的带渐变颜色填充的密度图

from colormaps import parula
#from matplotlib.axes import Axes
from proplot.axes import Axes
from proplot import rc

rc["font.family"] = "Times New Roman"
rc["axes.labelsize"] = 15
rc['tick.labelsize'] = 10
rc["suptitle.size"] = 16

x, y = FFTKDE(kernel="gaussian", bw=2).fit(data_01).evaluate()
img_data = x.reshape(1, -1)

cmap = parula
fig = pplt.figure(suptitle="Gaussian",figsize=(3.5,3))
ax = fig.subplot(xlabel='x axis', ylabel='y axis')
ax.format(abc='a.', abcloc='ul',abcsize=16,
          xlabel='Values', ylabel='Density',
          suptitle='Gaussian Kernel')
ax.plot(x,y, lw=1,color="k")
# 添加单独数据、
ax.plot(data_01, [0.005]*len(data_01), '|', color='k',lw=1)
fill_line,= ax.fill(x, y,facecolor='none')
extent=[*ax.get_xlim(), *ax.get_ylim()]
im = Axes.imshow(ax, img_data, aspect='auto',cmap=cmap,extent=extent)
im.set_clip_path(fill_line)
fig.colorbar(im,title="Values",tickminor=True,tickdirection="in")

fig.savefig('\第3章 单变量图形的绘制\图3-2-8 带渐变颜色填充的密度图_b.pdf',)
fig.savefig('\第3章 单变量图形的绘制\图3-2-8 带渐变颜色填充的密度图_b.png', dpi=300)
plt.show()  

#(c)利用SciencePlots 绘制的带渐变颜色填充的密度图

from KDEpy import NaiveKDE
from colormaps import parula
from matplotlib.axes import Axes

customer_ages = [5.1,5.2,5.3,5.4,5.5,6.0,6.2,6.3,6.4,6.5,
                 7.0,7.5,8.0,8.5,8.8,8.9,9.0,9.5,10,11,
                 11.5,12,13,14,14.5,15,15.5,16,16.5,17]
x, y = NaiveKDE(kernel="gaussian",bw=2).fit(customer_ages).evaluate()
img_data = x.reshape(1, -1)
cmap = parula

from matplotlib.axes import Axes
with plt.style.context(['science']):
    fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
    ax.plot(x,y, lw=1,color="k")
    # 添加单独数据、
    ax.plot(data_01, [0.005]*len(data_01), '|', color='k',lw=1)
    #ax.tick_params(which="both",direction='in')
    ax.set_xlabel("Values")
    ax.set_ylabel("Density")
    ax.set_title("Gaussian Kernel",size=15)
    ax.text(.05,.88,"a.",transform=ax.transAxes,fontsize=25,fontweight="bold")
    extent=[*ax.get_xlim(), *ax.get_ylim()]
    im = Axes.imshow(ax, img_data, aspect='auto',cmap=cmap,extent=extent)
    fill_line,= ax.fill(x, y,facecolor='none')
    im.set_clip_path(fill_line)
    colorbar = fig.colorbar(im,ax=ax,aspect=12,label="Values")
    fig.savefig('\第3章 单变量图形的绘制\图3-2-8 带渐变颜色填充的密度图_c.pdf',)
    fig.savefig('\第3章 单变量图形的绘制\图3-2-8 带渐变颜色填充的密度图_c.png', 
                dpi=300)
plt.show() 