"""
编写时间：2022年2月05日 19：20

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。

代码中Proplot包绘制的部分可能与Matplotlib绘制不同，需注意两者绘图语法的不同~~

"""

import pandas as pd
import numpy as np
import proplot as pplt
import matplotlib.pyplot as plt

fig = pplt.figure(share=False, refwidth=2.3)

# Colorbars
ax = fig.subplot(121)
state = np.random.RandomState(51423)
m = ax.heatmap(state.rand(10, 10), colorbar='t', cmap='grays')
ax.colorbar(m, loc='r')
ax.colorbar(m, loc='ll', label='colorbar label')
ax.format(title='Axes colorbars')

# Legends
ax = fig.subplot(122)
ax.format(title='Axes legends', titlepad='0em')
hs = ax.plot(
    (state.rand(10, 5) - 0.5).cumsum(axis=0), linewidth=3,
    cycle='ggplot', legend='t',
    labels=list('abcde'), legend_kw={'ncols': 5, 'frame': False}
)
ax.legend(hs, loc='r', ncols=1, frame=False)
ax.legend(hs, loc='ll', label='legend label')
fig.format(abc="(a)", abcloc="ul",abcsize=15, 
           xlabel='xlabel', ylabel='ylabel')
           
fig.save('\第2章 绘制工具及其重要特征\图2-3-4 Proplot_axes_cb_legend.png', 
         bbox_inches='tight',dpi=600)
fig.save('\第2章 绘制工具及其重要特征\图2-3-4 Proplot_axes_cb_legend.pdf', 
         bbox_inches='tight')
plt.show()