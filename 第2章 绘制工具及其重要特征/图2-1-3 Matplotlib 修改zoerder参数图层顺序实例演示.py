"""
编写时间：2022年2月05日 10：00

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

r = np.linspace(0.3, 1, 30)
theta = np.linspace(0, 4*np.pi, 30)
x = r * np.sin(theta)
y = r * np.cos(theta)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6, 3.5),facecolor="w",sharey=True)
ax1.plot(x, y, 'C3', lw=4)
ax1.scatter(x, y, s=180,color="#FFCC37",ec="k",label="zorder=2")
ax1.set_title('Lines on top of dots',fontsize=15)
ax1.legend()
ax2.plot(x, y, 'C3', lw=4)
ax2.scatter(x, y, s=180, color="#FFCC37",ec="k",zorder=3,label="zorder=3")  # move dots on top of line
ax2.set_title('Dots on top of lines',fontsize=15)
ax2.legend()

plt.tight_layout()
plt.savefig(r'\第2章 绘制工具及其重要特征\图2-1-3 Matplotlib 修改zoerder参数图层顺序实例演示.pdf',bbox_inches='tight')
plt.savefig(r'\第2章 绘制工具及其重要特征\图2-1-3 Matplotlib 修改zoerder参数图层顺序实例演示.png', 
            bbox_inches='tight',dpi=300)
            
plt.show()

