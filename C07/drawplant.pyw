"""绘制使用L系统模拟的分形植物
"""
import turtle as tt


def generate(n, result="[X]"):
    """传入迭代次数和初始值返回结果值
    """
    rules = {
        "X": "F-[[X]+X]+F[+FX]-X",
        "F": "FF"}
    # 在迭代中使用规则字典对字符串执行查找替换
    for _ in range(n):
        for k, v in rules.items():
            result = result.replace(k, v)
    return result


def draw(cmds, size=2):
    """传入结果值和线段长度绘制图形
    """
    stack = []          # 模拟栈的列表
    for cmd in cmds:    # 根据命令字符执行相应操作
        if cmd == "F":
            tt.forward(size)
        elif cmd == "-":
            tt.left(25)
        elif cmd == "+":
            tt.right(25)
        elif cmd == "X":
            pass
        elif cmd == "[":
            stack.append((tt.position(), tt.heading()))
        elif cmd == "]":
            position, heading = stack.pop()
            tt.penup()
            tt.setposition(position)
            tt.setheading(heading)
            tt.pendown()
    tt.update()


def main():
    tt.hideturtle()
    tt.tracer(0)
    tt.color("green")
    tt.speed(0)
    tt.left(60)
    tt.pensize(2)
    tt.penup()
    tt.goto(-tt.window_width()/3, -tt.window_height()/3)
    tt.pendown()
    plant = generate(6)
    draw(plant)
    tt.exitonclick()    # 在窗口上单击鼠标时退出
    tt.bye()


if __name__ == "__main__":
    main()
