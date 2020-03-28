"""生成器：2的正整数次幂"""


def Power2n(n):
    """2的正整数次幂数列生成器"""
    for i in range(1, n + 1):
        yield 2 ** i


if __name__ == "__main__":
    p = Power2n(10)
    print(*p)
