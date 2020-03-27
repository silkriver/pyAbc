"""图片查看器
"""
import os
import tkinter as tk
from tkinter.filedialog import askopenfilename
appname = "图片查看器"


def main():
    def show(image):    # 显示图片
        canvas.delete("all")
        cw, ch = canvas.winfo_width(), canvas.winfo_height()
        canvas.create_image((cw//2, ch//2), image=image)

    def c_open():       # 打开图片文件
        nonlocal image
        filename = askopenfilename(
            filetypes=[("图片文件", "*.png *.gif"),])
        if filename:
            root.title(f"{os.path.basename(filename)} - {appname}")
            image = tk.PhotoImage(file=filename)
            show(image)

    def c_zoomin():     # 放大图片
        nonlocal image, x
        if x < 4:
            x += 1
            image = image.zoom(2)
            show(image)

    def c_zoomout():    # 缩小图片
        nonlocal image, x
        if x > 1:
            x -= 1
            image = image.subsample(2)
            show(image)

    root = tk.Tk()
    root.geometry("600x480")
    root.title(appname)
    toolbar = tk.Frame(root, bd=1, relief=tk.RAISED)    # 创建工具栏
    toolbar_open = tk.Button(toolbar, text="打开(Ctrl+O)", command=c_open)
    toolbar_open.pack(side=tk.LEFT)
    toolbar_zoomin = tk.Button(toolbar, text="放大(+)", command=c_zoomin)
    toolbar_zoomin.pack(side=tk.LEFT)
    toolbar_zoomout = tk.Button(toolbar, text="缩小(-)", command=c_zoomout)
    toolbar_zoomout.pack(side=tk.LEFT)
    toolbar.pack(side=tk.TOP, fill=tk.X)
    canvas = tk.Canvas(root)
    image = tk.PhotoImage()
    x = 1   # 图片放大倍数
    canvas.pack(expand=tk.YES, fill=tk.BOTH)
    root.bind('<Control-o>', lambda e: c_open())
    root.bind('<KP_Add>', lambda e: c_zoomin())
    root.bind('<KP_Subtract>', lambda e: c_zoomout())
    tk.mainloop()


if __name__ == "__main__":
    main()
