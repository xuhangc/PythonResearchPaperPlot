"""
编写时间：2022年5月06日 17：30

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。

代码中Proplot包绘制的部分可能与Matplotlib绘制不同，需注意两者绘图语法的不同~~

"""
#注意：本案例中引入的SciencePlots库主题方式会随着SciencePlots版本的更新发生改变，读者还需参考其官网引入的正确方式。

import math
import PythonMeta as PMA
import numpy as np
from proplot import rc

rc["figure.facecolor"]="w"
rc["font.family"] = "Times New Roman"
rc["axes.labelsize"] = 15
rc["tick.labelsize"] = 12
rc["suptitle.size"] = 15
rc["title.size"] = 14

import PythonMeta as PMA
samp_cate = [  
        "Fang 2015,15,40,24,37",
        "Gong 2012,10,40,18,35",
        "Liu 2015,30,50,40,50",
        "Long 2012,19,40,26,40",
        "Wang 2003,7,86,15,86",
        "Chen 2008,20,60,28,60",
        "Guo 2014,31,51,41,51",
        "Li 2015,29,61,31,60",
        "Yang 2006,21,40,31,40",
        "Zhao 2012,27,40,30,40",]
settings = {
        "datatype": "CATE",  # for CATEgorical/count/binary/dichotomous data
        "models": "Fixed",  # models: Fixed or Random
        "algorithm": "MH",  # algorithm: MH, Peto or IV
        "effect": "RR"}  # effect size: RR, OR, RD

d = PMA.Data()  
m = PMA.Meta()  # Load Meta class
f = PMA.Fig()  # Load Fig class
# You should always tell the datatype first!!!
d.datatype = settings["datatype"]  # set data type, 'CATE' for binary data or 'CONT' for continuous data
studies = d.getdata(samp_cate)  # load data
# studies = d.getdata(d.readfile("studies.txt"))  #get data from a data file, see examples of data files
#print(showstudies(studies, d.datatype))  # show studies
m.subgroup = d.subgroup  # set the subgroup
m.datatype = d.datatype  # set data type for meta-analysis calculating
m.models = settings["models"]  # set effect models: 'Fixed' or 'Random'
m.algorithm = settings["algorithm"]  # set algorithm, based on datatype and effect size
m.effect = settings["effect"]  # set effect size:RR/OR/RD for binary data; SMD/MD for continuous data
results = m.meta(studies)  # performing the analysis

effs = results
if effs[0][0] in "OR,RR" :
    def _x_tran0(x):
        return math.log(x)
    def _x_tran1(x):
        return math.exp(x)
elif effs[0][0] in "RD,MD,SMD" :
    def _x_tran0(x):
        return x
    def _x_tran1(x):
        return x
    
x=[];y=[];ci=[]
for i in range(1,len(effs)):
    x.append(_x_tran0(effs[i][1]))
    y.append(effs[i][6])
    ci.append(_x_tran0(effs[i][1])-effs[i][6]*1.96)
    ci.append(_x_tran0(effs[i][1])+effs[i][6]*1.96)
    
#(a) 常规漏斗图绘制示例
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
ax.plot(x,y,"o",markersize=7,color="r",mec="k",label = "Studies",zorder=10)

ymax = max(y)
cimax = max(ci)
#plt.ylim(ymax*1.05,0)
ax.set_ylim((ymax*1,0))
x0 = _x_tran0(effs[0][1])
ax.plot([x0,x0],[0,ymax],color="k", linestyle=":", lw=1,label="Overall effect line")
ax.plot([x0,2*x0-cimax],[0,ymax],color="k", linestyle="--", lw=1)
ax.plot([x0,cimax],[0,ymax],color="k", linestyle="--", label="Boundary lines of effect",lw=1)
#绘制三角填充
trianglex = [2*x0-cimax, x0,cimax] 
triangley = [ ymax,0, ymax]
ax.fill(trianglex, triangley,"white")

ax.grid(False,axis="x")
ax.grid(axis="y",linewidth=.8,color="w",alpha=1)
ax.set_facecolor("#D3D3D3")
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.set_xticklabels([round(_x_tran1(x),2) for x in ax.get_xticks()])
ax.set(xlabel="Effect Size",ylabel="Standard Error")
#ax.legend(loc="center",ncol=2,fontsize=8,bbox_to_anchor=(.5,-.3),handletextpad=.1)
ax.legend(loc="upper right",ncol=1,fontsize=7.2,handletextpad=.1)
plt.tight_layout()

fig.savefig('\第7章 其他类型图的绘制\图7-6-1常规漏斗图和等值线增强漏斗图绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第7章 其他类型图的绘制\图7-6-1常规漏斗图和等值线增强漏斗图绘制示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# (b)等值线增强漏斗图绘制示例

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
ax.plot(x,y,"o",markersize=6,color="k",label = "Studies",zorder=10)

ymax = max(y)
cimax = max(ci)
ax.set_ylim((ymax*1,0))
x0 = _x_tran0(effs[0][1])
ax.plot([x0,x0],[0,ymax],color="k", linestyle="-", lw=1,label="Overall effect line",
        zorder=12)

#绘制contour enhanced
# 1%< p <5%
trianglex = [ -2.58*max(y), 0, 2.58*max(y)] 
triangley = [ max(y),0, max(y)] 
ax.fill(trianglex, triangley,color="#FDA429",lw=.5,ec="k",label="1%< p <5%")
#5%< p <10%
trianglex = [ -1.96*max(y), 0,1.96*max(y)] 
triangley = [ max(y),0, max(y)] 
ax.fill(trianglex, triangley,color="#FC0D1B",lw=.5,ec="k",label="5%< p <10%")
#p > 10%
trianglex = [ -1.65*max(y), 0,1.65*max(y)] 
triangley = [ max(y),0, max(y)] 
ax.fill(trianglex, triangley,color="w",lw=.5,ec="k",label="p > 10%")

ax.grid(False,axis="x")
ax.grid(axis="y",linewidth=.8,color="w",alpha=1)
ax.set_facecolor("#D3D3D3")
ax.set_axisbelow(True)
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.legend(loc="upper right",ncol=1,fontsize=7.5)
ax.set(xlabel="Effect Size",ylabel="Standard Error")
plt.tight_layout()

fig.savefig('\第7章 其他类型图的绘制\图7-6-1常规漏斗图和等值线增强漏斗图绘制示例_b.pdf',bbox_inches='tight')
fig.savefig('\第7章 其他类型图的绘制\图7-6-1常规漏斗图和等值线增强漏斗图绘制示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()


