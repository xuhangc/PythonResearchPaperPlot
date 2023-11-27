
"""
编写时间：2022年4月19日 16：40

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""
#pyvista 建议运行结果在Pycharm中运行代码

# a）利用PyVista绘制的3D曲面图样式一
import pyvista as pv
import numpy as np
from colormaps import parula

x=y=np.linspace(-10, 10,20)
[X, Y] = np.meshgrid(x,y)
Z = X + Y
grid = pv.StructuredGrid(X,Y,Z)

plotter = pv.Plotter()
plotter.set_scale(zscale=0.4)
plotter.add_mesh(grid, scalars=grid.points[:, -1], show_edges=True,lighting=True,colormap=parula,
                 scalar_bar_args={'vertical': True,
                                  "title":"Values",
                                  "title_font_size":20,
                                  "label_font_size":18,
                                  "n_labels":6,
                                  "color":"k",
                                  "font_family":"times",
                                  "width":.06,
                                  "position_x":.85,
                                  "position_y":.3,
                                  })
plotter.set_background('white')
#plotter.show_grid()
plotter.show_bounds(color='black',all_edges=True,font_size=25,font_family="times",
                    minor_ticks=True,grid='front',location='outer',ticks="outside",
                    )
plotter.camera.azimuth = 190
plotter.camera.elevation = -15
plotter.camera.zoom(.9)

#plotter.view_isometric()
plotter.save_graphic(filename=r"\第5章 多变量图形的绘制\图5-4-13 利用PyVista绘制的不同3D曲面图示例_a.pdf")
plotter.save_graphic(filename=r"\第5章 多变量图形的绘制\图5-4-13 利用PyVista绘制的不同3D曲面图示例_a.svg")

plotter.camera.view_angle = 35.0
#plotter.camera.zoom(.9)
#plotter.enable_zoom_style()
plotter.show()

# b）利用PyVista绘制的3D曲面图样式二
import numpy as np
import pandas as pd
import pyvista as pv
from colormaps import parula

X = np.linspace(-2, 2, 100)
Y = np.linspace(-1, 2, 100)
X, Y = np.meshgrid(X, Y)
Z = X**2 + Y**2  # "sphere" function

grid = pv.StructuredGrid(X,Y,Z)
plotter = pv.Plotter()
plotter.set_scale(zscale=0.3)
plotter.add_mesh(grid, scalars=grid.points[:, -1], show_edges=True,lighting=True,colormap=parula,
                 scalar_bar_args={'vertical': True,
                                  "title":"Values",
                                  "title_font_size":20,
                                  "label_font_size":18,
                                  "n_labels":6,
                                  "color":"k",
                                  "font_family":"times",
                                  "width":.06,
                                  "position_x":.85,
                                  "position_y":.3,
                                  })
plotter.set_background('white')
#plotter.show_grid()
plotter.show_bounds(color='black',all_edges=True,font_size=22,font_family="times",
                    minor_ticks=True,grid='front',location='outer',ticks="outside",
                    )
plotter.camera.azimuth = 190
plotter.camera.elevation = -15
plotter.camera.zoom(.9)


plotter.save_graphic(filename=r"\第5章 多变量图形的绘制\图5-4-13 利用PyVista绘制的不同3D曲面图示例_b.pdf")
plotter.save_graphic(filename=r"\第5章 多变量图形的绘制\图5-4-13 利用PyVista绘制的不同3D曲面图示例_b.svg")

#plotter.camera.view_angle = 35.0
plotter.show()


# c）利用PyVista绘制的3D曲面图样式三
mport numpy as np
import pandas as pd
import pyvista as pv
from colormaps import parula


x = np.linspace(-2, 0, 20)
y = np.linspace(0, 2, 20)
[X, Y] = np.meshgrid(x,y)
# Define the function Z = f(X,Y)
Z = 2./np.exp((X-.5)**2+Y**2)-2./np.exp((X+.5)**2+Y**2)

grid = pv.StructuredGrid(X,Y,Z)
plotter = pv.Plotter()
plotter.set_scale(zscale=.9999)
plotter.add_mesh(grid, scalars=grid.points[:, -1], show_edges=True,lighting=True,colormap=parula,
                 scalar_bar_args={'vertical': True,
                                  "title":"Values",
                                  "title_font_size":20,
                                  "label_font_size":18,
                                  "n_labels":6,
                                  "color":"k",
                                  "font_family":"times",
                                  "width":.06,
                                  "position_x":.85,
                                  "position_y":.3,
                                  })
plotter.set_background('white')
#plotter.show_grid()
plotter.show_bounds(color='black',all_edges=True,font_size=22,font_family="times",
                    minor_ticks=True,grid='front',location='outer',ticks="outside",
                    )
plotter.camera.azimuth = 190
plotter.camera.elevation = -15
plotter.camera.zoom(.9)


plotter.save_graphic(filename=r"\第5章 多变量图形的绘制\图5-4-13 利用PyVista绘制的不同3D曲面图示例_c.pdf")
plotter.save_graphic(filename=r"\第5章 多变量图形的绘制\图5-4-13 利用PyVista绘制的不同3D曲面图示例_c.svg")

#plotter.camera.view_angle = 35.0
plotter.show()

# d）利用PyVista绘制的3D曲面图样式四

import numpy as np
import pandas as pd
import pyvista as pv
from colormaps import parula

mul_data = pd.read_excel(r"\第5章 多变量图形的绘制\Multiple Surfaces in Same Layer.xlsx",header=None)

x = np.arange(0,len(mul_data), 1)
y = np.arange(0,len(mul_data), 1)
X, Y = np.meshgrid(x, y)
Z = mul_data.values


grid = pv.StructuredGrid(X,Y,Z)
plotter = pv.Plotter()
plotter.set_scale(zscale=.9999)
plotter.add_mesh(grid, scalars=grid.points[:, -1], show_edges=False,lighting=True,
                 colormap="YlGnBu",
                 scalar_bar_args={'vertical': True,
                                  "title":"Values",
                                  "title_font_size":20,
                                  "label_font_size":18,
                                  "n_labels":6,
                                  "color":"k",
                                  "font_family":"times",
                                  "width":.06,
                                  "position_x":.85,
                                  "position_y":.3,
                                  })
plotter.set_background('white')
#plotter.show_grid()
plotter.show_bounds(color='black',all_edges=True,font_size=22,font_family="times",
                    minor_ticks=True,grid='front',location='outer',ticks="outside",
                    )
plotter.camera.azimuth = 190
plotter.camera.elevation = -15
plotter.camera.zoom(.9)

plotter.save_graphic(filename=r"\第5章 多变量图形的绘制\图5-4-13 利用PyVista绘制的不同3D曲面图示例_d.pdf")
plotter.save_graphic(filename=r"\第5章 多变量图形的绘制\图5-4-13 利用PyVista绘制的不同3D曲面图示例_d.svg")

#plotter.camera.view_angle = 35.0
plotter.show()


