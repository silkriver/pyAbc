"""测试画布：对象的移动
"""
import tkinter as tk
import math


def main():
    def leftMove(e):    # 左移小球
        if canvas.coords(ball)[0] > 0:
            canvas.move(ball, -10, 0)

    def rightMove(e):   # 右移小球
        if canvas.coords(ball)[2] < 500:
            canvas.move(ball, 10, 0)

    def upMove(e):      # 上移小球
        if canvas.coords(ball)[1] > 0:
            canvas.move(ball, 0, -10)

    def downMove(e):    # 下移小球
        if canvas.coords(ball)[3] < 280:
            canvas.move(ball, 0, 10)

    root = tk.Tk()
    root.title("测试画布：对象的移动")
    root.geometry("500x280")
    canvas = tk.Canvas(root, bg="white")
    ball = canvas.create_oval(230, 120, 270, 160, fill="red")
    canvas.pack(expand=tk.YES, fill=tk.BOTH)
    # 按方向键时调用相应的函数
    root.bind('<Left>', leftMove)
    root.bind('<Right>', rightMove)
    root.bind('<Up>', upMove)
    root.bind('<Down>', downMove)
    root.mainloop()


if __name__ == "__main__":
    main()
