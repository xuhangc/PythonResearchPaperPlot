"""
编写时间：2022年2月05日 10：20

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。

代码中Proplot包绘制的部分可能与Matplotlib绘制不同，需注意两者绘图语法的不同~~

"""

import pandas as pd
import numpy as np
import proplot as pplt
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter, FixedLocator

from proplot import rc
rc["font.family"] = "Times New Roman"
rc['tick.labelsize'] = 12
rc["suptitle.size"] = 15

np.random.seed(19680801)
# make up some data in the interval ]0, 1[
y = np.random.normal(loc=0.5, scale=0.4, size=1000)
y = y[(y > 0) & (y < 1)]
y.sort()
x = np.arange(len(y))

# plot with various axes scales
fig, axs = plt.subplots(2, 2, figsize=(6, 4.5),
                        constrained_layout=True)
# linear
ax = axs[0, 0]
ax.plot(x, y,color="#2FBE8F",lw=3)
ax.set_yscale('linear')
ax.set_title('linear')
ax.grid(True)
# log
ax = axs[0, 1]
ax.plot(x, y,color="#2FBE8F",lw=3)
ax.set_yscale('log')
ax.set_title('log')
ax.grid(True)
# symmetric log
ax = axs[1, 1]
ax.plot(x, y - y.mean(),color="#2FBE8F",lw=3)
ax.set_yscale('symlog', linthresh=0.02)
ax.set_title('symlog')
ax.grid(True)
# logit
ax = axs[1, 0]
ax.plot(x, y,color="#2FBE8F",lw=3)
ax.set_yscale('logit')
ax.set_title('logit')
ax.grid(True)

plt.tight_layout()
plt.savefig(r'\第2章 绘制工具及其重要特征\图2-1-4 Matplotlib库中4种轴比例方式的绘制效果.pdf',bbox_inches='tight')
plt.savefig(r'\第2章 绘制工具及其重要特征\图2-1-4 Matplotlib库中4种轴比例方式的绘制效果.png', 
            bbox_inches='tight',dpi=300)
            
plt.show()


