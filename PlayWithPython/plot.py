import matplotlib.pyplot as plt   # 导入模块 matplotlib.pyplot，并简写成 plt
import numpy as np                # 导入模块 numpy，并简写成 np

# 图形输入值
input_values = [1,2,3,4,5]
# 图形输出值
squares = [1,4,9,16,25]

# plot根据列表绘制出有意义的图形，linewidth是图形线宽，可省略
plt.plot(input_values, squares, linewidth=1.3)
# 设置图标标题
plt.title("EEG raw data", fontsize = 24)
# 设置坐标轴标签
plt.xlabel("Time", fontsize = 9)
plt.ylabel("Raw-data", fontsize = 9)
# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize = 9)
# 打开matplotlib查看器，并显示绘制图形
plt.show()
