
"""
编写时间：2022年4月18日 14：30

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

"""
此代码为使用Python-Prolot包进行学术风格图表绘制，绘图语法和Matplotlib有所不同，需注意。
"""
import pandas as pd
import numpy as np
import proplot as pplt
import seaborn as sns
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

from proplot import rc
rc["axes.labelsize"] = 15
rc['tick.labelsize'] = 13
rc["suptitle.size"] = 15
rc["font.family"] = "Times New Roman"
rc["xtick.minor.visible"] = False
rc["ytick.minor.visible"] = False
rc["xtick.bottom"] = False
rc["ytick.left"] = False

heatmap_data = pd.read_excel(r"\第4章 双变量图形的绘制\相关性热力图_P值.xlsx")


# a）seaborn相关性矩阵热力图样式一

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
sns.heatmap(heatmap_data.corr(),annot=True,fmt='.2f',cmap=parula,vmin=-1, vmax=1,
            annot_kws={"size":8,"fontweight":"bold"},linecolor="k",linewidths=.2,
            cbar_kws={"aspect":13},ax=ax)
ax.yaxis.set_tick_params(labelrotation=0)
# 使用 matplotlib.colorbar.Colorbar object
cbar = ax.collections[0].colorbar
cbar.ax.tick_params(direction="in",width=.5,labelsize=10)
cbar.ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
cbar.outline.set_visible(True)
cbar.outline.set_linewidth(.5)

fig.savefig('\第4章 双变量图形的绘制\图4-2-19 利用seaborn绘制的相关性矩阵热力图示例_a.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-2-19 利用seaborn绘制的相关性矩阵热力图示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# b）seaborn相关性矩阵热力图样式二（下三角）
corr_df = heatmap_data.corr()
np.tril(np.ones(corr_df.shape))

mask2 = np.tril(np.ones(corr_df.shape))
lower_triang_df = corr_df.where(np.tril(np.ones(corr_df.shape)).astype(np.bool))

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
sns.heatmap(lower_triang_df,annot=True,fmt='.2f',cmap=parula,vmin=-1, vmax=1,
            annot_kws={"size":8,"fontweight":"bold"},linecolor="k",linewidths=.2,
             cbar_kws={"aspect":13},ax=ax)

ax.yaxis.set_tick_params(labelrotation=0)
# 使用 matplotlib.colorbar.Colorbar object
cbar = ax.collections[0].colorbar
cbar.ax.tick_params(direction="in",width=.5,labelsize=10)
cbar.ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
cbar.outline.set_visible(True)
cbar.outline.set_linewidth(.5)

fig.savefig('\第4章 双变量图形的绘制\图4-2-19 利用seaborn绘制的相关性矩阵热力图示例_b.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-2-19 利用seaborn绘制的相关性矩阵热力图示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# c）seaborn相关性矩阵热力图样式三（上三角）

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
cor_up = heatmap_data.corr().where(np.triu(np.ones(heatmap_data.corr().shape)).astype(np.bool))
sns.heatmap(cor_up,annot=True,fmt='.2f',cmap=parula,vmin=-1, vmax=1,
            annot_kws={"size":8,"fontweight":"bold"},linecolor="k",linewidths=.2,
            cbar_kws={"aspect":13},ax=ax)
ax.yaxis.set_tick_params(labelrotation=0)
# 使用 matplotlib.colorbar.Colorbar object
cbar = ax.collections[0].colorbar
cbar.ax.tick_params(direction="in",width=.5,labelsize=10)
cbar.ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
cbar.outline.set_visible(True)
cbar.outline.set_linewidth(.5)

fig.savefig('\第4章 双变量图形的绘制\图4-2-19 利用seaborn绘制的相关性矩阵热力图示例_c.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-2-19 利用seaborn绘制的相关性矩阵热力图示例_c.png', 
            bbox_inches='tight',dpi=300)
plt.show()


# d）seaborn相关性矩阵热力图样式四（相关性数值和颜色块组合）

import matplotlib.pyplot as plt
from colormaps import parula
from matplotlib.ticker import FormatStrFormatter
from matplotlib.colors import ListedColormap

labels = heatmap_data.corr().where(np.triu(np.ones(heatmap_data.corr().shape)).astype(np.bool))

mask = np.zeros_like(heatmap_data.corr())
mask[np.triu_indices_from(mask)] = True
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")

sns.heatmap(heatmap_data.corr(),annot=False,mask=mask,cmap=parula,vmin=-1, vmax=1,
            annot_kws={"size":8,"fontweight":"bold"},linecolor="k",linewidths=.2,
            cbar_kws={"aspect":13},ax=ax)

sns.heatmap(labels,annot=True,fmt='.2f',cmap= ListedColormap(['white']),vmin=-1, vmax=1,
            annot_kws={"size":8,"fontweight":"bold"},linecolor="k",linewidths=.2,
            cbar=False,ax=ax)

ax.yaxis.set_tick_params(labelrotation=0)
# 使用 matplotlib.colorbar.Colorbar object
cbar = ax.collections[0].colorbar
cbar.ax.tick_params(direction="in",width=.5,labelsize=10)
cbar.ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
cbar.outline.set_visible(True)
cbar.outline.set_linewidth(.5)

fig.savefig('\第4章 双变量图形的绘制\图4-2-19 利用seaborn绘制的相关性矩阵热力图示例_d.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-2-19 利用seaborn绘制的相关性矩阵热力图示例_d.png', 
            bbox_inches='tight',dpi=300)
plt.show()
