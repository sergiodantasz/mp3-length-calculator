from PySide6.QtWidgets import QMainWindow
from interface.ui.window import Ui_MainWindow


class Window(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
