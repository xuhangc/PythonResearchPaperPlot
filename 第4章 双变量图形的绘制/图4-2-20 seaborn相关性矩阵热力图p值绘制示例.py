
"""
编写时间：2022年4月18日 14：50

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

from scipy.stats import pearsonr
pvals = heatmap_data.corr(method=lambda x, y: pearsonr(x, y)[1]) - np.eye(len(heatmap_data.columns)) 

#转换P值为星号
def convert_pvalue_to_asterisks(pvalue):
    if pvalue <= 0.001:
        return "***"
    elif pvalue <= 0.01:
        return "**"
    elif pvalue <= 0.05:
        return "*"
    return ""

pval_star = pvals.applymap(lambda x:convert_pvalue_to_asterisks(x))

# 转换成numpy 类型
corr_star_annot = pval_star.to_numpy()

# a）seaborn 相关性矩阵热力图p值绘制示例一

import matplotlib.pyplot as plt
from colormaps import parula
from matplotlib.ticker import FormatStrFormatter

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
sns.heatmap(heatmap_data.corr(),annot=corr_star_annot,fmt='',cmap=parula,vmin=-1, vmax=1,
            annot_kws={"size":13,"fontweight":"bold"},linecolor="k",linewidths=.2,
            cbar_kws={"aspect":13},ax=ax)
ax.tick_params(bottom=False, labelbottom=True,labeltop=False,left=False,pad=1,labelsize=12)
ax.yaxis.set_tick_params(labelrotation=0)
# 使用 matplotlib.colorbar.Colorbar object
cbar = ax.collections[0].colorbar
cbar.ax.tick_params(direction="in",width=.5,labelsize=10)
cbar.ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
cbar.outline.set_visible(True)
cbar.outline.set_linewidth(.5)

fig.savefig('\第4章 双变量图形的绘制\图4-2-20 seaborn相关性矩阵热力图p值绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-2-20 seaborn相关性矩阵热力图p值绘制示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# b）seaborn 相关性矩阵热力图p值绘制示例二

corr_labels = heatmap_data.corr().to_numpy()
p_labels = corr_star_annot
shape = corr_labels.shape
#合并labels
labels = (np.asarray(["{0:.2f}\n{1}".format(data,p) for data, p in zip(corr_labels.flatten(), p_labels.flatten())])).reshape(shape)

import matplotlib.pyplot as plt
from colormaps import parula
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
sns.heatmap(heatmap_data.corr(),annot=labels,fmt='',cmap=parula,vmin=-1, vmax=1,
            annot_kws={"size":7.5,"fontweight":"bold"},linecolor="k",linewidths=.2,
            cbar_kws={"aspect":13},ax=ax)
ax.tick_params(bottom=False, labelbottom=True,labeltop=False,left=False,pad=1,labelsize=12)
ax.yaxis.set_tick_params(labelrotation=0)
# 使用 matplotlib.colorbar.Colorbar object
cbar = ax.collections[0].colorbar
cbar.ax.tick_params(direction="in",width=.5,labelsize=10)
cbar.ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
cbar.outline.set_visible(True)
cbar.outline.set_linewidth(.5)

fig.savefig('\第4章 双变量图形的绘制\图4-2-20 seaborn相关性矩阵热力图p值绘制示例_b.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-2-20 seaborn相关性矩阵热力图p值绘制示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# c）seaborn 相关性矩阵热力图p值（colorbar）示例一

import matplotlib.pyplot as plt
from colormaps import parula
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
sns.heatmap(heatmap_data.corr(),annot=corr_star_annot,fmt='',cmap="BR",vmin=-1, vmax=1,
            annot_kws={"size":13,"fontweight":"bold"},linecolor="k",linewidths=.2,
            cbar_kws={"aspect":13},ax=ax)
ax.tick_params(bottom=False, labelbottom=True,labeltop=False,left=False,pad=1,labelsize=12)
ax.yaxis.set_tick_params(labelrotation=0)
# 使用 matplotlib.colorbar.Colorbar object
cbar = ax.collections[0].colorbar
cbar.ax.tick_params(direction="in",width=.5,labelsize=10)
cbar.ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
cbar.outline.set_visible(True)
cbar.outline.set_linewidth(.5)

fig.savefig('\第4章 双变量图形的绘制\图4-2-20 seaborn相关性矩阵热力图p值绘制示例_c.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-2-20 seaborn相关性矩阵热力图p值绘制示例_c.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# d）seaborn 相关性矩阵热力图p值（colorbar） 示例二

import matplotlib.pyplot as plt
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
sns.heatmap(heatmap_data.corr(),annot=corr_star_annot,fmt='',cmap="ColdHot",vmin=-1, vmax=1,
            annot_kws={"size":13,"fontweight":"bold"},linecolor="k",linewidths=.2,
            cbar_kws={"aspect":13},ax=ax)
ax.tick_params(bottom=False, labelbottom=True,labeltop=False,left=False,pad=1,labelsize=12)
ax.yaxis.set_tick_params(labelrotation=0)
# 使用 matplotlib.colorbar.Colorbar object
cbar = ax.collections[0].colorbar
cbar.ax.tick_params(direction="in",width=.5,labelsize=10)
cbar.ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
cbar.outline.set_visible(True)
cbar.outline.set_linewidth(.5)

fig.savefig('\第4章 双变量图形的绘制\图4-2-20 seaborn相关性矩阵热力图p值绘制示例_d.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-2-20 seaborn相关性矩阵热力图p值绘制示例_d.png', 
            bbox_inches='tight',dpi=300)
plt.show()

