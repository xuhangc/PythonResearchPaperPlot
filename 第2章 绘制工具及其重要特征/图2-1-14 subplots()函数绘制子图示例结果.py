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


fig, axs = plt.subplots(2, 3,figsize=(6,4),dpi=100,sharex=True, sharey=True)
axs[0,0].text(0.5, 0.5, "subplots(0,0)", alpha=0.75, ha="center", va="center", weight="bold", size=12)
axs[0,1].text(0.5, 0.5, "subplots(0,1)", alpha=0.75, ha="center", va="center", weight="bold", size=12)
axs[0,2].text(0.5, 0.5, "subplots(0,2)", alpha=0.75, ha="center", va="center", weight="bold", size=12)
axs[1,0].text(0.5, 0.5, "subplots(1,0)", alpha=0.75, ha="center", va="center", weight="bold", size=12)
axs[1,1].text(0.5, 0.5, "subplots(1,1)", alpha=0.75, ha="center", va="center", weight="bold", size=12)
axs[1,2].text(0.5, 0.5, "subplots(1,2)", alpha=0.75, ha="center", va="center", weight="bold", size=12)

plt.tight_layout()
plt.savefig(r'\第2章 绘制工具及其重要特征\图2-1-14 subplots()函数绘制子图示例结果.pdf',bbox_inches='tight')
plt.savefig(r'\第2章 绘制工具及其重要特征\图2-1-14 subplots()函数绘制子图示例结果.png', 
            bbox_inches='tight',dpi=300)       
plt.show()

