"""
编写时间：2022年2月05日 19：20

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。

代码中Proplot包绘制的部分可能与Matplotlib绘制不同，需注意两者绘图语法的不同~~

"""

import pandas as pd
import numpy as np
import proplot as pplt
import matplotlib.pyplot as plt


state = np.random.RandomState(51423)

# Plots with minimum and maximum sharing settings
# Note that all x and y axis limits and ticks are identical
spans = (True, True)
shares = (True, 'all')
titles = ('Minimum sharing', 'Maximum sharing')
for span, share, title in zip(spans, shares, titles):
    fig = pplt.figure(refwidth=1, span=span, share=share)
    axs = fig.subplots(nrows=2, ncols=4)
    for ax in axs:
        data = (state.rand(100, 20) - 0.4).cumsum(axis=0)
        ax.plot(data, cycle='grays')
    axs.format(
        xlabel='xlabel', ylabel='ylabel',
        grid=False, xticks=25, yticks=5,labelsize=13
    )
fig.save(r'\第2章 绘制工具及其重要特征\图2-3-2 Proplot_subplot_span.png', 
         bbox_inches='tight',dpi=600)
fig.save(r'\第2章 绘制工具及其重要特征\图2-3-2 Proplot_subplot_span.pdf', 
         bbox_inches='tight')
         
         
plt.show()


