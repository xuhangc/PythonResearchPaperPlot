"""
编写时间：2022年5月06日 10：50

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。

代码中Proplot包绘制的部分可能与Matplotlib绘制不同，需注意两者绘图语法的不同~~

"""
#注意：本案例中引入的SciencePlots库主题方式会随着SciencePlots版本的更新发生改变，读者还需参考其官网引入的正确方式。
#      建议按照官网引入方式进行操作和使用最新版本的ScienePlots。如引入方式发生改变，请关注微信公众号【DataCharm】进行实时获取代码更新。

import scipy
import numpy as np
import pandas as pd
import pingouin as pg
import matplotlib.pyplot as plt
from proplot import rc
rc["xtick.minor.visible"] = False
rc["ytick.minor.visible"] = False

ba_data = pd.read_excel(r"\第7章 其他类型图的绘制\前后图数据.xlsx")

#*************************图7-2-3 Matplotlib前后图样式绘制示例*******************************

#a）前后图基础样式绘制
ticks = ["Before","After"]
Before = ba_data["Before"].values
After = ba_data["After"].values
x = np.arange(len(ticks))

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
for i in range(len(Before)):
    ax.plot([0,1], [Before[i], After[i]], c='k',zorder=0,lw=.8)
ax.scatter(np.repeat(x[0],len(Before)), Before,color="k",s=50)
ax.scatter(np.repeat(x[1],len(After)), After,color = "k",s=50)
# 修饰
for spine in ["top","right"]:
    ax.spines[spine].set_visible(False)
# 添加刻度和刻度标签
ax.set(xlim=(-.5,1.5),ylim=(0.3,2.5),xticks=[0,1], xticklabels=['Before', 'After'],
       xlabel="X Axis Title",ylabel="T Axis Title")
