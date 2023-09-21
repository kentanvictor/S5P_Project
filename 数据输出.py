import netCDF4 as nc  # 导入netCDF4库，用于处理NetCDF文件
import pandas as pd  # 导入pandas库，用于数据处理
import numpy as np  # 导入numpy库，用于数值计算
from mpl_toolkits.basemap import Basemap  # 导入Basemap类，用于绘制地图

# 读取nc文件
nc_file = nc.Dataset('S5P_OFFL_L2__CH4____20230910T063145_20230910T081315_30615_03_020500_20230912T014127.nc', 'r')  # 打开NetCDF文件

# 获取所需的变量
latitude = nc_file['PRODUCT']['latitude'][0, :, :]  # 从NetCDF文件中提取纬度数据
print(f"latitude : {latitude.shape}")  # 打印纬度数据的形状
longitude = nc_file['PRODUCT']['longitude'][0, :, :]  # 从NetCDF文件中提取经度数据
print(f"longitude : {longitude.shape}")  # 打印经度数据的形状
time = nc_file['PRODUCT']['time_utc'][0, :]  # 从NetCDF文件中提取时间数据
methane_data = nc_file['PRODUCT']['methane_mixing_ratio'][0, :, :]  # 从NetCDF文件中提取甲烷混合比数据

# 检查是否存在 NaN 值，并将其替换为特定值，例如 12
methane_data = np.where(np.isnan(methane_data), 12, methane_data)

# 获取数据的形状
num_rows, num_cols = methane_data.shape  # 获取甲烷混合比数据的行数和列数

print(f"num_rows is {num_rows}")  # 打印数据的行数
print(f"num_cols is {num_cols}")  # 打印数据的列数

# 创建一个包含所有数据的列表
data_list = []

# 遍历数据并将其添加到列表
for i in range(latitude.shape[0]):  # 遍历行
    for j in range(latitude.shape[1]):  # 遍历列
        data_list.append({
            'Longitude': longitude[i, j],  # 经度
            'Latitude': latitude[i, j],  # 纬度
            'Time_UTC': time[i],  # 时间
            'Methane_Mixing_Ratio': methane_data[i, j]  # 甲烷混合比
        })

# 使用列表一次性创建 DataFrame
df = pd.DataFrame(data_list)  # 使用data_list创建DataFrame

# 保存为CSV文件
df.to_csv('methane_data.csv', index=False)  # 将DataFrame保存为CSV文件，不包括行索引
