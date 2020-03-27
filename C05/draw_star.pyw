"""自定义的海龟绘图函数集
"""
import turtle as tt


def star5p(x, y, size=20, angle=0):
    """在指定位置画一颗五角星
    """
    tt.color("white")
    tt.penup()
    tt.setpos(x, y)     # 起点坐标
    tt.right(angle)     # 倾角
    tt.begin_fill()     # 开始填充
    for _ in range(5):
        tt.forward(size)
        tt.left(72)
        tt.forward(size)
        tt.right(144)
    tt.end_fill()


def test():
    """测试绘图函数：随机画十颗五角星
    """
    from random import randint
    tt.setup(width=720, height=480, startx=None, starty=None)
    tt.hideturtle()
    tt.speed(0)
    tt.bgcolor("purple")
    tt.penup()
    for _ in range(10):
        x = randint(-300, 300)
        y = randint(-200, 200)
        s = randint(10, 30)
        a = randint(0, 72)
        star5p(x, y, s, a)  # 带参数调用五角星函数
    tt.done()
    tt.bye()


if __name__ == "__main__":  # 运行模块时调用测试绘图函数
    test()