ax.grid(False)
plt.tight_layout()
fig.savefig('\第7章 其他类型图的绘制\图7-2-3 Matplotlib前后图样式绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第7章 其他类型图的绘制\图7-2-3 Matplotlib前后图样式绘制示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()

#b）前后图误差属性添加样式绘制
# 计算标准误差
before_mean = ba_data["Before"].mean()
after_mean = ba_data["After"].mean()
before_sd = ba_data["Before"].std()
after_sd = ba_data["After"].std()

ticks_labels = ["Before/\nError","Before","After","After/\nError"]
Before = ba_data["Before"].values
After = ba_data["After"].values
x = np.arange(len(ticks_labels))

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
for i in range(len(Before)):
    ax.plot([0,1], [Before[i], After[i]], c='k',zorder=0,lw=.8)
ax.scatter(np.repeat(x[0],len(Before)), Before,color="k",s=50)
ax.scatter(np.repeat(x[1],len(After)), After,color = "k",s=50)
# 绘制误差图
ax.errorbar(-.5,before_mean,before_sd,fmt='o',markersize=8,color="k",linewidth=1, capsize=5)
ax.errorbar(1.5,after_mean,after_sd,fmt='o',markersize=8,color="k",linewidth=1, capsize=5)
# 修饰
for spine in ["top","right"]:
    ax.spines[spine].set_visible(False)
ax.set(xlim=(-1,2),ylim=(0.3,2.5),xticks=[-.5,0,1,1.5], xticklabels=ticks_labels,
       xlabel="X Axis Title",ylabel="T Axis Title")
ax.grid(False)
plt.tight_layout()
fig.savefig('\第7章 其他类型图的绘制\图7-2-3 Matplotlib前后图样式绘制示例_b.pdf',bbox_inches='tight')
fig.savefig('\第7章 其他类型图的绘制\图7-2-3 Matplotlib前后图样式绘制示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()

#c）前后图均值柱形图添加样式绘制
# 计算标准误差
before_mean = ba_data["Before"].mean()
after_mean = ba_data["After"].mean()
ticks_labels = ["Before","After",]
Before = ba_data["Before"].values
After = ba_data["After"].values
x = np.arange(len(ticks_labels))

#计算errorbar 
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
for i in range(len(Before)):
    ax.plot([0,1], [Before[i], After[i]], c='k',zorder=0,lw=.8)
ax.scatter(np.repeat(x[0],len(Before)), Before,color="k",s=50)
ax.scatter(np.repeat(x[1],len(After)), After,color = "k",s=50)
# 绘制均值柱形图
ax.bar(x=0,height=before_mean,width=.6,color="lightgray",zorder=0)
ax.bar(x=1,height=after_mean,width=.6,color="lightgray",zorder=0,label="Before/After Mean")
# 修饰
for spine in ["top","right"]:
    ax.spines[spine].set_visible(False)
ax.set(xlim=(-1,2),ylim=(0.3,2.5),xticks=[0,1,], xticklabels=ticks_labels,
       xlabel="X Axis Title",ylabel="T Axis Title")
ax.legend(frameon=False,loc="upper left")
ax.grid(False)
plt.tight_layout()

fig.savefig('\第7章 其他类型图的绘制\图7-2-3 Matplotlib前后图样式绘制示例_c.pdf',bbox_inches='tight')
fig.savefig('\第7章 其他类型图的绘制\图7-2-3 Matplotlib前后图样式绘制示例_c.png', 
            bbox_inches='tight',dpi=300)
plt.show()


#d）前后图均值柱形图p值添加样式绘制
#添加P值
import scipy
Before = ba_data["Before"].values
After = ba_data["After"].values

stat,p_value = scipy.stats.ttest_ind(Before,After,equal_var=False)

# *号转换
def convert_pvalue_to_asterisks(pvalue):
    if pvalue <= 0.0001:
        return "****"
    elif pvalue <= 0.001:
        return "***"
    elif pvalue <= 0.01:
        return "**"
    elif pvalue <= 0.05:
        return "*"
    return "ns"
p_value_cov = convert_pvalue_to_asterisks(p_value)


ticks = ["Before","After",]
Before = ba_data["Before"].values
After = ba_data["After"].values
x = np.arange(len(ticks))

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
for i in range(len(Before)):
    ax.plot([0,1], [Before[i], After[i]], c='k',zorder=0,lw=.8)
ax.scatter(np.repeat(x[0],len(Before)), Before,color="k",s=50)
ax.scatter(np.repeat(x[1],len(After)), After,color = "k",s=50)

# 绘制均值柱形图
ax.bar(x=0,height=before_mean,width=.6,color="lightgray",zorder=0)
ax.bar(x=1,height=after_mean,width=.6,color="lightgray",zorder=0,label="Before/\nAfter Mean")

# 添加P值
x1, x2 = 0, 1
y,h = 2.4,.05
#绘制横线位置
ax.plot([x1, x1, x2, x2], [y, y+h, y+h, y], lw=1, c="k") 
#添加P值属性
ax.text((x1+x2)*.5, y+h, p_value_cov, ha='center', va='bottom', color="k",fontsize=15,fontweight="bold")
# 修饰
for spine in ["top","right"]:
    ax.spines[spine].set_visible(False)
ax.set(xlim=(-1,2),ylim=(0.3,2.5),xticks=[0,1], xticklabels=ticks,
       xlabel="X Axis Title",ylabel="T Axis Title")
ax.grid(False)
ax.legend(frameon=False,loc="upper left")
plt.tight_layout()
fig.savefig('\第7章 其他类型图的绘制\图7-2-3 Matplotlib前后图样式绘制示例_d.pdf',bbox_inches='tight')
fig.savefig('\第7章 其他类型图的绘制\图7-2-3 Matplotlib前后图样式绘制示例_d.png', 
            bbox_inches='tight',dpi=300)
plt.show()

#*************************图7-2-4 Matplotlib前后图样式绘制示例（彩色系）*******************************

import scipy
import numpy as np
import pandas as pd
import pingouin as pg
import matplotlib.pyplot as plt
from proplot import rc
rc["xtick.minor.visible"] = False
rc["ytick.minor.visible"] = False

ba_data = pd.read_excel(r"\第7章 其他类型图的绘制\前后图数据.xlsx")

#a）前后图基础样式绘制（彩色）
ticks = ["Before","After"]
Before = ba_data["Before"].values
After = ba_data["After"].values
x = np.arange(len(ticks))

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
for i in range(len(Before)):
    ax.plot([0,1], [Before[i], After[i]], c='k',zorder=0,lw=.8)
ax.scatter(np.repeat(x[0],len(Before)), Before,color="#459DFF",ec="k",s=80,label="Before")
ax.scatter(np.repeat(x[1],len(After)), After,color="#FFCC37",ec="k",s=80,label="After")
ax.legend(loc="upper left",frameon=False)
# 修饰
for spine in ["top","right"]:
    ax.spines[spine].set_visible(False)
# 添加刻度和刻度标签
ax.set(xlim=(-.5,1.5),ylim=(0.3,2.5),xticks=[0,1], xticklabels=['Before', 'After'],
       xlabel="X Axis Title",ylabel="T Axis Title")
ax.grid(False)
plt.tight_layout()
fig.savefig('\第7章 其他类型图的绘制\图7-2-4 Matplotlib前后图样式绘制示例（彩色系）_a.pdf',bbox_inches='tight')
fig.savefig('\第7章 其他类型图的绘制\图7-2-4 Matplotlib前后图样式绘制示例（彩色系）_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()

#b）前后图误差属性添加样式绘制（彩色）
# 计算标准误差
before_mean = ba_data["Before"].mean()
after_mean = ba_data["After"].mean()
before_sd = ba_data["Before"].std()
after_sd = ba_data["After"].std()

ticks_labels = ["Before/\nError","Before","After","After/\nError"]
Before = ba_data["Before"].values
After = ba_data["After"].values
x = np.arange(len(ticks_labels))

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
for i in range(len(Before)):
    ax.plot([0,1], [Before[i], After[i]], c='k',zorder=0,lw=.8)
ax.scatter(np.repeat(x[0],len(Before)), Before,color="#459DFF",ec="k",s=80,label="Before")
ax.scatter(np.repeat(x[1],len(After)), After,color = "#FFCC37",ec="k",s=80,label="After")
# 绘制误差图
ax.errorbar(-.5,before_mean,before_sd,fmt='o',markersize=10,color="#459DFF",mec='k',linewidth=1, capsize=5)
ax.errorbar(1.5,after_mean,after_sd,fmt='o',markersize=10,color="#FFCC37",mec='k',linewidth=1, capsize=5)
# 修饰
for spine in ["top","right"]:
    ax.spines[spine].set_visible(False)
ax.set(xlim=(-1,2),ylim=(0.3,2.5),xticks=[-.5,0,1,1.5], xticklabels=ticks_labels,
       xlabel="X Axis Title",ylabel="T Axis Title")
ax.grid(False)
ax.legend(loc="upper left",frameon=False)
plt.tight_layout()
fig.savefig('\第7章 其他类型图的绘制\图7-2-4 Matplotlib前后图样式绘制示例（彩色系）_b.pdf',bbox_inches='tight')
fig.savefig('\第7章 其他类型图的绘制\图7-2-4 Matplotlib前后图样式绘制示例（彩色系）_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()

#c）前后图均值柱形图添加样式绘制（彩色）
# 计算标准误差
before_mean = ba_data["Before"].mean()
after_mean = ba_data["After"].mean()
ticks_labels = ["Before","After",]
Before = ba_data["Before"].values
After = ba_data["After"].values
x = np.arange(len(ticks_labels))

#计算errorbar 

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
for i in range(len(Before)):
    ax.plot([0,1], [Before[i], After[i]], c='k',zorder=0,lw=.8)
ax.scatter(np.repeat(x[0],len(Before)), Before,color="#459DFF",ec="k",s=80,label="Before")
ax.scatter(np.repeat(x[1],len(After)), After,color = "#FFCC37",ec="k",s=80,label="After")

# 绘制均值柱形图
ax.bar(x=0,height=before_mean,width=.6,color="none",edgecolor="#459DFF",zorder=0,label="Before Mean")
ax.bar(x=1,height=after_mean,width=.6,color="none",edgecolor="#FFCC37",zorder=0,label="After Mean")

# 修饰
for spine in ["top","right"]:
    ax.spines[spine].set_visible(False)
ax.set(xlim=(-1,2),ylim=(0.3,2.5),xticks=[0,1,], xticklabels=ticks_labels,
       xlabel="X Axis Title",ylabel="T Axis Title")
ax.legend(frameon=False,loc="upper left",handlelength=1,handleheight=1,fontsize=10)
ax.grid(False)
plt.tight_layout()
fig.savefig('\第7章 其他类型图的绘制\图7-2-4 Matplotlib前后图样式绘制示例（彩色系）_c.pdf',bbox_inches='tight')
fig.savefig('\第7章 其他类型图的绘制\图7-2-4 Matplotlib前后图样式绘制示例（彩色系）_c.png', 
            bbox_inches='tight',dpi=300)
plt.show()

#d）前后图均值柱形图p值添加样式绘制（彩色）
import scipy
Before = ba_data["Before"].values
After = ba_data["After"].values
stat,p_value = scipy.stats.ttest_ind(Before,After,equal_var=False)
p_value_cov = convert_pvalue_to_asterisks(p_value)
ticks = ["Before","After",]
Before = ba_data["Before"].values
After = ba_data["After"].values
x = np.arange(len(ticks))

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
for i in range(len(Before)):
    ax.plot([0,1], [Before[i], After[i]], c='k',zorder=0,lw=.8)
ax.scatter(np.repeat(x[0],len(Before)), Before,color="#459DFF",ec="k",s=80,label="Before")
ax.scatter(np.repeat(x[1],len(After)), After,color = "#FFCC37",ec="k",s=80,label="After")
# 绘制均值柱形图
ax.bar(x=0,height=before_mean,width=.6,color="none",edgecolor="#459DFF",zorder=0,label="Before Mean")
ax.bar(x=1,height=after_mean,width=.6,color="none",edgecolor="#FFCC37",zorder=0,label="After Mean")
# 添加P值
x1, x2 = 0, 1
y,h = 2.4,.05
#绘制横线位置
ax.plot([x1, x1, x2, x2], [y, y+h, y+h, y], lw=1, c="k") 
#添加P值属性
ax.text((x1+x2)*.5, y+h, p_value_cov, ha='center', va='bottom', color="k",fontsize=15,fontweight="bold")
# 修饰
for spine in ["top","right"]:
    ax.spines[spine].set_visible(False)
ax.set(xlim=(-1,2),ylim=(0.3,2.5),xticks=[0,1], xticklabels=ticks,
       xlabel="X Axis Title",ylabel="T Axis Title")
ax.grid(False)
ax.legend(frameon=False,loc="upper left",handlelength=1,handleheight=1.2,fontsize=10)
plt.tight_layout()
fig.savefig('\第7章 其他类型图的绘制\图7-2-4 Matplotlib前后图样式绘制示例（彩色系）_d.pdf',bbox_inches='tight')
fig.savefig('\第7章 其他类型图的绘制\图7-2-4 Matplotlib前后图样式绘制示例（彩色系）_d.png', 
            bbox_inches='tight',dpi=300)
plt.show()