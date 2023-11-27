"""
编写时间：2022年4月24日 16：30

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

import numpy as np
import pandas as pd
import seaborn as sns
import proplot as pplt
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from colormaps import parula

from proplot import rc
rc["font.family"] = "Times New Roman"
rc["axes.labelsize"] = 15
rc["tick.labelsize"] = 12
rc["suptitle.size"] = 15
rc["title.size"] = 14

from sklearn import datasets
iris = datasets.load_iris()

X = iris.data
y = iris.target
#标准化处理
# data scaling
x_scaled = StandardScaler().fit_transform(X)


#PCA降维到3维
from sklearn.decomposition import PCA
pca = PCA(n_components=3)
pca_features = pca.fit_transform(x_scaled)

pca_df = pd.DataFrame(data=pca_features, columns=['PCA1', 'PCA2', 'PCA3'])

# 降低到2维数据
pca = PCA(n_components=2)
pca_features = pca.fit_transform(x_scaled)
 
# Create dataframe
pca_df = pd.DataFrame(data=pca_features, columns=['PCA1', 'PCA2'])
# map target names to PCA features   
target_names = {
    0:'setosa',
    1:'versicolor', 
    2:'virginica'
}
 
pca_df['target'] = y
pca_df['target'] = pca_df['target'].map(target_names)



# a）未添加置信椭圆区间的主成分分析图绘制示例
colors = plt.cm.Set1.colors
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
pca_scatter = sns.scatterplot(data=pca_df,x="PCA1",y="PCA2",hue="target",palette=colors,
                              s=40,ec="k",ax=ax)
ax.set(xlim=(-3, 4),ylim=(-3, 3))
plt.tight_layout()

fig.savefig('\第5章 多变量图形的绘制\图5-7-1 利用Matplotlib绘制的主成分分析图示例_a.pdf',bbox_inches='tight')
fig.savefig('\第5章 多变量图形的绘制\图5-7-1 利用Matplotlib绘制的主成分分析图示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()



# b）添加置信椭圆区间的主成分分析图绘制示例

# 添加置信椭圆
from matplotlib.patches import Ellipse
import matplotlib.transforms as transforms

def confidence_ellipse(x, y, ax, n_std=3.0, facecolor='none', **kwargs):
    if x.size != y.size:
        raise ValueError("x and y must be the same size")
    cov = np.cov(x, y)
    pearson = cov[0, 1]/np.sqrt(cov[0, 0] * cov[1, 1])
    ell_radius_x = np.sqrt(1 + pearson)
    ell_radius_y = np.sqrt(1 - pearson)
    ellipse = Ellipse((0, 0), width=ell_radius_x * 2, height=ell_radius_y * 2,
                      facecolor=facecolor, **kwargs)

    scale_x = np.sqrt(cov[0, 0]) * n_std
    mean_x = np.mean(x)
    scale_y = np.sqrt(cov[1, 1]) * n_std
    mean_y = np.mean(y)

    transf = transforms.Affine2D() \
        .rotate_deg(45) \
        .scale(scale_x, scale_y) \
        .translate(mean_x, mean_y)

    ellipse.set_transform(transf + ax.transData)
    return ax.add_patch(ellipse)

setosa = pca_df[pca_df["target"]=="setosa"]
versicolor = pca_df[pca_df["target"]=="versicolor"]
virginica = pca_df[pca_df["target"]=="virginica"]

colors = plt.cm.Set1.colors
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
pca_scatter = sns.scatterplot(data=pca_df,x="PCA1",y="PCA2",hue="target",palette=colors,
                              s=40,ec="k",ax=ax)

confidence_ellipse(setosa.PCA1,setosa.PCA2,ax,n_std=2,facecolor=colors[0],edgecolor=colors[0],
                   alpha=.5,zorder=0)
confidence_ellipse(versicolor.PCA1,versicolor.PCA2,ax,n_std=2,facecolor=colors[1],edgecolor=colors[1],
                   alpha=.5,zorder=0)
confidence_ellipse(virginica.PCA1,virginica.PCA2,ax,n_std=2,facecolor=colors[2],edgecolor=colors[2],
                   alpha=.5,zorder=0)
ax.set(xlim=(-3, 4),ylim=(-3, 3))
plt.tight_layout()

fig.savefig('\第5章 多变量图形的绘制\图5-7-1 利用Matplotlib绘制的主成分分析图示例_b.pdf',bbox_inches='tight')
fig.savefig('\第5章 多变量图形的绘制\图5-7-1 利用Matplotlib绘制的主成分分析图示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()
