"""测试画布：各种绘图方法
"""
import tkinter as tk
import math


def main():
    root = tk.Tk()
    root.title("测试画布：各种绘图方法")
    root.geometry("500x280")
    canvas = tk.Canvas(root, bg="white")
    # 画矩形方法
    canvas.create_rectangle(30, 30, 120, 80, fill="#ff0", outline="#009")
    # 画椭圆方法（也可用于画圆）
    canvas.create_oval(
        160, 30, 230, 100, outline="#f33", fill="#3f3", width=2)
    # 画扇形方法
    canvas.create_arc(260, 30, 330, 100, start=0, extent=135, width=2)
    points = [360, 30, 410, 50, 480, 90, 400, 90, 430, 80]
    # 画多边形方法
    canvas.create_polygon(points, outline="#333", fill="#f0c")
    image = tk.PhotoImage(width=400, height=100)    # 定义图像部件
    canvas.create_image((260, 160), image=image)    # 创建位图方法
    for x in range(500):                            # 在图像部件中添加像素点
        y = int(50 + 50 * math.sin(x/10))
        image.put("{red red} {red red}", (x, y))
    text = "Beautiful is better than ugly"
    # 创建文本方法
    canvas.create_text((260, 240), font=(None, 20, "bold"), text=text)
    canvas.pack(expand=tk.YES, fill=tk.BOTH)
    root.mainloop()


if __name__ == "__main__":
    main()
