"""
编写时间：2022年2月05日 14：30

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。

代码中Proplot包绘制的部分可能与Matplotlib绘制不同，需注意两者绘图语法的不同~~

"""

import pandas as pd
import numpy as np
import proplot as pplt
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from proplot import rc
rc["font.family"] = "Times New Roman"
rc['tick.labelsize'] = 12
rc["suptitle.size"] = 15

pi = np.pi
theta=np.arange(0,2*pi,0.02)#极角，弧度制
r1 = 1*(1 -np.sin(theta))
r2 = 3+ np.cos(7* theta)

#(a) Matplotlib中的极坐标系绘图示例1

fig, ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w",subplot_kw={'projection': 'polar'})
ax.plot(theta, r1, "k",lw=1)
plt.savefig(r'\第2章 绘制工具及其重要特征\图2-1-9 Matplotlib中的极坐标系绘图示例_a.pdf',bbox_inches='tight')
plt.savefig(r'\第2章 绘制工具及其重要特征\图2-1-9 Matplotlib中的极坐标系绘图示例_a.png', 
            bbox_inches='tight',dpi=300)       
plt.show()


#(b)Matplotlib中的极坐标系绘图示例2
fig, ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w",subplot_kw={'projection': 'polar'})
ax.plot(theta, r2, "k",lw=1)
plt.savefig(r'\第2章 绘制工具及其重要特征\图2-1-9 Matplotlib中的极坐标系绘图示例_b.pdf',bbox_inches='tight')
plt.savefig(r'\第2章 绘制工具及其重要特征\图2-1-9 Matplotlib中的极坐标系绘图示例_b.png', 
            bbox_inches='tight',dpi=300)       
plt.show()

