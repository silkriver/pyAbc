"""测试画布
"""
import tkinter as tk


def main():
    root = tk.Tk()
    root.title("测试画布")
    root.geometry("400x220")
    canvas = tk.Canvas(root, bg="white")    # 创建画布
    canvas.create_line(                     # 在画布上添加连续线段
        60, 60, 160, 60, 110, 150, 60, 60,
        dash=(5, 2), width=2, fill="#009")
    canvas.pack(expand=tk.YES, fill=tk.BOTH)
    root.mainloop()


if __name__ == "__main__":
    main()
