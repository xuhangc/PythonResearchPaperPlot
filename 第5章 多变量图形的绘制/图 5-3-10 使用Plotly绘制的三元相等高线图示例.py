"""
编写时间：2022年4月16日 10：50

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

"""
此代码为使用Python-Prolot包进行学术风格图表绘制，绘图语法和Matplotlib有所不同，需注意。

"""
import pandas as pd
import numpy as np
import plotly.figure_factory as ff

contour_data = pd.read_excel(r"\第5章 多变量图形的绘制\ternary_countor.xlsx")
variable1 = contour_data["Variable 1"].values
variable2 = contour_data["Variable 2"].values
variable3 = contour_data["Variable 3"].values
Size = contour_data["Size"].values

fig = ff.create_ternary_contour(coordinates=np.array([variable1, variable2, variable3]),
                                values=Size,pole_labels=['Top', 'Left', 'Right'],
                                interp_mode='cartesian',ncontours=10,
                                colorscale="Rainbow",
                                showscale=True)
fig.update_layout(
    font_family="Times New Roman",
    font_color="black")
fig.show()

fig.write_image(r'\第5章 多变量图形的绘制\图 5-3-10 使用Plotly绘制的三元相等高线图示例.pdf')
fig.write_image(r'\第5章 多变量图形的绘制\图 5-3-10 使用Plotly绘制的三元相等高线图示例.png',width=4.5,height=4,
                scale=10)