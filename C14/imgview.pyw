"""基于PyQt5的图片查看器
"""
from os.path import basename
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import (
    QAction, QApplication, QFileDialog, QLabel, QMainWindow, QMenu,
    QMessageBox, QScrollArea)


class Main(QMainWindow):    # 主窗体类
    def __init__(self):     # 初始化主窗体
        super().__init__()
        self.name = "图片查看器"
        self.img = QLabel()                     # 图片标签
        self.img.setScaledContents(True)        # 图片可缩放
        self.scale = 1.0                        # 图片缩放倍数
        self.scrollArea = QScrollArea()         # 滚动条区域
        self.scrollArea.setWidget(self.img)     # 图片标签加入区域
        self.scrollArea.setAlignment(Qt.AlignCenter)    # 区域内容居中
        self.setCentralWidget(self.scrollArea)          # 区域设为中心部件
        self.initAct()                                  # 初始化动作功能
        self.setWindowTitle(self.name)
        self.resize(600, 480)
        self.showMaximized()

    def initAct(self):      # 初始化动作功能
        self.openAct = QAction("打开", self, shortcut="Ctrl+O")
        self.openAct.setToolTip("打开(Ctrl+O)")
        self.openAct.triggered.connect(self.openImage)
        self.zoominAct = QAction("放大", self, shortcut="+", enabled=False)
        self.zoominAct.setToolTip("放大(+)")
        self.zoominAct.triggered.connect(self.zoomin)
        self.zoomoutAct = QAction("缩小", self, shortcut="-", enabled=False)
        self.zoomoutAct.setToolTip("缩小(-)")
        self.zoomoutAct.triggered.connect(self.zoomout)
        toolbar = self.addToolBar("主工具栏")
        toolbar.addAction(self.openAct)
        toolbar.addAction(self.zoominAct)
        toolbar.addAction(self.zoomoutAct)

    def contextMenuEvent(self, event):  # 右键菜单事件处理
        menu = QMenu(self)
        menu.addAction(self.openAct)
        menu.addAction(self.zoominAct)
        menu.addAction(self.zoomoutAct)
        menu.exec_(self.mapToGlobal(event.pos()))

    def openImage(self):    # 打开图片文件
        fil = "图片文件 (*.png *.gif *.jpg *.jpeg *.bmp *.svg);;所有文件 (*.*)"
        fileName, _ = QFileDialog.getOpenFileName(self, "打开文件", "", fil)
        if fileName:
            image = QImage(fileName)
            if image.isNull():
                QMessageBox.information(self, "错误", f"无法打开{fileName}")
                return
            self.setWindowTitle(f"{basename(fileName)} - {self.name}")
            self.img.setPixmap(QPixmap.fromImage(image))
            self.img.adjustSize()
            self.zoominAct.setEnabled(True)
            self.zoomoutAct.setEnabled(True)

    def scaleImage(self, factor):   # 改变图片缩放倍数
        self.scale *= factor
        self.img.resize(self.scale * self.img.pixmap().size())
        self.zoominAct.setEnabled(self.scale < 8)
        self.zoomoutAct.setEnabled(self.scale > 0.125)

    def zoomin(self):   # 放大图片
        self.scaleImage(2)

    def zoomout(self):  # 缩小图片
        self.scaleImage(0.5)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
