
"""
编写时间：2022年2月06日 09：50

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。

代码中Proplot包绘制的部分可能与Matplotlib绘制不同，需注意两者绘图语法的不同~~

"""
#注意：本案例中引入的SciencePlots库主题方式会随着SciencePlots版本的更新发生改变，读者还需参考其官网引入的正确方式。
#      建议按照官网引入方式进行操作和使用最新版本的ScienePlots。如引入方式发生改变，请关注微信公众号【DataCharm】进行实时获取代码更新。



import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["xtick.minor.visible"] = True
plt.rcParams["ytick.minor.visible"] = True
plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"
plt.rcParams["xtick.labelsize"] = 12
plt.rcParams["ytick.labelsize"] = 12

#构建数据集
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
                        
                        

nrow = 2
ncol = 2
ax_label = ["a.","b.","c.","d."]
titles = ["Type One","Type Two","Type Three","Type Four"]
indexs = [i for i in data_df.columns] 

fig,axs = plt.subplots(nrow,ncol,figsize=(5,4),dpi=100,facecolor="w",sharey=True,sharex=True,
                      constrained_layout=True)
for ax, index,label in zip(axs.flat, indexs,ax_label):
    x,y = NaiveKDE(kernel="Gaussian",bw=2).fit(data_df[index].values).evaluate()
    ax.plot(x,y, lw=1,color="#1BB71B")
    ax.fill(x,y,color="#1BB71B",alpha=.6)
    # 添加单独数据、
    ax.plot(data_df[index].values, [0.005]*len(data_df[index].values), '|', color='k',lw=1)
    ax.text(0.05, 0.95, label, transform=ax.transAxes,fontsize=16, fontweight='bold', va='top')
    ax.text(0.65, 0.95, index,transform=ax.transAxes,fontsize=14, fontweight='bold', va='top')
fig.supxlabel('Values')
fig.supylabel('Density')
fig.savefig('\第3章 单变量图形的绘制\图3-2-6 不同数据、同一个核函数绘制密度图示例.pdf',bbox_inches='tight')
fig.savefig('\第3章 单变量图形的绘制\图3-2-6 不同数据、同一个核函数绘制密度图示例.png', 
            bbox_inches='tight',dpi=300)                        

plt.show()                    