import turtle as tt
tt.speed(0)                      # 绘图速度设为最快
tt.color("red", "yellow")        # 红色线条，黄色填充
tt.begin_fill()
cnt = 0
while cnt < 36:         # 外层循环36次绘制多芒星
    tt.forward(200)
    if cnt % 2 > 0:     # 在外层循环的奇数次执行内层循环绘制五角星
        cnt2 = 0
        while cnt2 < 5:
            tt.forward(10)
            tt.right(144)
            cnt2 += 1
    tt.left(170)
    cnt += 1
tt.end_fill()
tt.hideturtle()
tt.done()
tt.bye()  # 在 Spyder 中运行时应当调用bye函数来结束海龟绘图
