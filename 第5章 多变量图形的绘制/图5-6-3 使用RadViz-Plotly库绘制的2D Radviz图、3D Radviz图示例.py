"""
编写时间：2022年4月23日 16：30

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

# from RadViz import main
from RadViz.main import RadViz2D
from RadViz.main import RadViz3D
import pandas as pd
import time
import plotly.io as pio
import seaborn as sns


data= sns.load_dataset("iris")
y=data['species']
X=data.drop(['species'], axis=1)

#绘制2D可视化结果
BPs=1000
time_start = time.time()
RadViz2D(y,X,BPs)


#绘制3D可视化结果
BPs=10000
time_start = time.time()
fig = RadViz3D(y,X,BPs)

