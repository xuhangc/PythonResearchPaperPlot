
"""
编写时间：2022年5月06日 09：50

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。

代码中Proplot包绘制的部分可能与Matplotlib绘制不同，需注意两者绘图语法的不同~~

"""
#注意：本案例中引入的SciencePlots库主题方式会随着SciencePlots版本的更新发生改变，读者还需参考其官网引入的正确方式。
#      建议按照官网引入方式进行操作和使用最新版本的ScienePlots。如引入方式发生改变，请关注微信公众号【DataCharm】进行实时获取代码更新。

import numpy as np
import pandas as pd
import pingouin as pg
import matplotlib.pyplot as plt
from proplot import rc
rc["xtick.minor.visible"] = False
rc["ytick.minor.visible"] = False

#a）配对图基础样式一
df = pg.read_dataset('mixed_anova').query("Time != 'January'")
df = df.query("Group == 'Meditation' and Subject > 40")

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
ax = pg.plot_paired(data=df, dv='Scores', within='Time',
                    subject='Subject', 
                    boxplot_kwargs={"linewidth":1},
                    ax=ax)
ax.grid(False)
plt.tight_layout()
fig.savefig('\第7章 其他类型图的绘制\图7-2-1配对图基础样式绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第7章 其他类型图的绘制\图7-2-1配对图基础样式绘制示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()

#b）配对图基础样式二
import pingouin as pg
df = pg.read_dataset('mixed_anova').query("Time != 'January'")
df = df.query("Group == 'Control'")
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
ax = pg.plot_paired(data=df, dv='Scores', within='Time',
                    subject='Subject', boxplot_in_front=True,
                    boxplot_kwargs={"linewidth":1},ax=ax)
ax.grid(False)
plt.tight_layout()

fig.savefig('\第7章 其他类型图的绘制\图7-2-1配对图基础样式绘制示例_b.pdf',bbox_inches='tight')
fig.savefig('\第7章 其他类型图的绘制\图7-2-1配对图基础样式绘制示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()


#c）配对图基础样式三

import pingouin as pg
import matplotlib.pyplot as plt
df = pg.read_dataset('mixed_anova').query("Time != 'January'")
df = df.query("Group == 'Meditation' and Subject > 40")

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
pg.plot_paired(data=df, dv='Scores', within='Time',
               subject='Subject', ax=ax, boxplot=False,
               colors=['k', 'k', 'k'])  
ax.grid(False)
plt.tight_layout()
fig.savefig('\第7章 其他类型图的绘制\图7-2-1配对图基础样式绘制示例_c.pdf',bbox_inches='tight')
fig.savefig('\第7章 其他类型图的绘制\图7-2-1配对图基础样式绘制示例_c.png', 
            bbox_inches='tight',dpi=300)
plt.show()

#d）配对图基础样式四

import pingouin as pg
import matplotlib.pyplot as plt
df = pg.read_dataset('mixed_anova').query("Group == 'Meditation'")
df = df.query("Group == 'Meditation' and Subject > 40")
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
ax = pg.plot_paired(data=df, dv='Scores', within='Time',
               subject='Subject', orient='h',ax=ax)  
ax.grid(False)
plt.tight_layout()
fig.savefig('\第7章 其他类型图的绘制\图7-2-1配对图基础样式绘制示例_d.pdf',bbox_inches='tight')
fig.savefig('\第7章 其他类型图的绘制\图7-2-1配对图基础样式绘制示例_d.png', 
            bbox_inches='tight',dpi=300)
plt.show()