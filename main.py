import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtGui import QIcon, QCursor
from PyQt5.QtCore import Qt, QSize, QPoint


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowIcon(QIcon("resources/icons/icon.png"))
        self.setWindowTitle("Libris")
        self.setGeometry(100, 100, 1300, 800)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.center()
        self.initUI()

        self.is_dragging = False
        self.drag_position = QPoint()

    def center(self):
        qr = self.frameGeometry()
        cp = QApplication.primaryScreen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def initUI(self):
        left_column = QWidget(self)
        left_column.setObjectName("left_column")
        left_column.setFixedWidth(260)
        left_column.setStyleSheet("""
            background-color: #F3F7FA;
            border-top-left-radius: 15px;
            border-bottom-left-radius: 15px;
        """)

        left_column_layout = QVBoxLayout(left_column)

        settings_button = QPushButton("Configurações", self)
        settings_button.setCursor(QCursor(Qt.PointingHandCursor))
        settings_button.setStyleSheet("""
            color: #999999;
            font-size: 15px;
            background-color: #FFFFFF;
            border: 1px solid #999999;
            padding: 5px;
            border-radius: 5px;
        """)

        left_column_layout.addStretch()
        left_column_layout.addWidget(settings_button)

        right_column = QWidget(self)
        right_column.setObjectName("right_column")
        right_column.setStyleSheet("""
            background-color: #FFFFFF;
            border-top-right-radius: 15px;
            border-bottom-right-radius: 15px;
        """)

        right_column_layout = QHBoxLayout(right_column)
        right_column_layout.setAlignment(Qt.AlignRight | Qt.AlignTop)
        right_column_layout.setContentsMargins(0, 0, 0, 0)

        minimize_button = QPushButton("", self)
        minimize_button.setFixedSize(40, 30)
        minimize_button.setCursor(QCursor(Qt.PointingHandCursor))
        minimize_button.setIcon(QIcon("resources/icons/minimize.svg"))
        minimize_button.setIconSize(QSize(15, 15))
        minimize_button.clicked.connect(self.showMinimized)
        minimize_button.setStyleSheet("""
            QPushButton:hover {
                background-color: #E5E5E5;
            }
            QPushButton {
                border-radius: 0px;
            }
        """)

        maximize_button = QPushButton("", self)
        maximize_button.setFixedSize(40, 30)
        maximize_button.setCursor(QCursor(Qt.PointingHandCursor))
        maximize_button.setIcon(QIcon("resources/icons/maximize.svg"))
        maximize_button.setIconSize(QSize(15, 15))
        maximize_button.clicked.connect(self.toggleMaximize)
        maximize_button.setStyleSheet("""
            QPushButton:hover {
                background-color: #E5E5E5;
            }
            QPushButton {
                border-radius: 0px;
            }
        """)

        self.close_button = QPushButton("", self)
        self.close_button.setFixedSize(40, 30)
        self.close_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_button.setObjectName("close_button")
        self.close_button.setIcon(QIcon("resources/icons/close.svg"))
        self.close_button.setIconSize(QSize(15, 15))
        self.close_button.clicked.connect(self.close)
        self.close_button.setStyleSheet("""
            QPushButton:hover {
                background-color: #FD5359;
            }
            QPushButton {
                border-top-right-radius: 15px;
                border-bottom-right-radius: 0px;
            }
        """)

        # Conectar eventos de hover
        self.close_button.enterEvent = self.onCloseButtonHoverEnter
        self.close_button.leaveEvent = self.onCloseButtonHoverLeave

        right_column_layout.addWidget(minimize_button)
        right_column_layout.addWidget(maximize_button)
        right_column_layout.addWidget(self.close_button)

        layout = QHBoxLayout()
        layout.addWidget(left_column)
        layout.addWidget(right_column)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def toggleMaximize(self):
        is_maximized = self.isMaximized()
        self.showNormal() if is_maximized else self.showMaximized()

        border_radius = "15px" if is_maximized else "0px"

        self.centralWidget().findChild(QWidget, "left_column").setStyleSheet(f"""
            background-color: #F3F7FA;
            border-top-left-radius: {border_radius};
            border-bottom-left-radius: {border_radius};
        """)
        self.centralWidget().findChild(QWidget, "right_column").setStyleSheet(f"""
            background-color: #FFFFFF;
            border-top-right-radius: {border_radius};
            border-bottom-right-radius: {border_radius};
        """)
        self.close_button.setStyleSheet(f"""
            QPushButton:hover {{
                background-color: #FD5359;
            }}
            QPushButton {{
                border-top-right-radius: {border_radius};
                border-bottom-right-radius: 0px;
            }}
        """)

    def onCloseButtonHoverEnter(self, event):
        self.close_button.setIcon(QIcon("resources/icons/close-light.svg"))
        event.accept()

    def onCloseButtonHoverLeave(self, event):
        self.close_button.setIcon(QIcon("resources/icons/close.svg"))
        event.accept()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and event.pos().y() <= 30:
            self.is_dragging = True
            self.drag_position = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if self.is_dragging:
            self.move(event.globalPos() - self.drag_position)
            event.accept()

    def mouseReleaseEvent(self, event):
        self.is_dragging = False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
