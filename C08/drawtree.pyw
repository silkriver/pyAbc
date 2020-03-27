"""绘制勾股树（Pythagoras Tree）并保存为EPS图形文件
"""
import turtle as tt
# 可设置使用随机颜色绘制正方形，参考被注释掉的代码
# import random


def ptree(ax, ay, bx, by, depth=0):
    """以递归方式绘制勾股树
    """
    if depth > 0:
        # 使用公式计算端点坐标
        dx, dy = bx - ax, ay - by
        x3, y3 = bx - dy, by - dx
        x4, y4 = ax - dy, ay - dx
        x5, y5 = x4 + (dx - dy) / 2, y4 - (dx + dy) / 2
        # r = random.randint(1, 255)
        # g = random.randint(1, 255)
        # b = random.randint(1, 255)
        # tt.color(r, g, b)
        tt.goto(ax, ay)
        tt.pendown()
        tt.begin_fill()
        for x, y in ((bx, by), (x3, y3), (x4, y4), (ax, ay)):
            tt.goto(x, y)
        tt.end_fill()
        tt.penup()
        ptree(x4, y4, x5, y5, depth - 1)
        ptree(x5, y5, x3, y3, depth - 1)


def main():
    tt.hideturtle()
    tt.speed(0)
    tt.color("red", "yellow")
    # tt.colormode(255)
    tt.penup()
    ptree(50, -200, -50, -200, depth=8)
    # 将图形保存为EPS文件
    cv = tt.getcanvas()
    cv.postscript(file="ptree.eps", colormode="color")
    tt.done()
    tt.bye()


if __name__ == "__main__":
    main()
