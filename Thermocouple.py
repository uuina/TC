# 导入所需的库
import pandas as pd
import numpy as np
# 读取T分度号热电偶的分度表，存储为一个DataFrame对象
df = pd.read_excel("Thermocouple.xlsx", header=None)
print("T型热电偶的分度表范围-220~400℃")
def query(values, type="摄氏温度"):
    for value in values:
        if type == "摄氏温度":
            x = df.iloc[:,1].values  # 第二行是温度的值 
            y = df.iloc[:,0].values  # 第一行是电势的值
            result = np.interp(value, x, y)
            print(f"温度为{value}°C时，电势为{result:.3f}mV")
        elif type == "电势":
            x = df.iloc[:,0].values  # 第一行是电势的值
            y = df.iloc[:,1].values  # 第二行是温度的值
            result = np.interp(value, x, y)
            print(f"电势为{value}mV时，温度为{result:.3f}°C")
        elif type == "开尔文温度":
            value = value - 273.15  # 将开尔文温度转换为摄氏度
            x = df.iloc[:,1].values  # 第二行是温度的值
            y = df.iloc[:,0].values  # 第一行是电势的值
            result = np.interp(value, x, y)
            print(f"温度为{value+273.15}K时，电势为{result:.3f}mV")
        else:
            print("请输入正确的查询类型：温度、电势或开尔文")

a=input("请输入已知数据类型（填摄氏温度或开尔文温度或电势）：")
b=[float(i) for i in input("请输入已知值（不要带单位，多个值请用逗号分隔）：").split(',')]
query(b,a)