"""
编写时间：2022年4月19日 16：40

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

"""
此代码为使用Python-Prolot包进行学术风格图表绘制，绘图语法和Matplotlib有所不同，需注意。
"""

import pandas as pd
import numpy as np
import proplot as pplt
import seaborn as sns
from scipy import interpolate
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from colormaps import parula

from proplot import rc
rc["axes.labelsize"] = 12
rc['tick.labelsize'] = 10
rc["suptitle.size"] = 15
rc["xtick.major.pad"] =.5
rc["xtick.minor.visible"] = False
rc["ytick.minor.visible"] = False
rc["font.family"] = "Times New Roman"


# a）利用Mayavi绘制的真实网格数据3D曲面图示例一

mul_data = pd.read_excel(r"\第5章 多变量图形的绘制\\Multiple Surfaces in Same Layer.xlsx",header=None)
x = np.arange(0,len(mul_data), 1)
y = np.arange(0,len(mul_data), 1)
X, Y = np.meshgrid(x, y)
Z = mul_data.values

Z = np.rollaxis(Z,0,2)
X = np.rollaxis(X,0,2)
Y = np.rollaxis(Y,0,2)

fig = mlab.figure(size=(1000,800), bgcolor=(1,1,1), fgcolor=(0,0,0))
surf = mlab.surf(X, Y, Z, warp_scale="auto", opacity=1,colormap='jet')

#surf = mlab.surf(X, Y, Z, warp_scale="auto", representation="wireframe",opacity=1,colormap='Spectral')
#mlab.surf()
mlab.outline(color=(0, 0, 0),line_width=2)
#mlab.outline()
axes = mlab.axes(color=(0, 0, 0), nb_labels=5,line_width=1)
axes.title_text_property.color = (0.0, 0.0, 0.0)
axes.title_text_property.font_family = 'times'
axes.label_text_property.color = (0.0, 0.0, 0.0)
axes.label_text_property.font_family = 'times'
axes.label_text_property.font_size= 25
# 添加colorbar
sbar = mlab.scalarbar(object=surf,title="Values",nb_labels=6,orientation="vertical")
sbar.label_text_property.font_family = 'times'
sbar.title_text_property.font_family = 'times'
sbar.title_text_property.font_size= 24

mlab.axes(xlabel='X', ylabel='Y', zlabel='Z')
mlab.view(azimuth=310, elevation=60, figure=fig, distance='auto')
#mlab.gcf().scene.parallel_projection = True 
#mlab.orientation_axes()
# 保存图片
mlab.savefig(filename=r"\第5章 多变量图形的绘制\图5-4-12 利用Mayavi绘制的真实数据集3D曲面图示例_a.png",
            figure=fig)
mlab.savefig(filename=r"\第5章 多变量图形的绘制\图5-4-12 利用Mayavi绘制的真实数据集3D曲面图示例_a.pdf",
            figure=fig)
mlab.show()

# b）利用Mayavi绘制的真实网格数据3D曲面图示例二

elevation = pd.read_excel(r"\第5章 多变量图形的绘制\elevation.xlsx",header=None)
elevation = elevation.replace("--",np.nan)

x = np.arange(0,elevation.shape[1], 1)
y = np.arange(0,elevation.shape[0], 1)
X, Y = np.meshgrid(x, y)
Z = elevation.values

Z = np.rollaxis(Z,0,2)
X = np.rollaxis(X,0,2)
Y = np.rollaxis(Y,0,2)

fig = mlab.figure(size=(1000,800), bgcolor=(1,1,1), fgcolor=(0,0,0))
surf = mlab.surf(X, Y, Z, warp_scale="auto", opacity=1,colormap='jet')

#mlab.surf()
mlab.outline(color=(0, 0, 0),line_width=2)
#mlab.outline()
axes = mlab.axes(color=(0, 0, 0), nb_labels=5,line_width=1)
axes.title_text_property.color = (0.0, 0.0, 0.0)
axes.title_text_property.font_family = 'times'
axes.label_text_property.color = (0.0, 0.0, 0.0)
axes.label_text_property.font_family = 'times'
axes.label_text_property.font_size= 25
# 添加colorbar
sbar = mlab.scalarbar(object=surf,title="Values",nb_labels=6,orientation="vertical")
sbar.label_text_property.font_family = 'times'
sbar.title_text_property.font_family = 'times'
sbar.title_text_property.font_size= 24

mlab.axes(xlabel='X', ylabel='Y', zlabel='Z')
mlab.view(azimuth=310, elevation=60, figure=fig, distance='auto')

# 保存图片
mlab.savefig(filename=r"\第5章 多变量图形的绘制\图5-4-12 利用Mayavi绘制的真实数据集3D曲面图示例_b.png",
            figure=fig)
mlab.savefig(filename=r"\第5章 多变量图形的绘制\图5-4-12 利用Mayavi绘制的真实数据集3D曲面图示例_b.pdf",
            figure=fig)
mlab.show()
