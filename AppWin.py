import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QCheckBox, QPushButton


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt6 text box and checkbox example'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create a label for text box
        label = QLabel('Name:', self)
        label.move(20, 20)

        # Create a text box
        textbox = QLineEdit(self)
        textbox.move(80, 20)
        textbox.resize(200, 20)

        # Create a label for checkbox
        label2 = QLabel('Hobbies:', self)
        label2.move(20, 50)

        # Create checkboxes
        cb1 = QCheckBox('Reading', self)
        cb1.move(80, 50)

        cb2 = QCheckBox('Travelling', self)
        cb2.move(80, 70)

        cb3 = QCheckBox('Sports', self)
        cb3.move(80, 90)

        # Create a button in the window
        button = QPushButton('Submit', self)
        button.move(80, 130)

        # connect button to function on_click
        button.clicked.connect(self.on_click)

    def on_click(self):
        print('Button clicked')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec())
