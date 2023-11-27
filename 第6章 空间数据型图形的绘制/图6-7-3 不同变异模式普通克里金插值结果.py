"""
编写时间：2022年4月30日 15：30

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

# a）linear 变异模式普通克里金插值结果

bounds = map_fig02.geometry.total_bounds
#插入400*400的网格点
grid_lon = np.linspace(bounds[0],bounds[2],400)
grid_lat = np.linspace(bounds[1],bounds[3],400)

point_x = df_city["long"]
point_y = df_city["lat"]
point_value = df_city["value"]
model = "linear"
OK = OrdinaryKriging(x=point_x,y=point_y,z=point_value,variogram_model=model)
# 对构建网格区域进行计算
z, ss = OK.execute("grid", grid_lon, grid_lat)
xgrid, ygrid = np.meshgrid(grid_lon, grid_lat)

#将插值网格数据整理
df_grid =pd.DataFrame(dict(lon=xgrid.flatten(),lat=ygrid.flatten()))
df_grid["OK_result"] = z.data.flatten()
df_grid_geo = gpd.GeoDataFrame(df_grid, geometry=gpd.points_from_xy(df_grid["lon"], df_grid["lat"]),
                               crs=map_fig02.crs)
#使用geopandas.clip()函数裁剪
map_Krig_clip = gpd.clip(df_grid_geo,map_fig02)

fig,ax = plt.subplots(figsize=(5,4.5),dpi=100,facecolor="w")
plot02 = map_fig02.plot("country",legend=False,ec="k",lw=.6,color="none",ax=ax,zorder=3)
map_Krig_clip.plot("OK_result",ax=ax,legend=True,s=1,cmap=parula,
                        legend_kwds=dict(label="Krige Values",aspect=11,shrink=0.4))

ax.grid(False)
ax.set_ylim((30, 60))
ax.set_xlim((100, 140))
ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)
ax.spines.left.set_position(("outward",10))
ax.spines.bottom.set_position(("outward",10))
ax.set_title(str.capitalize(model)+" Variogram Model",bbox=dict(boxstyle="round", fc="w"),pad=15)
#ax.set_title()
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
fig.tight_layout()

fig.savefig('\第6章 空间数据型图形的绘制\图6-7-3 不同变异模式普通克里金插值结果_a.pdf',bbox_inches='tight')
fig.savefig('\第6章 空间数据型图形的绘制\图6-7-3 不同变异模式普通克里金插值结果_a.png', 
            bbox_inches='tight',dpi=300)         
plt.show()


# b）power 变异模式普通克里金插值结果
import pykrige.kriging_tools as kt
from pykrige.ok import OrdinaryKriging

bounds = map_fig02.geometry.total_bounds
#插入400*400的网格点
grid_lon = np.linspace(bounds[0],bounds[2],400)
grid_lat = np.linspace(bounds[1],bounds[3],400)

point_x = df_city["long"]
point_y = df_city["lat"]
point_value = df_city["value"]
model = "power"
OK = OrdinaryKriging(x=point_x,y=point_y,z=point_value,variogram_model=model)
# 对构建网格区域进行计算
z, ss = OK.execute("grid", grid_lon, grid_lat)
xgrid, ygrid = np.meshgrid(grid_lon, grid_lat)

#将插值网格数据整理
df_grid =pd.DataFrame(dict(lon=xgrid.flatten(),lat=ygrid.flatten()))
df_grid["OK_result"] = z.data.flatten()
df_grid_geo = gpd.GeoDataFrame(df_grid, geometry=gpd.points_from_xy(df_grid["lon"], df_grid["lat"]),
                               crs=map_fig02.crs)
#使用geopandas.clip()函数裁剪
map_Krig_clip = gpd.clip(df_grid_geo,map_fig02)

fig,ax = plt.subplots(figsize=(5,4.5),dpi=100,facecolor="w")
plot02 = map_fig02.plot("country",legend=False,ec="k",lw=.6,color="none",ax=ax,zorder=3)
map_Krig_clip.plot("OK_result",ax=ax,legend=True,s=1,cmap=parula,
                        legend_kwds=dict(label="Krige Values",aspect=11,shrink=0.4))

ax.grid(False)
ax.set_ylim((30, 60))
ax.set_xlim((100, 140))
ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)
ax.spines.left.set_position(("outward",10))
ax.spines.bottom.set_position(("outward",10))
ax.set_title(str.capitalize(model)+" Variogram Model",bbox=dict(boxstyle="round", fc="w"),pad=15)
#ax.set_title()
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
fig.tight_layout()

fig.savefig('\第6章 空间数据型图形的绘制\图6-7-3 不同变异模式普通克里金插值结果_b.pdf',bbox_inches='tight')
fig.savefig('\第6章 空间数据型图形的绘制\图6-7-3 不同变异模式普通克里金插值结果_b.png', 
            bbox_inches='tight',dpi=300)         
plt.show()


# c）gaussian 变异模式普通克里金插值结果

import pykrige.kriging_tools as kt
from pykrige.ok import OrdinaryKriging

bounds = map_fig02.geometry.total_bounds
#插入400*400的网格点
grid_lon = np.linspace(bounds[0],bounds[2],400)
grid_lat = np.linspace(bounds[1],bounds[3],400)

point_x = df_city["long"]
point_y = df_city["lat"]
point_value = df_city["value"]
model = "gaussian"
OK = OrdinaryKriging(x=point_x,y=point_y,z=point_value,variogram_model=model)
# 对构建网格区域进行计算
z, ss = OK.execute("grid", grid_lon, grid_lat)
xgrid, ygrid = np.meshgrid(grid_lon, grid_lat)

#将插值网格数据整理
df_grid =pd.DataFrame(dict(lon=xgrid.flatten(),lat=ygrid.flatten()))
df_grid["OK_result"] = z.data.flatten()
df_grid_geo = gpd.GeoDataFrame(df_grid, geometry=gpd.points_from_xy(df_grid["lon"], df_grid["lat"]),
                               crs=map_fig02.crs)
#使用geopandas.clip()函数裁剪
map_Krig_clip = gpd.clip(df_grid_geo,map_fig02)

fig,ax = plt.subplots(figsize=(5,4.5),dpi=100,facecolor="w")
plot02 = map_fig02.plot("country",legend=False,ec="k",lw=.6,color="none",ax=ax,zorder=3)
map_Krig_clip.plot("OK_result",ax=ax,legend=True,s=1,cmap=parula,
                        legend_kwds=dict(label="Krige Values",aspect=11,shrink=0.4))

ax.grid(False)
ax.set_ylim((30, 60))
ax.set_xlim((100, 140))
ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)
ax.spines.left.set_position(("outward",10))
ax.spines.bottom.set_position(("outward",10))
ax.set_title(str.capitalize(model)+" Variogram Model",bbox=dict(boxstyle="round", fc="w"),pad=15)
#ax.set_title()
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
fig.tight_layout()

fig.savefig('\第6章 空间数据型图形的绘制\图6-7-3 不同变异模式普通克里金插值结果_c.pdf',bbox_inches='tight')
fig.savefig('\第6章 空间数据型图形的绘制\图6-7-3 不同变异模式普通克里金插值结果_c.png', 
            bbox_inches='tight',dpi=300)         
plt.show()

# d）spherical 变异模式普通克里金插值结果

import pykrige.kriging_tools as kt
from pykrige.ok import OrdinaryKriging

bounds = map_fig02.geometry.total_bounds
#插入400*400的网格点
grid_lon = np.linspace(bounds[0],bounds[2],400)
grid_lat = np.linspace(bounds[1],bounds[3],400)

point_x = df_city["long"]
point_y = df_city["lat"]
point_value = df_city["value"]
model = "spherical"
OK = OrdinaryKriging(x=point_x,y=point_y,z=point_value,variogram_model=model)
# 对构建网格区域进行计算
z, ss = OK.execute("grid", grid_lon, grid_lat)
xgrid, ygrid = np.meshgrid(grid_lon, grid_lat)

#将插值网格数据整理
df_grid =pd.DataFrame(dict(lon=xgrid.flatten(),lat=ygrid.flatten()))
df_grid["OK_result"] = z.data.flatten()
df_grid_geo = gpd.GeoDataFrame(df_grid, geometry=gpd.points_from_xy(df_grid["lon"], df_grid["lat"]),
                               crs=map_fig02.crs)
#使用geopandas.clip()函数裁剪
map_Krig_clip = gpd.clip(df_grid_geo,map_fig02)

fig,ax = plt.subplots(figsize=(5,4.5),dpi=100,facecolor="w")
plot02 = map_fig02.plot("country",legend=False,ec="k",lw=.6,color="none",ax=ax,zorder=3)
map_Krig_clip.plot("OK_result",ax=ax,legend=True,s=1,cmap=parula,
                        legend_kwds=dict(label="Krige Values",aspect=11,shrink=0.4))

ax.grid(False)
ax.set_ylim((30, 60))
ax.set_xlim((100, 140))
ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)
ax.spines.left.set_position(("outward",10))
ax.spines.bottom.set_position(("outward",10))
ax.set_title(str.capitalize(model)+" Variogram Model",bbox=dict(boxstyle="round", fc="w"),pad=15)
#ax.set_title()
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
fig.tight_layout()

fig.savefig('\第6章 空间数据型图形的绘制\图6-7-3 不同变异模式普通克里金插值结果_d.pdf',bbox_inches='tight')
fig.savefig('\第6章 空间数据型图形的绘制\图6-7-3 不同变异模式普通克里金插值结果_d.png', 
            bbox_inches='tight',dpi=300)         
plt.show()

# e）exponential变异模式普通克里金插值结果

import pykrige.kriging_tools as kt
from pykrige.ok import OrdinaryKriging

bounds = map_fig02.geometry.total_bounds
#插入400*400的网格点
grid_lon = np.linspace(bounds[0],bounds[2],400)
grid_lat = np.linspace(bounds[1],bounds[3],400)

point_x = df_city["long"]
point_y = df_city["lat"]
point_value = df_city["value"]
model = "exponential"
OK = OrdinaryKriging(x=point_x,y=point_y,z=point_value,variogram_model=model)
# 对构建网格区域进行计算
z, ss = OK.execute("grid", grid_lon, grid_lat)
xgrid, ygrid = np.meshgrid(grid_lon, grid_lat)

#将插值网格数据整理
df_grid =pd.DataFrame(dict(lon=xgrid.flatten(),lat=ygrid.flatten()))
df_grid["OK_result"] = z.data.flatten()
df_grid_geo = gpd.GeoDataFrame(df_grid, geometry=gpd.points_from_xy(df_grid["lon"], df_grid["lat"]),
                               crs=map_fig02.crs)
#使用geopandas.clip()函数裁剪
map_Krig_clip = gpd.clip(df_grid_geo,map_fig02)

fig,ax = plt.subplots(figsize=(5,4.5),dpi=100,facecolor="w")
plot02 = map_fig02.plot("country",legend=False,ec="k",lw=.6,color="none",ax=ax,zorder=3)
map_Krig_clip.plot("OK_result",ax=ax,legend=True,s=1,cmap=parula,
                        legend_kwds=dict(label="Krige Values",aspect=11,shrink=0.4))

ax.grid(False)
ax.set_ylim((30, 60))
ax.set_xlim((100, 140))
ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)
ax.spines.left.set_position(("outward",10))
ax.spines.bottom.set_position(("outward",10))
ax.set_title(str.capitalize(model)+" Variogram Model",bbox=dict(boxstyle="round", fc="w"),pad=15)
#ax.set_title()
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
fig.tight_layout()

fig.savefig('\第6章 空间数据型图形的绘制\图6-7-3 不同变异模式普通克里金插值结果_e.pdf',bbox_inches='tight')
fig.savefig('\第6章 空间数据型图形的绘制\图6-7-3 不同变异模式普通克里金插值结果_e.png', 
            bbox_inches='tight',dpi=300)         
plt.show()

# f）hole-effect 变异模式普通克里金插值结果

import pykrige.kriging_tools as kt
from pykrige.ok import OrdinaryKriging

bounds = map_fig02.geometry.total_bounds
#插入400*400的网格点
grid_lon = np.linspace(bounds[0],bounds[2],400)
grid_lat = np.linspace(bounds[1],bounds[3],400)

point_x = df_city["long"]
point_y = df_city["lat"]
point_value = df_city["value"]
model = "hole-effect"
OK = OrdinaryKriging(x=point_x,y=point_y,z=point_value,variogram_model=model)
# 对构建网格区域进行计算
z, ss = OK.execute("grid", grid_lon, grid_lat)
xgrid, ygrid = np.meshgrid(grid_lon, grid_lat)

#将插值网格数据整理
df_grid =pd.DataFrame(dict(lon=xgrid.flatten(),lat=ygrid.flatten()))
df_grid["OK_result"] = z.data.flatten()
df_grid_geo = gpd.GeoDataFrame(df_grid, geometry=gpd.points_from_xy(df_grid["lon"], df_grid["lat"]),
                               crs=map_fig02.crs)
#使用geopandas.clip()函数裁剪
map_Krig_clip = gpd.clip(df_grid_geo,map_fig02)

fig,ax = plt.subplots(figsize=(5,4.5),dpi=100,facecolor="w")
plot02 = map_fig02.plot("country",legend=False,ec="k",lw=.6,color="none",ax=ax,zorder=3)
map_Krig_clip.plot("OK_result",ax=ax,legend=True,s=1,cmap=parula,
                        legend_kwds=dict(label="Krige Values",aspect=11,shrink=0.4))

ax.grid(False)
ax.set_ylim((30, 60))
ax.set_xlim((100, 140))
ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)
ax.spines.left.set_position(("outward",10))
ax.spines.bottom.set_position(("outward",10))
ax.set_title(str.capitalize(model)+" Variogram Model",bbox=dict(boxstyle="round", fc="w"),pad=15)
#ax.set_title()
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
fig.tight_layout()

fig.savefig('\第6章 空间数据型图形的绘制\图6-7-3 不同变异模式普通克里金插值结果_f.pdf',bbox_inches='tight')
fig.savefig('\第6章 空间数据型图形的绘制\图6-7-3 不同变异模式普通克里金插值结果_f.png', 
            bbox_inches='tight',dpi=300)         
plt.show()

