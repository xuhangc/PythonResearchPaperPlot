"""
编写时间：2022年4月11日 15：30

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

"""
此代码为使用Python-Prolot包进行学术风格图表绘制，绘图语法和Matplotlib有所不同，需注意。
"""

import pandas as pd
import numpy as np
import seaborn as sns
import proplot as pplt
import matplotlib.pyplot as plt

from proplot import rc
rc["font.family"] = "Times New Roman"
rc["axes.labelsize"] = 15
rc["tick.labelsize"] = 13
rc["suptitle.size"] = 15
rc["title.size"] = 14
rc["tick.minor"] = False


# a）Matplotlib 的纹理填充堆积柱形图绘制示例
names = ["A","B","C","D","E"]
values = [2,5,8,12,20]

patterns = ['//','oo','xx','..','**']
width = .7
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
for name,value,pattern,label in zip(names,values,patterns,names):
    ax.bar(name, value, width,hatch=pattern, label=label,color='white',edgecolor='black')
ax.tick_params(which='major',direction='in',length=3,width=1.,bottom=False)
for spine in ["top","left","right"]:
    ax.spines[spine].set_visible(False)
ax.spines['bottom'].set_linewidth(2)
#设置刻度label
ax.set(xlabel="Name",ylabel="Values",xticklabels=names)
ax.legend(ncol=5,frameon=False,loc="upper left",bbox_to_anchor=(0, 1.08))      
plt.tight_layout()

fig.savefig('\第4章 双变量图形的绘制\图4-1-16 Matplotlib 和Excel的纹理填充堆积柱形图示例_a.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-16 Matplotlib 和Excel的纹理填充堆积柱形图示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()
