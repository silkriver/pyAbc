"""简易记事本
"""
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import askokcancel, showinfo
appname = "简易记事本"


def main():
    def c_new():    # 新建文件
        var_filename.set("")
        root.title(f"未命名 - {appname}")
        text.delete(1.0, "end")

    def c_open():   # 打开文件
        filename = askopenfilename()
        if filename:
            var_filename.set(filename)
            root.title(f"{filename} - {appname}")
            with open(filename) as f:
                text.delete(1.0, "end")
                text.insert(1.0, f.read())

    def c_save():   # 保存文件
        filename = var_filename.get()
        if not filename:
            filename = asksaveasfilename()
        if filename:
            var_filename.set(filename)
            root.title(f"{filename} - {appname}")
            with open(filename, "w") as f:
                content = text.get(1.0, "end-1c")
                f.write(content)

    def c_exit():   # 退出
        if askokcancel("退出", "你确定要退出吗？"):
            root.destroy()

    def c_about():  # 关于
        showinfo(f"关于{appname}", "小巧轻便的文本编辑器")

    root = tk.Tk()
    root.title(f"未命名 - {appname}")
    root.protocol("WM_DELETE_WINDOW", c_exit)   # 关闭窗口时执行c_exit函数
    var_filename = tk.StringVar(root)           # 字符串变量
    menu = tk.Menu(root)                        # 创建菜单栏
    root["menu"] = menu
    m_file = tk.Menu(menu)
    menu.add_cascade(label="文件", menu=m_file)
    m_file.add_command(label="新建", command=c_new)
    m_file.add_command(label="打开...", command=c_open)
    m_file.add_command(label="保存", command=c_save)
    m_file.add_separator()
    m_file.add_command(label="退出", command=c_exit)
    m_help = tk.Menu(menu)
    menu.add_cascade(label="帮助", menu=m_help)
    m_help.add_command(label="关于...", command=c_about)
    text = ScrolledText(root, width=100, height=40)
    text.pack()
    text.focus()
    root.mainloop()


if __name__ == "__main__":
    main()
