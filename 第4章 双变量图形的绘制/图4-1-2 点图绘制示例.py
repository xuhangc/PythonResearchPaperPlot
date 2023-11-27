"""
编写时间：2022年4月10日 13：40

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

"""
此代码为使用Python-Prolot包进行学术风格图表绘制，绘图语法和Matplotlib有所不同，需注意。
"""

# a）利用Matplotlib绘制的点图绘制

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

labels = ['a','b','c','d','e','f','g']
counts = [3, 1, 5, 6, 2, 4, 2]
x = np.arange(len(labels))

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
for value, count in zip(x, counts):
    ax.plot([value]*count, list(range(count)),marker='o',color="#2FBE8F",mec="k",ms=13,ls="")
ax.set_xlim(-1,7)
ax.set_ylim(-.4,5.5)
ax.grid(linewidth=.4)
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_xlabel("Class")
ax.set_ylabel("Values")

fig.savefig('\第4章 双变量图形的绘制\图4-1-2 点图绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-2 点图绘制示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()
             
# b）利用ProPlot 绘制的点图

import pandas as pd
import numpy as np
import seaborn as sns
import proplot as pplt
import matplotlib.pyplot as plt
from proplot import rc
rc["font.family"] = "Times New Roman"
rc["axes.labelsize"] = 15
rc["tick.labelsize"] = 12
rc["suptitle.size"] = 15
rc["title.size"] = 14

labels = ['a','b','c','d','e','f','g']
counts = [3, 1, 5, 6, 2, 4, 2]
x = np.arange(len(labels))

fig = pplt.figure(figsize=(3.5,3))
ax = fig.subplot()
ax.format(abc='a.', abcloc='ul',abcsize=16,
          xlabel='Class', ylabel='Values',
          xlim=(-1,7),ylim=(-.4,5.5))
for value, count in zip(x, counts):
    ax.plot([value]*count, list(range(count)),marker='o',color="#2FBE8F",mec="k",ms=13,ls="")
ax.set_xticks(x)
ax.set_xticklabels(labels)

fig.savefig('\第4章 双变量图形的绘制\图4-1-2 点图绘制示例_b.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-2 点图绘制示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# c）利用SciencePlots 绘制的点图:版本不同， SciencePlots引入方式不同，读者可参考SciencePlots官网 最新引入方式
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#使用SciencePlots包主题
plt.style.use('science') #全局

labels = ['a','b','c','d','e','f','g']
counts = [3, 1, 5, 6, 2, 4, 2]
x = np.arange(len(labels))

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
for value, count in zip(x, counts):
    ax.plot([value]*count, list(range(count)),marker='o',color="#2FBE8F",mec="k",ms=13,ls="")
ax.set_xlim(-1,7)
ax.set_ylim(-.4,5.5)
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_xlabel("Class")
ax.set_ylabel("Values")
fig.savefig('\第4章 双变量图形的绘制\图4-1-2 点图绘制示例_c.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-2 点图绘制示例_c.png', 
            bbox_inches='tight',dpi=300)
plt.show()



