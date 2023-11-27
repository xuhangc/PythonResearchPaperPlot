
"""
编写时间：2022年4月18日 16：50

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

"""
此代码为使用Python-Prolot包进行学术风格图表绘制，绘图语法和Matplotlib有所不同，需注意。
"""
import pandas as pd
import numpy as np
import proplot as pplt
import seaborn as sns
from biokit.viz import corrplot #需要安装biokit库
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from colormaps import parula

from proplot import rc
rc["axes.labelsize"] = 15
rc['tick.labelsize'] = 13
rc["suptitle.size"] = 15
rc["figure.facecolor"]="w"
rc["font.family"] = "Times New Roman"
rc["xtick.minor.visible"] = False
rc["ytick.minor.visible"] = False
rc["xtick.bottom"] = False
rc["ytick.left"] = False

# a）seaborn jointplot()边际组合图样式一
penguins = sns.load_dataset("penguins")
sns.jointplot(data=penguins, x="bill_length_mm", y="bill_depth_mm", 
              hue="species")
fig.savefig('\第4章 双变量图形的绘制\图4-2-22 seaborn不同样式边际组合图绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-2-22 seaborn不同样式边际组合图绘制示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# b）seaborn jointplot()边际组合图样式二

tips = sns.load_dataset("tips")
sns.jointplot(x="total_bill", y="tip", data=tips,
              xlim=(0, 60), ylim=(0, 12), color='k')
              
fig.savefig('\第4章 双变量图形的绘制\图4-2-22 seaborn不同样式边际组合图绘制示例_b.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-2-22 seaborn不同样式边际组合图绘制示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()             
              

# c）seaborn jointplot()边际组合图样式三

tips = sns.load_dataset("tips")
g = sns.jointplot(x="total_bill", y="tip", data=tips, kind="reg", 
                  scatter=False,
                  xlim=(0, 60), ylim=(0, 12), color='k')
sns.scatterplot(data=tips, x='total_bill', y='tip',
                hue='size', palette='husl',
                size='size', sizes=(10, 200), legend='full',
                ax=g.ax_joint)
                
fig.savefig('\第4章 双变量图形的绘制\图4-2-22 seaborn不同样式边际组合图绘制示例_c.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-2-22 seaborn不同样式边际组合图绘制示例_c.png', 
            bbox_inches='tight',dpi=300)
plt.show()                
                

# d）seaborn JointGrid()边际组合图样式

planets = sns.load_dataset("planets")

g = sns.JointGrid(data=planets, x="year", y="distance")
g.ax_joint.set(yscale="log")

# Create an inset legend for the histogram colorbar
cax = g.figure.add_axes([.18, .55, .02, .2])

# Add the joint and marginal histogram plots
g.plot_joint(
    sns.histplot, discrete=(True, False),
    cmap=parula, pmax=.8, cbar=True, cbar_ax=cax)
g.plot_marginals(sns.histplot, element="step", color="#2C4AC7")
plt.tight_layout()

fig.savefig('\第4章 双变量图形的绘制\图4-2-22 seaborn不同样式边际组合图绘制示例_d.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-2-22 seaborn不同样式边际组合图绘制示例_d.png', 
            bbox_inches='tight',dpi=300)
plt.show()
