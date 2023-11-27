

"""
编写时间：2022年4月11日 20：30

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

"""
此代码为使用Python-Prolot包进行学术风格图表绘制，绘图语法和Matplotlib有所不同，需注意。
"""

import pandas as pd
import numpy as np
import seaborn as sns
import proplot as pplt
import matplotlib.pyplot as plt

from proplot import rc
rc["font.family"] = "Times New Roman"
rc["axes.labelsize"] = 15
rc["tick.labelsize"] = 13
rc["suptitle.size"] = 15
rc["title.size"] = 14
rc["tick.minor"] = False


#a）自定义方法单组p值添加

iris = sns.load_dataset("iris")
data_p = iris[["sepal_length","species"]]

#计算P值
import scipy
stat,p_value = scipy.stats.ttest_ind(data_p[data_p["species"]=="setosa"]["sepal_length"],
                                     data_p[data_p["species"]=="versicolor"]["sepal_length"],
                                     equal_var=False)

# 定义函数进行P值和星号转换
def convert_pvalue_to_asterisks(pvalue):
    if pvalue <= 0.0001:
        return "****"
    elif pvalue <= 0.001:
        return "***"
    elif pvalue <= 0.01:
        return "**"
    elif pvalue <= 0.05:
        return "*"
    return "ns"
p_value_cov = convert_pvalue_to_asterisks(p_value)

palette=["#BC3C29FF","#0072B5FF","#E18727FF"]

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
ax = sns.barplot(x="species",y="sepal_length",data=iris,palette=palette,
                 estimator=np.mean,ci="sd", capsize=.1,errwidth=1,errcolor="k",
                 ax=ax,saturation=1,**{"edgecolor":"k","linewidth":1})
# 添加P值
x1, x2 = 0, 1
y,h = data_p["sepal_length"].mean()+1,.2
#绘制横线位置
ax.plot([x1, x1, x2, x2], [y, y+h, y+h, y], lw=1, c="k") 
#添加P值
ax.text((x1+x2)*.5, y+h, "T-test: "+ p_value_cov, ha='center', va='bottom', color="k")

ax.tick_params(which='major',direction='in',length=3,width=1.,labelsize=14,bottom=False)
for spine in ["top","left","right"]:
    ax.spines[spine].set_visible(False)
ax.spines['bottom'].set_linewidth(1.5)
ax.set_ylim(0,8)
plt.tight_layout()
fig.savefig('\第4章 双变量图形的绘制\图4-1-20 带p值误差柱形图绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-20 带p值误差柱形图绘制示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()


group_data = pd.read_excel(r"\第4章 双变量图形的绘制\分组误差柱形图数据.xlsx")

# b）statannotations 组内p值添加
from statannotations.Annotator import Annotator
palettea = ["#BC3C29FF","#0072B5FF"]

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
ax = sns.barplot(x="order",y="value",hue="class",data=group_data,palette=palette,ci="sd",
                 capsize=.1,errwidth=1,errcolor="k",ax=ax,saturation=1,
                 **{"edgecolor":"k","linewidth":1})

# 添加P值
box_pairs = [(("one","type01"),("one","type02")),
             (("two","type01"),("two","type02")),
             (("three","type01"),("three","type02"))]
annot = Annotator(ax, pairs=box_pairs,data=group_data,x="order",y="value",
                  hue="class")
annot.configure(test='t-test_ind',text_format='star',
                line_offset_to_group=.01,line_height=0.03,line_width=1)
annot.apply_and_annotate()

ax.tick_params(which='major',direction='in',length=3,width=1.,bottom=False)
for spine in ["top","left","right"]:
    ax.spines[spine].set_visible(False)
# 设置图例
ax.legend(title="Class")
ax.spines['bottom'].set_linewidth(1.5)
plt.tight_layout()

fig.savefig('\第4章 双变量图形的绘制\图4-1-20 带p值误差柱形图绘制示例_b.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-20 带p值误差柱形图绘制示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# c）statannotations 组间p值添加
from statannotations.Annotator import Annotator
palette = ["#BC3C29FF","#0072B5FF"]

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
ax = sns.barplot(x="order",y="value",hue="class",data=group_data,palette=palette,ci="sd",
                 capsize=.1,errwidth=1,errcolor="k",ax=ax,saturation=1,
                 **{"edgecolor":"k","linewidth":1})
# 添加P值
box_pairs = [(("one","type01"),("two","type01")),
             (("one","type02"),("two","type02")),
             (("one","type01"),("three","type01")),
             (("one","type02"),("three","type02")),
             (("two","type01"),("three","type01")),
             (("two","type02"),("three","type02"))]
annot = Annotator(ax, pairs=box_pairs,data=group_data, x="order",
                    y="value",hue="class")
annot.configure(test='t-test_ind',text_format='star',
                line_offset_to_group=.01,line_height=0.03,line_width=1)
annot.apply_and_annotate()

ax.tick_params(which='major',direction='in',length=3,width=1.,bottom=False)
for spine in ["top","left","right"]:
    ax.spines[spine].set_visible(False)
# 设置图例
ax.legend(title="Class",loc='upper left')
ax.spines['bottom'].set_linewidth(1.5)
plt.tight_layout()

fig.savefig('\第4章 双变量图形的绘制\图4-1-20 带p值误差柱形图绘制示例_c.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-1-20 带p值误差柱形图绘制示例_c.png', 
            bbox_inches='tight',dpi=300)
plt.show()
