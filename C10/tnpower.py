"""迭代器：2的正整数次幂"""


class Power2n:
    """2的正整数次幂数列迭代器类"""

    def __init__(self, n):
        self.n = n          # 数列长度
        self.cur = 1        # 当前幂次

    def __iter__(self):     # 可迭代对象必须实现__iter__方法来返回迭代器
        return self

    def __next__(self):     # 迭代器必须实现__next__方法来返回下一个元素
        if self.n >= self.cur:
            result = 2 ** self.cur
            self.cur += 1
            return result
        else:
            raise StopIteration()


if __name__ == "__main__":
    p = Power2n(10)
    print(*p)
