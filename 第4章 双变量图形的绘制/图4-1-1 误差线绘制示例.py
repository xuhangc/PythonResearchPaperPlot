"""
编写时间：2022年4月10日 13：30

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

from proplot import rc
rc["font.family"] = "Times New Roman"
rc["axes.labelsize"] = 15
rc["tick.labelsize"] = 12
rc["suptitle.size"] = 15
rc["title.size"] = 14

# a）基本的误差线样式
x = [2, 4, 6]
y = [4, 6, 3]
xerr = [0.5,0.8,1.1]
yerr = [0.8, 1.2, 0.6]

fig = pplt.figure(figsize=(3.5,3))
ax = fig.subplot()
ax.format(xlabel='Class', ylabel='Values',
          xlim=(0,8),ylim=(1,8))
ax.errorbar(x, y, xerr,yerr, fmt="o",ecolor="k", elinewidth=1.2,capsize=6,capthick=1.2,
           ms=12,mfc="w",mec="k")
ax.grid(False)
# plt.tight_layout()
fig.savefig('\第4章 双变量图形的绘制\图4-1-1 误差线绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-1 误差线绘制示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# b）在柱形图上添加误差线样式

x = [2, 4, 6]
y = [4, 6, 3]
xerr = [0.5,0.8,1.1]
yerr = [0.8, 1.2, 0.6]

fig = pplt.figure(figsize=(3.5,3))
ax = fig.subplot()
ax.format(xlabel='Class', ylabel='Values',
          xlim=(0,8),ylim=(1,8))
ax.bar(x,y,color="gray",ec="k",yerr=yerr,
       error_kw=dict(elinewidth=1.2,capsize=6,capthick=1.2))
ax.grid(False)
fig.savefig('\第4章 双变量图形的绘制\图4-1-1 误差线绘制示例_b.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-1 误差线绘制示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()

