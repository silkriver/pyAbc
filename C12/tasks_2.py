"""多进程并发执行多个任务
"""
import time
import multiprocessing


def work(tasknum):  # 耗时3秒的工作任务
    t = time.perf_counter()
    print(f"任务{tasknum}开始……")
    time.sleep(3)
    print(f"任务{tasknum}完成！耗时{time.perf_counter() - t}秒。")


def main():     # 在不同进程中执行工作任务
    multiprocessing.Process(target=work, args=(1,)).start()
    multiprocessing.Process(target=work, args=(2,)).start()


if __name__ == "__main__":
    t = time.perf_counter()
    main()
    print(f"主程序耗时{time.perf_counter() - t}秒。")
