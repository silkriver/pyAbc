from random import randint
import turtle as tt
tt.setup(width=800, height=450, startx=None, starty=None)  # 设置窗口大小
tt.hideturtle()     # 隐藏画笔图标
tt.color("blue")    # 画笔颜色为蓝色
tt.penup()          # 抬起画笔，移动时不画线
tt.setpos(-300, 0)  # 设置初始位置
myfont = ("黑体", 16, "normal")  # 定义字体
target = randint(1, 100)
tt.write("我想了一个1到100之间的整数，请你猜猜看吧：", font=myfont)
guess = 0
answer = ""
cnt = 0
while guess != target:
    cnt += 1
    # 使用对话框获取用户输入
    guess = tt.simpledialog.askinteger("猜数游戏", "请输入一个整数：")
    if guess == target:
        answer = f"你猜对了！这个数是{target}，你猜了{cnt}次。"
    elif not guess:     # 用户没有输入数字则中断循环
        tt.clear()      # 清空画布以便输出新文本
        tt.write("你放弃了，游戏结束。", font=myfont)
        break
    elif guess > target:
        answer = f"{guess}太大了，再猜一次："
    else:
        answer = f"{guess}太小了，再猜一次："
    tt.clear()
    tt.write(answer, font=myfont)
tt.done()
tt.bye()
