"""定时批量下载图片
"""
import os
import sys
import time


def main():
    pydir = os.path.dirname(os.path.abspath(__file__))
    base = os.path.split(pydir)[0]
    sys.path.insert(0, base)        # 将练习项目主目录插入模块搜索目录列表
    from C11.webcrawler import Crawler
    while True:
        c = Crawler()
        links = c.getlinks("国画")
        for i in links:
            c.savefile(i)
        print(f"本轮任务结束，共下载{c.cnt}个文件")
        print("进入休眠……")
        for _ in range(3600):       # 休眠一小时
            time.sleep(1)


if __name__ == "__main__":
    main()
