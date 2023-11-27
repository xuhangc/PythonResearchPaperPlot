"""
编写时间：2022年2月05日 19：20

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。

代码中Proplot包绘制的部分可能与Matplotlib绘制不同，需注意两者绘图语法的不同~~

"""

import pandas as pd
import numpy as np
import proplot as pplt
import matplotlib.pyplot as plt
from proplot import rc

# Sample data
state = np.random.RandomState(51423)
data = state.rand(6, 6)
data = pd.DataFrame(data, index=pd.Index(['a', 'b', 'c', 'd', 'e', 'f']))

fig = pplt.figure(share=False, refwidth=2.3)

rc["font.family"] = "Times New Roman"
ax = fig.subplot(231)
m = ax.heatmap(
    data, cmap='grays',
    labels=True, precision=2, labels_kw={'weight': 'bold'}
)
ax.format(title='Times New Roman Font')

rc["font.family"] = "TeX Gyre Schola"
ax = fig.subplot(232)
m = ax.heatmap(
    data, cmap='grays',
    labels=True, precision=2, labels_kw={'weight': 'bold'}
)
ax.format(title='TeX Gyre Schola Font')

rc["font.family"] = "TeX Gyre Heros"
ax = fig.subplot(233)
m = ax.heatmap(
    data, cmap='grays',
    labels=True, precision=2, labels_kw={'weight': 'bold'}
)
ax.format(title='TeX Gyre Heros Font')

rc["font.family"] = "TeX Gyre Cursor"
ax = fig.subplot(234)
m = ax.heatmap(
    data, cmap='grays',
    labels=True, precision=2, labels_kw={'weight': 'bold'}
)
ax.format(title='TeX Gyre Cursor Font')

rc["font.family"] = "TeX Gyre Chorus"
ax = fig.subplot(235)
m = ax.heatmap(
    data, cmap='grays',
    labels=True, precision=2, labels_kw={'weight': 'bold'}
)
ax.format(title='TeX Gyre Chorus Font')

rc["font.family"] = "TeX Gyre Adventor"
ax = fig.subplot(236)
m = ax.heatmap(
    data, cmap='grays',
    labels=True, precision=2, labels_kw={'weight': 'bold'}
)
ax.format(title='TeX Gyre Adventor Font')

fig.format(abc="(a)", abcloc="ul",abcsize=15,
           xlabel='xlabel', ylabel='ylabel',labelsize=14)
           
           
fig.save(r'\第2章 绘制工具及其重要特征\图2-3-7 Proplot_fonts.png', 
         bbox_inches='tight',dpi=600)
fig.save(r'\第2章 绘制工具及其重要特征\图2-3-7 Proplot_fonts.pdf', 
         bbox_inches='tight')
plt.show()

         