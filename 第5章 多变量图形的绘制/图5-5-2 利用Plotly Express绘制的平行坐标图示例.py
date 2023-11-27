"""
编写时间：2022年4月22日 15：40

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

"""
此代码为使用Python-Prolot包进行学术风格图表绘制，绘图语法和Matplotlib有所不同，需注意。
"""

import numpy as np
import pandas as pd
import seaborn as sns
import proplot as pplt
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler
import plotly.express as px
import plotly.graph_objects as go

from colormaps import parula

from proplot import rc
rc["font.family"] = "Times New Roman"
rc["axes.labelsize"] = 15
rc["tick.labelsize"] = 12
rc["suptitle.size"] = 15
rc["title.size"] = 14


iris = load_iris()
iris_data = np.hstack((iris.data, iris.target.reshape(-1,1)))
iris_df = pd.DataFrame(data=iris_data, columns=iris.feature_names+ ["FlowerType"])
iris_df.head()

# a）利用Plotly Express绘制的平行坐标图示例一

cols = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
fig = px.parallel_coordinates(iris_df, color="FlowerType",dimensions=cols,
                              color_continuous_scale=[(0.00, "red"),   (0.33, "red"),
                                                     (0.33, "green"), (0.66, "green"),
                                                     (0.66, "blue"),  (1.00, "blue")],
                               width=500, height=350,
                              title="IRIS Flowers Parallel Coorinates Plot")
fig.update_layout(
    font_family="Times New Roman",
    font_color="black",
    coloraxis_colorbar=dict(
              len=0.8,
              title="Species",
              tickvals=[0,1,2],
              ticktext=["setosa","versicolor","virginica"])
     )

fig.write_image(r'\第5章 多变量图形的绘制\图5-5-2 利用Plotly Express绘制的平行坐标图示例_a.pdf')
fig.write_image(r'\第5章 多变量图形的绘制\图5-5-2 利用Plotly Express绘制的平行坐标图示例_a.svg')
fig.write_image(r'\第5章 多变量图形的绘制\图5-5-2 利用Plotly Express绘制的平行坐标图示例_a.png',scale=3)
fig.show()

# b）利用Plotly Express绘制的平行坐标图示例二
cols = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
fig = px.parallel_coordinates(iris_df, color="FlowerType",dimensions=cols,
                              color_continuous_scale="viridis",
                              width=500, height=350,
                              title="IRIS Flowers Parallel Coorinates Plot")
fig.update_layout(
    font_family="Times New Roman",
    font_color="black",
    coloraxis_colorbar=dict(
              len=0.8,
              title="Species",
              tickvals=[0,1,2],
              ticktext=["setosa","versicolor","virginica"])
     )

fig.write_image(r'\第5章 多变量图形的绘制\图5-5-2 利用Plotly Express绘制的平行坐标图示例_b.pdf')
fig.write_image(r'\第5章 多变量图形的绘制\图5-5-2 利用Plotly Express绘制的平行坐标图示例_b.svg')
fig.write_image(r'\第5章 多变量图形的绘制\图5-5-2 利用Plotly Express绘制的平行坐标图示例_b.png',scale=3)
fig.show()