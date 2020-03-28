"""自定义类：船类的子类
"""
from ship import Ship


class Airship(Ship):
    """飞艇类"""

    def __init__(self, name=None):
        """初始化飞艇类实例"""
        super().__init__(name)
        self.passengers = 0  # 乘客


class Starship(Ship):
    """星舰类"""
    count = 0  # 类属性：星舰类实例总数

    def __init__(self, name=None, shipclass=None):
        """初始化星舰类实例"""
        super().__init__(name)
        self.shipclass = shipclass  # 舰级
        self.__class__.count += 1

    def __del__(self):
        """删除星舰类实例"""
        self.__class__.count -= 1
