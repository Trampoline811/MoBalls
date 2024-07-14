# 本文件用来测试项目中实现的各个函数的通达性

import numpy as np
import matplotlib.pyplot as plt

group_balls = ['红' + str(i) for i in range(1, 9)] + \
                      ['黄' + str(i) for i in range(1, 9)] + \
                      ['蓝' + str(i) for i in range(1, 9)]
group_balls = np.array(group_balls)  # 转换为numpy数组
weight = [1/24.0] * 24
res = np.random.choice(group_balls, size=12, replace=False, p=weight)
print(res)

# 测试画图的子图
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(10, 10))

x1 = np.array([1, 2, 3, 4])
y1 = np.array([1, 4, 9, 16])
x2 = np.array([1, 2, 3, 4])
y2 = np.array([1, 4, 9, 16])
ax1.plot(x1, y1)
ax2.plot(x2, y2)
ax3.plot([-1, -2, -3], [4, 2, 3])


# 按照余老师的教程
plt.figure('Analyse')
plt.subplot(2, 1, 2)
plt.plot(x1, y1)
# 设置标题
plt.title('Result over Round')
# 设置 x 轴的标签
plt.xlabel('Round')
# 设置 y 轴的标签
plt.ylabel('Result')

plt.subplot(2, 2, 1)
plt.bar(x2, y2)
# 设置标题
plt.title('Distribution of Groups')
# 设置 x 轴的标签
plt.xlabel('Group')
# 设置 y 轴的标签
plt.ylabel('Frequency')

plt.subplot(2, 2, 2)
plt.pie([4, 2, 3])
plt.title('Distribution of Groups')
# 设置 x 轴的标签
plt.xlabel('X3')
# 设置 y 轴的标签
# plt.show()


# 测试numpy的字典映射
import numpy as np

data = np.array(['A1', 'A5', 'B5', 'C2', 'C8', 'B7'])
mapping = {'A': '黄', 'B': '红', 'C': '蓝'}

# 将numpy数组转换为字符串数组
str_data = data.astype(str)
print(type(str_data))
# 使用字典映射替换元素
result = np.array([mapping[x[0]] + x[1] for x in str_data])
print(result)
print(result, type(result), result.shape)


A, B, C = 1, 2, 3
print(A, B, C)

