"""
编写时间：2022年2月04日 22：30

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。

代码中Proplot包绘制的部分可能与Matplotlib绘制不同，需注意两者绘图语法的不同~~

"""

import numpy as np
import pandas as pd
import seaborn as sns
import proplot as pplt
import matplotlib.pyplot as plt
from matplotlib import cm
from colorspacious import cspace_converter

from proplot import rc
rc["font.family"] = "Times New Roman"
rc["axes.labelsize"] = 13
rc['tick.labelsize'] = 11
rc["suptitle.size"] = 15

cmaps = {}

gradient = np.linspace(0, 1, 256)
gradient = np.vstack((gradient, gradient))


def plot_color_gradients(category, cmap_list):
    # Create figure and adjust figure height to number of colormaps
    nrows = len(cmap_list)
    figh = 0.35 + 0.15 + (nrows + (nrows - 1) * 0.1) * 0.22
    fig, axs = plt.subplots(nrows=nrows + 1, figsize=(6.4, figh))
    fig.subplots_adjust(top=1 - 0.35 / figh, bottom=0.15 / figh,
                        left=0.2, right=0.99)
    axs[0].set_title(f'{category} colormaps', fontsize=14)

    for ax, name in zip(axs, cmap_list):
        ax.imshow(gradient, aspect='auto', cmap=plt.get_cmap(name))
        ax.text(-0.01, 0.5, name, va='center', ha='right', fontsize=10,
                transform=ax.transAxes)

    # Turn off *all* ticks & spines, not just the ones with colormaps.
    for ax in axs:
        ax.set_axis_off()

    # Save colormap list for later.
    cmaps[category] = cmap_list
    return fig

colormap = [str.lower(i) for i in ['PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu', 'RdYlBu',
           'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic']]
fig = plot_color_gradients('Diverging',colormap)
fig.savefig(r'r"\第1章 科研论文配图的绘制与配色基础\图1-2-12 Matplotlib库中双色渐变色系颜色主题(Diverging colormaps).pdf',bbox_inches='tight')
fig.savefig(r'r"\第1章 科研论文配图的绘制与配色基础\图1-2-12 Matplotlib库中双色渐变色系颜色主题(Diverging colormaps).png', 
             bbox_inches='tight',dpi=300)
plt.show() 