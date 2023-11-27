
"""
编写时间：2022年4月25日 16：30

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

import numpy as np
import pandas as pd
import seaborn as sns
import proplot as pplt
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from colormaps import parula

from proplot import rc
rc["font.family"] = "Times New Roman"
rc["axes.labelsize"] = 15
rc["tick.labelsize"] = 12
rc["suptitle.size"] = 15
rc["title.size"] = 14

#  a）主成分分析载荷图绘制示例
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



pca = PCA(n_components=2)
pca_features = pca.fit_transform(x_scaled)

# 获取主成分相关系数
loadings = pca.components_
#特征个数
n_features = pca.n_features_
# 特征名称
feature_names = iris.feature_names

# PC names
pc_list = [f'PC{i}' for i in list(range(1, n_features + 1))]
# PC names
pc_list = [f'PC{i}' for i in list(range(1, n_features + 1))]
pc_loadings = dict(zip(pc_list, loadings))
loadings_df = pd.DataFrame.from_dict(pc_loadings)
loadings_df['feature_names'] = feature_names


# Get the loadings of x and y axes
xs = loadings[0]
ys = loadings[1]
 
# Plot the loadings on a scatterplot
fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
for i, varnames in enumerate(feature_names):
    ax.scatter(xs[i], ys[i], s=50,ec="k",color="#FFCC37",zorder=1)
    # 添加圆点指示箭头
    ax.arrow(0, 0, xs[i], ys[i], color='r',zorder=0)
    ax.text(xs[i], ys[i], varnames,fontsize=8)
#添加经过圆点互相处置的虚线
ax.axvline(c='k', lw=.8,ls=":")
ax.axhline(c='k', lw=.8,ls=":")
# 添加loading 图例
ax.scatter([],[],label="loadings",color="#FFCC37")

xticks = np.linspace(-0.8, 0.8, num=5)
yticks = np.linspace(-0.8, 0.8, num=5)
ax.grid(False)
ax.legend()
ax.set(xlabel="PC1",ylabel="PC2",xticks=xticks,yticks=yticks)
plt.tight_layout()

fig.savefig('\第5章 多变量图形的绘制\图5-7-2 利用Matplotlib绘制的主成分分析载荷图和主成分分析双标图示例_a.pdf',bbox_inches='tight')
fig.savefig('\第5章 多变量图形的绘制\图5-7-2 利用Matplotlib绘制的主成分分析载荷图和主成分分析双标图示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()


# b）主成分分析双标图绘制示例

pca_df_scaled = pca_df.copy()
 
scaler_df = pca_df[['PCA1', 'PCA2']]
scaler = 1 / (scaler_df.max() - scaler_df.min())
 
for index in scaler.index:
    pca_df_scaled[index] *= scaler[index]


xs = loadings[0]
ys = loadings[1]

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
pca_scatter = sns.scatterplot(data=pca_df_scaled,x="PCA1",y="PCA2",hue="target",
                              s=40,ec="k",ax=ax)
for i, varnames in enumerate(feature_names):
    ax.scatter(xs[i], ys[i], s=40,ec="k",color="#FFCC37",zorder=1)
    # 添加圆点指示箭头
    ax.arrow(0, 0, xs[i], ys[i], color='r',zorder=0)
    ax.text(xs[i], ys[i], varnames,color="#FFCC37",fontsize=8)
# 添加loading 图例
ax.scatter([],[],label="loadings",color="#FFCC37")
#添加经过圆点互相处置的虚线
ax.axvline(c='k', lw=.8,ls=":")
ax.axhline(c='k', lw=.8,ls=":")
xticks = np.linspace(-0.8, 0.8, num=5)
yticks = np.linspace(-0.8, 0.8, num=5)
ax.legend()
ax.grid(False)
ax.set(xlabel="PC1",ylabel="PC2",xticks=xticks,yticks=yticks)
plt.tight_layout()

fig.savefig('\第5章 多变量图形的绘制\图5-7-2 利用Matplotlib绘制的主成分分析载荷图和主成分分析双标图示例_b.pdf',bbox_inches='tight')
fig.savefig('\第5章 多变量图形的绘制\图5-7-2 利用Matplotlib绘制的主成分分析载荷图和主成分分析双标图示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()

