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
ax = fig.subplot(231)
state = np.random.RandomState(51423)
data = 1 + (state.rand(12, 10) - 0.45).cumsum(axis=0)
m = ax.heatmap(state.rand(10, 10), cmap='grays')
ax.colorbar(m, loc='ll', label='grays colorbar')
ax = fig.subplot(232)
m = ax.heatmap(state.rand(10, 10), cmap='viridis')
ax.colorbar(m, loc='ll', label='viridis colorbar')

ax = fig.subplot(233)
m = ax.heatmap(state.rand(10, 10), cmap='mako')
ax.colorbar(m, loc='ll', label='mako colorbar')

ax = fig.subplot(234)
m = ax.heatmap(state.rand(10, 10), cmap='marine')
ax.colorbar(m, loc='ll', label='marine colorbar')

ax = fig.subplot(235)
m = ax.heatmap(state.rand(10, 10), cmap='dense')
ax.colorbar(m, loc='ll', label='dense colorbar')

ax = fig.subplot(236)
m = ax.heatmap(state.rand(10, 10), cmap='batlow')
ax.colorbar(m, loc='ll', label='batlow colorbar')

fig.format(abc="(a)", abcloc="ul",abcsize=15,
           xlabel='xlabel', ylabel='ylabel',labelsize=15)
           
fig.save(r'\第2章 绘制工具及其重要特征\图2-3-6 Proplot_colormaps.png', 
         bbox_inches='tight',dpi=600)
fig.save(r'\第2章 绘制工具及其重要特征\图2-3-6 Proplot_colormaps.pdf', 
         bbox_inches='tight')
plt.show()