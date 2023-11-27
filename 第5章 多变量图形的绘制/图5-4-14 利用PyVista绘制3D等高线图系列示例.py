
"""
编写时间：2022年4月19日 17：40

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""
#pyvista 建议运行结果在Pycharm中运行代码


# a）利用PyVista 库绘制的3D等高线图示例
import numpy as np
import pyvista as pv
import numpy as np
import pandas as pd
from pyvista import examples
from colormaps import parula



mesh = examples.load_random_hills()

contours = mesh.contour()

plotter = pv.Plotter()
plotter.set_scale(zscale=1.4)
plotter.add_mesh(mesh, opacity=1,lighting=True,colormap=parula,
                 scalar_bar_args={'vertical': True,
                                  "title": "Values",
                                  "title_font_size": 20,
                                  "label_font_size": 18,
                                  "n_labels": 6,
                                  "color": "k",
                                  "font_family": "times",
                                  "width": .06,
                                  "position_x": .85,
                                  "position_y": .3,
                                  }
                 )
plotter.add_mesh(contours, color="w", line_width=2)

plotter.set_background('white')
#plotter.show_grid()
plotter.show_bounds(color='black',all_edges=True,font_size=22,font_family="times",
                    minor_ticks=True,grid='front',location='outer',ticks="outside",
                    )
plotter.camera.azimuth = 190
plotter.camera.elevation = -15
plotter.camera.zoom(.9)

plotter.save_graphic(filename=r"\第5章 多变量图形的绘制\图5-4-14 利用PyVista绘制3D等高线图系列示例_a.pdf")
plotter.save_graphic(filename=r"\第5章 多变量图形的绘制\图5-4-14 利用PyVista绘制3D等高线图系列示例_a.svg")

plotter.show()


# b）利用PyVista 库绘制的带指示向量的3D等高线图示例

import pyvista as pv
from pyvista import examples
from colormaps import parula
# Load St Helens DEM and warp the topography
# Example dataset with normals
mesh = examples.load_random_hills()

# create a subset of arrows using the glyph filter
arrows = mesh.glyph(scale="Normals", orient="Normals", tolerance=0.05)
contours = mesh.contour()

p = pv.Plotter()
p.set_scale(zscale=1.4)
p.set_background('white')
p.add_mesh(arrows, color="black")
p.add_mesh(mesh, scalars="Elevation", lighting=True,colormap=parula,
                 scalar_bar_args={'vertical': True,
                                  "title": "Values",
                                  "title_font_size": 20,
                                  "label_font_size": 18,
                                  "n_labels": 6,
                                  "color": "k",
                                  "font_family": "times",
                                  "width": .06,
                                  "position_x": .85,
                                  "position_y": .3,
                                  })

p.add_mesh(contours, color="w", line_width=2)

p.show_bounds(color='black',all_edges=True,font_size=22,font_family="times",
              minor_ticks=True,grid='front',location='outer',ticks="outside",
                    )

p.camera.azimuth = 190
p.camera.elevation = -15
p.camera.zoom(.9)
p.save_graphic(filename=r"\第5章 多变量图形的绘制\图5-4-14 利用PyVista绘制3D等高线图系列示例_b.pdf")
p.save_graphic(filename=r"\第5章 多变量图形的绘制\图5-4-14 利用PyVista绘制3D等高线图系列示例_b.svg")

# Display the scene
p.show()
