"""
编写时间：2022年5月06日 15：50

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。

代码中Proplot包绘制的部分可能与Matplotlib绘制不同，需注意两者绘图语法的不同~~

"""
#注意：本案例中引入的SciencePlots库主题方式会随着SciencePlots版本的更新发生改变，读者还需参考其官网引入的正确方式。
#

import skill_metrics as sm
import numpy as np
import pandas as pd
from venn import venn
import matplotlib.pyplot as plt
from proplot import rc

rc["font.family"] = "Times New Roman"
rc["axes.labelsize"] = 15
rc["tick.labelsize"] = 12
rc["suptitle.size"] = 15
rc["title.size"] = 14
rc["xtick.minor.visible"] = False
rc["ytick.minor.visible"] = False
rc["xtick.direction"] = "in"
rc["ytick.direction"] = "in"
rc["image.cmap"] ="jet"

taylor_data2 = pd.read_excel(r"\第7章 其他类型图的绘制\taylor_diagram_data_02.xlsx")
sdev = taylor_data2["SD"].to_numpy()
crmsd = taylor_data2["RMSE"].to_numpy()
ccoef = taylor_data2["Correlation Coefficient"].to_numpy()
label = taylor_data2["Model"].to_list()

# a）多模型精度比较泰勒图绘制样式一
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
sm.taylor_diagram(sdev,crmsd,ccoef,
                  markerLabel = label, markerSymbol="*",markercolor="k",markerSize=8,
                  colCOR="k",styleCOR="--",widthCOR=.9,
                  colSTD="b",widthSTD=.9,styleSTD="--",
                  widthRMS=.9,
                  colOBS="r",styleOBS="-",widthOBS=1,markerObs="^",titleOBS="Observation")
ax.grid(False)
fig.tight_layout()

fig.savefig('\第7章 其他类型图的绘制\图7-4-2多模型评估指标不同样式泰勒图绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第7章 其他类型图的绘制\图7-4-2多模型评估指标不同样式泰勒图绘制示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# b）多模型精度比较泰勒图绘制样式二
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
sm.taylor_diagram(sdev,crmsd,ccoef,
                  markerLabel = label,markercolor="k",markerSize=6,markerLegend = 'on',
                  colCOR="k",styleCOR="--",widthCOR=.9,
                  colSTD="b",widthSTD=.9,styleSTD="--",
                  widthRMS=.9,
                  colOBS="r",styleOBS="-",widthOBS=1,markerObs="^",titleOBS="Observation")
ax.grid(False)
fig.tight_layout()
fig.savefig('\第7章 其他类型图的绘制\图7-4-2多模型评估指标不同样式泰勒图绘制示例_b.pdf',bbox_inches='tight')
fig.savefig('\第7章 其他类型图的绘制\图7-4-2多模型评估指标不同样式泰勒图绘制示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()

#***注意：c、d两个结果是经过源码替换之后的绘制结果，读者可根据要求获取修改之后的py文件。
# c）多模型精度比较泰勒图colorbar样式一
rc["tick.labelsize"] = 12
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
tay = sm.taylor_diagram(sdev,crmsd,ccoef,
                        markerLabel = label, markerSymbol="*",
                        markerDisplayed = 'colorBar',
                        markerSize=12,titleColorbar = 'RMSEP',cmapzdata=crmsd,colormap="off",
                        colCOR="k",styleCOR="--",widthCOR=.9,
                        colSTD="b",widthSTD=.9,styleSTD="--",
                        widthRMS=.9,
                        colOBS="r",styleOBS="-",widthOBS=1,markerObs="o",titleOBS="Observation")
ax.grid(False)
fig.savefig('\第7章 其他类型图的绘制\图7-4-2多模型评估指标不同样式泰勒图绘制示例_c.pdf',bbox_inches='tight')
fig.savefig('\第7章 其他类型图的绘制\图7-4-2多模型评估指标不同样式泰勒图绘制示例_c.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# d）多模型精度比较泰勒图colorbar样式二
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
tay = sm.taylor_diagram(sdev,crmsd,ccoef,markerDisplayed = 'colorBar',
                        markerLabel = label, markerSymbol="*",
                        markerSize=10,titleColorbar = 'RMSEP',cmapzdata=crmsd,colormap="on",
                        locationcolorbar="eastoutside",
                        colCOR="k",styleCOR="--",widthCOR=.9,
                        colSTD="b",widthSTD=.9,styleSTD="--",
                        widthRMS=.9,
                        colOBS="r",styleOBS="-",widthOBS=1,markerObs="o",titleOBS="Observation")
ax.grid(False)

fig.savefig('\第7章 其他类型图的绘制\图7-4-2多模型评估指标不同样式泰勒图绘制示例_d.pdf',bbox_inches='tight')
fig.savefig('\第7章 其他类型图的绘制\图7-4-2多模型评估指标不同样式泰勒图绘制示例_d.png', 
            bbox_inches='tight',dpi=300)
plt.show()