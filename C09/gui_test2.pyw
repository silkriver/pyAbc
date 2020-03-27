"""GUI测试：多个部件用pack方法布局
"""
import tkinter as tk


def main():
    root = tk.Tk()
    root.title("多个部件用pack方法布局")
    label = tk.Label(root, text="标签文本")
    label.pack()
    button = tk.Button(root, text="按钮文本")
    button.pack(side=tk.BOTTOM)     # 按钮放在窗口底部
    entry = tk.Entry(root, width=50)
    entry.pack()
    text = tk.Text(root, width=50, height=12, background="wheat")
    text.pack()
    root.mainloop()


if __name__ == "__main__":
    main()
