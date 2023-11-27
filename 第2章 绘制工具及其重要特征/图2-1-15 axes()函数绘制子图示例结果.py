"""
编写时间：2022年2月05日 16：30

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。

代码中Proplot包绘制的部分可能与Matplotlib绘制不同，需注意两者绘图语法的不同~~

"""

import pandas as pd
import numpy as np
import proplot as pplt
from colormaps import parula  #自定义的颜色系
import matplotlib.pyplot as plt

from proplot import rc
rc["font.family"] = "Times New Roman"
rc["axes.labelsize"] = 15
rc['tick.labelsize'] = 13
rc["suptitle.size"] = 15

# Fixing random state for reproducibility
np.random.seed(19680801)
#plt.figure(figsize=(6,4))
plt.subplot(211)
plt.imshow(np.random.random((100, 100)),cmap=parula)
plt.subplot(212)
plt.imshow(np.random.random((100, 100)),cmap=parula)

plt.subplots_adjust(bottom=0.1, right=0.8, top=0.9)
cax = plt.axes([0.85, 0.1, 0.075, 0.8])
plt.colorbar(cax=cax)


plt.savefig(r'\第2章 绘制工具及其重要特征\图2-1-15 axes()函数绘制子图示例结果.pdf',bbox_inches='tight')
plt.savefig(r'\第2章 绘制工具及其重要特征\图2-1-15 axes()函数绘制子图示例结果.png', 
            bbox_inches='tight',dpi=300)       
plt.show()

