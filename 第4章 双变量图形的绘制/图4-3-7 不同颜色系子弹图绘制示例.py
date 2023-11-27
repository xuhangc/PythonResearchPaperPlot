
"""
编写时间：2022年4月18日 21：50

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

"""
此代码为使用Python-Prolot包进行学术风格图表绘制，绘图语法和Matplotlib有所不同，需注意。
"""
import pandas as pd
import numpy as np
import proplot as pplt
import seaborn as sns
import matplotlib.pyplot as plt
from proplot import rc
from colormaps import parula

rc["axes.labelsize"] = 15
rc['tick.labelsize'] = 13
rc["suptitle.size"] = 15
rc["figure.facecolor"]="w"
rc["font.family"] = "Times New Roman"
rc["xtick.minor.visible"] = False
rc["ytick.minor.visible"] = False
rc["xtick.bottom"] = False
rc["ytick.left"] = False

bullet_data = pd.read_excel(r"\第4章 双变量图形的绘制\bullet chart data.xlsx")

# a）灰色系子弹图绘制

def bullet_charts(ax,value,poor,average,good,target,name):
    #values
    ax.barh(y=.5,width=value,height=.3,color="k",zorder=5,label="Value")
    #Poor
    ax.barh(y=.5,width=poor,height=1,color="gray",zorder=4,label="Poor")
    #Average
    ax.barh(y=.5,width=average,height=1,color="silver",zorder=3,label="Average")
    #Good
    ax.barh(y=.5,width=good,height=1,color="whitesmoke",zorder=2,label="Good")
    #Target
    ax.axvline(x=target,ymin=0.2,ymax=0.8,color="k",lw=2,zorder=5)
    for spine in ["top","left","right"]:
        ax.spines[spine].set_visible(False)
        ax.text(-.03,.5,str(name).replace("\\n","\n"),transform=ax.transAxes,
                va="center",ha="right",fontsize=13,fontweight="bold")
        ax.set_yticks([])
        ax.set_ylim(0,1)
        ax.set_xlim(0,good)
        ax.grid(False)
    return ax
    
data_index = bullet_data["type"].to_list()
fig,axs = plt.subplots(5,1,figsize=(6,3.5),dpi=100,facecolor="w")

for ax, name in zip(axs.flat,data_index):
    value = bullet_data.loc[bullet_data["type"]==name,"value"].to_numpy()
    poor = bullet_data.loc[bullet_data["type"]==name,"poor"].to_numpy()
    average = bullet_data.loc[bullet_data["type"]==name,"average"].to_numpy()
    good = bullet_data.loc[bullet_data["type"]==name,"good"].to_numpy()
    target = bullet_data.loc[bullet_data["type"]==name,"target"].to_numpy()
    bullet_charts(ax,value,poor,average,good,target,name)
    
handles, labels = ax.get_legend_handles_labels()
fig.legend(handles, labels, ncol=4,loc='lower right',bbox_to_anchor=(.9,-1.5),
           bbox_transform=ax.transAxes,
           frameon=False,fontsize=11)
plt.tight_layout()

fig.savefig('\第4章 双变量图形的绘制\图4-3-7 不同颜色系子弹图绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-3-7 不同颜色系子弹图绘制示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show() 
    
# b）彩色系子弹图绘制

colors = ["#EF0000","#18276F","#FEC211","#3BC371","#666699"]
data_index = bullet_data["type"].to_list()

def bullet_charts_color(ax,value,poor,average,good,target,name):
    #values
    ax.barh(y=.5,width=value,height=.3,color=colors[0],label="Value",zorder=5)
    #Poor
    ax.barh(y=.5,width=poor,height=1,color=colors[1],label="Poor",zorder=4)
    #Average
    ax.barh(y=.5,width=average,height=1,color=colors[2],label="Average",zorder=3)
    #Good
    ax.barh(y=.5,width=good,height=1,color=colors[3],label="Good",zorder=2)
    #Target
    ax.axvline(x=target,ymin=0.2,ymax=0.8,color=colors[4],lw=2,zorder=5)
    for spine in ["top","left","right"]:
        ax.spines[spine].set_visible(False)
    ax.text(-.03,.5,str(name).replace("\\n","\n"),transform=ax.transAxes,
            va="center",ha="right",fontsize=13,fontweight="bold")
    ax.text(1.02,.5,str(value).replace("[","").replace(']',""),transform=ax.transAxes,
            va="center",ha="left",color=colors[0],fontsize=11,fontweight="bold")
    ax.set_yticks([])
    ax.set_ylim(0,1)
    ax.set_xlim(0,good)
    ax.grid(False)
    return ax
    
fig,axs = plt.subplots(5,1,figsize=(6,3.5),dpi=100,facecolor="w")
for ax, name in zip(axs.flat,data_index):
    value = bullet_data.loc[bullet_data["type"]==name,"value"].to_numpy()
    poor = bullet_data.loc[bullet_data["type"]==name,"poor"].to_numpy()
    average = bullet_data.loc[bullet_data["type"]==name,"average"].to_numpy()
    good = bullet_data.loc[bullet_data["type"]==name,"good"].to_numpy()
    target = bullet_data.loc[bullet_data["type"]==name,"target"].to_numpy()
    bullet_charts_color(ax,value,poor,average,good,target,name)
    
handles, labels = ax.get_legend_handles_labels()
fig.legend(handles, labels, ncol=4,loc='lower right',bbox_to_anchor=(1,-1.5),
           bbox_transform=ax.transAxes,
           frameon=False,fontsize=11)
plt.tight_layout()

fig.savefig('\第4章 双变量图形的绘制\图4-3-7 不同颜色系子弹图绘制示例_b.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-3-7 不同颜色系子弹图绘制示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show() 