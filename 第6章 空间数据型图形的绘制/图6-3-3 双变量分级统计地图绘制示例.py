"""
编写时间：2022年4月28日 20：30

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

"""
此代码为使用Python-Prolot包进行学术风格图表绘制，绘图语法和Matplotlib有所不同，需注意。
"""

import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from colormaps import parula

from proplot import rc
rc["font.family"] = "Times New Roman"
rc["axes.labelsize"] = 15
rc["tick.labelsize"] = 10
rc["suptitle.size"] = 15
rc["title.size"] = 14

Bivariate_data.read_excel(r"\第6章 空间数据型图形的绘制\Bivariate_choropleth_data.xlsx")
map_fig0 = gpd.read_file(r"\第6章 空间数据型图形的绘制\Virtual_Map1.shp")
# 合并数据
Biva_merge = map_fig0.merge(Bivariate_data,on="country")


# 定义 bins
bins = [0, 0.33, 0.66, 1]

# 第一个分箱变量 - x
Biva_merge['Var1_Class'] = pd.cut(Biva_merge['Bivariate_x'], bins=bins, include_lowest=True)
Biva_merge['Var1_Class'] = Biva_merge['Var1_Class'].astype('str')

# 第一个分箱变量 - y
Biva_merge['Var2_Class'] = pd.cut(Biva_merge['Bivariate_y'], bins=bins, include_lowest=True)
Biva_merge['Var2_Class'] = Biva_merge['Var2_Class'].astype('str')

# 分箱码转成 1, 2, 3
x_class_codes = np.arange(1, len(bins))
d = dict(zip(Biva_merge['Var1_Class'].value_counts().sort_index().index, x_class_codes))
Biva_merge['Var1_Class'] = Biva_merge['Var1_Class'].replace(d)

# 分箱码转成A, B, C
y_class_codes = ['A', 'B', 'C']
d = dict(zip(Biva_merge['Var2_Class'].value_counts().sort_index().index, y_class_codes))
Biva_merge['Var2_Class'] = Biva_merge['Var2_Class'].replace(d)

# 合并两个变量成最终的双变量纬度数据_Bi_Class
Biva_merge['Bi_Class'] = Biva_merge['Var1_Class'].astype('str') + Biva_merge['Var2_Class']


# 根据实际所需进行颜色筛选
colors = ['#e8e8e8', # 1A
          '#dfb0d6', # 1B
          #'#be64ac', # 1C
          #'#ace4e4', # 2A
          '#a5add3', # 2B
          '#8c62aa', # 2C
          '#5ac8c8', # 3A
          '#5698b9', # 3B
          '#3b4994'] # 3C
            
cmap = mpl.colors.ListedColormap(colors)

# a）双变量分级统计地图示例一
fig,ax = plt.subplots(figsize=(5,4.5),dpi=100,facecolor="w")
map_fig = map_fig02.plot("country",facecolor='none', edgecolor='k',lw=.4,zorder=5,ax=ax)
Bivariate_fig = Biva_merge.plot(column='Bi_Class',cmap=cmap,categorical=True,legend=False,ax=ax)

# 添加图例
ax2 = fig.add_axes([0.75, 0.25, 0.12, 0.12])                                
alpha = 1 
# Column 1
ax2.axvspan(xmin=0, xmax=0.33, ymin=0, ymax=0.33, alpha=alpha, color=all_colors[0])
ax2.axvspan(xmin=0, xmax=0.33, ymin=0.33, ymax=0.66, alpha=alpha, color=all_colors[1])
ax2.axvspan(xmin=0, xmax=0.33, ymin=0.66, ymax=1, alpha=alpha, color=all_colors[2])
# Column 2
ax2.axvspan(xmin=0.33, xmax=0.66, ymin=0, ymax=0.33, alpha=alpha, color=all_colors[3])
ax2.axvspan(xmin=0.33, xmax=0.66, ymin=0.33, ymax=0.66, alpha=alpha, color=all_colors[4])
ax2.axvspan(xmin=0.33, xmax=0.66, ymin=0.66, ymax=1, alpha=alpha, color=all_colors[5])
# Column 3
ax2.axvspan(xmin=0.66, xmax=1, ymin=0, ymax=0.33, alpha=alpha, color=all_colors[6])
ax2.axvspan(xmin=0.66, xmax=1, ymin=0.33, ymax=0.66, alpha=alpha, color=all_colors[7])
ax2.axvspan(xmin=0.66, xmax=1, ymin=0.66, ymax=1, alpha=alpha, color=all_colors[8])
ax2.axis('off')
ax2.annotate("", xy=(0, 1), xytext=(0, 0), 
             arrowprops=dict(arrowstyle="->", lw=.8)) # draw arrow for x 
ax2.annotate("", xy=(1, 0), xytext=(0, 0), 
             arrowprops=dict(arrowstyle="->", lw=.8)) # draw arrow for y 
ax2.text(s='Bivariate_x', x=0.05, y=-0.25,fontsize=7) # annotate x axis
ax2.text(s='Bivariate_y', x=-0.25, y=0.1, rotation=90,fontsize=7); 

ax.grid(False)
ax.set_ylim((30, 60))
ax.set_xlim((100, 140))
ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)
ax.spines.left.set_position(("outward",10))
ax.spines.bottom.set_position(("outward",10))
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
fig.tight_layout()
fig.savefig('\第6章 空间数据型图形的绘制\图6-3-3 双变量分级统计地图绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第6章 空间数据型图形的绘制\图6-3-3 双变量分级统计地图绘制示例_a.png', 
            bbox_inches='tight',dpi=300)         
plt.show()

# b）双变量分级统计地图示例二
import matplotlib as mpl
all_colors = all_colors = ['#e8e8e8', '#b0d5df', '#64acbe', '#e4acac', '#ad9ea5', 
                           '#627f8c', '#c85a5a', '#985356', '#574249']
# 根据实际所需进行颜色筛选
colors = ['#e8e8e8', # 1A
          '#b0d5df', # 1B
          # '#64acbe', # 1C
          #'#e4acac', # 2A
          '#ad9ea5', # 2B
          '#627f8c', # 2C
          '#c85a5a', # 3A
          '#985356', # 3B
          '#574249'] # 3C
     
cmap = mpl.colors.ListedColormap(colors)
fig,ax = plt.subplots(figsize=(5,4.5),dpi=100,facecolor="w")
map_fig = map_fig02.plot("country",facecolor='none', edgecolor='k',lw=.4,zorder=5,ax=ax)
Bivariate_fig = Biva_merge.plot(column='Bi_Class',cmap=cmap,categorical=True,legend=False,ax=ax)

# 添加图例
ax2 = fig.add_axes([0.75, 0.25, 0.12, 0.12])                                
alpha = 1 
# Column 1
ax2.axvspan(xmin=0, xmax=0.33, ymin=0, ymax=0.33, alpha=alpha, color=all_colors[0])
ax2.axvspan(xmin=0, xmax=0.33, ymin=0.33, ymax=0.66, alpha=alpha, color=all_colors[1])
ax2.axvspan(xmin=0, xmax=0.33, ymin=0.66, ymax=1, alpha=alpha, color=all_colors[2])
# Column 2
ax2.axvspan(xmin=0.33, xmax=0.66, ymin=0, ymax=0.33, alpha=alpha, color=all_colors[3])
ax2.axvspan(xmin=0.33, xmax=0.66, ymin=0.33, ymax=0.66, alpha=alpha, color=all_colors[4])
ax2.axvspan(xmin=0.33, xmax=0.66, ymin=0.66, ymax=1, alpha=alpha, color=all_colors[5])
# Column 3
ax2.axvspan(xmin=0.66, xmax=1, ymin=0, ymax=0.33, alpha=alpha, color=all_colors[6])
ax2.axvspan(xmin=0.66, xmax=1, ymin=0.33, ymax=0.66, alpha=alpha, color=all_colors[7])
ax2.axvspan(xmin=0.66, xmax=1, ymin=0.66, ymax=1, alpha=alpha, color=all_colors[8])
ax2.axis('off')
ax2.annotate("", xy=(0, 1), xytext=(0, 0), 
             arrowprops=dict(arrowstyle="->", lw=.8)) # draw arrow for x 
ax2.annotate("", xy=(1, 0), xytext=(0, 0), 
             arrowprops=dict(arrowstyle="->", lw=.8)) # draw arrow for y 
ax2.text(s='Bivariate_x', x=0.05, y=-0.25,fontsize=7) # annotate x axis
ax2.text(s='Bivariate_y', x=-0.25, y=0.1, rotation=90,fontsize=7); 

ax.grid(False)
ax.set_ylim((30, 60))
ax.set_xlim((100, 140))
ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)
ax.spines.left.set_position(("outward",10))
ax.spines.bottom.set_position(("outward",10))
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
fig.tight_layout()
fig.savefig('\第6章 空间数据型图形的绘制\图6-3-3 双变量分级统计地图绘制示例_b.pdf',bbox_inches='tight')
fig.savefig('\第6章 空间数据型图形的绘制\图6-3-3 双变量分级统计地图绘制示例_b.png', 
            bbox_inches='tight',dpi=300)         
plt.show()

# c）双变量分级统计地图示例三
import matplotlib as mpl
all_colors = all_colors = ['#e8e8e8', '#b8d6be', '#73ae80', '#b5c0da', '#90b2b3', 
                           '#5a9178', '#6c83b5', '#567994', '#2b5a5b']
# 根据实际所需进行颜色筛选
colors = ['#e8e8e8', # 1A
          '#b8d6be', # 1B
          # '#73ae80', # 1C
          #'#b5c0da', # 2A
          '#90b2b3', # 2B
          '#5a9178', # 2C
          '#6c83b5', # 3A
          '#567994', # 3B
          '#2b5a5b'] # 3C
     
cmap = mpl.colors.ListedColormap(colors)
fig,ax = plt.subplots(figsize=(5,4.5),dpi=100,facecolor="w")
map_fig = map_fig02.plot("country",facecolor='none', edgecolor='k',lw=.4,zorder=5,ax=ax)
Bivariate_fig = Biva_merge.plot(column='Bi_Class',cmap=cmap,categorical=True,legend=False,ax=ax)

# 添加图例
ax2 = fig.add_axes([0.75, 0.25, 0.12, 0.12])                                
alpha = 1 
# Column 1
ax2.axvspan(xmin=0, xmax=0.33, ymin=0, ymax=0.33, alpha=alpha, color=all_colors[0])
ax2.axvspan(xmin=0, xmax=0.33, ymin=0.33, ymax=0.66, alpha=alpha, color=all_colors[1])
ax2.axvspan(xmin=0, xmax=0.33, ymin=0.66, ymax=1, alpha=alpha, color=all_colors[2])
# Column 2
ax2.axvspan(xmin=0.33, xmax=0.66, ymin=0, ymax=0.33, alpha=alpha, color=all_colors[3])
ax2.axvspan(xmin=0.33, xmax=0.66, ymin=0.33, ymax=0.66, alpha=alpha, color=all_colors[4])
ax2.axvspan(xmin=0.33, xmax=0.66, ymin=0.66, ymax=1, alpha=alpha, color=all_colors[5])
# Column 3
ax2.axvspan(xmin=0.66, xmax=1, ymin=0, ymax=0.33, alpha=alpha, color=all_colors[6])
ax2.axvspan(xmin=0.66, xmax=1, ymin=0.33, ymax=0.66, alpha=alpha, color=all_colors[7])
ax2.axvspan(xmin=0.66, xmax=1, ymin=0.66, ymax=1, alpha=alpha, color=all_colors[8])
ax2.axis('off')
ax2.annotate("", xy=(0, 1), xytext=(0, 0), 
             arrowprops=dict(arrowstyle="->", lw=.8)) # draw arrow for x 
ax2.annotate("", xy=(1, 0), xytext=(0, 0), 
             arrowprops=dict(arrowstyle="->", lw=.8)) # draw arrow for y 
ax2.text(s='Bivariate_x', x=0.05, y=-0.25,fontsize=7) # annotate x axis
ax2.text(s='Bivariate_y', x=-0.25, y=0.1, rotation=90,fontsize=7); 

ax.grid(False)
ax.set_ylim((30, 60))
ax.set_xlim((100, 140))
ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)
ax.spines.left.set_position(("outward",10))
ax.spines.bottom.set_position(("outward",10))
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
fig.tight_layout()

fig.savefig('\第6章 空间数据型图形的绘制\图6-3-3 双变量分级统计地图绘制示例_c.pdf',bbox_inches='tight')
fig.savefig('\第6章 空间数据型图形的绘制\图6-3-3 双变量分级统计地图绘制示例_c.png', 
            bbox_inches='tight',dpi=300)         
plt.show()

# d）双变量分级统计地图示例四
import matplotlib as mpl
all_colors = all_colors = ['#e8e8e8', '#cbb8d7', '#9972af', '#e4d9ac', '#c8ada0', 
                           '#976b8a', '#c8b35a', '#af8e53', '#804d36']
# 根据实际所需进行颜色筛选
colors = ['#e8e8e8', # 1A
          '#cbb8d7', # 1B
          # '#9972af', # 1C
          #'#e4d9ac', # 2A
          '#c8ada0', # 2B
          '#976b8a', # 2C
          '#c8b35a', # 3A
          '#af8e53', # 3B
          '#804d36'] # 3C

cmap = mpl.colors.ListedColormap(colors)

fig,ax = plt.subplots(figsize=(5,4.5),dpi=100,facecolor="w")
map_fig = map_fig02.plot("country",facecolor='none', edgecolor='k',lw=.4,zorder=5,ax=ax)
Bivariate_fig = Biva_merge.plot(column='Bi_Class',cmap=cmap,categorical=True,legend=False,ax=ax)

# 添加图例
ax2 = fig.add_axes([0.75, 0.25, 0.12, 0.12])                                
alpha = 1 
# Column 1
ax2.axvspan(xmin=0, xmax=0.33, ymin=0, ymax=0.33, alpha=alpha, color=all_colors[0])
ax2.axvspan(xmin=0, xmax=0.33, ymin=0.33, ymax=0.66, alpha=alpha, color=all_colors[1])
ax2.axvspan(xmin=0, xmax=0.33, ymin=0.66, ymax=1, alpha=alpha, color=all_colors[2])
# Column 2
ax2.axvspan(xmin=0.33, xmax=0.66, ymin=0, ymax=0.33, alpha=alpha, color=all_colors[3])
ax2.axvspan(xmin=0.33, xmax=0.66, ymin=0.33, ymax=0.66, alpha=alpha, color=all_colors[4])
ax2.axvspan(xmin=0.33, xmax=0.66, ymin=0.66, ymax=1, alpha=alpha, color=all_colors[5])
# Column 3
ax2.axvspan(xmin=0.66, xmax=1, ymin=0, ymax=0.33, alpha=alpha, color=all_colors[6])
ax2.axvspan(xmin=0.66, xmax=1, ymin=0.33, ymax=0.66, alpha=alpha, color=all_colors[7])
ax2.axvspan(xmin=0.66, xmax=1, ymin=0.66, ymax=1, alpha=alpha, color=all_colors[8])
ax2.axis('off')
ax2.annotate("", xy=(0, 1), xytext=(0, 0), 
             arrowprops=dict(arrowstyle="->", lw=.8)) # draw arrow for x 
ax2.annotate("", xy=(1, 0), xytext=(0, 0), 
             arrowprops=dict(arrowstyle="->", lw=.8)) # draw arrow for y 
ax2.text(s='Bivariate_x', x=0.05, y=-0.25,fontsize=7) # annotate x axis
ax2.text(s='Bivariate_y', x=-0.25, y=0.1, rotation=90,fontsize=7); 

ax.grid(False)
ax.set_ylim((30, 60))
ax.set_xlim((100, 140))
ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)
ax.spines.left.set_position(("outward",10))
ax.spines.bottom.set_position(("outward",10))
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
fig.tight_layout()

fig.savefig('\第6章 空间数据型图形的绘制\图6-3-3 双变量分级统计地图绘制示例_d.pdf',bbox_inches='tight')
fig.savefig('\第6章 空间数据型图形的绘制\图6-3-3 双变量分级统计地图绘制示例_d.png', 
            bbox_inches='tight',dpi=300)         
plt.show()