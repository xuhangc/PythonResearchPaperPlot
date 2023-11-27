"""
编写时间：2022年4月25日 16：30

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

import numpy as np
import pandas as pd
import seaborn as sns
import proplot as pplt
import matplotlib.pyplot as plt
from mpl_chord_diagram import chord_diagram
from colormaps import parula

from proplot import rc
rc["font.family"] = "Times New Roman"
rc["axes.labelsize"] = 15
rc["tick.labelsize"] = 12
rc["suptitle.size"] = 15
rc["title.size"] = 14

plt.rcParams["image.composite_image"] = False


chord_df01 = pd.read_excel(r'\第5章 多变量图形的绘制\Chord Diagram data01_修订.xlsx')
# DataFrame.pivot_table()函数将长数据转换成宽数据
chord_df01_matx = pd.pivot_table(chord_df01,values="values",index="B",columns="A",fill_value=0)

color_list = ["#EF0000","#18276F","#FEC211","#3BC371","#666699",
              "#134B24","#FF6666","#6699CC","#CC6600","#009999"]
              
              
# a） 长数据和弦图绘制示例              
flux = chord_df01_matx.values
names = chord_df01_matx.columns.to_list()
colors = color_list[:len(names)]
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
chord_diagram(flux,names,chordwidth=.5,colors=colors,width=.05,fontsize=9,ax=ax)
plt.tight_layout()
fig.savefig('\第5章 多变量图形的绘制\图5-8-2 长、宽数据和弦图及其渐变色填充绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第5章 多变量图形的绘制\图5-8-2 长、宽数据和弦图及其渐变色填充绘制示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()


# b）长数据和弦图渐变色填充绘制示例
from mpl_chord_diagram import chord_diagram

flux = chord_df01_matx.values
names = chord_df01_matx.columns.to_list()
colors = color_list[:len(names)]
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
chord_diagram(flux,names,chordwidth=.5,colors=colors,width=.05,fontsize=9,use_gradient=True,ax=ax)
plt.tight_layout()

fig.savefig('\第5章 多变量图形的绘制\图5-8-2 长、宽数据和弦图及其渐变色填充绘制示例_b.pdf',bbox_inches='tight')
fig.savefig('\第5章 多变量图形的绘制\图5-8-2 长、宽数据和弦图及其渐变色填充绘制示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()



chord_df02 = pd.read_excel(r"\第5章 多变量图形的绘制\Chord Diagram data02.xlsx")

# c）宽数据和弦图绘制示例
from mpl_chord_diagram import chord_diagram

flux = chord_df02.values
names = chord_df02.columns.to_list()
colors = color_list[:len(names)]
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
chord_diagram(flux,names,chordwidth=.8,width=.05,fontsize=8,colors=colors,alpha=.8,ax=ax)
plt.tight_layout()
fig.savefig('\第5章 多变量图形的绘制\图5-8-2 长、宽数据和弦图及其渐变色填充绘制示例_c.pdf',bbox_inches='tight')
fig.savefig('\第5章 多变量图形的绘制\图5-8-2 长、宽数据和弦图及其渐变色填充绘制示例_c.png', 
            bbox_inches='tight',dpi=300)
plt.show()

# d）宽数据和弦图渐变色填充绘制示例

from mpl_chord_diagram import chord_diagram

flux = chord_df02.values
names = chord_df02.columns.to_list()
colors = color_list[:len(names)]
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
chord_diagram(flux,names,chordwidth=.8,width=.05,fontsize=8,colors=colors,alpha=.8,use_gradient=True,ax=ax)
plt.tight_layout()

fig.savefig('\第5章 多变量图形的绘制\图5-8-2 长、宽数据和弦图及其渐变色填充绘制示例_d.pdf',bbox_inches='tight')
fig.savefig('\第5章 多变量图形的绘制\图5-8-2 长、宽数据和弦图及其渐变色填充绘制示例_d.png', 
            bbox_inches='tight',dpi=300)
plt.show()
