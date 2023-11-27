"""
编写时间：2022年2月05日 16：30

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。

代码中Proplot包绘制的部分可能与Matplotlib绘制不同，需注意两者绘图语法的不同~~

"""

import pandas as pd
import numpy as np
import proplot as pplt
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

from proplot import rc
rc["font.family"] = "Times New Roman"
rc["axes.labelsize"] = 15
rc['tick.labelsize'] = 13
rc["suptitle.size"] = 15

def annotate_axes(ax, text, fontsize):
    ax.text(0.5, 0.5, text, transform=ax.transAxes,
            fontsize=fontsize, alpha=0.75, ha="center", va="center", weight="bold")
            

fig, axd = plt.subplot_mosaic([['upper left', 'right'],
                               ['lower left', 'right']],
                               figsize=(6,3), constrained_layout=True)
for k in axd:
    annotate_axes(axd[k], f'axd["{k}"]', fontsize=14)       

plt.tight_layout()
plt.savefig(r'\第2章 绘制工具及其重要特征\图2-1-18 subplot_mosaic()函数绘制子图示例结果.pdf',bbox_inches='tight')
plt.savefig(r'\第2章 绘制工具及其重要特征\图2-1-18 subplot_mosaic()函数绘制子图示例结果.png', 
            bbox_inches='tight',dpi=300)       
plt.show()


    