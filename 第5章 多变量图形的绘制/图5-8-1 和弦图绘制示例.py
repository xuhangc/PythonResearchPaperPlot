"""
编写时间：2022年4月25日 16：30

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

import numpy as np
import pandas as pd
import seaborn as sns
import proplot as pplt
import matplotlib.pyplot as plt
from mpl_chord_diagram import chord_diagram
from colormaps import parula

from proplot import rc
rc["font.family"] = "Times New Roman"
rc["axes.labelsize"] = 15
rc["tick.labelsize"] = 12
rc["suptitle.size"] = 15
rc["title.size"] = 14

plt.rcParams["image.composite_image"] = False


# a）和弦图绘制基本样式一

from mpl_chord_diagram import chord_diagram

flux_data = np.array([
    [0, 5, 6, 4, 7, 4],
    [5, 0, 5, 4, 6, 5],
    [6, 5, 0, 4, 5, 5],
    [4, 4, 4, 0, 5, 5],
    [7, 6, 5, 5, 0, 4],
    [4, 5, 5, 5, 4, 0],
])
names = ["A","B","C","D","E","F"]

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
chord_diagram = chord_diagram(mat=flux_data,names=names,alpha=.8,ax=ax)
plt.tight_layout()

fig.savefig('\第5章 多变量图形的绘制\图5-8-1 和弦图绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第5章 多变量图形的绘制\图5-8-1 和弦图绘制示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# b）和弦图绘制基本样式二

from mpl_chord_diagram import chord_diagram

flux_data = np.array([
    [0, 5, 6, 4, 7, 4],
    [5, 0, 5, 4, 6, 5],
    [6, 5, 0, 4, 5, 5],
    [4, 4, 4, 0, 5, 5],
    [7, 6, 5, 5, 0, 4],
    [4, 5, 5, 5, 4, 0],
])
names = ["A","B","C","D","E","F"]

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
chord_diagram = chord_diagram(mat=flux_data,names=names,alpha=.8,use_gradient=True,ax=ax)
plt.tight_layout()

fig.savefig('\第5章 多变量图形的绘制\图5-8-1 和弦图绘制示例_b.pdf',bbox_inches='tight')
fig.savefig('\第5章 多变量图形的绘制\图5-8-1 和弦图绘制示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()