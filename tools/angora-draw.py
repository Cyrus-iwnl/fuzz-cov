import csv

import matplotlib.pyplot as plt

exampleFile = open('angora.log')  # 打开csv文件
exampleReader = csv.reader(exampleFile)  # 读取csv文件
exampleData = list(exampleReader)  # csv数据转换为列表
length_zu = len(exampleData)  # 得到数据行数
length_yuan = len(exampleData[0])  # 得到每行长度

x = list()
y = list()

for i in range(0, length_zu):
    x.append(exampleData[i][0])
    y.append(exampleData[i][2])

plt.plot(x, y)  # 绘制x,y的折线图
plt.show()  # 显示折线图
