
"""
编写时间：2022年2月06日 10：30

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。

代码中Proplot包绘制的部分可能与Matplotlib绘制不同，需注意两者绘图语法的不同~~

"""
#注意：本案例中引入的SciencePlots库主题方式会随着SciencePlots版本的更新发生改变，读者还需参考其官网引入的正确方式。
#      建议按照官网引入方式进行操作和使用最新版本的ScienePlots。如引入方式发生改变，请关注微信公众号【DataCharm】进行实时获取代码更新。


import pandas as pd
import numpy as np
import proplot as pplt

group_data = pd.read_csv(r"第3章 单变量图形的绘制\山脊图绘制数据.csv")
sord_index = [i for i in group_data.color.unique()]
sord_index = sorted(sord_index,key=str.lower)


# a）利用ProPlot绘制的渐变颜色填充“山脊”图（fire）
from proplot.axes import Axes
from proplot import rc
rc["font.family"] = "Times New Roman"
rc["axes.labelsize"] = 15
rc['tick.labelsize'] = 10
rc["suptitle.size"] = 16
rc["image.composite_image"] = False

fig = pplt.figure(figsize=(5.,4.5))
ax = fig.subplot()
ax.format(xlabel='Depth', ylabel='Color',ytickminor=False)
for i,index in zip(range(len(sord_index)),sord_index):
    data = group_data.loc[group_data["color"]==index,"depth"].values
    x,y = NaiveKDE(kernel="Gaussian",bw=.8).fit(data).evaluate()
    img_data = x.reshape(1,-1)
    ax.plot(x,6*y+i, lw=1,color="k",zorder=100 - i)
    fill_line, = ax.fill(x,6*y+i,facecolor="none")
    ax.yaxis.set_tick_params(labelleft=True)
    ax.set_yticks(np.arange(len(sord_index)))
    ax.set_yticklabels(sord_index)
    
    extent=[*ax.get_xlim(), *ax.get_ylim()]
    #im = Axes.imshow(ax, img_data, aspect='auto',cmap=cmap,extent=extent) Fire
    im = Axes.imshow(ax, img_data, aspect='auto',cmap="Fire",extent=extent)
    im.set_clip_path(fill_line)

colorbar = fig.colorbar(im,tickminor=True,tickdirection="in",length=.5,width=.2)
colorbar.ax.set_title("Values",fontsize=8)

fig.savefig('\第3章 单变量图形的绘制\图3-2-13 利用ProPlot、SciencePlots绘制的渐变颜色填充“山脊”图示例_a.pdf',bbox_inches='tight')
fig.savefig('\第3章 单变量图形的绘制\图3-2-13 利用ProPlot、SciencePlots绘制的渐变颜色填充“山脊”图示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()  

#b）利用SciencePlots绘制的渐变颜色填充“山脊”图（plasma）

from matplotlib.axes import Axes
# 保存多个ax为pdf文件需要设置
plt.rcParams["image.composite_image"] = False
with plt.style.context(['science']):
    fig,ax = plt.subplots(figsize=(5.5,4.5),dpi=100,facecolor="w")
    for i,index in zip(range(len(sord_index)),sord_index):
        data = group_data.loc[group_data["color"]==index,"depth"].values
        x,y = NaiveKDE(kernel="Gaussian",bw=.8).fit(data).evaluate()
        img_data = x.reshape(1,-1)
        ax.plot(x,6*y+i, lw=1,color="k",zorder=100 - i)
        fill_line, = ax.fill(x,6*y+i,facecolor="none")
        #ax.axhline(i,ls="--",lw=.7,color="gray",zorder=100 - i)
        ax.grid(which="major",axis="y",ls="--",lw=.7,color="gray",zorder=-1)
        #ax.set_xlim(50,72)
        ax.yaxis.set_tick_params(labelleft=True)
        ax.set_yticks(np.arange(len(sord_index)))
        ax.set_yticklabels(sord_index)
        ax.set_xlabel("Depth")
        ax.set_ylabel("Color")
        ax.tick_params(which ="both",top=False,right=False)
        ax.tick_params(which = "minor",axis="both",left=False,bottom=False)
        for spin in ["top","right","bottom","left"]:
            ax.spines[spin].set_visible(False)
        extent=[*ax.get_xlim(), *ax.get_ylim()]
        im = Axes.imshow(ax, img_data, aspect='auto',cmap="plasma",extent=extent)
        im.set_clip_path(fill_line)
    colorbar = fig.colorbar(im,aspect=10,shrink=0.5)
    colorbar.ax.set_title("Values",fontsize=10)
    fig.savefig('\第3章 单变量图形的绘制\图3-2-13 利用ProPlot、SciencePlots绘制的渐变颜色填充“山脊”图示例_b.pdf',
                bbox_inches='tight')
    fig.savefig('\第3章 单变量图形的绘制\图3-2-13 利用ProPlot、SciencePlots绘制的渐变颜色填充“山脊”图示例_b.png', 
                 bbox_inches='tight',dpi=300)

plt.show() 