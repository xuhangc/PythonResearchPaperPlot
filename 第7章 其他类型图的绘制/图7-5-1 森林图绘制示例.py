
"""
编写时间：2022年5月06日 16：30

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。

代码中Proplot包绘制的部分可能与Matplotlib绘制不同，需注意两者绘图语法的不同~~

"""
#注意：本案例中引入的SciencePlots库主题方式会随着SciencePlots版本的更新发生改变，读者还需参考其官网引入的正确方式。

import numpy as np
from zepid.graphics import EffectMeasurePlot
from proplot import rc
rc["figure.facecolor"]="w"
rc["font.family"] = "Times New Roman"
rc["axes.labelsize"] = 15
rc["tick.labelsize"] = 12
rc["suptitle.size"] = 15
rc["title.size"] = 14


labs = ["Method 01(Isq=41.37% Tausq=0.146 pvalue=0.039 )",
        "Method 02(Isq=25.75% Tausq=0.092 pvalue=0.16 )",
        "Method 03(Isq=60.34% Tausq=0.121 pvalue=0.00 )",
        "Method 04(Isq=25.94% Tausq=0.083 pvalue=0.16 )",
        "Method 05(Isq=74.22% Tausq=0.465 pvalue=0.00 )"]
measure = [2.09,2.24,1.79,2.71,1.97]
lower = [1.49,1.63,1.33,2.00,1.25]
upper = [2.92,3.07,2.42,3.66,3.11]
p = EffectMeasurePlot(label=labs, effect_measure=measure, lcl=lower, ucl=upper)
p.labels(effectmeasure='OR')
p.colors(pointshape="D")

ax = p.plot(figsize=(8,4), t_adjuster=0.09, max_value=4, min_value=0.35)
#p.plot()
plt.title("Random Effect Model(Odds Ratio)",loc="right",x=1, y=1.045)
#plt.suptitle("Missing Data Imputation Method",x=0.2,y=.86,fontsize=14,fontweight="normal")
plt.suptitle("Study ID",x=0.2,y=.86,fontsize=14,fontweight="normal")
ax.set_xlabel("Favours Control      Favours Haloperidol       ", fontsize=10)
ax.grid(False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(True)
ax.spines['left'].set_visible(False)
plt.tight_layout()

fig.savefig('\第7章 其他类型图的绘制\图7-5-1 森林图绘制示例.pdf',bbox_inches='tight')
fig.savefig('\第7章 其他类型图的绘制\图7-5-1 森林图绘制示例.png', 
            bbox_inches='tight',dpi=300)
plt.show()

