import turtle as tt
r = 200      # 大圆半径200个像素
tt.width(3)  # 线宽3个像素
tt.color("black", "black")  # 黑色线条黑色填充
tt.begin_fill()             # 开始填充
tt.circle(r/2, 180)         # 从中心开始逆时针画黑色区头部的半圆
tt.circle(r, 180)           # 画黑色区左边的大半圆
tt.left(180)                # 在黑色区尾部调头朝右
tt.circle(-r/2, 180)        # 顺时针画半圆完成黑色区绘制
tt.end_fill()               # 结束填充黑色区
tt.left(90)                 # 在中心左转朝上
tt.up()                     # 抬起画笔
tt.forward(r*0.35)          # 跳到黑色区内部
tt.right(90)                # 右转朝右
tt.down()                   # 放下画笔
tt.color("black", "white")  # 黑色线条白色填充
tt.begin_fill()
tt.circle(r*0.15)           # 画出黑色区内部的白色小圆
tt.end_fill()
tt.left(90)                 # 左转朝上
tt.up()
tt.forward(r*0.65)          # 跳到大圆的上边缘
tt.down()
tt.right(90)                # 右转朝右
tt.circle(-r, 180)          # 顺时针画白色区右边的大半圆
tt.right(90)                # 右转朝上
tt.up()
tt.forward(r*0.35)          # 跳到白色区内部
tt.right(90)
tt.down()
tt.color("white", "black")
tt.begin_fill()
tt.circle(r*0.15)           # 画出白色区内部的黑色小圆
tt.end_fill()
tt.hideturtle()  # 隐藏海龟图标
tt.done()        # 完成绘图
