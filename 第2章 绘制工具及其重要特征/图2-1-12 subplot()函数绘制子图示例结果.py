"""
编写时间：2022年2月05日 16：30

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。

代码中Proplot包绘制的部分可能与Matplotlib绘制不同，需注意两者绘图语法的不同~~

"""

import pandas as pd
import numpy as np
import proplot as pplt
import matplotlib.pyplot as plt

from proplot import rc
rc["font.family"] = "Times New Roman"
rc["axes.labelsize"] = 15
rc['tick.labelsize'] = 13
rc["suptitle.size"] = 15


plt.figure(figsize=(6,3),dpi=100,facecolor="w")
ax1 = plt.subplot(212)
ax1.text(0.5, 0.5, "subplot(212)", alpha=0.75, ha="center", va="center", weight="bold", size=12)
ax2 = plt.subplot(221)
ax2.text(0.5, 0.5, "subplot(221)", alpha=0.75, ha="center", va="center", weight="bold", size=12)
ax3 = plt.subplot(222)
ax3.text(0.5, 0.5, "subplot(222)", alpha=0.75, ha="center", va="center", weight="bold", size=12)

plt.tight_layout()
plt.savefig(r'\第2章 绘制工具及其重要特征\图2-1-12 subplot()函数绘制子图示例结果.pdf',bbox_inches='tight')
plt.savefig(r'\第2章 绘制工具及其重要特征\图2-1-12 subplot()函数绘制子图示例结果.png', 
            bbox_inches='tight',dpi=300)       
plt.show()
