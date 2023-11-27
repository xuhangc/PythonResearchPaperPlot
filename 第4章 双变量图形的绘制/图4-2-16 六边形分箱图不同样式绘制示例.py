
"""
编写时间：2022年4月17日 15：30

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

"""
此代码为使用Python-Prolot包进行学术风格图表绘制，绘图语法和Matplotlib有所不同，需注意。
"""

import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats
import matplotlib.pyplot as plt
from colormaps import parula

# 需安装SciencePlots 包（pip install SciencePlots）,注意最新版本引用方式
plt.style.use('science') # 设置全局绘图样式

hist2d_data = pd.read_csv(r"\第4章 双变量图形的绘制\hist2d_hexbin_data.csv")

x,y = hist2d_data["x values"],hist2d_data["y values"]

# a）hexbin()函数绘制六边形分箱图示例一

bins = 10
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
hexbin_fig = plt.hexbin(x=x,y=y,gridsize=bins,cmap=parula,mincnt=.9)
colorbar = plt.colorbar(aspect=14,label="Number of points per pixel")
colorbar.ax.tick_params(left=True,direction="in",width=.4,length=5,labelsize=10)
colorbar.ax.tick_params(which="minor",right=False)
colorbar.outline.set_linewidth(.4)
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("gridsize=%d"%bins,fontweight="bold")

fig.savefig('\第4章 双变量图形的绘制\图4-2-16 六边形分箱图不同样式绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-2-16 六边形分箱图不同样式绘制示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# b）hexbin()函数绘制六边形分箱图示例二

bins = 40
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
hexbin_fig = plt.hexbin(x=x,y=y,gridsize=bins,cmap=parula,mincnt=.9)
colorbar = plt.colorbar(aspect=14,label="Number of points per pixel")
colorbar.ax.tick_params(left=True,direction="in",width=.4,length=5,labelsize=10)
colorbar.ax.tick_params(which="minor",right=False)
colorbar.outline.set_linewidth(.4)
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("gridsize=%d"%bins,fontweight="bold")

fig.savefig('\第4章 双变量图形的绘制\图4-2-16 六边形分箱图不同样式绘制示例_b.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-2-16 六边形分箱图不同样式绘制示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()





