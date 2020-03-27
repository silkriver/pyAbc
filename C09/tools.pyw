"""实用工具集
"""
import os
import tkinter as tk
import subprocess as sp
import webbrowser as wb
mytools = {     # 个人工具字典
    "颜色列表": lambda: sp.Popen("python ../C06/colorstable.pyw", shell=True),
    "简易记事本": lambda: sp.Popen("python mynotepad.pyw", shell=True),
    "图片查看器": lambda: sp.Popen("python tkimage.pyw", shell=True),
}
links = {       # 网络链接字典
    "Python官方文档": lambda: wb.open("https://docs.python.org/zh-cn/"),
    "Python包索引": lambda: wb.open("https://pypi.org/"),
    "Spyder官方文档": lambda: wb.open("https://docs.spyder-ide.org/"),
}
index = {       # 分类字典
    "个人工具": mytools,
    "网络链接": links,
}


def main():
    pydir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(pydir)
    root = tk.Tk()
    root.title("实用工具集")
    font = ("Courier", 12)
    for k, v in index.items():  # 迭代所有分类
        label = tk.Label(root, text=k, font=("Courier", 18, "bold"))
        label.pack()
        frame = tk.Frame(root, bd=1)
        r, c = 0, 0             # 网格布局的行列号
        for n, f in v.items():  # 迭代每个分类的所有工具
            button = tk.Button(frame, width=20, font=font, text=n, command=f)
            button.grid(row=r, column=c, sticky="ew", padx=5, pady=5)
            c += 1
            if c > 2:           # 每放三个按钮换一行
                c = 0
                r += 1
        frame.pack(fill=tk.X)
    root.mainloop()


if __name__ == "__main__":
    main()
