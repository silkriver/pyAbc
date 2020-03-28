"""自定义类：特征属性
"""
from ship import Ship


class Cruiseship(Ship):
    """邮轮类"""

    def __init__(self, name=None, tonnage=10000):
        """初始化邮轮类实例"""
        super().__init__(name)
        self._passengers = 0        # 乘客
        self._tonnage = tonnage     # 吨位

    @property                       # 特征属性获取方法
    def passengers(self):
        return self._passengers

    @passengers.setter              # 特征属性设置方法
    def passengers(self, val):
        if val < 0 or val > 10000:
            print("无效的乘客数（应在0～10000之间）")
        else:
            self._passengers = val

    @property
    def tonnage(self):
        return self._tonnage
