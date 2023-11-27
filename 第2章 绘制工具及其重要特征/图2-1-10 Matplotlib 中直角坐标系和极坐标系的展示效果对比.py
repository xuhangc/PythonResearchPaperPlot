"""
编写时间：2022年2月05日 15：30

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。

代码中Proplot包绘制的部分可能与Matplotlib绘制不同，需注意两者绘图语法的不同~~

"""

import pandas as pd
import numpy as np
import proplot as pplt
import matplotlib.pyplot as plt

from proplot import rc
rc["font.family"] = "Times New Roman"
rc['tick.labelsize'] = 12
rc["suptitle.size"] = 15

# (a)直角坐标系中的柱形图示例
import matplotlib.pyplot as plt
import numpy as np
# make data:
np.random.seed(3)
x = 0.5 + np.arange(8)
y = np.random.uniform(2, 7, len(x))
# plot
fig, ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
ax.bar(x, y, width=.8, color="#2796EC",edgecolor="k", linewidth=0.7)

plt.tight_layout()
plt.savefig(r'\第2章 绘制工具及其重要特征\图2-1-10 Matplotlib 中直角坐标系和极坐标系的展示效果对比_a.pdf',bbox_inches='tight')
plt.savefig(r'\第2章 绘制工具及其重要特征\图2-1-10 Matplotlib 中直角坐标系和极坐标系的展示效果对比_a.png', 
            bbox_inches='tight',dpi=300)       
plt.show()

# (b)极坐标系中的柱形图示例
# make data:
np.random.seed(3)
x = 0.5 + np.arange(8)
y = np.random.uniform(2, 7, len(x))

fig, ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w",subplot_kw={'projection': 'polar'})
ax.bar(x, y, width=.6, color="#2796EC",edgecolor="k", linewidth=0.7,zorder=1)

plt.tight_layout()
plt.savefig(r'\第2章 绘制工具及其重要特征\图2-1-10 Matplotlib 中直角坐标系和极坐标系的展示效果对比_b.pdf',bbox_inches='tight')
plt.savefig(r'\第2章 绘制工具及其重要特征\图2-1-10 Matplotlib 中直角坐标系和极坐标系的展示效果对比_b.png', 
            bbox_inches='tight',dpi=300)       
plt.show()

# (c)直角坐标系中的散点图示例
# make the data
np.random.seed(3)
x = 4 + np.random.normal(0, 2, 24)
y = 4 + np.random.normal(0, 2, len(x))
# plot
fig, ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
ax.scatter(x, y, c="#FFCC37",s=180,ec="k")

plt.tight_layout()
plt.savefig(r'\第2章 绘制工具及其重要特征\图2-1-10 Matplotlib 中直角坐标系和极坐标系的展示效果对比_c.pdf',bbox_inches='tight')
plt.savefig(r'\第2章 绘制工具及其重要特征\图2-1-10 Matplotlib 中直角坐标系和极坐标系的展示效果对比_c.png', 
            bbox_inches='tight',dpi=300)       
plt.show()

# (d)极坐标系中的散点图示例
# make the data
np.random.seed(3)
x = 4 + np.random.normal(0, 2, 24)
y = 4 + np.random.normal(0, 2, len(x))
# plot
fig, ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w",subplot_kw={'projection': 'polar'})
ax.scatter(x, y, c="#FFCC37",s=180,ec="k",zorder=3)
ax.set_ylim(0,9)
plt.tight_layout()
plt.savefig(r'\第2章 绘制工具及其重要特征\图2-1-10 Matplotlib 中直角坐标系和极坐标系的展示效果对比_d.pdf',bbox_inches='tight')
plt.savefig(r'\第2章 绘制工具及其重要特征\图2-1-10 Matplotlib 中直角坐标系和极坐标系的展示效果对比_d.png', 
            bbox_inches='tight',dpi=300)       
plt.show()
