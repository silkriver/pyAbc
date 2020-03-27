"""多窗口管理
"""
import tkinter as tk


def top(num):   # 定义顶层窗口
    win = tk.Toplevel()
    win.geometry("360x200")
    label = tk.Label(win, text=f"{num}号窗口", font=(None, 18))
    label.pack()


def main():
    root = tk.Tk()
    root.geometry("400x240")
    # 定义网格布局的列权重以保持两列宽度相同
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    label = tk.Label(root, height=3, text="多窗口管理", font=(None, 18, "bold"))
    label.grid(row=0, column=0, columnspan=2)
    # 添加两个按钮，点击时分别打开不同的顶层窗口
    button1 = tk.Button(root, text="1号窗口", command=lambda: top(1))
    button1.grid(row=1, column=0, ipadx=10)
    button2 = tk.Button(root, text="2号窗口", command=lambda: top(2))
    button2.grid(row=1, column=1, ipadx=10)
    root.mainloop()


if __name__ == "__main__":
    main()
