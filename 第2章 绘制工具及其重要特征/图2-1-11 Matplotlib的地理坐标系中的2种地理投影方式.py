"""
编写时间：2022年2月05日 15：50

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。

代码中Proplot包绘制的部分可能与Matplotlib绘制不同，需注意两者绘图语法的不同~~

"""

import pandas as pd
import numpy as np
import proplot as pplt
import matplotlib.pyplot as plt

from proplot import rc
rc["font.family"] = "Times New Roman"


#(a)Lambert 投影方式
rc['tick.labelsize'] = 6
fig, ax = plt.subplots(figsize=(3, 2),subplot_kw={'projection': 'lambert'})
plt.grid(True)

plt.tight_layout()
plt.savefig(r'\第2章 绘制工具及其重要特征\图2-1-11 Matplotlib的地理坐标系中的2种地理投影方式_a.pdf',bbox_inches='tight')
plt.savefig(r'\第2章 绘制工具及其重要特征\图2-1-11 Matplotlib的地理坐标系中的2种地理投影方式_a.png', 
            bbox_inches='tight',dpi=300)       
plt.show()

#(b)Mollweide 投影方式
rc['tick.labelsize'] = 8
fig, ax = plt.subplots(figsize=(3, 2),subplot_kw={'projection': 'mollweide'})
plt.grid(True)

plt.tight_layout()
plt.savefig(r'\第2章 绘制工具及其重要特征\图2-1-11 Matplotlib的地理坐标系中的2种地理投影方式_b.pdf',bbox_inches='tight')
plt.savefig(r'\第2章 绘制工具及其重要特征\图2-1-11 Matplotlib的地理坐标系中的2种地理投影方式_b.png', 
            bbox_inches='tight',dpi=300)       
plt.show()


