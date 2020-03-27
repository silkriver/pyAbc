"""数字组合
用四个数字0、1、2、3组合出所有互不相同且无重复数字的三位数，从小到大打印输出
"""


def main():
    digits = [0, 1, 2, 3]
    result = []
    # 使用三重循环列出所有可能的三个数字组合
    for i in digits:
        for j in digits:
            for k in digits:
                # 根据数字组合创建集合，确定满足条件的三位数加入结果列表
                if len(set([i, j, k])) == 3 and i != 0:
                    result.append(i * 100 + j * 10 + k)
    # 通过序列切片每行打印10项
    for i in range(len(result) // 10 + 1):
        print(*result[i * 10: i * 10 + 10])


if __name__ == "__main__":
    main()
