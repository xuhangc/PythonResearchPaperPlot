
"""
编写时间：2022年4月18日 15：50

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

"""
此代码为使用Python-Prolot包进行学术风格图表绘制，绘图语法和Matplotlib有所不同，需注意。
"""
import pandas as pd
import numpy as np
import proplot as pplt
import seaborn as sns
from biokit.viz import corrplot #需要安装biokit库
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

# a）BioKit相关性矩阵热力图（circle）

#method="circle"
c = corrplot.Corrplot(heatmap_data.corr())
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
ax = c.plot(colorbar=True, method='circle', shrink=.9,fontsize=12,rotation=0,ax=ax)

fig.savefig('\第4章 双变量图形的绘制\图4-2-21 利用BioKit绘制的不同相关性矩阵热力图示例_a.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-2-21 利用BioKit绘制的不同相关性矩阵热力图示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# b）BioKit相关性矩阵热力图（square/rectangle）

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
c = corrplot.Corrplot(heatmap_data.corr())
ax = c.plot(colorbar=True, method='square', shrink=.9,fontsize=12,rotation=0,ax=ax)

fig.savefig('\第4章 双变量图形的绘制\图4-2-21 利用BioKit绘制的不同相关性矩阵热力图示例_b.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-2-21 利用BioKit绘制的不同相关性矩阵热力图示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# c）BioKit相关性矩阵热力图（ellipse）

#method='ellipse
c = corrplot.Corrplot(heatmap_data.corr())
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
ax = c.plot(colorbar=True, method='ellipse', shrink=.9,fontsize=12,rotation=0,ax=ax)

fig.savefig('\第4章 双变量图形的绘制\图4-2-21 利用BioKit绘制的不同相关性矩阵热力图示例_c.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-2-21 利用BioKit绘制的不同相关性矩阵热力图示例_c.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# d）BioKit相关性矩阵热力图（pie）
c = corrplot.Corrplot(heatmap_data.corr())
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
ax = c.plot(colorbar=True, method='pie', shrink=.9,fontsize=12,rotation=0,ax=ax)

fig.savefig('\第4章 双变量图形的绘制\图4-2-21 利用BioKit绘制的不同相关性矩阵热力图示例_d.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-2-21 利用BioKit绘制的不同相关性矩阵热力图示例_d.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# e）BioKit相关性矩阵热力图（text/number）

c = corrplot.Corrplot(heatmap_data.corr())
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
c.plot(colorbar=True, method='number', shrink=.8,fontsize=9,rotation=0,ax=ax)

fig.savefig('\第4章 双变量图形的绘制\图4-2-21 利用BioKit绘制的不同相关性矩阵热力图示例_e.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-2-21 利用BioKit绘制的不同相关性矩阵热力图示例_e.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# f）BioKit相关性矩阵热力图（color）
c = corrplot.Corrplot(heatmap_data.corr())
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
c.plot(colorbar=True, method='color', shrink=.8,fontsize=12,rotation=0,ax=ax)

fig.savefig('\第4章 双变量图形的绘制\图4-2-21 利用BioKit绘制的不同相关性矩阵热力图示例_f.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-2-21 利用BioKit绘制的不同相关性矩阵热力图示例_f.png', 
            bbox_inches='tight',dpi=300)
plt.show()


# g）BioKit相关性矩阵热力图（lower）

c = corrplot.Corrplot(heatmap_data.corr())
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
c.plot(colorbar=True, method='square', shrink=.9, lower='square',fontsize=12,ax=ax)

fig.savefig('\第4章 双变量图形的绘制\图4-2-21 利用BioKit绘制的不同相关性矩阵热力图示例_g.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-2-21 利用BioKit绘制的不同相关性矩阵热力图示例_g.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# h）BioKit相关性矩阵热力图（upper）
c = corrplot.Corrplot(heatmap_data.corr())
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
c.plot(colorbar=True, method='square', shrink=.9, upper='square',fontsize=12,ax=ax)

fig.savefig('\第4章 双变量图形的绘制\图4-2-21 利用BioKit绘制的不同相关性矩阵热力图示例_h.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-2-21 利用BioKit绘制的不同相关性矩阵热力图示例_h.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# i）BioKit相关性矩阵热力图（circle+square）
c = corrplot.Corrplot(heatmap_data.corr())

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
c.plot(colorbar=True, method='circle', shrink=.8, upper='circle',lower='square',
       fontsize=12,rotation=0,ax=ax)
       
fig.savefig('\第4章 双变量图形的绘制\图4-2-21 利用BioKit绘制的不同相关性矩阵热力图示例_i.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-2-21 利用BioKit绘制的不同相关性矩阵热力图示例_i.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# j）BioKit相关性矩阵热力图（ellipse+text）
c = corrplot.Corrplot(heatmap_data.corr())

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
c.plot(colorbar=True, method='ellipse', shrink=.8, upper='ellipse',lower='text',
       fontsize=9.5,rotation=0,ax=ax)

fig.savefig('\第4章 双变量图形的绘制\图4-2-21 利用BioKit绘制的不同相关性矩阵热力图示例_j.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-2-21 利用BioKit绘制的不同相关性矩阵热力图示例_j.png', 
            bbox_inches='tight',dpi=300)
plt.show()
