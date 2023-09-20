# 暑假历险记
# 加油呀
from netCDF4 import Dataset
import numpy as np
from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import matplotlib


if __name__ == '__main__':
    read_nc = Dataset(r'S5P_OFFL_L2__CH4____20230910T063145_20230910T081315_30615_03_020500_20230912T014127.nc', 'r')
    print(type(read_nc))
    print(read_nc.groups)
    print('*******1********')
    print(read_nc.groups['PRODUCT'])
    print('*******2********')
    print(read_nc.groups['PRODUCT'].variables.keys())
    print('*******3********')
    print(read_nc.groups['PRODUCT'].variables['methane_mixing_ratio_precision'])

    lons = read_nc.groups['PRODUCT'].variables['longitude'][:][0, :, :]
    lats = read_nc.groups['PRODUCT'].variables['latitude'][:][0, :, :]
    CH4 = read_nc.groups['PRODUCT'].variables['methane_mixing_ratio_precision'][0, :, :]
    print(CH4)
    print('lons shape :')
    print(type(lons))
    print(lons.shape)
    print('lats shape :')
    print(type(lats))
    print(lats.shape)
    print('CH4 shape :')
    print(CH4.shape)
    print(type(CH4))

    CH4_units = read_nc.groups['PRODUCT'].variables['methane_mixing_ratio_precision'].units
    print(CH4_units)

    lon_0 = lons.mean()
    lat_0 = lats.mean()
    print(type(lon_0))
    print(type(lat_0))

    # 读图
    CH4_draw = np.squeeze(CH4)
    fig = plt.figure(figsize=(64, 48), dpi=100)
    m = Basemap()  # 绘制底图

    xi, yi = m(lons, lats)  # 绘制底图的坐标矩阵

    boundaries = np.arange(0, 0.5, 0.005)
    cmap_reds = plt.cm.get_cmap('jet_r', len(boundaries))
    cs = m.pcolormesh(xi, yi, CH4_draw, shading='auto', cmap='jet', vmin=0, vmax=12)  # pcolor函数是指使用xi和yi为横纵坐标
    # m.drawparallels(np.arange(0, 360, 50), labels=[1, 0, 0, 0], fontsize=10)
    # m.drawmeridians(np.arange(0, 360, 50), labels=[0, 0, 0, 1], fontsize=10)
    m.drawparallels(np.arange(-80., 81., 10.), labels=[1, 0, 0, 0], fontsize=10)
    m.drawmeridians(np.arange(-180., 181., 10.), labels=[0, 0, 0, 1], fontsize=10)
    m.drawcoastlines()
    m.drawstates()
    m.drawcounties()
    cbar = m.colorbar(location='bottom', pad="10%")
    cbar.set_label(CH4_units)
    fig.savefig('test.png', dpi=100)
    plt.show()



