"""
编写时间：2022年4月22日 19：40

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

"""
此代码为使用Python-Prolot包进行学术风格图表绘制，绘图语法和Matplotlib有所不同，需注意。
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler
from colormaps import parula

plt.rcParams["font.family"] ="Times New Roman"
plt.rcParams["figure.figsize"] = (7,3.5)


iris = load_iris()
iris_data = np.hstack((iris.data, iris.target.reshape(-1,1)))
iris_df = pd.DataFrame(data=iris_data, columns=iris.feature_names+ ["FlowerType"])

iris_data_scaled = MinMaxScaler().fit_transform(iris.data)
iris_data_scaled = np.hstack((iris_data_scaled, iris.target.reshape(-1,1)))

iris_scaled_df = pd.DataFrame(data=iris_data_scaled, columns=iris.feature_names+ ["FlowerType"])


cols = iris_scaled_df.columns
paxfig = paxplot.pax_parallel(n_axes=len(cols))
paxfig.plot(iris_scaled_df.to_numpy(),
            line_kwargs={"linewidth":.7})
paxfig.set_labels(cols)
color_col = 0
paxfig.add_colorbar(ax_idx=color_col,cmap=parula,
     colorbar_kwargs={'label':  cols[color_col],
                      "aspect":12,"shrink":.8})


paxfig.savefig(fname=r'\第5章 多变量图形的绘制\图5-5-3 利用Paxplot库绘制的平行坐标图示例.pdf')
paxfig.savefig(fname=r'\第5章 多变量图形的绘制\图5-5-3 利用Paxplot库绘制的平行坐标图示例.png', 
             bbox_inches='tight',dpi=300)

plt.show()