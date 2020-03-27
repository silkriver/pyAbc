"""GUI测试：标签
"""
import tkinter as tk


def main():
    root = tk.Tk()
    root.geometry("500x300")
    # 创建标签并放入窗口的指定位置
    label = tk.Label(root, text="标签文本")
    label.place(x=220, y=120)
    root.mainloop()


if __name__ == "__main__":
    main()
