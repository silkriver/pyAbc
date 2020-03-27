"""绘制方块螺旋图案
"""
import tkinter as tk
import math
from random import randint


def main():
    def rotate(points, angle, axis):    # 旋转任意多边形
        angle = math.radians(angle)     # 通过三角函数进行端点变换
        cos_val = math.cos(angle)
        sin_val = -math.sin(angle)
        ax, ay = axis
        new_points = []
        for x_old, y_old in points:
            x_old -= ax
            y_old -= ay
            x_new = x_old * cos_val - y_old * sin_val
            y_new = x_old * sin_val + y_old * cos_val
            new_points.append([x_new + ax, y_new + ay])
        return new_points

    root = tk.Tk()
    root.resizable(False, False)
    canvas = tk.Canvas(root, width=640, height=480, bg="white")
    canvas.pack(expand=tk.YES, fill=tk.BOTH)
    # 定义初始正方形端点
    s = [[310, 230], [330, 230], [330, 250], [310, 250]]
    # 循环绘制150个正方形
    for i in range(0, 300, 2):
        points = [
            [s[0][0] - i, s[0][1] - i],
            [s[1][0] + i, s[1][1] - i],
            [s[2][0] + i, s[2][1] + i],
            [s[3][0] - i, s[3][1] + i],
        ]
        points = rotate(points, i, (320, 240))
        r = randint(0, 15)
        g = randint(0, 15)
        b = randint(0, 15)
        color = "#%x%x%x" % (r, g, b)
        canvas.create_polygon(points, outline=color, fill="", width=2)
    root.mainloop()


if __name__ == "__main__":
    main()
