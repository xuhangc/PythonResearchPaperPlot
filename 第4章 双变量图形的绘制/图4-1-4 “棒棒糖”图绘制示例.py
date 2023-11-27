
"""
编写时间：2022年4月10日 14：50

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

"""
此代码为使用Python-Prolot包进行学术风格图表绘制，绘图语法和Matplotlib有所不同，需注意。
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from proplot import rc
rc["font.family"] = "Times New Roman"
rc["axes.labelsize"] = 15
rc["tick.labelsize"] = 12
rc["suptitle.size"] = 15
rc["title.size"] = 14

# a）利用ProPlot绘制的横向“棒棒糖”图

values = [2,3.5,4.2,5,6.8,7.5]
labels = ['a','b','c','d','e',"f"]
index = np.arange(len(labels))

fig = pplt.figure(figsize=(3.5,3))
ax = fig.subplot()
ax.format(abc='a.', abcloc='ur',abcsize=16,
          xlabel='Values', ylabel='Class',
          xlim=(0, 9),ylim=(-1,6))
ax.scatter(x=values,y=index,s=100,color="gray",ec="k",zorder=2)
ax.hlines(y=index,x1=0,x2=values,color="k",zorder=1)
ax.set_yticks(index)
ax.set_yticklabels(labels)
fig.savefig('\第4章 双变量图形的绘制\图4-1-4 “棒棒糖”图绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-4 “棒棒糖”图绘制示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# b）利用ProPlot绘制的纵向“棒棒糖”图

values = [2,3.5,4.2,5,6.8,7.5]
labels = ['a','b','c','d','e',"f"]
index = np.arange(len(labels))

fig = pplt.figure(figsize=(3.5,3))
ax = fig.subplot()
ax.format(abc='a.', abcloc='ur',abcsize=16,
          xlabel='Values', ylabel='Class',
          xlim=(-1, 6),ylim=(0,9))
ax.scatter(x=index,y=values,s=100,color="gray",ec="k",zorder=2)
ax.vlines(x=index,y1=0,y2=values,color="k",zorder=1)
ax.set_xticks(index)
ax.set_xticklabels(labels)
fig.savefig('\第4章 双变量图形的绘制\图4-1-4 “棒棒糖”图绘制示例_b.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-4 “棒棒糖”图绘制示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# c）利用ProPlot绘制的多组“棒棒糖”图

values1 = [2,3.7,4.1,5,6.8,7.5]
values2 = [1.1,3,4.9,5.7,6,7]

index = np.arange(len(labels))

fig = pplt.figure(figsize=(3.5,3))
ax = fig.subplot()
ax.format(abc='a.', abcloc='ur',abcsize=16,
          xlabel='Values', ylabel='Class',
          xlim=(0, 9),ylim=(-1,6))
ax.scatter(x=values1,y=index,s=100,color="#FF5B9B",ec="k",label="Value1")
ax.scatter(x=values2,y=index,s=100,color="#FFCC37",ec="k",label="Value2")
#绘制连接线
ax.hlines(y=index,x1=values1,x2=values2,color="k",zorder=-1)
ax.set_yticks(index)
ax.set_yticklabels(labels)
ax.legend(ncol=1)
fig.savefig('\第4章 双变量图形的绘制\图4-1-4 “棒棒糖”图绘制示例_c.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-4 “棒棒糖”图绘制示例_c.png', 
            bbox_inches='tight',dpi=300)
plt.show()

