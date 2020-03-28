"""并发版定时批量下载图片
"""
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor


def main():
    pydir = os.path.dirname(os.path.abspath(__file__))
    base = os.path.split(pydir)[0]
    sys.path.insert(0, base)
    from C11.webcrawler import Crawler
    while True:
        t = time.perf_counter()
        c = Crawler()
        links = c.getlinks("高清动漫")
        # 使用线程池执行器并发执行30个下载任务
        with ThreadPoolExecutor(max_workers=30) as executor:
            executor.map(c.savefile, links, timeout=5)
        print(f"本轮任务结束，共下载{c.cnt}个文件")
        print(f"共耗时{time.perf_counter() - t}秒，进入休眠……")
        for _ in range(3600):   # 休眠一小时
            time.sleep(1)


if __name__ == "__main__":
    main()
