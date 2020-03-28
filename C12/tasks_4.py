"""多协程并发执行多个任务
"""
import time
import asyncio


async def work(tasknum):    # 耗时3秒的异步工作任务
    t = time.perf_counter()
    print(f"任务{tasknum}开始……")
    await asyncio.sleep(3)
    print(f"任务{tasknum}完成！耗时{time.perf_counter() - t}秒。")


async def main():   # 异步执行两个工作任务
    tasks = asyncio.gather(work(1), work(2))
    await tasks


if __name__ == "__main__":
    t = time.perf_counter()
    loop = asyncio.get_event_loop()                 # 获取事件循环
    asyncio.run_coroutine_threadsafe(main(), loop)  # 运行主协程函数
    # 直接执行脚本时用下面这句运行主协程函数
    # loop.run_until_complete(main())
    # 在Python 3.7中用下面这一句即可，不必再去获取事件循环
    # asyncio.run(main())
    print(f"主程序耗时{time.perf_counter() - t}秒。")
