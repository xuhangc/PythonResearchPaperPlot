"""
编写时间：2022年2月05日 19：20

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。

代码中Proplot包绘制的部分可能与Matplotlib绘制不同，需注意两者绘图语法的不同~~

"""

import pandas as pd
import numpy as np
import proplot as pplt
import matplotlib.pyplot as plt

N = 50
M = 40
state = np.random.RandomState(51423)
cycle = pplt.Cycle('grays', M, left=0.1, right=0.8)

datas = []
for scale in (1, 3, 7, 0.2):
    data = scale * (state.rand(N, M) - 0.5).cumsum(axis=0)[N // 2:, :]
    datas.append(data)

# Plots with different sharing and spanning settings
# Note that span=True and share=True are the defaults
spans = (False, False, False, False)
shares = (False, 'labels', 'limits', True)
for i, (span, share) in enumerate(zip(spans, shares)):
    fig = pplt.figure(refaspect=1, refwidth=1.06, spanx=span, sharey=share)
    axs = fig.subplots(ncols=3)
    for ax, data in zip(axs, datas):
        on = ('off', 'on')[int(span)]
        ax.plot(data, cycle=cycle)
        ax.format(
            grid=False, xlabel='X labels', ylabel='shared axis',
            #suptitle=f'Sharing mode {share!r} (level {i}) with spanning labels {on}'
        )
        fig.save(r'\第2章 绘制工具及其重要特征\Proplot_subplot_share'+str(share)+'.png', bbox_inches='tight',dpi=600)
        fig.save(r'\第2章 绘制工具及其重要特征\\Proplot_subplot_share'+str(share)+'.pdf', bbox_inches='tight')

plt.show()