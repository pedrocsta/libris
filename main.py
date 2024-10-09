import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QWidget, QHBoxLayout, QSplitter
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowIcon(QIcon("resources/icons/icon.png"))
        self.setWindowTitle("Libris")
        self.setGeometry(100, 100, 1300, 800)

        self.setWindowFlags(Qt.FramelessWindowHint)

        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet("background-color: #FFFFFF; border-radius: 15px;")

        self.center()
        self.initUI()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def initUI(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QHBoxLayout()

        layout.setContentsMargins(0, 0, 0, 0)

        splitter = QSplitter(Qt.Horizontal)
        splitter.setHandleWidth(0)
        splitter.setDisabled(True)

        left_column = QWidget()
        left_column.setFixedWidth(260)
        left_column.setStyleSheet("background-color: #F3F7FA;")

        right_column = QWidget()
        right_column.setStyleSheet("background-color: #FFFFFF;")

        splitter.addWidget(left_column)
        splitter.addWidget(right_column)

        layout.addWidget(splitter)

        central_widget.setLayout(layout)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec_())
