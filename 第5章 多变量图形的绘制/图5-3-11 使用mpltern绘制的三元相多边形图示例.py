
"""
编写时间：2022年4月16日 13：50

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

"""
此代码为使用Python-Prolot包进行学术风格图表绘制，绘图语法和Matplotlib有所不同，需注意。
"""
import mpltern  
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

colors = ["#2FBE8F","#459DFF","#FF5B9B","#FFCC37","#751DFE"]

fig = plt.figure(figsize=(4.5, 4),dpi=100,facecolor="w")
ax = fig.add_subplot(projection='ternary')

ax.tick_params(length=8)
ax.grid(color="k",linewidth=0.5)
ax.set_tlabel('Top')
ax.set_llabel('Left')
ax.set_rlabel('Right')

t = [0.2, 0.4, 0.2]
l = [0.0, 0.2, 0.4]
r = [0.8, 0.4, 0.4]
ax.fill(t, l, r, color="#2FBE8F",zorder=2)

t = [0.4, 0.6, 0.6, 0.4]
l = [0.2, 0.2, 0.4, 0.4]
r = [0.4, 0.2, 0.0, 0.2]
ax.fill(t, l, r, color="#459DFF",zorder=2)

t = [0.2, 0.4, 0.4, 0.0, 0.0]
l = [0.4, 0.4, 0.6, 1.0, 0.6]
r = [0.4, 0.2, 0.0, 0.0, 0.4]
ax.fill(t, l, r, color="#FF5B9B",zorder=2)

ax.text(-0.2,0.7,0.5,s="Variable 1",fontsize=16, fontweight="bold")
ax.text(0.2,0.4,-.1,s="Variable 2",fontsize=16, fontweight="bold",rotation="60")
ax.text(0.2,-.02,0.35,s="Variable 3",fontsize=16, fontweight="bold",rotation="-60")
plt.savefig(r'\第5章 多变量图形的绘制\图5-3-11 使用mpltern绘制的三元相多边形图示例.pdf', bbox_inches='tight',)
plt.savefig(r'\第5章 多变量图形的绘制\图5-3-11 使用mpltern绘制的三元相多边形图示例.png', 
            bbox_inches='tight',dpi=600)
plt.show()