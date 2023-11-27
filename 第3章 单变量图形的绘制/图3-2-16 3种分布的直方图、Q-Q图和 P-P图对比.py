"""
编写时间：2022年2月06日 11：20

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。

代码中Proplot包绘制的部分可能与Matplotlib绘制不同，需注意两者绘图语法的不同~~

"""
#注意：本案例中引入的SciencePlots库主题方式会随着SciencePlots版本的更新发生改变，读者还需参考其官网引入的正确方式。
#      建议按照官网引入方式进行操作和使用最新版本的ScienePlots。如引入方式发生改变，请关注微信公众号【DataCharm】进行实时获取代码更新。

import numpy as np
import pandas as pd
import seaborn as sns
import statsmodels.api as sm
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["axes.linewidth"] = 1
plt.rcParams["axes.labelsize"] = 15
plt.rcParams["xtick.minor.visible"] = True
plt.rcParams["ytick.minor.visible"] = True
plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"
plt.rcParams["xtick.labelsize"] = 12
plt.rcParams["ytick.labelsize"] = 12
plt.rcParams["xtick.top"] = True
plt.rcParams["ytick.right"] = True


# a）均匀分布直方图
uniform_data = np.random.uniform(0.5,1.5, 400)
uniform_data_df = pd.Series(uniform_data)

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
uniform_data_df.plot.kde(ax=ax, color="r",lw=1,legend=False)
uniform_data_df.plot.hist(density=True, color="#FF5B9B",ec="k",lw=.8,ax=ax)
ax.set_ylabel('Frequency')
ax.set_xlabel('Values')

fig.savefig('\第3章 单变量图形的绘制\图3-2-16 3种分布的直方图、Q-Q图和 P-P图对比_a.pdf',bbox_inches='tight')
fig.savefig('\第3章 单变量图形的绘制\图3-2-16 3种分布的直方图、Q-Q图和 P-P图对比_a.png', 
            bbox_inches='tight',dpi=300) 
plt.show() 

# b）均匀分布Q-Q图
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
qq_x = sm.ProbPlot(uniform_data, fit=True)
qq_x.qqplot(line='45',marker='o', markerfacecolor='#FF5B9B', markeredgecolor='k',markeredgewidth=.5,
            markersize=6,ax=ax)
            
fig.savefig('\第3章 单变量图形的绘制\图3-2-16 3种分布的直方图、Q-Q图和 P-P图对比_b.pdf',bbox_inches='tight')
fig.savefig('\第3章 单变量图形的绘制\图3-2-16 3种分布的直方图、Q-Q图和 P-P图对比_b.png', 
            bbox_inches='tight',dpi=300) 
plt.show() 

#c）均匀分布P-P图
import statsmodels.graphics.gofplots as sm 
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
pp_x = sm.ProbPlot(uniform_data, fit=True)

pp_x.ppplot(line='45',marker='o', markerfacecolor='#FF5B9B', markeredgecolor='k',markeredgewidth=.5,
          markersize=6,ax=ax)
ax.set_xlim((-.05, 1.05))
ax.set_ylim((-.05, 1.05))
fig.savefig('\第3章 单变量图形的绘制\图3-2-16 3种分布的直方图、Q-Q图和 P-P图对比_c.pdf',bbox_inches='tight')
fig.savefig('\第3章 单变量图形的绘制\图3-2-16 3种分布的直方图、Q-Q图和 P-P图对比_c.png', 
            bbox_inches='tight',dpi=300) 
plt.show() 

# d）正态分布直方图
normal_data = np.random.normal(0,1, 400)
normal_data_df = pd.Series(normal_data)

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
normal_data_df.plot.kde(ax=ax, color="r",lw=1,legend=False)
normal_data_df.plot.hist(density=True, color="#459DFF",ec="k",lw=.8,ax=ax)
ax.set_ylabel('Frequency')
ax.set_xlabel('Values')

