"""
编写时间：2022年2月05日 19：20

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。

代码中Proplot包绘制的部分可能与Matplotlib绘制不同，需注意两者绘图语法的不同~~

"""

import pandas as pd
import numpy as np
import proplot as pplt
import matplotlib.pyplot as plt


fig = pplt.figure(figsize=(8,5.5),space=1, refwidth='10em')
axs = fig.subplots(nrows=3, ncols=3)
locs = ("c","l","r","lc","uc","ur","ul","ll","lr")
abcs = ("a","a.","(a)","[a]","(a","A","A.","(A)","(A.)")
axs.format(abcsize=16,xlabel='x axis', ylabel='y axis',labelsize=18) 
axs[-3:].format(abcbbox=True) 
axs[0, 0].format(abc="a", abcloc="c",abcborder=True)  
axs[0, 1].format(abc="a.", abcloc="l")  
axs[0, 2].format(abc="(a)", abcloc="r")  
axs[1, 0].format(abc="[a]", abcloc="lc",facecolor='gray5')  
axs[1, 1].format(abc="(a", abcloc="uc",facecolor='gray5')  
axs[1, 2].format(abc="A", abcloc="ur",facecolor='gray5')  
axs[2, 0].format(abc="A.", abcloc="ul",)  
axs[2, 1].format(abc="(A)", abcloc="ll")  
axs[2, 2].format(abc="(A.)", abcloc="lr") 
fig.save(r'\第2章 绘制工具及其重要特征\\图2-3-3 Proplot_abc.png', 
         bbox_inches='tight',dpi=600)
fig.save(r'\第2章 绘制工具及其重要特征\\图2-3-3 Proplot_abc.pdf', 
         bbox_inches='tight')
plt.show()