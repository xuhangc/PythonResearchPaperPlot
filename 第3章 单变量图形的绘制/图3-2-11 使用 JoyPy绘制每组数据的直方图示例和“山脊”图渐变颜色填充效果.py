
"""
编写时间：2022年2月06日 10：30

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。

代码中Proplot包绘制的部分可能与Matplotlib绘制不同，需注意两者绘图语法的不同~~

"""
#注意：本案例中引入的SciencePlots库主题方式会随着SciencePlots版本的更新发生改变，读者还需参考其官网引入的正确方式。
#      建议按照官网引入方式进行操作和使用最新版本的ScienePlots。如引入方式发生改变，请关注微信公众号【DataCharm】进行实时获取代码更新。

import joypy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


plt.rcParams["font.family"] = "Times New Roman"

group_data = pd.read_csv(r"第3章 单变量图形的绘制\山脊图绘制数据.csv")

sord_index = [i for i in group_data.color.unique()]
sord_index = sorted(sord_index,key=str.lower)
sord_index = sord_index[::-1]

#a）使用JoyPy库绘制每组数据的直方图示例

fig, axes = joypy.joyplot(group_data, by="color", column="depth", labels=sord_index, 
                          grid="y", linewidth=1, figsize=(7,6),color="gray",hist=True,
                          xlabelsize=15,ylabelsize=15)
                          
fig.savefig('\第3章 单变量图形的绘制\图3-2-11 使用 JoyPy绘制每组数据的直方图示例和“山脊”图渐变颜色填充效果_a.pdf',bbox_inches='tight')
fig.savefig('\第3章 单变量图形的绘制\图3-2-11 使用 JoyPy绘制每组数据的直方图示例和“山脊”图渐变颜色填充效果_a.png', 
            bbox_inches='tight',dpi=300)

plt.show()     

# b）“山脊”图渐变颜色填充效果（颜色映射）
import joypy
from colormaps import parula
plt.rcParams["font.family"] = "Times New Roman"

 fig, axes = joypy.joyplot(group_data, by="color", column="depth", labels=sord_index, 
                          grid="y", linewidth=1, figsize=(7,6),hist=False,
                          colormap=parula,
                          xlabelsize=15,ylabelsize=15) 
fig.savefig('\第3章 单变量图形的绘制\图3-2-11 使用 JoyPy绘制每组数据的直方图示例和“山脊”图渐变颜色填充效果_b.pdf',bbox_inches='tight')
fig.savefig('\第3章 单变量图形的绘制\图3-2-11 使用 JoyPy绘制每组数据的直方图示例和“山脊”图渐变颜色填充效果_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()    

                       