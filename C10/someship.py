"""自定义类：类方法与静态方法
"""
from ship import Ship


class Warship(Ship):
    """战舰类"""
    number = 0  # 类属性：战舰数量

    @classmethod
    def build(cls, number):
        """建造多艘战舰"""
        insts = []
        for _ in range(number):
            cls.number += 1
            inst = cls()
            inst.number = f"{cls.number:03}"
            insts.append(inst)
        return insts

    @staticmethod
    def test():
        """测试战舰类"""
        fleet = Warship.build(3)
        for i in fleet:
            print(f"新建战舰：舷号{i.number}")
        print(f"现有战舰共计{Warship.number}艘。")


if __name__ == "__main__":
    Warship.test()
