"""桌面计算器
"""
import tkinter as tk


class Calc(tk.Tk):
    """计算器窗体类"""
    btnlist = [
        "C", "M->", "->M", "/",
        "7", "8", "9", "*",
        "4", "5", "6", "-",
        "1", "2", "3", "+",
        "+/-", "0", ".", "="]

    def __init__(self):
        """初始化计算器窗体"""
        super().__init__()
        self.title("桌面计算器")
        self.memory = 0     # 暂存数值
        self.entry = tk.Entry(
            self, width=24, borderwidth=4, relief=tk.SUNKEN, justify="right",
            bg="LightCyan1", font=("Consolas", 18))
        self.entry.pack(padx=12, pady=(12, 0))
        frame = tk.Frame(self)
        frame.pack(pady=8)
        r, c = 0, 0
        for b in self.__class__.btnlist:
            button = tk.Button(
                frame, text=b, width=5, pady=10,
                command=lambda x=b: self.click(x))
            button.grid(row=r, column=c, padx=8, pady=6)
            c += 1
            if c > 3:
                c = 0
                r += 1
        # 按下任意键时执行keypress方法
        self.bind_all("<Key>", self.keypress)

    def keypress(self, event):
        """处理键盘事件"""
        key = "=" if event.char == "\r" else event.char.upper()
        if key in self.__class__.btnlist:
            self.click(key)

    def click(self, key):
        """处理鼠标点击"""
        if key == "=":      # 输出结果
            exp = self.entry.get()
            if exp:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(eval(exp)))
        elif key == "C":    # 清空输入框
            self.entry.delete(0, tk.END)
        elif key == "->M":  # 存入数值
            self.memory = self.entry.get()
            self.title("M=" + self.memory)
        elif key == "M->":  # 取出数值
            if self.memory:
                self.entry.insert(tk.END, self.memory)
        elif key == "+/-":  # 正负翻转
            if self.entry.get()[0] == "-":
                self.entry.delete(0)
            else:
                self.entry.insert(0, "-")
        else:               # 其他键
            self.entry.insert(tk.END, key)


if __name__ == "__main__":
    Calc().mainloop()
