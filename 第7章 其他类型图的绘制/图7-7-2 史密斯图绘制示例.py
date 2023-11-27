
"""
编写时间：2022年5月06日 17：50

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。

代码中Proplot包绘制的部分可能与Matplotlib绘制不同，需注意两者绘图语法的不同~~

"""
#注意：本案例中引入的SciencePlots库主题方式会随着SciencePlots版本的更新发生改变，读者还需参考其官网引入的正确方式。

import smithplot
import numpy as np
import pandas as pd
from proplot import rc
from smithplot import SmithAxes
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams["font.family"] = "Times New Roman"
rcParams["xtick.labelsize"] =12
rcParams["ytick.labelsize"] =15
from proplot import rc
rc["font.family"] = "Times New Roman"
rc["axes.labelsize"] = 15
rc["tick.labelsize"] = 12
rc["suptitle.size"] = 15
rc["title.size"] = 14

smith_data = pd.read_excel(r"\第7章 其他类型图的绘制\smith plot data.xlsx")
Real_01 = smith_data["Real01"].values
Imag_01 = smith_data["Imag01"].values
Real_02 = smith_data["Real02"].values
Imag_02 = smith_data["Imag02"].values

# a）史密斯图散点绘制样式一
plt.figure(figsize=(5, 5),dpi=100,facecolor="w")
ax = plt.subplot(projection='smith')
for Real,image in zip(Real_01,Imag_01):
    ax.plot(Real*50+image*50j,datatype=SmithAxes.Z_PARAMETER,marker="o",markersize=7,color="r",mec="k")
for Real,image in zip(Real_02,Imag_02):
    ax.plot(Real*50+image*50j,datatype=SmithAxes.Z_PARAMETER,marker="o",markersize=7,color="b",mec="k")
plt.tight_layout()

fig.savefig('\第7章 其他类型图的绘制\图7-7-2 史密斯图绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第7章 其他类型图的绘制\图7-7-2 史密斯图绘制示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# b）史密斯图散点绘制样式二

data = np.loadtxt("\第7章 其他类型图的绘制\s11.csv", delimiter=",", skiprows=1)[::100]
val1 = data[:, 1] + data[:, 2] * 1j
data = np.loadtxt("第7章 其他类型图的绘制\s22.csv", delimiter=",", skiprows=1)[::100]
val2 = data[:, 1] + data[:, 2] * 1j

colors = ["#2FBE8F","#459DFF","#FF5B9B","#FFCC37","#751DFE"]

plt.figure(figsize=(5, 5),dpi=100,facecolor="w")
ax = plt.subplot(projection='smith')
ax.plot([10, 100], markevery=1)

ax.plot(200 + 100j, datatype=SmithAxes.Z_PARAMETER,marker="o",markersize=10,color="r",mec="k")
ax.plot(100 + 25.5j, datatype=SmithAxes.Z_PARAMETER,marker="o",markersize=10,color="b",mec="k")
ax.plot(10 + 3j, datatype=SmithAxes.Z_PARAMETER,marker="o",markersize=10,color="g",mec="k")
ax.plot(50 * val1, label="default", datatype=SmithAxes.Z_PARAMETER,color=colors[0])
ax.plot(50 * val2, markevery=1, label="interpolate=3", interpolate=3, datatype=SmithAxes.Z_PARAMETER,
       color=colors[1])
ax.plot(val1, markevery=1, label="equipoints=22", equipoints=22, datatype=SmithAxes.S_PARAMETER,
       color=colors[2])
ax.plot(val2, markevery=3, label="equipoints=22, \nmarkevery=3", equipoints=22, 
        datatype=SmithAxes.S_PARAMETER,color=colors[3])

ax.legend(loc="center",ncol=1,fontsize=10,bbox_to_anchor=(.93,1),fancybox=False,edgecolor="k")
plt.tight_layout()

fig.savefig('\第7章 其他类型图的绘制\图7-7-2 史密斯图绘制示例_b.pdf',bbox_inches='tight')
fig.savefig('\第7章 其他类型图的绘制\图7-7-2 史密斯图绘制示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()