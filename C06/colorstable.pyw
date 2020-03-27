"""显示颜色表
"""
import turtle as tt


def showcolor(x, y, color="black"):
    """显示颜色块和颜色名
    """
    tt.speed(0)
    tt.color(color)     # 显示颜色块
    tt.penup()
    tt.setpos(x, y)
    tt.begin_fill()
    for _ in range(4):
        tt.forward(16)
        tt.left(90)
    tt.forward(18)
    tt.end_fill()
    tt.color("black")   # 显示颜色名
    tt.write(color)


def showcolors():
    """显示所有颜色
    """
    from colorsinfo import COLORS
    tt.setup(1200, 820)
    tt.setworldcoordinates(0, -810, 1200, 10)
    tt.hideturtle()
    tt.speed(0)
    tt.tracer(0)    # 关闭动效以减少耗时
    tt.penup()
    row = 0         # 输出颜色表，每列45行
    col = 0
    for color in COLORS:
        showcolor(col * 100, row * -18, color)
        row += 1
        if row > 45:
            row = 0
            col += 1
    tt.done()
    tt.bye()


if __name__ == "__main__":
    showcolors()
