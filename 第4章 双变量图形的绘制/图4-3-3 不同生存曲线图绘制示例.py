
"""
编写时间：2022年4月18日 18：50

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
from lifelines import KaplanMeierFitter
from proplot import rc
rc["axes.labelsize"] = 15
rc['tick.labelsize'] = 13
rc["suptitle.size"] = 15
rc["figure.facecolor"]="w"
rc["font.family"] = "Times New Roman"
rc["xtick.minor.visible"] = False
rc["ytick.minor.visible"] = False
rc["xtick.bottom"] = False
rc["ytick.left"] = False


survive_data = pd.read_csv(r"\第4章 双变量图形的绘制\Survivorship Curve_data.csv")
#数据处理
select = ['time', 'status', 'age', 'sex', 'ph.ecog', 'ph.karno','pat.karno', 'meal.cal', 'wt.loss']
survive_data = survive_data[select]

survive_data["status"] = survive_data["status"] - 1
survive_data["sex"] = survive_data["sex"] - 1

survive_data["ph.karno"].fillna(survive_data["ph.karno"].mean(), inplace = True)
survive_data["pat.karno"].fillna(survive_data["pat.karno"].mean(), inplace = True)
survive_data["meal.cal"].fillna(survive_data["meal.cal"].mean(), inplace = True)
survive_data["wt.loss"].fillna(survive_data["wt.loss"].mean(), inplace = True)
survive_data.dropna(inplace=True)
survive_data["ph.ecog"] = survive_data["ph.ecog"].astype("int64")

T = survive_data["time"]
E = survive_data["status"]

# a）单系列数据生存曲线图绘制（未添加置信区间）

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
kmf = KaplanMeierFitter()
kmf.fit(durations = T, event_observed = E)
ax = kmf.plot_survival_function(ci_show=False,color="k",lw=1,ax=ax)
ax.grid(False)
ax.set(xlabel="Timeline",ylabel="Survival Probability")
plt.tight_layout()

fig.savefig('\第4章 双变量图形的绘制\图4-3-3 不同生存曲线图绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-3-3 不同生存曲线图绘制示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()    

# b）单系列数据生存曲线图绘制（添加置信区间）

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
kmf = KaplanMeierFitter()
kmf.fit(durations = T, event_observed = E)
ax = kmf.plot_survival_function(color="k",lw=1,ax=ax)
ax.grid(False)
ax.set(xlabel="Timeline",ylabel="Survival Probability")
plt.tight_layout()

fig.savefig('\第4章 双变量图形的绘制\图4-3-3 不同生存曲线图绘制示例_b.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-3-3 不同生存曲线图绘制示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show() 

# c）单系列数据生存曲线图绘制（添加统计文本信息）

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
kmf = KaplanMeierFitter()
kmf.fit(durations = T, event_observed = E)
ax = kmf.plot_survival_function(color="k",lw=1,at_risk_counts=True,ax=ax)
ax.grid(False)
ax.set(xlabel="Timeline",ylabel="Survival Probability")
plt.tight_layout()

fig.savefig('\第4章 双变量图形的绘制\图4-3-3 不同生存曲线图绘制示例_c.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-3-3 不同生存曲线图绘制示例_c.png', 
            bbox_inches='tight',dpi=300)
plt.show() 

# d）双系列数据生存曲线图绘制（添加统计文本信息）

rc["axes.labelsize"] = 11
rc["tick.labelsize"] = 8
rc["suptitle.size"] = 15
rc["title.size"] = 14

#绘制多生存曲线
Male_data = survive_data.loc[survive_data["sex"]==0,"time"]
#绘制多生存曲线
from lifelines.plotting import add_at_risk_counts

Male_data = survive_data[survive_data["sex"]==0]
Female_data = survive_data[~survive_data["sex"]==0]

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
kmf_Male = kmf.fit(durations = Male_data["time"], event_observed = Male_data["status"], label = "Male")
kmf_Male.plot_survival_function(color="r",lw=1,ax=ax)

kmf_Female = kmf.fit(durations = Female_data["time"], event_observed = Female_data["status"], label = "Female")
kmf_Female.plot_survival_function(color="k",lw=1,ax=ax)

ax.grid(False)
ax.set(xlabel="Timeline",ylabel="Survival Probability")
ax.legend(loc="lower left")
# 添加文本信息
add_at_risk_counts(kmf_Male, kmf_Female, ax=ax)
plt.tight_layout()

fig.savefig('\第4章 双变量图形的绘制\图4-3-3 不同生存曲线图绘制示例_d.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-3-3 不同生存曲线图绘制示例_d.png', 
            bbox_inches='tight',dpi=300)
plt.show() 


