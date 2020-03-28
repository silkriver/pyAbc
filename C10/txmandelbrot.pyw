"""绘制曼德布罗分形图
"""
import tkinter as tk
import time


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        # 复数取值范围
        xa, xb, ya, yb = -2.25, 0.75, -1.25, 1.25
        # 显示窗口大小
        x, y = 600, 500
        canvas = tk.Canvas(width=x, height=y)
        canvas.pack()
        self.img = tk.PhotoImage(width=x, height=y)
        canvas.create_image((0, 0), image=self.img, anchor=tk.NW)
        # 计算并显示图像
        t1 = time.process_time()
        pixels = type(self).mandelbrot_image(xa, xb, ya, yb, x, y)
        self.img.put(pixels)
        print("运行耗时：{}秒。".format(time.process_time() - t1))

    @staticmethod
    def mandelbrot_pixel(c):
        """返回曼德布罗平面像素点对应索引号"""
        maxiter = 256
        z = complex(0.0, 0.0)
        for i in range(maxiter):
            z = z * z + c
            if abs(z) >= 2.0:
                return i
        return 256

    @classmethod
    def mandelbrot_image(cls, xa, xb, ya, yb, x, y):
        """返回曼德布罗平面图像字符串"""
        colors = ["#%02x%02x%02x" % (   # 索引号0-255对应不同颜色
                int(255 * ((i / 255) ** 8)) % 64 * 4,
                int(255 * ((i / 255) ** 8)) % 128 * 2,
                int(255 * ((i / 255) ** 8)) % 256) for i in range(255, -1, -1)]
        colors.append("#000000")        # 索引号256对应黑色
        # 计算复平面坐标对应的像素点
        xm = [xa + (xb - xa) * kx / x for kx in range(x)]
        ym = [ya + (yb - ya) * ky / y for ky in range(y)]
        # 生成图像字符串
        return " ".join((("{" + " ".join(
            colors[cls.mandelbrot_pixel(complex(i, j))]
            for i in xm)) + "}" for j in ym))


if __name__ == "__main__":
    App().mainloop()
