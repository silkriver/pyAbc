"""GUI测试：多个部件用grid方法布局
"""
import tkinter as tk


def main():
    root = tk.Tk()
    root.title("多个部件用grid方法布局")
    label = tk.Label(root, text="标签文本")
    label.grid(row=0, column=0)                 # 标签放在0行0列
    button = tk.Button(root, text="按钮文本")
    button.grid(row=0, column=1)                # 按钮放在0行1列
    entry = tk.Entry(root, width=50)
    entry.grid(row=1, column=0, columnspan=2)   # 输入框放在1行0列横跨两列
    text = tk.Text(root, width=50, height=12, background="wheat")
    text.grid(row=2, column=0, columnspan=2)    # 文本区放在2行1列
    root.mainloop()


if __name__ == "__main__":
    main()
