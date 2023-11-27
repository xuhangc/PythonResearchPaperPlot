"""
编写时间：2022年5月06日 09：50

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。

代码中Proplot包绘制的部分可能与Matplotlib绘制不同，需注意两者绘图语法的不同~~

"""
#注意：本案例中引入的SciencePlots库主题方式会随着SciencePlots版本的更新发生改变，读者还需参考其官网引入的正确方式。
#      建议按照官网引入方式进行操作和使用最新版本的ScienePlots。如引入方式发生改变，请关注微信公众号【DataCharm】进行实时获取代码更新。

import scipy
import numpy as np
import pandas as pd
import pingouin as pg
import matplotlib.pyplot as plt
from proplot import rc
rc["xtick.minor.visible"] = False
rc["ytick.minor.visible"] = False


df = pg.read_dataset('mixed_anova').query("Time != 'January'")
df = df.query("Group == 'Meditation' and Subject > 40")

August_scor = df.loc[df["Time"]=="August","Scores"].to_numpy()
June_scor = df.loc[df["Time"]=="June","Scores"].to_numpy()

stat,p_value = scipy.stats.ttest_ind(August_scor,June_scor,equal_var=False)

# *号转换
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

# a）添加显著性水平配对T检验图样式一

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
ax = pg.plot_paired(data=df, dv='Scores', within='Time',
                    subject='Subject', 
                    boxplot_kwargs={"linewidth":1},
                    ax=ax)
# 添加P值信息
x1, x2 = 0, 1
y,h = 8.8,.15
#绘制横线位置
ax.plot([x1, x1, x2, x2], [y, y+h, y+h, y], lw=.8, c="k") 
#添加P值属性
ax.text((x1+x2)*.5, y+h, p_value_cov, ha='center', va='bottom', color="k",fontsize=15,
        fontweight="bold")
# 修饰
ax.grid(False)
plt.tight_layout()
fig.savefig('\第7章 其他类型图的绘制\图7-2-2 配对T检验图绘制样式示例_a.pdf',bbox_inches='tight')
fig.savefig('\第7章 其他类型图的绘制\图7-2-2 配对T检验图绘制样式示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# b）添加显著性水平配对T检验图样式二

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
pg.plot_paired(data=df, dv='Scores', within='Time',
               subject='Subject', ax=ax, boxplot=False,
               colors=['k', 'k', 'k'])  
# 添加P值信息
x1, x2 = 0, 1
y,h = 8.8,.15
#绘制横线位置
ax.plot([x1, x1, x2, x2], [y, y+h, y+h, y], lw=.8, c="k") 
#添加P值属性
ax.text((x1+x2)*.5, y+h, p_value_cov, ha='center', va='bottom', color="k",fontsize=15,
        fontweight="bold")
ax.set_xlim(-.5,1.5)
ax.grid(False)
plt.tight_layout()
fig.savefig('\第7章 其他类型图的绘制\图7-2-2 配对T检验图绘制样式示例_b.pdf',bbox_inches='tight')
fig.savefig('\第7章 其他类型图的绘制\图7-2-2 配对T检验图绘制样式示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()


# c）添加显著性水平配对T检验图样式三
August_scor_mean = df.loc[df["Time"]=="August","Scores"].mean()
June_scor_mean = df.loc[df["Time"]=="June","Scores"].mean()

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
pg.plot_paired(data=df, dv='Scores', within='Time',
               subject='Subject', ax=ax, boxplot=False,
               colors=['k', 'k', 'k'])  
# 添加P值信息
x1, x2 = 0, 1
y,h = 8.8,.15
#绘制横线位置
ax.plot([x1, x1, x2, x2], [y, y+h, y+h, y], lw=.8, c="k") 
#添加P值属性
ax.text((x1+x2)*.5, y+h, p_value_cov, ha='center', va='bottom', color="k",fontsize=15,
        fontweight="bold")
ax.set_xlim(-.5,1.5)

bottom = 3
ax.bar(x=0,height=August_scor_mean-bottom,width=.3,bottom=bottom,color="lightgray",zorder=0)
ax.bar(x=1,height=June_scor_mean-bottom,width=.3,bottom=bottom,color="lightgray",
       zorder=0,label="Values Mean")
ax.grid(False)
ax.legend(frameon=False,loc="upper left",bbox_to_anchor=(.02,.82))
plt.tight_layout()
fig.savefig('\第7章 其他类型图的绘制\图7-2-2 配对T检验图绘制样式示例_c.pdf',bbox_inches='tight')
fig.savefig('\第7章 其他类型图的绘制\图7-2-2 配对T检验图绘制样式示例_c.png', 
            bbox_inches='tight',dpi=300)
plt.show()

