
"""
编写时间：2022年4月12日 21：50

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

"""
此代码为使用Python-Prolot包进行学术风格图表绘制，绘图语法和Matplotlib有所不同，需注意。
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from superviolin import test_plot,plot
from superviolin.plot import Superviolin

plt.rcParams["figure.facecolor"] = "w"
plt.rcParams["axes.spines.right"] = True
plt.rcParams["axes.spines.top"] = True
plt.rcParams['text.usetex'] = True


# a）高级”小提琴”图绘制样式1

file_name = r"demo_data.csv"
violin = Superviolin(filename=file_name,condition="drug",value="variable",dpi=100,cmap="Dark2",
                    linewidth=0.7,return_stats=True,stats_on_plot="yes")
violin.generate_plot()

fig.savefig('\第4章 双变量图形的绘制\图4-1-33 高级“小提琴”图绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-33 高级“小提琴”图绘制示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()


# b）高级”小提琴”图绘制样式2

file_name2 = r"multiple_conditions.csv"
violin = Superviolin(filename=file_name2,condition="condition",value="variable",cmap="Dark2",
                     replicate="replicate",dpi=100,linewidth=0.7)
violin.generate_plot()

fig.savefig('\第4章 双变量图形的绘制\图4-1-33 高级“小提琴”图绘制示例_b.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-33 高级“小提琴”图绘制示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()

