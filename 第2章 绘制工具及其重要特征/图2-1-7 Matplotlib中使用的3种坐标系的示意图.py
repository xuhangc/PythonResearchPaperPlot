
"""
编写时间：2022年2月05日 10：50

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。

代码中Proplot包绘制的部分可能与Matplotlib绘制不同，需注意两者绘图语法的不同~~

"""

import pandas as pd
import numpy as np
import proplot as pplt
import matplotlib.pyplot as plt

#(a)直角坐标系
# Select length of axes and the space between tick labels
xmin, xmax, ymin, ymax = -5, 5, -5, 5
ticks_frequency = 1

# Plot points
fig, ax = plt.subplots(figsize=(3, 3))

# Set identical scales for both axes
ax.set(xlim=(xmin-1, xmax+1), ylim=(ymin-1, ymax+1), aspect='equal')

# Set bottom and left spines as x and y axes of coordinate system
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')
# Remove top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Create 'x' and 'y' labels placed at the end of the axes
ax.set_xlabel('x', size=8, labelpad=-24, x=1.03)
ax.set_ylabel('y', size=8, labelpad=-21, y=1.02, rotation=0)

# Create custom major ticks to determine position of tick labels
x_ticks = np.arange(xmin, xmax+1, ticks_frequency)
y_ticks = np.arange(ymin, ymax+1, ticks_frequency)
# ax.set_xticks(x_ticks[x_ticks != 0])
# ax.set_yticks(y_ticks[y_ticks != 0])
ax.set_xticks([])
ax.set_yticks([])
# Create minor ticks placed at each integer to enable drawing of minor grid
# lines: note that this has no effect in this example with ticks_frequency=1
ax.set_xticks(np.arange(xmin, xmax+1), minor=True)
ax.set_yticks(np.arange(ymin, ymax+1), minor=True)

# Draw major and minor grid lines
ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)

# Draw arrows
arrow_fmt = dict(markersize=4, color='black', clip_on=False)
ax.plot((1), (0), marker='>', transform=ax.get_yaxis_transform(), **arrow_fmt)
ax.plot((0), (1), marker='^', transform=ax.get_xaxis_transform(), **arrow_fmt)
plt.savefig(r'\第2章 绘制工具及其重要特征\图2-1-7 Matplotlib中使用的3种坐标系的示意图_a.pdf',bbox_inches='tight')
plt.savefig(r'\第2章 绘制工具及其重要特征\图2-1-7 Matplotlib中使用的3种坐标系的示意图_a.png', 
            bbox_inches='tight',dpi=300)       
plt.show()

#(b)极坐标系

import pandas as pd
import numpy as np
import proplot as pplt
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Times New Roman"

fig, ax = plt.subplots(figsize=(3, 3),subplot_kw={'projection': 'polar'})
plt.savefig(r'\第2章 绘制工具及其重要特征\图2-1-7 Matplotlib中使用的3种坐标系的示意图_b.pdf',bbox_inches='tight')
plt.savefig(r'\第2章 绘制工具及其重要特征\图2-1-7 Matplotlib中使用的3种坐标系的示意图_b.png', 
            bbox_inches='tight',dpi=300)       
plt.show()


#(c)地理坐标系

import pandas as pd
import numpy as np
import proplot as pplt
import matplotlib.pyplot as plt

from proplot import rc
rc["font.family"] = "Times New Roman"
rc['tick.labelsize'] = 12
rc["suptitle.size"] = 15

fig, ax = plt.subplots(figsize=(3, 3),subplot_kw={'projection': 'lambert'})
plt.grid(True)

plt.savefig(r'\第2章 绘制工具及其重要特征\图2-1-7 Matplotlib中使用的3种坐标系的示意图_c.pdf',bbox_inches='tight')
plt.savefig(r'\第2章 绘制工具及其重要特征\图2-1-7 Matplotlib中使用的3种坐标系的示意图_c.png', 
            bbox_inches='tight',dpi=300)       
plt.show()











