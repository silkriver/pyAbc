"""银行列表排序
按市值从大到小输出保存在列表中的银行信息
"""
banklist = [
    "摩根大通", 3909.34, "美国银行", 3253.31, "富国银行", 3080.13,
    "工商银行", 3452.14, "建设银行", 2573.99
]


def main():
    names = banklist[::2]               # 切片得到名称列表
    values = banklist[1::2]             # 切片得到市值列表
    pairs = list(zip(names, values))    # 聚合得到由名称市值元组构成的列表
    pairs.sort(key=lambda i: i[1], reverse=True)    # 列表按市值原地排序
    print("银行名称  |  市值(美元)")                  # 输出结果
    print("-" * 22)
    for name, value in pairs:
        print(f"{name:6}|{value:>9}亿")


if __name__ == "__main__":
    main()
