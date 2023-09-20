
import netCDF4 as nc
import pandas as pd
import numpy as np

# 读取nc文件
data = nc.Dataset('E:\\S5P_OFFL_L2__CH4____20230910T063145_20230910T081315_30615_03_020500_20230912T014127.nc')

# 将数据转换为DataFrame格式

# 假设data.groups['PRODUCT'].variables['methane_mixing_ratio_precision']返回的数据是(1, 4173, 215)形状的
data = data.groups['PRODUCT'].variables['methane_mixing_ratio']
data_2d = np.reshape(data, ((245190,62500)))
df = pd.DataFrame(data_2d)

# 输出为csv格式
df.to_csv('output.csv', index=False)
