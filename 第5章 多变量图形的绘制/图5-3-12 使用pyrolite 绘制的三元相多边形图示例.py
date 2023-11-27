
"""
编写时间：2022年4月16日 14：50

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

"""
此代码为使用Python-Prolot包进行学术风格图表绘制，绘图语法和Matplotlib有所不同，需注意。
"""

import mpltern  
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from pyrolite.util.classification import USDASoilTexture
from pyrolite.util.plot.style import color_ternary_polygons_by_centroid

# a）使用pyrolite绘制的三元相多边形图样式一
clf = USDASoilTexture()
ax = clf.add_to_axes(ax=ax, add_labels=True)
ax.tick_params(length=8)
color_ternary_polygons_by_centroid(ax)

plt.savefig(r'\第5章 多变量图形的绘制\图5-3-12 使用pyrolite 绘制的三元相多边形图示例_a.pdf', bbox_inches='tight',)
plt.savefig(r'\第5章 多变量图形的绘制\图5-3-12 使用pyrolite 绘制的三元相多边形图示例_a.png', 
            bbox_inches='tight',dpi=600)
plt.show()


# b）使用pyrolite 绘制的三元相多边形图样式二
fig,ax = plt.subplots(figsize=(4.5, 4),dpi=100,facecolor="w")

clf = USDASoilTexture()
ax = clf.add_to_axes(ax=ax, add_labels=True)
ax.tick_params(length=8)
color_ternary_polygons_by_centroid(ax,colors=("#FFCC37","#459DFF","#FF5B9B"))

plt.savefig(r'\第5章 多变量图形的绘制\图5-3-12 使用pyrolite 绘制的三元相多边形图示例_b.pdf', bbox_inches='tight',)
plt.savefig(r'\第5章 多变量图形的绘制\图5-3-12 使用pyrolite 绘制的三元相多边形图示例_b.png', 
            bbox_inches='tight',dpi=600)
plt.show()