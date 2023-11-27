
"""
编写时间：2022年4月13日 20：50

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
from sinaplot import sinaplot  # 需要单独安装

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


violin_data = pd.read_excel(r"\第4章 双变量图形的绘制\小提琴图数据.xlsx")
violin_data['values'] = violin_data['values'].astype('float')

# a）无密度轮廓的密度缩放抖动图

colors = ["#2FBE8F","#459DFF","#FF5B9B"]
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
sina_plot = sinaplot(x="class",y="values",data=violin_data,palette=colors,saturation=1,
                     violin=False,ax=ax)
ax.set_xlabel("Class")
ax.set_ylabel("Values")
fig.savefig('\第4章 双变量图形的绘制\图4-1-34 不同样式密度缩放抖动图绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-34 不同样式密度缩放抖动图绘制示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# b）有密度轮廓的密度缩放抖动图

colors = ["#2FBE8F","#459DFF","#FF5B9B"]
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
sina_plot = sinaplot(x="class",y="values",data=violin_data,palette=colors,saturation=1,
                     violin=True,ax=ax)
ax.set_xlabel("Class")
ax.set_ylabel("Values")

fig.savefig('\第4章 双变量图形的绘制\图4-1-34 不同样式密度缩放抖动图绘制示例_b.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-34 不同样式密度缩放抖动图绘制示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# c）带统计p值的密度缩放抖动图

from statannotations.Annotator import Annotator
df = violin_data
x = "class"
y = "values"
order = ['cluster1', 'cluster2', 'cluster3',]
colors = ["#2FBE8F","#459DFF","#FF5B9B"]
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
sina_plot = sinaplot(x="class",y="values",data=violin_data,palette=colors,saturation=1,
                     violin=True,ax=ax)
ax.set_xlabel("Class")
ax.set_ylabel("Values")

pairs=[("cluster1", "cluster2"), ("cluster1", "cluster3"), ("cluster2", "cluster3")]
annotator = Annotator(ax, pairs, data=df, x=x, y=y, order=order)
annotator.configure(test='t-test_ind', text_format='simple',line_height=0.03,line_width=1)
annotator.apply_and_annotate()

fig.savefig('\第4章 双变量图形的绘制\图4-1-34 不同样式密度缩放抖动图绘制示例_c.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-34 不同样式密度缩放抖动图绘制示例_c.png', 
            bbox_inches='tight',dpi=300)
plt.show()


