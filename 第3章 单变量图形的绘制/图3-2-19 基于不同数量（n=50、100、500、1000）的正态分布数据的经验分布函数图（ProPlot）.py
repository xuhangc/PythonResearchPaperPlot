
"""
编写时间：2022年2月06日 11：20

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。

代码中Proplot包绘制的部分可能与Matplotlib绘制不同，需注意两者绘图语法的不同~~

"""
#注意：本案例中引入的SciencePlots库主题方式会随着SciencePlots版本的更新发生改变，读者还需参考其官网引入的正确方式。
#      建议按照官网引入方式进行操作和使用最新版本的ScienePlots。如引入方式发生改变，请关注微信公众号【DataCharm】进行实时获取代码更新。


import numpy as np
import pandas as pd
import proplot as pplt
from scipy import stats
from statsmodels.distributions.empirical_distribution import ECDF
from proplot import rc
rc['legend.fontsize'] = 8


def epsilon(n, alpha=0.05):
    return np.sqrt(1. / (2. * n) * np.log(2. / alpha))
low = -3
high = 3
name = "Normal Distribution"
sample_num = [50,100,500,1000]

fig, axs = pplt.subplots(ncols=2, nrows=2,refwidth=2.5,refheight=2)
axs.format(
    abc='a.', abcloc='ul',abcsize=15,
    xlabel='Normal Distribution Values', ylabel='Percentile',
)

for ax, num in zip(axs,sample_num):
    norm = stats.norm(0, 1)
    samples = norm.rvs(num)
    ecdf = ECDF(samples)
    x = np.linspace(low, high, 10000)
    eps = epsilon(n=len(samples))
    df = pd.DataFrame(ecdf(x), index=x)
    # ECDF plot
    ax.plot(x,ecdf(x),color="#459DFF",label='ECDF')
    #CDF plot
    ax.plot(x,norm.cdf(x),'r--',label='CDF')

    df['upper'] = pd.Series(ecdf(x), index=x).apply(lambda x: min(x + eps, 1.))
    df['lower'] = pd.Series(ecdf(x), index=x).apply(lambda x: max(x - eps, 0.))
    # Confidence Band
    ax.fill_between(x, df['upper'], df['lower'], color="gray",alpha=0.15, lw=.05,label='Confidence Band')
    ax.legend(ncols=1,loc='lower right',frame=False)
    ax.format(title='%s ECDF (n=%d)' % (name, len(samples)),titleweight='bold',titlesize=10)

fig.savefig('\第3章 单变量图形的绘制\图3-2-19 基于不同数量（n=50、100、500、1000）的正态分布数据的经验分布函数图（ProPlot）.pdf',bbox_inches='tight')
fig.savefig('\第3章 单变量图形的绘制\图3-2-19 基于不同数量（n=50、100、500、1000）的正态分布数据的经验分布函数图（ProPlot）.png', 
            bbox_inches='tight',dpi=300) 
plt.show() 
            