fig.savefig('\第3章 单变量图形的绘制\图3-2-16 3种分布的直方图、Q-Q图和 P-P图对比_d.pdf',bbox_inches='tight')
fig.savefig('\第3章 单变量图形的绘制\图3-2-16 3种分布的直方图、Q-Q图和 P-P图对比_d.png', 
            bbox_inches='tight',dpi=300) 
plt.show() 

# e）正态分布Q-Q图
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
qq_x = sm.ProbPlot(normal_data, fit=True)
qq_x.qqplot(line='45',marker='o', markerfacecolor='#459DFF', markeredgecolor='k',markeredgewidth=.5,
          markersize=6,ax=ax)
ax.set_xlim((-3.5, 3.0))
ax.set_ylim((-3.5, 3.0))
fig.savefig('\第3章 单变量图形的绘制\图3-2-16 3种分布的直方图、Q-Q图和 P-P图对比_e.pdf',bbox_inches='tight')
fig.savefig('\第3章 单变量图形的绘制\图3-2-16 3种分布的直方图、Q-Q图和 P-P图对比_e.png', 
            bbox_inches='tight',dpi=300) 
plt.show() 

#f）正态分布P-P图
import statsmodels.graphics.gofplots as sm 

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
pp_x = sm.ProbPlot(normal_data, fit=True)

pp_x.ppplot(line='45',marker='o', markerfacecolor='#459DFF', markeredgecolor='k',markeredgewidth=.5,
          markersize=6,ax=ax)
ax.set_xlim((-.05, 1.05))
ax.set_ylim((-.05, 1.05))
fig.savefig('\第3章 单变量图形的绘制\图3-2-16 3种分布的直方图、Q-Q图和 P-P图对比_f.pdf',bbox_inches='tight')
fig.savefig('\第3章 单变量图形的绘制\图3-2-16 3种分布的直方图、Q-Q图和 P-P图对比_f.png', 
            bbox_inches='tight',dpi=300) 
plt.show() 

# g）指数分布直方图
ex_data = np.random.exponential(size=400)
ex_data_df = pd.Series(ex_data)

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
ex_data_df.plot.kde(ax=ax, color="r",lw=1,legend=False)
ex_data_df.plot.hist(density=True, color="#FFCC37",ec="k",lw=.8,ax=ax)
ax.set_ylabel('Frequency')
ax.set_xlabel('Values')
fig.savefig('\第3章 单变量图形的绘制\图3-2-16 3种分布的直方图、Q-Q图和 P-P图对比_g.pdf',bbox_inches='tight')
fig.savefig('\第3章 单变量图形的绘制\图3-2-16 3种分布的直方图、Q-Q图和 P-P图对比_g.png', 
            bbox_inches='tight',dpi=300) 
plt.show() 

# h）指数分布Q-Q图

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
qq_x = sm.ProbPlot(ex_data, fit=True)
qq_x.qqplot(line='45',marker='o', markerfacecolor='#FFCC37', markeredgecolor='k',markeredgewidth=.5,
            markersize=6,ax=ax)

fig.savefig('\第3章 单变量图形的绘制\图3-2-16 3种分布的直方图、Q-Q图和 P-P图对比_h.pdf',bbox_inches='tight')
fig.savefig('\第3章 单变量图形的绘制\图3-2-16 3种分布的直方图、Q-Q图和 P-P图对比_h.png', 
            bbox_inches='tight',dpi=300) 
plt.show() 
# i）指数分布P-P图
import statsmodels.graphics.gofplots as sm 

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
pp_x = sm.ProbPlot(ex_data, fit=True)

pp_x.ppplot(line='45',marker='o', markerfacecolor='#FFCC37', markeredgecolor='k',markeredgewidth=.5,
          markersize=6,ax=ax)
ax.set_xlim((-.05, 1.05))
ax.set_ylim((-.05, 1.05))
fig.savefig('\第3章 单变量图形的绘制\图3-2-16 3种分布的直方图、Q-Q图和 P-P图对比_i.pdf',bbox_inches='tight')
fig.savefig('\第3章 单变量图形的绘制\图3-2-16 3种分布的直方图、Q-Q图和 P-P图对比_i.png', 
            bbox_inches='tight',dpi=300) 
plt.show() 

