# file: tooltip.py
# !/usr/bin/python

"""
ZetCode PyQt6 tutorial

This example shows a tooltip on
a window and a button.

Author: Jan Bodnar
Website: zetcode.com
"""

import sys
from PyQt6.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication)
from PyQt6.QtGui import QFont


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 气泡提示框,静态方法给气泡提示框设置了字体，这里使用了10pt 的 SansSerif 字体
        QToolTip.setFont(QFont('SansSerif', 10))
        # 调用 setTooltip 方法创建气泡提示框，使用富文本内容
        self.setToolTip('This is a <b>QWidget</b> widget')
        # 在气泡提示框上添加了一个按钮部件
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        # 在气泡提示框上添加了一个按钮部件
        # sizeHint 方法是给按钮一个系统建议的尺寸，然后使用move方法移动这个按钮的位置。
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
