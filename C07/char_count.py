"""字符统计
执行脚本并从标准输出读取文本，统计其中每个英文字母出现的次数（不区分大小写）
"""
import subprocess as sp
import string


def main():
    # 在子进程中运行this模块
    p = sp.Popen("python -m this", shell=True, text=True, stdout=sp.PIPE)
    d = {}
    while True:
        line = p.stdout.readline()  # 从子进程的标准输出读取一行字符串
        if not line:                # 读到空值则中断循环结束读取
            break
        for c in line.lower():
            if c in string.ascii_letters:   # 如果字符为英文字母则更新频度字典
                d.setdefault(c, 0)
                d[c] += 1
    # 根据频度字典键值对视图生成按值大小降序排列的二元组列表
    result = sorted(d.items(), key=lambda i: i[1], reverse=True)
    cnt = 0
    for k, v in result:     # 打印键值对，每行五项
        print(f"{k}: {v:>2}", end="\t")
        if cnt % 5 == 4:
            print()
        cnt += 1
    print()


if __name__ == "__main__":
    main()
