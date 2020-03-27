import turtle as tt
from random import randint
tt.speed(0)     # 绘图速度为最快
tt.width(2)     # 线宽为2个像素
tt.bgcolor("black")     # 背景色为黑色
tt.setpos(-25, 25)      # 改变初始位置，这可以让图案居中
tt.colormode(255)       # 颜色模式为真彩色
for i in range(500):    # 连续画500条线段
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    tt.pencolor(r, g, b)    # 画笔颜色每次随机
    tt.forward(50 + i)      # 每一条线段比前一条长1个像素
    tt.right(91)
tt.done()
tt.bye()
