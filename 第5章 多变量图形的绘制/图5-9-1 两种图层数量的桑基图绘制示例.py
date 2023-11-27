"""
编写时间：2022年4月25日 21：30

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

import numpy as np
import pandas as pd
import seaborn as sns
import proplot as pplt
import matplotlib.pyplot as plt
from colormaps import parula

from proplot import rc
rc["font.family"] = "Times New Roman"
rc["axes.labelsize"] = 15
rc["tick.labelsize"] = 12
rc["suptitle.size"] = 15
rc["title.size"] = 14


colorDict = {
    'apple':'#EF0000',
    'blueberry':'#18276F',
    'banana':'#FEC211',
    'lime':'#3BC371',
    'orange':'#666699'}
    

# a）桑基图绘制示例(单个图层)
from pysankey2.datasets import load_fruits
from pysankey2 import Sankey

df1 = load_fruits()
sky = Sankey(df1,colorMode="global",colorDict=colorDict,stripColor='left')
fig,ax = sky.plot(figSize=(4, 4),fontSize=13,boxWidth=.2,text_kws={"family":"Times New Roman"})
plt.tight_layout()
fig.savefig('\第5章 多变量图形的绘制\图5-9-1 两种图层数量的桑基图绘制示例_a.pdf',bbox_inches='tight')
fig.savefig('\第5章 多变量图形的绘制\图5-9-1 两种图层数量的桑基图绘制示例_a.png', 
            bbox_inches='tight',dpi=300)
plt.show()


# b）桑基图绘制示例(两个图层)
from pysankey2 import Sankey
from pysankey2.datasets import load_countrys
df2 = load_countrys()

sky_auto_global_colors = Sankey(df2,colorMode="global",stripColor='left')
fig,ax = sky_auto_global_colors.plot(figSize=(4, 3),fontSize=4.5,boxWidth=.5,
                                     text_kws={"family":"Times New Roman"})
plt.tight_layout()
fig.savefig('\第5章 多变量图形的绘制\图5-9-1 两种图层数量的桑基图绘制示例_b.pdf',bbox_inches='tight')
fig.savefig('\第5章 多变量图形的绘制\图5-9-1 两种图层数量的桑基图绘制示例_b.png', 
            bbox_inches='tight',dpi=300)
plt.show()
