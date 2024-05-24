import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation, FFMpegWriter

plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 基础参数
w = 1  # 角频率 (rad/s)
v = 1  # 速度 (m/s)
A = 1  # 振幅 (m)
init1, init2 = 0, 0  # 初始相位 (rad)

# 设置参数
x_min, x_max = -10, 10  # x轴的范围
y_min, y_max = -10, 10  # y轴的范围
x = np.linspace(x_min, x_max, 500)  # x轴的采样点
y = np.linspace(y_min, y_max, 500)  # y轴的采样点
X, Y = np.meshgrid(x, y)  # 生成网格点
distance = 0

# 波源的位置
source1 = (0, 0)
source2 = (5, 0)
x3, y3 = (source1[0]+source2[0])/2, (source1[1] + source2[1])/2

# 分析振幅点位置
_source1 = (-3, 0)



# 波的振幅函数
def wave_amplitude(x, y, t, source):
    distance = np.sqrt((x - source[0])**2 + (y - source[1])**2)
    return np.where(t > distance / v, 1.3*np.cos(w * np.pi * (distance / v - t)+np.pi/2), 0)# if (t>distance/v) else 0#np.where(t > distance / v, np.cos(w * np.pi * (distance / v - t)), 0)

def my_amplitude(_source1, source1, color, t):
    # 添加切面余弦曲线
    # k = (_source1[1]-source1[1])/(_source1[0]-source1[0]) # 斜率
    angle = np.pi / 2 if _source1[0] - source1[0] == 0 else np.arctan(
        (_source1[1] - source1[1]) / (_source1[0] - source1[0]))
    k = np.tan(angle)
    base_X1 = np.linspace(source1[0], _source1[0], 200)
    base_Y1 = k * (base_X1 - source1[0]) + source1[1]
    if angle==np.pi/2:
        base_Y1 = np.linspace(source1[1], _source1[1], 200)
        base_X1 = base_Y1*0 + source1[0]
    # if angle==np.pi/2:
    #     _X1 = source1[0]
    #
    # 绘制方向轴
    plt.plot(base_X1, base_Y1, color=color, linestyle="dashed")
    ampl = wave_amplitude(base_X1, base_Y1, t, source1)
    angle1 = (angle + np.pi / 2) % np.pi
    _X1 = base_X1 + ampl * np.cos(angle1)
    _Y1 = base_Y1 + ampl * np.sin(angle1)
    # 绘制余弦图像
    plt.plot(_X1, _Y1, color=color)
    # 添加端点的小黑点
    plt.scatter(_source1[0], _source1[1], color='black', s=30)

def update(t):
    t = t/2
    plt.clf()  # 清除之前的图像，避免叠加显示
    distance = np.sqrt((X - x3)**2 + (Y - y3)**2)
    # distance = np.where(distance>0, distance, 0)
    k = 1 - 1.2*distance/15
    k = np.where(k>0, k, 0)
    Z = k*(wave_amplitude(X, Y, t, source1)+wave_amplitude(X, Y, t, source2)) #if t>distance/v else 0
    plt.title('两波的干涉 (时间: {:.2f})'.format(2*t))
    plt.imshow(Z, cmap='RdYlBu', extent=[x_min, x_max, y_min, y_max], origin='lower', vmin=-1.5, vmax=1.5)
    # 添加波源的小黑点
    plt.scatter([source1[0], source2[0]], [source1[1], source2[1]], color='black', s=80)

    # my_amplitude(_source1, source1, "red", t)
    my_amplitude([2.5, 6], source1, "red", t)
    my_amplitude([2.5, 6], source2, "blue", t)
    my_amplitude([-5, 0], source1, "red", t)
    my_amplitude([-5, 0], source2, "blue", t)


    return plt

# 创建动画
fig = plt.figure(figsize=(8, 8))
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 60, 0.1), interval=100)

# 导出视频
writer = FFMpegWriter(fps=10, metadata=dict(artist='lisanndesu'), bitrate=2000000)
ani.save("加切面.mp4", writer=writer)

# 显示动画
plt.show()

#加clf
#加vmin， vmax
#cos(  +np.pi/2)
#在导出视频时，ani中的interval参数不会影响视频的播放速度
# v和fps同时增大为原来三倍，画面更连续，同时速度不变
# 通过调整合适w，来调整波长