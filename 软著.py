import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation, FFMpegWriter

plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题


# 默认基础参数
is_video = "n"
w = 1  # 角频率 (rad/s)
v = 1  # 速度 (m/s)
A = 1  # 振幅 (m)
init1, init2 = 0, 0  # 初始相位 (rad)
_source = (0, 0)

# 根据输入调整cfg
print("------------------------配置参数-----------------------")
print("1.y 表示yes    n 表示 no  其他选择视为no")
print("2.在选择后摁下回车确定")
print("3.不输入数据直接回车表示使用默认参数\n\n")
is_video = input("是否导出视频：y/n(默认no)")
high_bite = "n"
if is_video=="y":
    video_name = input("请输入导出视频名称(默认output_video)")
    if not video_name:
        video_name = "output_video"
    high_bite = input("是否导出高清视频(占用内存大）(y/n)(默认no)")

# 波源位置
source1 = list(map(int, input("波源位置（坐标用空格隔开，如\“3 5\"):(默认[0, 0])").split()))
source2 = list(map(int, input("第二波源位置：(默认[5, 0])").split()))
if not source1 or len(source1)!=2:
    source1 = (0, 0)
if not source2 or len(source2)!=2:
    source2 = (5, 0)
x3, y3 = (source1[0]+source2[0])/2, (source1[1] + source2[1])/2



# 传播速度
try:
    v = int(input("波的传播速度：(默认1)"))
except:
    v = 1

# 是否平面化某一点振幅合成情况
is_flatten = input("是否平面化某一点振幅合成情况(y/n)(默认no)")
if is_flatten=="y":
    _source =  list(map(int, input("该点坐标：（默认[2.5, 6])").split()))
    if not _source or len(_source)!=2:
        _source = [2.5, 6]

is_sub = input("是否振幅随距离衰减(y/n)(默认n)")
if not is_sub:
    is_sub = "n"

if is_video=="y":
    print("正在导出视频,这大概需要一分钟(视频会被存放在本目录下)")


# 设置默认参数
x_min, x_max = -10, 10  # x轴的范围
y_min, y_max = -10, 10  # y轴的范围
x = np.linspace(x_min, x_max, 1000)  # x轴的采样点
y = np.linspace(y_min, y_max, 1000)  # y轴的采样点
X, Y = np.meshgrid(x, y)  # 生成网格点
distance = 0

# 波源的位置




# 分析振幅点位置
# _source1 = (-3, 0)y



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

def total_amplitude(_source, t):
    my_amplitude(_source, source1, "red", t)
    my_amplitude(_source, source2, "blue", t)

def update(t):
    t = t/2
    plt.clf()  # 清除之前的图像，避免叠加显示
    distance = np.sqrt((X - x3)**2 + (Y - y3)**2)
    # distance = np.where(distance>0, distance, 0)
    k = 1 - 1.2*distance/15
    k = np.where(k>0, k, 0)
    if is_sub=="n":
        k = 1
    Z = k*(wave_amplitude(X, Y, t, source1)+wave_amplitude(X, Y, t, source2)) #if t>distance/v else 0
    plt.title('两波的干涉 (时间: {:.2f})'.format(2*t))
    plt.imshow(Z, cmap='RdYlBu', extent=[x_min, x_max, y_min, y_max], origin='lower', vmin=-1.5, vmax=1.5)
    # 添加波源的小黑点
    plt.scatter([source1[0], source2[0]], [source1[1], source2[1]], color='black', s=80)

    # my_amplitude(_source1, source1, "red", t)
    if is_flatten=="y":
        total_amplitude(_source, t)



    return plt

# 创建动画
fig = plt.figure(figsize=(8, 8))
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 60, 0.1), interval=100)

# 导出视频
if is_video=="y":
    writer = FFMpegWriter(fps=10, metadata=dict(artist='lisanndesu'), bitrate=2000000 if high_bite=="y" else 1000)
    ani.save(video_name+".mp4", writer=writer)
    print("成功导出视频，已存放至本程序所在目录下")

# 显示动画
plt.show()

#加clf
#加vmin， vmax
#cos(  +np.pi/2)
#在导出视频时，ani中的interval参数不会影响视频的播放速度
# v和fps同时增大为原来三倍，画面更连续，同时速度不变
# 通过调整合适w，来调整波长