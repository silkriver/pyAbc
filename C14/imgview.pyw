"""基于PyQt5的图片查看器
"""
from PyQt5.QtWidgets import QApplication
from main import Main       # 主窗体模块
from multi import Multi     # 多图片窗体模块


class Controller:           # 窗体切换控制器类
    def __init__(self):
        self.main = Main()
        self.multi = None

    def show_main(self, imgfile=None):    # 显示主窗体
        self.main.signal.connect(self.show_multi)
        if self.multi:
            self.multi.hide()
        self.main.show()
        if imgfile:
            self.main.openImage(imgfile)

    def show_multi(self, imgdir):   # 显示多图片窗体
        if not self.multi:
            self.multi = Multi(".")
        self.multi.signal.connect(self.show_main)
        self.main.hide()
        self.multi.show()
        self.multi.openDir(imgdir)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    controller = Controller()
    controller.show_main()
    sys.exit(app.exec_())
