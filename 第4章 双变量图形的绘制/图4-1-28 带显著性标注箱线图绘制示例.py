
"""
编写时间：2022年4月12日 16：30

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


box_p_data = sns.load_dataset("iris")


# a）单组箱线图显著性标注
from statannotations.Annotator import Annotator
df = sns.load_dataset("tips")
x = "day"
y = "total_bill"
order = ['Sun', 'Thur', 'Fri', 'Sat']
colors = ["#2FBE8F","#459DFF","#FF5B9B","#FFCC37"]
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
ax = sns.boxplot(data=df, x=x, y=y, order=order,palette=colors,saturation=1,
                      width=.7,linewidth=1.2,ax=ax)
ax.set_xlabel("Time")
ax.set_ylabel("Values")

pairs=[("Thur", "Fri"), ("Thur", "Sat"), ("Fri", "Sun")]
annotator = Annotator(ax, pairs, data=df, x=x, y=y, order=order)
annotator.configure(test='Mann-Whitney', text_format='simple',line_height=0.03,line_width=1)
annotator.apply_and_annotate()

fig.savefig('\第4章 双变量图形的绘制\图4-1-28 带显著性标注箱线图绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-28 带显著性标注箱线图绘制示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()


# b）单组散点箱线图显著性标注

from statannotations.Annotator import Annotator
df = sns.load_dataset("tips")
x = "day"
y = "total_bill"
order = ['Sun', 'Thur', 'Fri', 'Sat']
colors = ["#2FBE8F","#459DFF","#FF5B9B","#FFCC37"]
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
ax = sns.boxplot(data=df, x=x, y=y, order=order,palette=colors,saturation=1,
                      width=.7,linewidth=1.2,whis=np.inf,ax=ax)
sns.stripplot(x=x, y=y, data=df,palette=colors,size=6,edgecolor="k",
                         linewidth=.6)
ax.set_xlabel("Time")
ax.set_ylabel("Values")

pairs=[("Thur", "Fri"), ("Thur", "Sat"), ("Fri", "Sun")]
annotator = Annotator(ax, pairs, data=df, x=x, y=y, order=order)
annotator.configure(test='Mann-Whitney', text_format='simple',line_height=0.03,line_width=1)
annotator.apply_and_annotate()

fig.savefig('\第4章 双变量图形的绘制\图4-1-28 带显著性标注箱线图绘制示例_b.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-28 带显著性标注箱线图绘制示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# c）分组箱线图显著性标注


from statannotations.Annotator import Annotator
df = sns.load_dataset("tips")

x = "day"
y = "total_bill"
hue = "smoker"
pairs = [(("Thur", "No"), ("Fri", "No")),
         (("Sat", "Yes"), ("Sat", "No")),
         (("Sun", "No"), ("Thur", "Yes"))]
colors = ["#2FBE8F","#459DFF"]

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
ax = sns.boxplot(data=df, x=x, y=y, hue=hue,palette=colors,saturation=1,width=.7,linewidth=1.2)
ax.set_xlabel("Time")
ax.set_ylabel("Values")

annot = Annotator(ax,pairs,data=df, x=x, y=y, hue=hue)
annot.configure(test='t-test_ind', text_format='full', loc='inside',
                comparisons_correction=None, line_height=0.05, line_width=1,text_offset=2)
annot.apply_test().annotate(line_offset_to_group=0.2, line_offset=0.1)
ax.legend(loc='upper left', bbox_to_anchor=(1.00, 1))
fig.savefig('\第4章 双变量图形的绘制\图4-1-28 带显著性标注箱线图绘制示例_c.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-28 带显著性标注箱线图绘制示例_c.png', 
            bbox_inches='tight',dpi=300)
plt.show()