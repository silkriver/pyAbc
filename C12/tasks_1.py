"""多个任务依次执行
"""
import time


def work(tasknum):  # 耗时3秒的工作任务
    t = time.perf_counter()
    print(f"任务{tasknum}开始……")
    time.sleep(3)
    print(f"任务{tasknum}完成！耗时{time.perf_counter() - t}秒。")


def main():     # 依次执行两个工作任务
    work(1)
    work(2)


if __name__ == "__main__":
    t = time.perf_counter()
    main()
    print(f"主程序耗时{time.perf_counter() - t}秒。")
