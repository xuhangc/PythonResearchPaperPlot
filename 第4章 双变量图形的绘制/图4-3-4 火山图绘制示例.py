
"""
编写时间：2022年4月18日 19：50

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

"""
此代码为使用Python-Prolot包进行学术风格图表绘制，绘图语法和Matplotlib有所不同，需注意。
"""
import pandas as pd
import numpy as np
import proplot as pplt
import seaborn as sns
import matplotlib.pyplot as plt
from bioinfokit import analys, visuz #需安装bioinfokit库
from proplot import rc
rc["axes.labelsize"] = 15
rc['tick.labelsize'] = 13
rc["suptitle.size"] = 15
rc["figure.facecolor"]="w"
rc["font.family"] = "Times New Roman"
rc["xtick.minor.visible"] = False
rc["ytick.minor.visible"] = False
rc["xtick.bottom"] = False
rc["ytick.left"] = False

volcano_data  = analys.get_data('volcano').data

# a）基本火山图样式绘制示例

visuz.gene_exp.volcano(df=volcano_data, lfc='log2FC', pv='p-value',figname="volcano01")
visuz.gene_exp.volcano(df=volcano_data, lfc='log2FC', pv='p-value',figname="volcano01",figtype='pdf')

# b）火山图定制化样式绘制示例
#修改样式
visuz.gene_exp.volcano(df=volcano_data, lfc='log2FC', pv='p-value',geneid="GeneNames", 
                       color=("#00239CFF", "grey", "#E10600FF"),
    genenames=({"LOC_Os09g01000.1":"EP", "LOC_Os01g50030.1":"CPuORF25", "LOC_Os06g40940.3":"GDH", "LOC_Os03g03720.1":"G3PD"}),
    gstyle=2, sign_line=True, xlm=(-6,6,1), ylm=(0,61,5), figtype='png', axtickfontsize=12,
    axtickfontname='Times New Roman',axlabelfontname="Times New Roman",axlabelfontsize=15,
                       plotlegend=True,
                       figname="volcano02")
                       
    