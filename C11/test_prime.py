"""测试质数模块
"""
import unittest
import prime


class TestPrime(unittest.TestCase):
    def test_isprime(self):     # 测试isprime函数
        self.assertTrue(prime.isprime(37))
        self.assertFalse(prime.isprime(37.5))

    def test_genprimes(self):   # 测试genprimes函数
        code = [x for x in prime.genprimes(1, 50)]
        out = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        self.assertEqual(code, out)
