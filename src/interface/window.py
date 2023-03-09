from PySide6.QtWidgets import QMainWindow
from interface.ui.window import Ui_MainWindow


class Window(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self._disable_select_all()
        self._disable_calculate()

    def _enable_select_all(self):
        self.checkBox_select_all.setEnabled(True)

    def _disable_select_all(self):
        self.checkBox_select_all.setEnabled(False)

    def _enable_calculate(self):
        self.pushButton_calculate.setEnabled(True)

    def _disable_calculate(self):
        self.pushButton_calculate.setEnabled(False)
