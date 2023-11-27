"""
编写时间：2022年4月19日 19：40

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""
#pyvista 建议运行结果在Pycharm中运行代码


import pyvista as pv
from pyvista import examples
from colormaps import parula
# Load St Helens DEM and warp the topography
mesh = examples.download_st_helens().warp_by_scalar()

# First a default plot with jet colormap
p = pv.Plotter()
p.set_background('white')
# Add the data, use active scalar for coloring, and show the scalar bar
p.add_mesh(mesh,lighting=True,colormap=parula,
                 scalar_bar_args={'vertical': True,
                                  "title": "Values",
                                  "title_font_size": 20,
                                  "label_font_size": 18,
                                  "n_labels": 6,
                                  "color": "k",
                                  #"font_family": "times",
                                  "width": .06,
                                  "height":.3,
                                  "position_x": .85,
                                  "position_y": .3,
                                  })

p.show_bounds(color='black',all_edges=True,font_size=22,font_family="times",
                    minor_ticks=True,grid='front',location='outer',ticks="outside",
                    )
p.camera.azimuth = 190
p.camera.elevation = -15
p.camera.zoom(.9)

p.save_graphic(filename=r"\第5章 多变量图形的绘制\图5-4-15 利用PyVista绘制的DEM数据的3D可视化结果.pdf")
p.save_graphic(filename=r"\第5章 多变量图形的绘制\图5-4-15 利用PyVista绘制的DEM数据的3D可视化结果.svg")

# Display the scene
p.show()