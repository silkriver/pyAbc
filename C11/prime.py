"""质数模块
示例：
>>> isprime(1)
False
>>> [x for x in genprimes(1, 50)]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
"""
import math


def isprime(n):
    """检测数字是否为质数
    示例：
    >>> isprime(2)
    True
    >>> isprime(98)
    False
    """
    if type(n) == int and n > 1:
        return all(n % x for x in range(2, int(math.sqrt(n) + 1)))
    else:
        return False


def genprimes(start, end):
    """返回指定区间内质数的生成器
    示例：
    >>> genprimes(1, 100)
    <generator object genprimes.<locals>.<genexpr> at 0x...>
    """
    return (x for x in range(start, end) if isprime(x))


if __name__ == "__main__":
    import doctest  # 导入doctest模块执行文档测试
    doctest.testmod(optionflags=doctest.ELLIPSIS)
