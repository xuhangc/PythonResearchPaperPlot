
"""
编写时间：2022年4月18日 18：50

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

"""
此代码为使用Python-Prolot包进行学术风格图表绘制，绘图语法和Matplotlib有所不同，需注意。
"""
import pandas as pd
import numpy as np
import proplot as pplt
import seaborn as sns

from scipy.stats import pearsonr
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from colormaps import parula

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
from sklearn.pipeline import make_pipeline
#
# Load the breast cancer data set
bc = datasets.load_breast_cancer()
X, y = bc.data, bc.target
# Create training and test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=1, stratify=y)
# Create the estimator - pipeline
pipeline = make_pipeline(StandardScaler(), LogisticRegression(random_state=1))
# Create training test splits using two features
pipeline.fit(X_train[:,[2, 13]],y_train)
probs = pipeline.predict_proba(X_test[:,[2, 13]])
fpr1, tpr1, thresholds = roc_curve(y_test, probs[:, 1], pos_label=1)
roc_auc1 = auc(fpr1, tpr1)
# Create training test splits using two different features
pipeline.fit(X_train[:,[4, 14]],y_train)
probs2 = pipeline.predict_proba(X_test[:,[4, 14]])
fpr2, tpr2, thresholds = roc_curve(y_test, probs2[:, 1], pos_label=1)
roc_auc2 = auc(fpr2, tpr2)
# Create training test splits using all features
pipeline.fit(X_train,y_train)
probs3 = pipeline.predict_proba(X_test)
fpr3, tpr3, thresholds = roc_curve(y_test, probs3[:, 1], pos_label=1)
roc_auc3 = auc(fpr3, tpr3)

fig,ax = plt.subplots(figsize=(4,3.5),dpi=100,facecolor="w")
 
ax.plot(fpr1, tpr1, lw=1,label='ROC Curve 1 (AUC = %0.2f)' % (roc_auc1))
ax.plot(fpr2, tpr2, lw=1,label='ROC Curve 2 (AUC = %0.2f)' % (roc_auc2))
ax.plot(fpr3, tpr3, lw=1,label='ROC Curve 3 (AUC = %0.2f)' % (roc_auc3))
ax.plot([0, 1], [0, 1], linestyle='--', lw=1,color='red', label='Random Classifier')   
ax.plot([0, 0, 1], [0, 1, 1], linestyle=':', lw=1,color='green', label='Perfect Classifier')
ax.set(xlim=(-0.05, 1.05),ylim=(-0.05, 1.05),xlabel="False Positive Rate",ylabel="True Positive Rate")
ax.legend(loc="lower right")
ax.grid(False)
plt.tight_layout()

fig.savefig('\第4章 双变量图形的绘制\图4-3-2 不同AUC值的ROC曲线绘制示例.pdf',bbox_inches='tight')
fig.savefig('\第4章 双变量图形的绘制\图4-3-2 不同AUC值的ROC曲线绘制示例.png', 
            bbox_inches='tight',dpi=300)
plt.show()      

