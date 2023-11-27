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
fig, axs = pplt.subplots(
    ncols=2, nrows=2, order='F', refwidth=1.7, wspace=2.5, share=False
)

# Plot data
data = (state.rand(50, 50) - 0.1).cumsum(axis=0)
for ax in axs[:2]:
    m = ax.contourf(data, cmap='grays', extend='both')
hs = []
colors = pplt.get_colors('grays', 5)
for abc, color in zip('ABCDEF', colors):
    data = state.rand(10)
    for ax in axs[2:]:
        h, = ax.plot(data, color=color, lw=3, label=f'line {abc}')
    hs.append(h)

# Add colorbars and legends
fig.colorbar(m, length=0.8, label='colorbar label', loc='b', col=1, locator=5)
fig.colorbar(m, label='colorbar label', loc='l')
fig.legend(hs, ncols=2, center=True, frame=False, loc='b', col=2)
fig.legend(hs, ncols=1, label='legend label', frame=False, loc='r')
fig.format(abc='A', abcloc='ul')
for ax, title in zip(axs, ('2D {} #1', '2D {} #2', 'Line {} #1', 'Line {} #2')):
    ax.format(xlabel='xlabel', title=title.format('dataset'))
    
fig.save(r'\第2章 绘制工具及其重要特征\Proplot_figure_cb_legend.png', 
         bbox_inches='tight',dpi=600)
fig.save(r'\第2章 绘制工具及其重要特征\Proplot_figure_cb_legend.pdf', 
         bbox_inches='tight')
plt.show()
         
