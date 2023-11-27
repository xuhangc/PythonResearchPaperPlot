
"""
编写时间：2022年5月06日 09：20

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。

代码中Proplot包绘制的部分可能与Matplotlib绘制不同，需注意两者绘图语法的不同~~

"""
#注意：本案例中引入的SciencePlots库主题方式会随着SciencePlots版本的更新发生改变，读者还需参考其官网引入的正确方式。
#      建议按照官网引入方式进行操作和使用最新版本的ScienePlots。如引入方式发生改变，请关注微信公众号【DataCharm】进行实时获取代码更新。

import numpy as np
import pandas as pd
import seaborn as sns
import proplot as pplt
import pingouin as pg
import matplotlib.pyplot as plt

from proplot import rc
rc["font.family"] = "Times New Roman"
rc["axes.labelsize"] = 15
rc["tick.labelsize"] = 12
rc["suptitle.size"] = 15
rc["title.size"] = 14

bal_df = pg.read_dataset("blandaltman")

fig,ax = plt.subplots(figsize=(5,3.5),dpi=100,facecolor="w")
ax = pg.plot_blandaltman(bal_df['A'], bal_df['B'],scatter_kws={"color":"red","ec":"k"},ax=ax)
ax.axhline(lw=2,color="b",zorder=0)
ax.grid(False)
plt.tight_layout()

fig.savefig('\第7章 其他类型图的绘制\图7-1-1 Bland-Altman图绘制示例.pdf',bbox_inches='tight')
fig.savefig('\第7章 其他类型图的绘制\图7-1-1 Bland-Altman图绘制示例.png', 
            bbox_inches='tight',dpi=300)
plt.show()