"""
编写时间：2022年4月30日 14：30

作者: 宁海涛，代码运行出错或者因包版本更新出错，请关注微信公众号【DataCharm】进行实时获取更新。
"""

"""
此代码为使用Python-Prolot包进行学术风格图表绘制，绘图语法和Matplotlib有所不同，需注意。
"""

import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pykrige.kriging_tools as kt
from pykrige.ok import OrdinaryKriging
from colormaps import parula

from proplot import rc
rc["font.family"] = "Times New Roman"
rc["axes.labelsize"] = 15
rc["tick.labelsize"] = 10
rc["suptitle.size"] = 15
rc["title.size"] = 14


map_fig02 = gpd.read_file(r"\第6章 空间数据型图形的绘制\Virtual_Map1.shp")
df_city = pd.read_csv(r"\第6章 空间数据型图形的绘制\Virtual_huouse.csv")
#插值计算
bounds = map_fig02.geometry.total_bounds
#插入400*400的网格点
grid_lon = np.linspace(bounds[0],bounds[2],400)
grid_lat = np.linspace(bounds[1],bounds[3],400)

point_x = df_city["long"]
point_y = df_city["lat"]
point_value = df_city["value"]

OK = OrdinaryKriging(x=point_x,y=point_y,z=point_value,variogram_model="linear")
# 对构建网格区域进行计算
z, ss = OK.execute("grid", grid_lon, grid_lat)

xgrid, ygrid = np.meshgrid(grid_lon, grid_lat)
levels = np.linspace(z.data.min(), z.data.max(), 5)

# a）利用PyKrige库进行插值计算的网格样式
fig,ax = plt.subplots(figsize=(5,4.5),dpi=100,facecolor="w")
plot02 = map_fig02.plot("country",legend=False,ec="k",lw=1,color="none",
                         ax=ax,zorder=3)
cp = ax.pcolormesh(xgrid, ygrid,z.data,cmap=parula)
ct = ax.contour(xgrid, ygrid,z.data,levels=levels,colors='w',linewidths=.4)
# 添加colorbar
cbar = fig.colorbar(cp,shrink=.4,aspect=10)
cbar.ax.set_ylabel(ylabel="Krige Values",fontsize=11)
cbar.ax.set_title("Values",fontsize=12,pad=5)
cbar.ax.tick_params(left=True,direction="in",labelsize=10)
cbar.ax.tick_params(which="minor",right=False)

ax.grid(False)
ax.set_ylim((30, 60))
ax.set_xlim((100, 140))
ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)
ax.spines.left.set_position(("outward",10))
ax.spines.bottom.set_position(("outward",10))
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
fig.tight_layout()

fig.savefig('\第6章 空间数据型图形的绘制\图6-7-2 利用PyKrige库进行插值计算的网格样式和根据地图文件裁剪的插值结果_a.pdf',bbox_inches='tight')
fig.savefig('\第6章 空间数据型图形的绘制\图6-7-2 利用PyKrige库进行插值计算的网格样式和根据地图文件裁剪的插值结果_a.png', 
            bbox_inches='tight',dpi=300)         
plt.show()

# b）根据地图文件裁剪的插值结果:裁剪操作 使用geopandas.clip()函数操作
#将插值网格数据整理
df_grid =pd.DataFrame(dict(lon=xgrid.flatten(),lat=ygrid.flatten()))
df_grid["OK_result"] = z.data.flatten()
# 将构建的网格数据转换成geopandas类型

df_grid_geo = gpd.GeoDataFrame(df_grid, geometry=gpd.points_from_xy(df_grid["lon"], df_grid["lat"]),
                               crs=map_fig02.crs)
#使用geopandas.clip()函数裁剪
map_Krig_line_clip = gpd.clip(df_grid_geo,map_fig02)

fig,ax = plt.subplots(figsize=(5,4.5),dpi=100,facecolor="w")
plot02 = map_fig02.plot("country",legend=False,ec="k",lw=.8,color="none",ax=ax,zorder=3)
map_Krig_line_clip.plot("OK_result",ax=ax,legend=True,s=2,cmap=parula,
                        legend_kwds=dict(label="Krige Values",aspect=11,shrink=0.4))
ax.grid(False)
ax.set_ylim((30, 60))
ax.set_xlim((100, 140))
ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)
ax.spines.left.set_position(("outward",10))
ax.spines.bottom.set_position(("outward",10))
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
fig.tight_layout()
fig.savefig('\第6章 空间数据型图形的绘制\图6-7-2 利用PyKrige库进行插值计算的网格样式和根据地图文件裁剪的插值结果_b.pdf',bbox_inches='tight')
fig.savefig('\第6章 空间数据型图形的绘制\图6-7-2 利用PyKrige库进行插值计算的网格样式和根据地图文件裁剪的插值结果_b.png', 
            bbox_inches='tight',dpi=300)         
plt.show()


#外一种裁剪方法
import fiona
from shapely.geometry import Polygon,Point
mask_shp = map_fig02

masked_value = [value if mask_shp["geometry"].contains(Point(long,lat)).any()==True \
                else np.nan for long,lat,value in zip(df_grid["lon"],df_grid["lat"],df_grid["OK_result"])]
                
df_grid["mask_value"] = masked_value
#转换矩阵形状
mask_value_grid = df_grid["mask_value"].values.reshape(xgrid.shape)
levels = np.linspace(z.data.min(), z.data.max(), 5) 

fig,ax = plt.subplots(figsize=(5,4.5),dpi=100,facecolor="w")
plot02 = map_fig02.plot("country",legend=False,ec="k",lw=.8,color="none",
                         ax=ax,zorder=3)
cp = ax.pcolormesh(xgrid, ygrid,mask_value_grid,cmap=parula)
ct = ax.contour(xgrid, ygrid,mask_value_grid,levels,colors='w',linewidths=.4)
# 添加colorbar
cbar = fig.colorbar(cp,shrink=.4,aspect=12)
cbar.ax.set_ylabel(ylabel="Krige Values",fontsize=11)
cbar.ax.set_title("Values",fontsize=12,pad=5)
cbar.ax.tick_params(left=True,direction="in",labelsize=10)
cbar.ax.tick_params(which="minor",right=False)

ax.grid(False)
ax.set_ylim((30, 60))
ax.set_xlim((100, 140))
ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)
ax.spines.left.set_position(("outward",10))
ax.spines.bottom.set_position(("outward",10))
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
fig.tight_layout() 

fig.savefig('\第6章 空间数据型图形的绘制\图6-7-2 利用PyKrige库进行插值计算的网格样式和根据地图文件裁剪的插值结果_b_mask.pdf',bbox_inches='tight')
fig.savefig('\第6章 空间数据型图形的绘制\图6-7-2 利用PyKrige库进行插值计算的网格样式和根据地图文件裁剪的插值结果_b_mask.png', 
            bbox_inches='tight',dpi=300)         
plt.show()            