
"""
编写时间：2022年2月06日 10：50

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。

代码中Proplot包绘制的部分可能与Matplotlib绘制不同，需注意两者绘图语法的不同~~

"""
#注意：本案例中引入的SciencePlots库主题方式会随着SciencePlots版本的更新发生改变，读者还需参考其官网引入的正确方式。
#      建议按照官网引入方式进行操作和使用最新版本的ScienePlots。如引入方式发生改变，请关注微信公众号【DataCharm】进行实时获取代码更新。


import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

data_01 = [5.1,5.2,5.3,5.4,5.5,6.0,6.2,6.3,6.4,6.5,
           7.0,7.5,8.0,8.5,8.8,8.9,9.0,9.5,10,11,
           11.5,12,13,14,14.5,15,15.5,16,16.5,17]

data_02 = [5.1,5.2,5.3,5.4,5.5,6.0,7.0,7.3,7.4,7.5,
           8.0,8.2,8.4,8.6,8.8,9.0,9.2,9.4,9.6,9.8,
           10,10.2,11,11.5,12,12.5,13,13.5,15,16]
data_03 = [5.1,5.2,5.3,5.4,5.6,6.0,6.1,6.2,6.4,6.8,
           7.1,8.2,8.8,9.0,9.2,10.2,10.4,10.8,11,11.6,
           12,12.4,12.6,12.8,13,13.2,13.4,13.6,13.7,13.8]

data_04 = [5.0,5.2,5.3,5.4,5.6,5.8,6.0,6.2,6.4,6.6,
             6.8,7.0,7.2,7.4,7.6,8.0,9.0,9.2,9.6,9.8,
             10,10.3,11,12,16,16,18,18.5,19,22]
data_df = pd.DataFrame({"data_01":data_01,"data_02":data_02,
                        "data_03":data_03,"data_04":data_04})


#a）利用ProPlot 绘制的结果  

from scipy import stats
from proplot import rc
rc["axes.labelsize"] = 15
rc['tick.labelsize'] = 12
rc["suptitle.size"] = 15
palette = ["#352A87","#108ED2","#65BE86","#FFC337"]

fig = pplt.figure(figsize=(3.5,3))
ax = fig.subplot()
ax.format(abc='a.', abcloc='ul',abcsize=16,
          xlabel='Values', ylabel='Density')

for i, index,color in zip(range(len(palette)),data_df.columns,palette):
    data = data_df[index].values
    density = stats.kde.gaussian_kde(data)
    x = np.linspace(-2,25,500)
    y = density(x)
    ax.plot(x,y, lw=.5,color="k",zorder=5-i)
    ax.fill(x,y,color=color,label=index,alpha=.7)
ax.legend(ncols=1,frame=False,loc='ur')

fig.savefig('\第3章 单变量图形的绘制\图3-2-15 利用ProPlot、SciencePlots分别绘制的“同一 坐标系中的多个密度图”_a.pdf',bbox_inches='tight')
fig.savefig('\第3章 单变量图形的绘制\图3-2-15 利用ProPlot、SciencePlots分别绘制的“同一 坐标系中的多个密度图”_a.png', 
            bbox_inches='tight',dpi=300) 
plt.show() 


#b）利用ProPlot seaborn对象绘制的结果 

from proplot import rc
rc["axes.labelsize"] = 15
rc['tick.labelsize'] = 10
rc["suptitle.size"] = 16
rc["legend.fontsize"] = 5

palette = ["#352A87","#108ED2","#65BE86","#FFC337"]

fig = pplt.figure(figsize=(3.5,3))
ax = fig.subplot()
ax.format(abc='a.', abcloc='ul',abcsize=16,
          xlabel='Values', ylabel='Density')

sns.kdeplot(data=data_df,shade=True,palette = palette,alpha=.6,ax=ax)
fig.savefig('\第3章 单变量图形的绘制\图3-2-15 利用ProPlot、SciencePlots分别绘制的“同一 坐标系中的多个密度图”_b.pdf',bbox_inches='tight')
fig.savefig('\第3章 单变量图形的绘制\图3-2-15 利用ProPlot、SciencePlots分别绘制的“同一 坐标系中的多个密度图”_b.png', 
            bbox_inches='tight',dpi=300) 
plt.show() 

#c）利用SciencePlots绘制的结果 使用全局变量设置，字体显示正常

import matplotlib.pyplot as plt
plt.style.use('science')

from scipy import stats
palette = ["#352A87","#108ED2","#65BE86","#FFC337"]
titles = ["Type One","Type Two","Type Three","Type Four"]
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
for i, index,color,label in zip(range(len(palette)),data_df.columns,palette,titles):
    data = data_df[index].values
    density = stats.kde.gaussian_kde(data)
    x = np.linspace(-2,25,500)
    y = density(x)
    ax.plot(x,y, lw=.5,color="k",zorder=5-i)
    ax.fill(x,y,color=color,label=label,alpha=.7)
ax.set_xlabel("Values")
ax.set_ylabel("Density")
ax.legend()

fig.savefig('\第3章 单变量图形的绘制\图3-2-15 利用ProPlot、SciencePlots分别绘制的“同一 坐标系中的多个密度图”_c.pdf',bbox_inches='tight')
fig.savefig('\第3章 单变量图形的绘制\图3-2-15 利用ProPlot、SciencePlots分别绘制的“同一 坐标系中的多个密度图”_c.png', 
            bbox_inches='tight',dpi=300) 
plt.show() 
                    
