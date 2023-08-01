import sys
from PyQt6.QtWidgets import QApplication, QWidget


# 基础小组件位于 PyQt6.QtWidgets 模块

def main():
    # 每个PyQt6应用程序都必须创建一个应用程序对象。sys.argv参数是来自命令行的参数列表。
    # Python脚本可以从shell运行，这是应用启动的一种方式
    app = QApplication(sys.argv)
    # QWidget小部件是PyQt6中所有用户界面对象的基类。提供了默认构造函数。默认构造函数没有父级。没有父级的小部件称为窗口
    w = QWidget()
    # resize方法改变了小部件的尺寸，现在它250像素宽，150像素高
    w.resize(250, 200)
    # move方法把小部件移动到屏幕的指定坐标(300, 300)
    w.move(300, 300)
    # 使用setWindowTitle给窗口设置标题，标题显示在标题栏
    w.setWindowTitle('Simple')
    # show方法是在屏幕上显示小部件的方法。显示一个部件的步骤是首先在内存里创建，然后在屏幕上显示。
    w.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
