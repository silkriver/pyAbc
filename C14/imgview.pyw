"""基于PyQt5的图片查看器
"""
from PyQt5.QtWidgets import QApplication
from main import Main   # 主窗体模块


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
