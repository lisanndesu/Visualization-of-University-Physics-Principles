import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
from matplotlib.animation import FuncAnimation, FFMpegWriter
from matplotlib.colors import ListedColormap
from matplotlib.colors import LinearSegmentedColormap

# 设置参数
x_min, x_max = -10, 10  # x轴的范围
y_min, y_max = -10, 10  # y轴的范围
x = np.linspace(x_min, x_max, 1000)  # x轴的采样点
y = np.linspace(y_min, y_max, 1000)  # y轴的采样点
X, Y = np.meshgrid(x, y)  # 生成网格点

# 条件参数
time = 1
f = 2
wave_len = 1
n1 = 1.3
n2 = 1.6

# 中心亮斑的位置
source = (0, 3)

# 波的振幅函数
def wave_amplitude(x, y, t, source):  # （x,y)点在t时间由source引起的振幅
    r = 0.5 * np.sqrt((x - source[0]) ** 2 + (y - source[1]) ** 2)  # （x, y)与source的距离
    i = np.arctan(r / f)
    h = abs((time - t) * 5)  # 加绝对值还是会突变
    angle = (4 * np.pi / wave_len) * (2 * h) * np.sqrt((n1 ** 2 - (n2 * np.sin(i)) ** 2)) + np.pi
    return np.cos(angle / 2)  # 振幅计算公式    y = Acos(2Π（t-x/v)+Q

# 动画更新函数
def update_with_new_cmap(t):
    # 清除之前的图形
    plt.clf()
    # Z为和振幅
    Z = wave_amplitude(X, Y, t, source)
    plt.title('equal inclination interference (time: {:.2f})'.format(t))
    # plt.imshow(Z, cmap='hot', extent=[x_min, x_max, y_min, y_max], origin='lower')
    # colors = ['black', 'red']
    # cmap = ListedColormap(colors)
    # plt.imshow(Z, cmap=ListedColormap(colors), extent=[x_min, x_max, y_min, y_max], origin='lower')

    # 定义颜色映射的颜色
    colors = ['black', '#800000', 'red']  # 使用十六进制表示红色的中间色
    # 定义颜色映射的位置
    positions = [0.0, 0.5, 1.0]
    # 创建自定义的颜色映射
    cmap = LinearSegmentedColormap.from_list('CustomRedBlack', list(zip(positions, colors)))
    plt.imshow(Z, cmap=cmap, extent=[x_min, x_max, y_min, y_max], origin='lower')

    # 添加平行四边形表示高度
    basex, basey = -5, y_min+2  # 平行四边形左下角坐标
    wide = 8         # 平行四边形底边长
    height = 3      # 平行四边形高
    bottom_height = y_min + 2
    top_height = bottom_height + abs((time - t) * 2)# 两平面间距
    points_bottom = [[basex, bottom_height], [basex+wide, bottom_height], [basex+wide+wide/4, bottom_height+height], [basex+wide/4, bottom_height+height]]
    points_top = [[basex, top_height], [basex+wide, top_height], [basex+wide+wide/4, top_height+height], [basex+wide/4, top_height+height]]
    polygon_bottom = plt.Polygon(points_bottom, closed=True, color='blue', alpha=0.5)
    polygon_top = plt.Polygon(points_top, closed=True, color='green', alpha=0.5)
    plt.gca().add_patch(polygon_bottom)
    plt.gca().add_patch(polygon_top)

    # 显示高度值
    _y = y_min + 2 - 1
    # if time < t:
    #     _y = y_min + 2 + 1
    plt.text(-2, _y, 'distance: {:.2f}'.format(abs(time - t) * 5), color='b', fontsize=12)
    plt.text(basex-2, bottom_height, 'M2\''.format(abs(time - t) * 5), color='b', fontsize=12)
    plt.text(basex-1, top_height, 'M1'.format(abs(time - t) * 5), color='red', fontsize=12)
    return plt

# 创建动画
fig = plt.figure(figsize=(8, 8))
frames = np.arange(0, 2 * time, 0.005)

ani = animation.FuncAnimation(fig, update_with_new_cmap, frames=frames, interval=150)

# 导出视频
writer = FFMpegWriter(fps=10, metadata=dict(artist='lisanndesu'), bitrate=200000)
ani.save("equal inclination interference_plus.mp4", writer=writer)

# 显示动画
plt.show()
print("successfully")