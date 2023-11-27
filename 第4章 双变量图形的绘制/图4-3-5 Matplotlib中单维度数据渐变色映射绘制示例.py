
"""
编写时间：2022年4月18日 19：50

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

"""
此代码为使用Python-Prolot包进行学术风格图表绘制，绘图语法和Matplotlib有所不同，需注意。
"""
import pandas as pd
import numpy as np
import proplot as pplt
import seaborn as sns
import matplotlib.pyplot as plt
from bioinfokit import analys, visuz #需安装bioinfokit库
from proplot import rc
from colormaps import parula
rc["axes.labelsize"] = 15
rc['tick.labelsize'] = 13
rc["suptitle.size"] = 15
rc["figure.facecolor"]="w"
rc["font.family"] = "Times New Roman"
rc["xtick.minor.visible"] = False
rc["ytick.minor.visible"] = False
rc["xtick.bottom"] = False
rc["ytick.left"] = False


volcano_data  = analys.get_data('volcano').data

volcano_data["logpv_add_axy"] = -(np.log10(volcano_data["p-value"]))
x=volcano_data['log2FC']
y=volcano_data['logpv_add_axy']
lfc_thr=(1, 1)
pv_thr=(0.05, 0.05)

from mpl_toolkits.axes_grid1.inset_locator import inset_axes

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
volcano = ax.scatter(x,y,s=15,c=x,ec="k",lw=.1,cmap=parula)
ax.grid(False)

ax.axhline(y=-np.log10(pv_thr[0]), linestyle='--', color='#7d7d7d', linewidth=1)
ax.axvline(x=lfc_thr[0], linestyle='--', color='#7d7d7d', linewidth=1)
ax.axvline(x=-lfc_thr[1], linestyle='--', color='#7d7d7d', linewidth=1)

# 添加调整位置colorbar
axins = inset_axes(ax,
                    width="7%",  
                    height="40%",
                    loc='upper left',
                    bbox_transform=ax.transAxes,
                    bbox_to_anchor=(0, 0., 1, 1),
                    borderpad=3)

cbar = fig.colorbar(volcano,cax=axins)
cbar.ax.tick_params(left=True,labelleft=True,labelright=False,direction="in",width=.4,labelsize=10)
cbar.ax.tick_params(which="minor",right=False)
cbar.ax.set_title(r'$ log_{2}(Fold Change)$',fontsize=9)
cbar.outline.set_linewidth(.4)

ax.set(xlim=(-6,6),ylim=(0,61),xlabel=r'$ log_{2}(Fold Change)$',ylabel=r'$ -log_{10}(P-value)$')
plt.tight_layout()
fig.savefig('\第4章 双变量图形的绘制\图4-3-5 Matplotlib中单维度数据渐变色映射绘制示例.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-3-5 Matplotlib中单维度数据渐变色映射绘制示例.png', 
            bbox_inches='tight',dpi=300)
plt.show()    

