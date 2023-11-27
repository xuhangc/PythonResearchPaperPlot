"""
编写时间：2022年4月15日 19：30

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

"""
此代码为使用Python-Prolot包进行学术风格图表绘制，绘图语法和Matplotlib有所不同，需注意。

"""

import pandas as pd
import numpy as np
import proplot as pplt
import seaborn as sns
import matplotlib.pyplot as plt
from mpltern.ternary.datasets import get_triangular_grid

from proplot import rc
rc["font.family"] = "Times New Roman"
rc["axes.labelsize"] = 15
rc["tick.labelsize"] = 12
rc["suptitle.size"] = 15
rc["title.size"] = 14

t, l, r = get_triangular_grid()
fig = plt.figure(figsize=(4.5, 4),dpi=100,facecolor="w")
ax = fig.add_subplot(projection='ternary')
ax.tick_params(length=8)
ax.triplot(t, l, r,color="k",lw=.5,alpha=.5)


ax.scatter(0.3,0.4,0.3,s=150,color="#459DFF",ec="k",lw=.8,zorder=2)
ax.plot([0, 0.3], [0.7, 0.4], [0.3, 0.3],color="r",lw=1,zorder=1)
ax.plot([0.3, 0.3], [0., 0.4], [0.7, 0.3],color="r",lw=1,zorder=1)
ax.plot([0.45, 0.3], [0.3, 0.4], [0., 0.3],color="r",lw=1,zorder=1)

ax.text(.55, .55, .4, 'S',size=18, ha='center', va='center',fontstyle="italic",fontweight="bold")
ax.text(.1, .95, .35, 'a',size=18, ha='center', va='center',fontstyle="italic",fontweight="bold")
ax.text(.35, .05, .65, 'b',size=18, ha='center', va='center',fontstyle="italic",fontweight="bold")
ax.text(.8, .5, .1, 'c',size=18, ha='center', va='center',fontstyle="italic",fontweight="bold")
ax.set_tlabel('A')
ax.set_llabel('B')
ax.set_rlabel('C')
ax.text(-0.2,0.7,0.5,s="Variable 1",fontsize=16, fontweight="bold")
ax.text(0.2,0.4,-.1,s="Variable 2",fontsize=16, fontweight="bold",rotation="60")
ax.text(0.2,-.02,0.35,s="Variable 3",fontsize=16, fontweight="bold",rotation="-60")
plt.savefig(r'\第5章 多变量图形的绘制\图5-3-1 利用mpltern绘制的三元相图示意图.pdf', bbox_inches='tight',)
plt.savefig(r'\第5章 多变量图形的绘制\图5-3-1 利用mpltern绘制的三元相图示意图.png', 
            bbox_inches='tight',dpi=600)
plt.show()