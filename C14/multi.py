"""多图片窗体模块
"""
from os import listdir
from os.path import abspath, dirname, join
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap
import PyQt5.QtWidgets as qw


class XLabel(qw.QLabel):            # 可点击标签类
    clicked = pyqtSignal(str)

    def mousePressEvent(self, e):
        self.clicked.emit(self.imgfile)


class Multi(qw.QMainWindow):        # 多图片窗体类
    signal = pyqtSignal(str)

    def __init__(self, imgdir):     # 初始化多图片窗体
        super().__init__()
        self.name = "多图片显示"
        self.imgdir = dirname(abspath(imgdir))
        self.initAct()
        self.setWindowTitle(f"{self.imgdir} - {self.name}")
        self.resize(600, 480)
        self.showMaximized()
        self.createLayout()

    def switch(self, imgfile=None):   # 切换窗体
        self.signal.emit(imgfile)

    def initAct(self):  # 初始化动作功能
        self.openAct = qw.QAction("打开目录", self, shortcut="Ctrl+O")
        self.openAct.setToolTip("打开目录(Ctrl+O)")
        self.openAct.triggered.connect(self.openDir)
        self.mainAct = qw.QAction("主窗体", self, shortcut="Ctrl+M")
        self.mainAct.setToolTip("主窗体(Ctrl+M)")
        self.mainAct.triggered.connect(self.switch)
        toolbar = self.addToolBar("主工具栏")
        toolbar.addAction(self.openAct)
        toolbar.addAction(self.mainAct)

    def contextMenuEvent(self, event):  # 右键菜单事件处理
        menu = qw.QMenu(self)
        menu.addAction(self.openAct)
        menu.exec_(self.mapToGlobal(event.pos()))

    def openDir(self, imgdir=None):     # 打开目录
        if not imgdir:
            imgdir = qw.QFileDialog.getExistingDirectory(self, "打开目录")
        if imgdir:
            self.imgdir = abspath(imgdir)
            self.setWindowTitle(f"{self.imgdir} - {self.name}")
            self.createLayout()

    def createLayout(self):             # 创建网格布局图片显示部件
        filetypes = (".png", ".gif", ".jpg", ".jpeg", ".bmp", ".svg")
        img_list = []
        for file in listdir(self.imgdir):
            if file.lower().endswith(filetypes):
                img_list.append(file)
        layout = qw.QGridLayout()
        widget = qw.QWidget()
        widget.setLayout(layout)
        self.scrollArea = qw.QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(widget)
        self.setCentralWidget(self.scrollArea)
        cnt = self.width() // 200 - 1
        for (i, img_name) in enumerate(img_list):
            img = XLabel()
            imgfile = join(self.imgdir, img_name)
            pixmap = QPixmap(imgfile)
            if pixmap.isNull():
                continue
            img.resize(200, 200)
            img.setPixmap(pixmap.scaled(img.size(), Qt.KeepAspectRatio))
            img.setToolTip(img_name)
            setattr(img, "imgfile", imgfile)
            img.clicked.connect(self.switch)
            layout.addWidget(img, i // cnt, i % cnt)


if __name__ == "__main__":
    import sys
    app = qw.QApplication(sys.argv)
    multi = Multi(".")
    multi.show()
    sys.exit(app.exec_())
