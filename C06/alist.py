"""数字排序
输入以空格分隔的任意多个整数，按降序排列以空格分隔输出（注意末尾不带空格）
"""


def main():
    s = input()
    alist = s.split()               # 将输入内容拆分为字符串列表
    alist = list(map(int, alist))   # 对列表项应用int函数得到对应的整数列表
    alist.sort(reverse=True)        # 列表原地排序
    result = ""
    for i in alist[:-1]:            # 拼接列表元素带空格
        result += str(i) + " "
    result += str(alist[-1])        # 拼接末尾元素不带空格
    print(result)
    # print(*alist)                 # 输出结果的更好方法


if __name__ == "__main__":
    main()
