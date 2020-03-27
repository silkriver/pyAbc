"""GUI测试：按钮点击事件处理
"""
import tkinter as tk


def main():
    def save():
        # 定义保存文件函数
        if entry.get():
            name = entry.get()
            with open(name, "w", encoding="utf-8") as f:
                f.write(text.get("1.0", "end-1c"))
            label["text"] = "文件已保存"
    root = tk.Tk()
    root.title("按钮点击事件处理")
    label = tk.Label(root, text="请点击保存文件按钮")
    label.grid(row=0, column=0)
    # 指定点击按钮时执行save函数
    button = tk.Button(root, text="保存文件", command=save)
    button.grid(row=0, column=1)
    entry = tk.Entry(root, width=50)
    entry.insert(0, "info.txt")
    entry.grid(row=1, column=0, columnspan=2)
    text = tk.Text(root, width=50, height=12, background="wheat")
    text.grid(row=2, column=0, columnspan=2)
    text.focus()
    root.mainloop()


if __name__ == "__main__":
    main()
