import netCDF4 as nc
import pandas as pd
import numpy as np
from mpl_toolkits.basemap import Basemap

# 读取nc文件
nc_file = nc.Dataset('S5P_OFFL_L2__CH4____20230910T063145_20230910T081315_30615_03_020500_20230912T014127.nc', 'r')  # 替换为你的NetCDF文件路径

# 获取所需的变量
latitude = nc_file['PRODUCT']['latitude'][0, :, :]
print(f"latitude : {latitude.shape}")
longitude = nc_file['PRODUCT']['longitude'][0, :, :]
print(f"longitude : {longitude.shape}")
time = nc_file['PRODUCT']['time_utc'][0, :]
methane_data = nc_file['PRODUCT']['methane_mixing_ratio'][0, :, :]

# 检查是否存在 NaN 值，并将其替换为特定值，例如 12
methane_data = np.where(np.isnan(methane_data), 12, methane_data)

# 获取数据的形状
num_rows, num_cols = methane_data.shape

print(f"num_rows is {num_rows}")
print(f"num_cols is {num_cols}")

# 创建一个包含所有数据的列表
data_list = []

# 遍历数据并将其添加到列表
for i in range(latitude.shape[0]):
    for j in range(latitude.shape[1]):
        data_list.append({
            'Longitude': longitude[i, j],
            'Latitude': latitude[i, j],
            'Time_UTC': time[i],
            'Methane_Mixing_Ratio': methane_data[i, j]
        })

# 使用列表一次性创建 DataFrame
df = pd.DataFrame(data_list)

# 保存为CSV文件
df.to_csv('methane_data.csv', index=False)
