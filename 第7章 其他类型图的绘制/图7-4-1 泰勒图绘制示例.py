"""
编写时间：2022年5月06日 15：30

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

taylor_01 = pd.read_excel(r"\第7章 其他类型图的绘制\taylor_diagram_data_01.xlsx")

#计算泰勒图的统计量
taylor_stats1 = sm.taylor_statistics(taylor_01.pred1,taylor_01.ref,'taylor_01')
taylor_stats2 = sm.taylor_statistics(taylor_01.pred2,taylor_01.ref,'taylor_01')
taylor_stats3 = sm.taylor_statistics(taylor_01.pred3,taylor_01.ref,'taylor_01')

#将统计信息存储在数组中
sdev = np.array([taylor_stats1['sdev'][0], taylor_stats1['sdev'][1], 
                 taylor_stats2['sdev'][1], taylor_stats3['sdev'][1]])
crmsd = np.array([taylor_stats1['crmsd'][0], taylor_stats1['crmsd'][1], 
                  taylor_stats2['crmsd'][1], taylor_stats3['crmsd'][1]])
ccoef = np.array([taylor_stats1['ccoef'][0], taylor_stats1['ccoef'][1], 
                  taylor_stats2['ccoef'][1], taylor_stats3['ccoef'][1]])
                  
# a）泰勒图默认样式绘制示例                
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
sm.taylor_diagram(sdev,crmsd,ccoef)
ax.grid(False)
fig.tight_layout()   
fig.savefig('\第7章 其他类型图的绘制\图7-4-1 泰勒图绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第7章 其他类型图的绘制\图7-4-1 泰勒图绘制示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()

#b）泰勒图自定义样式绘制示例
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
sm.taylor_diagram(sdev,crmsd,ccoef,markerSize=12,widthCOR=.9,markercolor='k',
                  colCOR="k",styleCOR="--",colSTD="b",widthSTD=.9,tickSTD=np.arange(0,25,5),styleSTD="--",
                  widthRMS=.9,tickRMS=np.arange(0,25,5),
                  colOBS="r",styleOBS="-",widthOBS=1,markerObs="^",titleOBS="Observation")
ax.grid(False)
fig.tight_layout()

fig.savefig('\第7章 其他类型图的绘制\图7-4-1 泰勒图绘制示例_b.pdf',bbox_inches='tight')
fig.savefig('\第7章 其他类型图的绘制\图7-4-1 泰勒图绘制示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()              