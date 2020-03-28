"""多线程并发执行多个任务
"""
import time
import threading
import sys


def work(tasknum):  # 耗时3秒的工作任务
    t = time.perf_counter()
    sys.stdout.write(f"任务{tasknum}开始……\n")
    time.sleep(3)
    sys.stdout.write(f"任务{tasknum}完成！耗时{time.perf_counter() - t}秒。\n")


def main():     # 在不同进程中执行工作任务
    threading.Thread(target=work, args=(1,)).start()
    threading.Thread(target=work, args=(2,)).start()


if __name__ == "__main__":
    t = time.perf_counter()
    main()
    print(f"主程序耗时{time.perf_counter() - t}秒。")
