"""
编写时间：2022年4月14日 09：50

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

"""
此代码为使用Python-Prolot包进行学术风格图表绘制，绘图语法和Matplotlib有所不同，需注意。
"""

import pandas as pd
import numpy as np
import seaborn as sns
import proplot as pplt
from scipy import stats 
import matplotlib.pyplot as plt

from proplot import rc
rc["font.family"] = "Times New Roman"
rc["axes.labelsize"] = 15
rc["tick.labelsize"] = 12
rc["suptitle.size"] = 15
rc["title.size"] = 14

# a）学术色系环形图绘制

sizes = [12, 40, 25, 15,8]
labels = ['A','B','C','D',"E"]
colors = ["#2FBE8F","#459DFF","#FF5B9B","#FFCC37","#751DFE"]

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
explode = (0, 0., 0, 0,0)  
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
       shadow=False, startangle=90,colors=colors,pctdistance=.82,
       wedgeprops={'linewidth':.8, 'edgecolor': 'k',"width":.38},
       textprops={'size': 12,"weight":"bold"})
ax.legend(labels,loc ='upper left',fontsize=9,handlelength=1.2,handleheight=1.2)
plt.tight_layout()
fig.savefig('\第4章 双变量图形的绘制\图4-1-37 不同样式环形图绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-37 不同样式环形图绘制示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# b）灰色系环形图绘制

sizes = [12, 40, 25, 15,8]
labels = ['A','B','C','D',"E"]
colors = plt.cm.gray(np.linspace(0.2,0.8,len(sizes)))

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
explode = (0, 0., 0, 0,0)  
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
       shadow=False, startangle=90,colors=colors,pctdistance=.82,
       wedgeprops={'linewidth':.8, 'edgecolor': 'k',"width":.38},
       textprops={'size': 12,"weight":"bold"})
ax.legend(labels,loc ='upper left',fontsize=9,handlelength=1.2,handleheight=1.2)
plt.tight_layout()
fig.savefig('\第4章 双变量图形的绘制\图4-1-37 不同样式环形图绘制示例_b.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-37 不同样式环形图绘制示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# c）纹理填充环形图绘制

hatches = ['\\','+','x', 'o', '*']
sizes = [12, 40, 25, 15,8]
labels = ['A','B','C','D',"E"]
colors = plt.cm.gray(np.linspace(0.2,0.8,len(sizes)))
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
explode = (0, 0., 0, 0,0)  
pie = ax.pie(sizes, explode=explode, autopct='%1.1f%%',
       shadow=False, startangle=90,colors=colors,pctdistance=1.18,
       wedgeprops={'linewidth':.8, 'edgecolor': 'k',"width":.38},
       textprops={'size': 13,"weight":"bold",})
for patch, hatch in zip(pie[0],hatches):
    patch.set_hatch(hatch)
ax.legend(labels,loc ='upper left',fontsize=9)
plt.tight_layout()

fig.savefig('\第4章 双变量图形的绘制\图4-1-37 不同样式环形图绘制示例_c.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-37 不同样式环形图绘制示例_c.png', 
            bbox_inches='tight',dpi=300)
plt.show()