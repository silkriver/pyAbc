"""主窗体模块"""
from os.path import abspath, basename, dirname
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import (QAction, QFileDialog, QLabel, QMainWindow, QMenu,
                             QMessageBox, QScrollArea)


class Main(QMainWindow):    # 主窗体类
    signal = pyqtSignal(str)

    def __init__(self):     # 初始化主窗体
        super().__init__()
        self.name = "图片查看器"
        self.imgdir = "."
        self.img = QLabel()                 # 图片标签
        self.img.setScaledContents(True)    # 图片可缩放
        self.scale = 1.0                    # 图片缩放倍数
        self.scrollArea = QScrollArea()     # 滚动条区域
        self.scrollArea.setWidget(self.img)             # 图片标签加入区域
        self.scrollArea.setAlignment(Qt.AlignCenter)    # 区域内容居中
        self.setCentralWidget(self.scrollArea)          # 区域设为中心部件
        self.initAct()                                  # 初始化动作功能
        self.setWindowTitle(self.name)
        self.resize(600, 480)
        self.showMaximized()

    def switch(self):   # 切换窗体
        self.signal.emit(self.imgdir)

    def initAct(self):  # 初始化动作功能
        self.openAct = QAction("打开", self, shortcut="Ctrl+O")
        self.openAct.setToolTip("打开(Ctrl+O)")
        self.openAct.triggered.connect(self.openImage)
        self.zoominAct = QAction("放大", self, shortcut="+", enabled=False)
        self.zoominAct.setToolTip("放大(+)")
        self.zoominAct.triggered.connect(lambda: self.scaleImage(2))
        self.zoomoutAct = QAction("缩小", self, shortcut="-", enabled=False)
        self.zoomoutAct.setToolTip("缩小(-)")
        self.zoomoutAct.triggered.connect(lambda: self.scaleImage(0.5))
        self.isizeAct = QAction("原尺寸", self, shortcut="1", enabled=False)
        self.isizeAct.setToolTip("原尺寸(1)")
        self.isizeAct.triggered.connect(self.initsize)
        self.asizeAct = QAction("自适应", self, shortcut="0", enabled=False)
        self.asizeAct.setToolTip("自适应(0)")
        self.asizeAct.triggered.connect(self.autosize)
        self.multiAct = QAction("多图显示", self, shortcut="Ctrl+M")
        self.multiAct.setToolTip("多图显示(Ctrl+M)")
        self.multiAct.triggered.connect(self.switch)
        toolbar = self.addToolBar("主工具栏")
        toolbar.addAction(self.openAct)
        toolbar.addAction(self.zoominAct)
        toolbar.addAction(self.zoomoutAct)
        toolbar.addAction(self.isizeAct)
        toolbar.addAction(self.asizeAct)
        toolbar.addAction(self.multiAct)

    def contextMenuEvent(self, event):  # 右键菜单事件处理
        menu = QMenu(self)
        menu.addAction(self.openAct)
        menu.addAction(self.zoominAct)
        menu.addAction(self.zoomoutAct)
        menu.addAction(self.isizeAct)
        menu.addAction(self.asizeAct)
        menu.exec_(self.mapToGlobal(event.pos()))

    def openImage(self):                # 打开图片文件
        fil = "图片文件 (*.png *.gif *.jpg *.jpeg *.bmp *.svg);;所有文件 (*.*)"
        fileName, _ = QFileDialog.getOpenFileName(self, "打开文件", "", fil)
        if fileName:
            image = QImage(fileName)
            if image.isNull():
                QMessageBox.information(self, "错误", f"无法打开{fileName}")
                return
            self.imgdir = dirname(abspath(fileName))
            self.setWindowTitle(f"{basename(fileName)} - {self.name}")
            self.img.setPixmap(QPixmap.fromImage(image))
            self.img.adjustSize()
            self.updateAct()
            self.isizeAct.setEnabled(True)
            self.asizeAct.setEnabled(True)

    def scaleImage(self, factor):   # 改变图片缩放倍数
        self.scale *= factor
        self.img.resize(self.scale * self.img.pixmap().size())
        self.updateAct()

    def initsize(self):             # 原尺寸图片
        self.img.adjustSize()
        self.scale = 1.0
        self.updateAct()

    def autosize(self):             # 自适应图片
        maxw, maxh = self.scrollArea.width(), self.scrollArea.height()
        w, h = self.img.pixmap().width(), self.img.pixmap().height()
        self.scale = min(maxw / w, maxh / h)
        self.img.resize(self.scale * self.img.pixmap().size())
        self.updateAct()

    def updateAct(self):            # 更新动作允许或禁用放大或缩小
        w, h = self.img.width(), self.img.height()
        self.zoominAct.setEnabled(max(w, h) < 10000)
        self.zoomoutAct.setEnabled(min(w, h) > 10)
