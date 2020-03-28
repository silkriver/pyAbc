"""绘制不对称的勾股树
"""
import tkinter as tk
import math


class App(tk.Tk):
    def __init__(self):         # 初始化界面
        super().__init__()
        self.geometry("800x500")
        self.canvas = tk.Canvas(background="white")
        self.canvas.pack(fill=tk.BOTH, expand=1)
        block = [(400, 350), (500, 350), (500, 450), (400, 450)]
        self.ptree(block, 8)

    @staticmethod               # 静态方法：平移多边形
    def move(points, x, y):
        new_points = []
        for x_old, y_old in points:
            x_new = x_old - x
            y_new = y_old - y
            new_points.append([x_new, y_new])
        return new_points

    @staticmethod               # 静态方法：旋转和缩放多边形
    def rotate(points, angle, axis, scale=1):
        angle = math.radians(angle)
        cos_val = math.cos(angle)
        sin_val = -math.sin(angle)
        ax, ay = axis
        new_points = []
        for x_old, y_old in points:
            x_old -= ax
            y_old -= ay
            x_new = (x_old * cos_val - y_old * sin_val) * scale
            y_new = (x_old * sin_val + y_old * cos_val) * scale
            new_points.append([x_new + ax, y_new + ay])
        return new_points

    def ptree(self, block, depth):  # 递归绘制勾股树的构成单元
        if depth:
            # 下方块：边长1
            self.canvas.create_polygon(block, outline="red", fill="yellow")
            # 左上方块：边长4/5，以左下角为轴心左转37度
            lb = self.move(
                block, block[3][0] - block[0][0], block[3][1] - block[0][1])
            lb = App.rotate(lb, 37, lb[3], 0.8)
            self.ptree(lb, depth - 1)
            # 右上方块：边长3/5，以右下角为轴心右转53度
            rb = self.move(
                block, block[3][0] - block[0][0], block[3][1] - block[0][1])
            rb = App.rotate(rb, -53, rb[2], 0.6)
            self.ptree(rb, depth - 1)


if __name__ == '__main__':
    App().mainloop()
