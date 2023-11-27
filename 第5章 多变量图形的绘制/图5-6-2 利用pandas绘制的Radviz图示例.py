"""
编写时间：2022年4月23日 15：40

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
rc["tick.labelsize"] = 12
rc["suptitle.size"] = 15
rc["title.size"] = 14


data_df = sns.load_dataset("iris")
colors = plt.cm.Set1.colors

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
radviz = pd.plotting.radviz(data_df, 'species',edgecolors='k',marker='o',s=35,linewidths=1,
                        color=colors,
                        ax=ax)
# 添加圆圈线
angle=np.arange(360)/180*3.14159
x=np.cos(angle)
y=np.sin(angle)
ax.plot(x,y,color='k',lw=1,zorder=0)

ax.axis('off')
ax.legend(loc="lower right",bbox_to_anchor=(1.1,0.05),frameon=False,handletextpad=.1)
plt.tight_layout()
fig.savefig('\第5章 多变量图形的绘制\图5-6-2 利用pandas绘制的Radviz图示例.pdf',bbox_inches='tight')
fig.savefig('\第5章 多变量图形的绘制\图5-6-2 利用pandas绘制的Radviz图示例.png', 
            bbox_inches='tight',dpi=300)
plt.show()
