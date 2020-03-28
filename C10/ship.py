"""自定义类：船
"""


class Ship:
    """船类"""

    def __init__(self, name=None):
        """初始化船实例"""
        self.name = name    # 船名
        self.crew = 0       # 船员人数

    def join(self, number):
        """船员加入"""
        self.crew += number
        return self.crew
