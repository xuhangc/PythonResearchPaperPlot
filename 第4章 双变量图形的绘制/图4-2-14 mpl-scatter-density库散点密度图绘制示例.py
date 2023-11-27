
"""
编写时间：2022年4月17日 14：30

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

import mpl_scatter_density

# 需安装SciencePlots 包（pip install SciencePlots）,注意最新版本引用方式
plt.style.use('science') # 设置全局绘图样式

# a）mpl-scatter-density库绘制散点密度图示例一

density_scatter = pd.read_excel(r"\第4章 双变量图形的绘制\相关性散点密度图.xlsx")
x,y = density_scatter["Values"],density_scatter["Estimated Values"]
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)

fig = plt.figure(figsize=(4,3.5),dpi=100,facecolor="w")
ax = fig.add_subplot(1, 1, 1, projection='scatter_density')
density = ax.scatter_density(x, y,cmap=parula,vmax=140,)
linreg = ax.plot(x, intercept + slope*x, 'r', label='Fitted Line',lw=.8)

colorbar = fig.colorbar(density,aspect=17,label="Number of points per pixel")
colorbar.ax.tick_params(left=True,direction="in",width=.4,labelsize=10)
colorbar.ax.tick_params(which="minor",right=False)
colorbar.outline.set_linewidth(.4)

# 添加文本信息
fontdict = {"size":14,"fontstyle":"italic","weight":"bold","color":"white"}
ax.text(-4,7.5,r'$R=$'+str(round(r_value,2)),fontdict=fontdict)
ax.text(-4,5.8,r'$y=$'+str(round(slope,2))+'$x$'+ str(round(intercept,3)),
        fontdict=fontdict)
ax.set_xlabel("Values")
ax.set_ylabel("Estimated Values")
legend = ax.legend(loc="lower right",frameon=False,labelspacing=.4,handletextpad=.5,fontsize=10)
for l,text in zip(legend.legendHandles,legend.get_texts()):
    text.set_color("white")
    l.set_linewidth(2)

fig.savefig('\第4章 双变量图形的绘制\图4-2-14 mpl-scatter-density库散点密度图绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-2-14 mpl-scatter-density库散点密度图绘制示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# b）mpl-scatter-density库绘制散点密度图示例二

import numpy as np
import matplotlib.pyplot as plt
import mpl_scatter_density  # noqa

fig = plt.figure(figsize=(4,3.5),dpi=100,facecolor="w")
ax = fig.add_subplot(1, 1, 1, projection='scatter_density')

n = 10000000

x = np.random.normal(0.5, 0.3, n)
y = np.random.normal(0.5, 0.3, n)
ax.scatter_density(x, y, color='#2C4AC7')

x = np.random.normal(1.0, 0.2, n)
y = np.random.normal(0.6, 0.2, n)
ax.scatter_density(x, y, color='#F5E61C')

ax.set_xlim(-0.5, 1.5)
ax.set_ylim(-0.5, 1.5)
ax.set_xlabel("Variable 01")
ax.set_ylabel("Variable 02")

fig.savefig('\第4章 双变量图形的绘制\图4-2-14 mpl-scatter-density库散点密度图绘制示例_b.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-2-14 mpl-scatter-density库散点密度图绘制示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()



