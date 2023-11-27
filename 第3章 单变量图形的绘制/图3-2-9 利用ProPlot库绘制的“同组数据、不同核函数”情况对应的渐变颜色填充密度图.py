
"""
编写时间：2022年2月06日 10：20

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。

代码中Proplot包绘制的部分可能与Matplotlib绘制不同，需注意两者绘图语法的不同~~

"""
#注意：本案例中引入的SciencePlots库主题方式会随着SciencePlots版本的更新发生改变，读者还需参考其官网引入的正确方式。
#      建议按照官网引入方式进行操作和使用最新版本的ScienePlots。如引入方式发生改变，请关注微信公众号【DataCharm】进行实时获取代码更新。

from colormaps import parula
from proplot.axes import Axes
from KDEpy import NaiveKDE
from proplot import rc

rc["font.family"] = "Times New Roman"
rc["axes.labelsize"] = 15
rc['tick.labelsize'] = 10
rc["suptitle.size"] = 16



data_01 = [5.1,5.2,5.3,5.4,5.5,6.0,6.2,6.3,6.4,6.5,
                 7.0,7.5,8.0,8.5,8.8,8.9,9.0,9.5,10,11,
                 11.5,12,13,14,14.5,15,15.5,16,16.5,17]


cmap = parula
kde_kernels = NaiveKDE._available_kernels.keys()
fig, axs = pplt.subplots(ncols=3, nrows=3,refwidth=1.5,refheight=1.2)
axs.format(
    abc='a.', abcloc='ul',abcsize=16,
    xlabel='Values', ylabel='Density',
)
for ax, kernel in zip(axs,kde_kernels):
    x,y = NaiveKDE(kernel=kernel,bw=2).fit(data_01).evaluate()
    img_data = x.reshape(1, -1)
    ax.plot(x,y, lw=1,color="k")
    fill_line,= ax.fill(x, y,facecolor='none')
     # 添加单独数据、
    ax.plot(data_01, [0.005]*len(data_01), '|', color='k',lw=.5)
    ax.format(title=str.capitalize(kernel),titleweight='bold',titlesize=12)
    
    extent=[*ax.get_xlim(), *ax.get_ylim()]
    im = Axes.imshow(ax, img_data, aspect='auto',cmap=cmap,extent=extent)
    im.set_clip_path(fill_line)
    colorbar = fig.colorbar(im,tickminor=True,tickdirection="in",ax=ax)
    colorbar.ax.set_title("Values",fontsize=8)
fig.savefig('\第3章 单变量图形的绘制\图3-2-9 利用ProPlot库绘制的“同组数据、不同核函数”情况对应的渐变颜色填充密度图.pdf')
fig.savefig('\第3章 单变量图形的绘制\图3-2-9 利用ProPlot库绘制的“同组数据、不同核函数”情况对应的渐变颜色填充密度图.png')
plt.show() 



