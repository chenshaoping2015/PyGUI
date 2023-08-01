# -*- coding:utf-8 -*-
# @Time  :2023/8/1 21:12
# @Author: stevenchen
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton
import sys
# 在PyQt 6.0中，你可以通过信号（Signal）和槽（Slot）机制将窗口的文本信息作为参数传递给后端。
# 信号和槽是PyQt中用于实现事件处理和通信的机制，它们允许对象之间进行通信，如窗口和后端。
'''
在这个示例中，我们创建了一个简单的主窗口，其中包含一个文本输入框和一个提交按钮。当用户点击提交按钮时，通过连接按钮的点击事件和槽函数，
获取文本输入框中的文本内容，并将其作为参数传递给后端处理函数backend_process。请注意，backend_process函数在示例中只是简单地打印
传递的文本内容，你可以根据实际情况将文本传递给后端的其他函数或模块进行实际处理。
以上是使用PyQt 6.0传递窗口的文本信息给后端的一个基本示例，你可以根据自己的需求进行进一步的扩展和修改。
'''

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建主窗口部件
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # 创建布局和部件
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.text_input = QLineEdit(self)
        layout.addWidget(self.text_input)

        self.submit_button = QPushButton("提交", self)
        layout.addWidget(self.submit_button)

        # 连接按钮的点击事件和槽函数
        self.submit_button.clicked.connect(self.on_submit)

    def on_submit(self):
        # 获取文本输入框的文本内容
        text = self.text_input.text()

        # 调用后端处理函数，并将文本内容作为参数传递
        self.backend_process(text)

    def backend_process(self, text):
        # 这里模拟后端处理过程，你可以在此处将text传递给后端的其他函数或模块进行进一步处理
        print("后端接收到文本内容：", text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
