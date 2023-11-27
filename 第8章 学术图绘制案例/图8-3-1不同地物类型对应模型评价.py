"""
编写时间：2022年5月12日 19：50

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。

代码中Proplot包绘制的部分可能与Matplotlib绘制不同，需注意两者绘图语法的不同~~

"""
#注意：本案例中引入的SciencePlots库主题方式会随着SciencePlots版本的更新发生改变，读者还需参考其官网引入的正确方式。

import random,string
import numpy as np
import pandas as pd
import seaborn as sns
import proplot as pplt
from scipy import stats
import skill_metrics as sm
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid
from sklearn.metrics import mean_squared_error

from proplot import rc
rrc["font.family"] = "Times New Roman"
rc["axes.labelsize"] = 15
rc["tick.labelsize"] = 12
rc["suptitle.size"] = 15
rc["title.size"] = 14
rc["xtick.minor.visible"] = False
rc["ytick.minor.visible"] = False
rc["xtick.direction"] = "in"
rc["ytick.direction"] = "in"
rc["image.cmap"] ="jet"


#a）cropland类型模型精度泰勒图展示
cropland_tay = pd.read_excel(r"\第8章 学术图绘制案例\cropland_tay.xlsx")
sdev = cropland_tay["SD"].to_numpy()
crmsd = cropland_tay["RMSE"].to_numpy()
ccoef = cropland_tay["Correlation Coefficient"].to_numpy()
label = cropland_tay["Model"].to_list()

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
sm.taylor_diagram(sdev,crmsd,ccoef,markerLabel = label,
                  markerSize=15,markerSymbol="*",
                  MarkerDisplayed="colorBar",titleColorbar='RMSE',
                  cmapzdata=crmsd,colormap="off",axismax = 20.0,
                  widthCOR=.9,colOBS="r",colCOR="k",styleCOR="--",
                  colSTD="b",widthSTD=.9,
                  styleSTD="--",
                  widthRMS=.9,tickRMS=np.arange(0,22,4),
                  styleOBS="-",widthOBS=1,markerObs="^",titleOBS="Observation")
ax.grid(False)
fig.savefig('第8章 学术图绘制案例\图8-3-1不同地物类型对应模型评价_a.pdf',bbox_inches='tight')
fig.savefig('第8章 学术图绘制案例\图8-3-1不同地物类型对应模型评价_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()

#b）forest类型模型精度泰勒图展示
forest_tay = pd.read_excel(r"\第8章 学术图绘制案例\forest_tay.xlsx")
sdev = forest_tay["SD"].to_numpy()
crmsd = forest_tay["RMSE"].to_numpy()
ccoef = forest_tay["Correlation Coefficient"].to_numpy()
label = forest_tay["Model"].to_list()
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
sm.taylor_diagram(sdev,crmsd,ccoef,markerLabel = label,
                  markerSize=15,markerSymbol="*",
                  MarkerDisplayed="colorBar",titleColorbar='RMSE',
                  cmapzdata=crmsd,colormap="off",axismax = 20.0,
                  widthCOR=.9,colOBS="r",colCOR="k",styleCOR="--",
                  colSTD="b",widthSTD=.9,
                  styleSTD="--",
                  widthRMS=.9,tickRMS=np.arange(0,22,4),
                  styleOBS="-",widthOBS=1,markerObs="^",titleOBS="Observation")
ax.grid(False)
fig.savefig('第8章 学术图绘制案例\图8-3-1不同地物类型对应模型评价_b.pdf',bbox_inches='tight')
fig.savefig('第8章 学术图绘制案例\图8-3-1不同地物类型对应模型评价_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()

#c）grassland类型模型精度泰勒图展示
grassland_tay = pd.read_excel(r"\第8章 学术图绘制案例\grassland_tay.xlsx")
sdev = grassland_tay["SD"].to_numpy()
crmsd = grassland_tay["RMSE"].to_numpy()
ccoef = grassland_tay["Correlation Coefficient"].to_numpy()
label = grassland_tay["Model"].to_list()
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
sm.taylor_diagram(sdev,crmsd,ccoef,markerLabel = label,
                  markerSize=15,markerSymbol="*",
                  MarkerDisplayed="colorBar",titleColorbar='RMSE',
                  cmapzdata=crmsd,colormap="off",axismax = 20.0,
                  widthCOR=.9,colOBS="r",colCOR="k",styleCOR="--",
                  colSTD="b",widthSTD=.9,
                  styleSTD="--",
                  widthRMS=.9,tickRMS=np.arange(0,22,4),
                  styleOBS="-",widthOBS=1,markerObs="^",titleOBS="Observation")
ax.grid(False)
fig.savefig('第8章 学术图绘制案例\图8-3-1不同地物类型对应模型评价_c.pdf',bbox_inches='tight')
fig.savefig('第8章 学术图绘制案例\图8-3-1不同地物类型对应模型评价_c.png', 
            bbox_inches='tight',dpi=300)
plt.show()


#d）savanna类型模型精度泰勒图展示
savanna_tay = pd.read_excel(r"\第8章 学术图绘制案例\savanna_tay.xlsx")
sdev = savanna_tay["SD"].to_numpy()
crmsd = savanna_tay["RMSE"].to_numpy()
ccoef = savanna_tay["Correlation Coefficient"].to_numpy()
label = savanna_tay["Model"].to_list()

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
sm.taylor_diagram(sdev,crmsd,ccoef,
                  markerLabel = label,markerSymbol="*",
                  markerSize=15,
                  MarkerDisplayed="colorBar",titleColorbar='RMSE',
                  cmapzdata=crmsd,colormap="off",
                  widthCOR=.9,colOBS="r",colCOR="k",styleCOR="--",
                  colSTD="b",widthSTD=.9,
                  styleSTD="--",
                  widthRMS=.9,tickRMS=np.arange(0,20,4),
                  styleOBS="-",widthOBS=1,markerObs="^",titleOBS="Observation")
ax.grid(False)

fig.savefig('第8章 学术图绘制案例\图8-3-1不同地物类型对应模型评价_d.pdf',bbox_inches='tight')
fig.savefig('第8章 学术图绘制案例\图8-3-1不同地物类型对应模型评价_d.png', 
            bbox_inches='tight',dpi=300)
plt.show()
