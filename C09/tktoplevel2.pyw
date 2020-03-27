"""多窗口管理：层级关系
"""
import tkinter as tk


def top(parent):    # 定义从属于指定父窗口的子窗口
    x, y = parent.winfo_x(), parent.winfo_y()
    win = tk.Toplevel(parent)
    win.geometry(f"360x200+{x+20}+{y+5}")
    label1 = tk.Label(win, text=f"当前窗口ID：{id(win)}", font=(None, 16))
    label1.pack()
    label2 = tk.Label(win, text=f"父窗口ID：{id(parent)}", font=(None, 18))
    label2.pack()
    # 添加按钮，点击时打开子窗口
    button = tk.Button(win, text="打开子窗口", command=lambda: top(win))
    button.pack()


def main():
    root = tk.Tk()
    root.title("多窗口管理：层级关系")
    root.geometry("400x240")
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    label = tk.Label(
        root, height=3, text=f"根窗口ID：{id(root)}", font=(None, 18, "bold"))
    label.grid(row=0, column=0, columnspan=2)
    button1 = tk.Button(root, text="1号窗口", command=lambda: top(root))
    button1.grid(row=1, column=0, ipadx=10)
    button2 = tk.Button(root, text="2号窗口", command=lambda: top(root))
    button2.grid(row=1, column=1, ipadx=10)
    root.mainloop()


if __name__ == "__main__":
    main()
