"""
编写时间：2022年4月15日 15：00

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

"""
此代码为使用Python-Prolot包进行学术风格图表绘制，绘图语法和Matplotlib有所不同，需注意。

"""

import numpy as np
import pandas as pd
import seaborn as sns
import proplot as pplt
import matplotlib.pyplot as plt
from colormaps import parula

from proplot import rc
rc["font.family"] = "Times New Roman"
rc["axes.labelsize"] = 15
rc["tick.labelsize"] = 12
rc["suptitle.size"] = 15
rc["title.size"] = 14

data = pd.read_excel(r"\第5章 多变量图形的绘制\coutour_data.xlsx",header=None)

x = np.arange(0,len(data), 1)
y = np.arange(0,len(data), 1)
X, Y = np.meshgrid(x, y)
Z = data.values

# a）利用Matplotlib绘制的纹理填充等值线图样式一
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
cs = ax.contourf(X, Y, Z, hatches=['-', '//', '\\', '//',"**"],
                  cmap='gray', extend='both', alpha=0.5)
ax.grid(False)
ax.set(xlabel='X Axis title', ylabel='Y Axis title')
fig.colorbar(cs)
fig.tight_layout()
fig.savefig('\第5章 多变量图形的绘制\图5-1-2 利用Matplotlib绘制的纹理填充等值线图示例_a.pdf',bbox_inches='tight')
fig.savefig('\第5章 多变量图形的绘制\图5-1-2 利用Matplotlib绘制的纹理填充等值线图示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()


# b）利用Matplotlib绘制的纹理填充等值线图样式二
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
n_levels = 6
ax.contour(X, Y, Z, n_levels,linewidths=1,colors='black', linestyles='-')
cs = ax.contourf(X, Y, Z, n_levels, colors='none',
                  hatches=['.', '/', '\\', None, '\\\\', '*'],
                  extend='lower')
ax.grid(False)
ax.set(xlabel='X Axis title', ylabel='Y Axis title')
# create a legend for the contour set
artists, labels = cs.legend_elements(str_format='{:2.1f}'.format)
ax.legend(artists, labels, handleheight=2, framealpha=1)
fig.tight_layout()

fig.savefig('\第5章 多变量图形的绘制\图5-1-2 利用Matplotlib绘制的纹理填充等值线图示例_b.pdf',bbox_inches='tight')
fig.savefig('\第5章 多变量图形的绘制\图5-1-2 利用Matplotlib绘制的纹理填充等值线图示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()