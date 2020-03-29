"""多图片窗体模块
"""
from os import listdir
from os.path import abspath, dirname, join
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import PyQt5.QtWidgets as qw


class Multi(qw.QMainWindow):        # 多图片窗体类
    def __init__(self, imgdir):     # 初始化多图片窗体
        super().__init__()
        self.name = "多图片显示"
        self.imgdir = dirname(abspath(imgdir))
        self.initAct()
        self.setWindowTitle(f"{self.imgdir} - {self.name}")
        self.resize(600, 480)
        self.showMaximized()
        self.createLayout()

    def initAct(self):                  # 初始化动作功能
        self.openAct = qw.QAction("打开目录", self, shortcut="Ctrl+O")
        self.openAct.setToolTip("打开目录(Ctrl+O)")
        self.openAct.triggered.connect(self.openDir)
        toolbar = self.addToolBar("主工具栏")
        toolbar.addAction(self.openAct)

    def contextMenuEvent(self, event):  # 右键菜单事件处理
        menu = qw.QMenu(self)
        menu.addAction(self.openAct)
        menu.exec_(self.mapToGlobal(event.pos()))

    def openDir(self):                  # 打开目录
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
            img = qw.QLabel()
            pixmap = QPixmap(join(self.imgdir, img_name))
            if pixmap.isNull():
                continue
            img.resize(200, 200)
            img.setPixmap(pixmap.scaled(img.size(), Qt.KeepAspectRatio))
            img.setToolTip(img_name)
            layout.addWidget(img, i // cnt, i % cnt)


if __name__ == "__main__":
    import sys
    app = qw.QApplication(sys.argv)
    multi = Multi(".")
    multi.show()
    sys.exit(app.exec_())
