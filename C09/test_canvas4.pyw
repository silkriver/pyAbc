"""测试画布：动画效果
"""
import tkinter as tk
from random import randint


def main():
    def randMove(shape, tx=1, ty=1):    # 随机移动shape
        pos = canvas.coords(shape)      # shape在画布中的坐标
        if pos[0] < 0 or pos[2] > 500:  # shape坐标超出达画布边缘则反向
            tx = -tx
        if pos[1] < 0 or pos[3] > 300:
            ty = -ty
        # 随机设置位移量并移动形状
        dx = randint(0, 5) * tx
        dy = randint(0, 5) * ty
        canvas.move(shape, dx, dy)
        # 50毫秒之后再次调用randMove函数
        canvas.after(50, lambda: randMove(shape, tx, ty))

    root = tk.Tk()
    root.title("测试画布：动画效果")
    root.resizable(False, False)
    canvas = tk.Canvas(root, width=500, height=300, bg="white")
    canvas.pack(expand=tk.YES, fill=tk.BOTH)
    ball = canvas.create_oval(0, 0, 30, 30, fill="red")
    randMove(ball)
    root.mainloop()


if __name__ == "__main__":
    main()
