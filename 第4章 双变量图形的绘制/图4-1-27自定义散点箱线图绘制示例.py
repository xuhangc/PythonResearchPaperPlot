"""
编写时间：2022年4月12日 15：30

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

"""
此代码为使用Python-Prolot包进行学术风格图表绘制，绘图语法和Matplotlib有所不同，需注意。
"""


import pandas as pd
import numpy as np
import seaborn as sns
from scipy import stats 
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["axes.linewidth"] = .8
plt.rcParams["axes.labelsize"] = 15
plt.rcParams["xtick.minor.visible"] = False
plt.rcParams["ytick.minor.visible"] = True
plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"
plt.rcParams["xtick.labelsize"] = 12
plt.rcParams["ytick.labelsize"] = 12
plt.rcParams["xtick.top"] = False
plt.rcParams["ytick.right"] = False


scatterbox = pd.read_excel(r"第4章 双变量图形的绘制\scatterbox_data.xlsx")

groups = sorted(scatterbox["group"].unique())
y_data = [scatterbox[scatterbox["group"] == group]["values"].values for group in groups]

# 自定义抖动散点所需要的x值
jitter = 0.06
x_data = [np.array([i] * len(d)) for i, d in enumerate(y_data)]
x_jittered = [x + stats.t(df=6, scale=jitter).rvs(len(x)) for x in x_data]

colors = ["#2FBE8F","#459DFF","#FF5B9B"]
labels = groups
fig,ax = plt.subplots(figsize=(5,3.5),dpi=100,facecolor="w")
boxplot = ax.boxplot(y_data, positions=[0,1,2],patch_artist=True,labels=labels,widths=.7,
                     medianprops={"color":"k","linewidth":2},showcaps=False)  
# 修改箱线图填充颜色
for patch, color in zip(boxplot['boxes'], colors):
    patch.set_facecolor(color)
# 添加抖动散点
for x, y, color in zip(x_jittered, y_data, colors):
    ax.scatter(x, y, s = 80, color=color, ec="k",lw=1,zorder=3)
ax.set_xlabel("Group")
ax.set_ylabel("Values")
ax.set(ylim=(0,25))

fig.savefig('\第4章 双变量图形的绘制\图4-1-27自定义散点箱线图绘制示例.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-27自定义散点箱线图绘制示例.png', 
            bbox_inches='tight',dpi=300)
plt.show()