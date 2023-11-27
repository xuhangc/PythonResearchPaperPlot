"""
编写时间：2022年2月05日 18：30

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。

代码中Proplot包绘制的部分可能与Matplotlib绘制不同，需注意两者绘图语法的不同~~

"""

import pandas as pd
import numpy as np
import proplot as pplt
import seaborn as sns
import matplotlib.pyplot as plt


from proplot import rc
rc["font.family"] = "Times New Roman"
rc["axes.labelsize"] = 15
rc['tick.labelsize'] = 13

df = sns.load_dataset('tips') 
  
graph = sns.FacetGrid(df, col ='time', hue ='smoker') 
# map the above form facetgrid with some attributes 
graph.map(sns.regplot, "total_bill", "tip").add_legend() 
graph.add_legend() 

plt.savefig(r'\第2章 绘制工具及其重要特征\图2-2-1 FacetGrid ()函数绘制分面图结果.pdf',bbox_inches='tight')
plt.savefig(r'\第2章 绘制工具及其重要特征\图2-2-1 FacetGrid ()函数绘制分面图结果.png', 
            bbox_inches='tight',dpi=300)       
plt.show()
