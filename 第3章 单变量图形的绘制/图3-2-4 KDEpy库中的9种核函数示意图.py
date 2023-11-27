
"""
编写时间：2022年2月06日 09：50

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。

代码中Proplot包绘制的部分可能与Matplotlib绘制不同，需注意两者绘图语法的不同~~

"""
#注意：本案例中引入的SciencePlots库主题方式会随着SciencePlots版本的更新发生改变，读者还需参考其官网引入的正确方式。
#      建议按照官网引入方式进行操作和使用最新版本的ScienePlots。如引入方式发生改变，请关注微信公众号【DataCharm】进行实时获取代码更新。


import numpy as np
import pandas as pd
from proplot import rc
from KDEpy import NaiveKDE
import matplotlib.pyplot as plt

rc["axes.labelsize"] = 15
rc['tick.labelsize'] = 12
rc["suptitle.size"] = 15

kde_kernels = NaiveKDE._available_kernels.keys()

fig, axs = pplt.subplots(ncols=3, nrows=3,refwidth=1.5,refheight=1.2)
axs.format(
    abc='a.', abcloc='ul',abcsize=16,
    xlabel='Values', ylabel='Density'
)
for ax, kernel in zip(axs,kde_kernels):
    x, y = NaiveKDE(kernel=kernel).fit([0]).evaluate()
    ax.plot(x,y, lw=1,color="#246CDA")
    ax.fill(x,y,color="#246CDA",alpha=.6)
    ax.format(title=str.capitalize(kernel),titleweight='bold',titlesize=12)
    
fig.savefig('\第3章 单变量图形的绘制\图3-2-4 KDEpy库中的9种核函数示意图.pdf')
fig.savefig('\第3章 单变量图形的绘制\图3-2-4 KDEpy库中的9种核函数示意图.png')
plt.show()

