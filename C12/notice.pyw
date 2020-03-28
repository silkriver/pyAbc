"""整点提醒
"""
import tkinter as tk
import time
from datetime import datetime, timedelta


def notice(hour):   # 弹出提醒窗口
    root = tk.Tk()
    root.title("整点提醒")
    root.geometry("400x160")
    label = tk.Label(root, text=f"现在时间：{hour}点整", font=("Courier", 20))
    label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    root.after(30000, root.destroy)     # 30000毫秒后销毁窗口
    root.lift()
    root.mainloop()


if __name__ == "__main__":
    while True:
        dt = datetime.now() + timedelta(hours=1)    # 下一个整点执行任务
        dt = dt.replace(minute=0, second=0, microsecond=0)
        while datetime.now() < dt:
            time.sleep(1)
        notice(dt.hour)
