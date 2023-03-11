from PySide6.QtWidgets import QMainWindow, QFileDialog, QListWidgetItem
from PySide6.QtCore import Qt
from interface.ui.window import Ui_MainWindow
from audio.processing import get_mp3_files
from audio.convert import sum_bytes, sum_duration


class Window(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.path = None
        self.audios = None
        self.items = None

        self._disable_select_all()
        self._disable_calculate()

        self.pushButton_choose_path.clicked.connect(self.choose_path)
        self.pushButton_calculate.clicked.connect(self.calculate)
        self.checkBox_select_all.clicked.connect(self.select_all)

    def _enable_select_all(self):
        self.checkBox_select_all.setEnabled(True)

    def _disable_select_all(self):
        self.checkBox_select_all.setEnabled(False)

    def _enable_calculate(self):
        self.pushButton_calculate.setEnabled(True)

    def _disable_calculate(self):
        self.pushButton_calculate.setEnabled(False)
    
    def choose_path(self):
        chosen_path = QFileDialog.getExistingDirectory(self, 'Choose a path', self.path)
        if chosen_path:
            self.path = chosen_path
            self.lineEdit_path_output.setText(self.path)
            self.clean_total()
            self.clean_audios_list()
            self.set_audios()
    
    def set_audios(self):
        self.checkBox_select_all.setChecked(False)
        self.audios = get_mp3_files(self.path)
        if len(self.audios) >= 1:
            items = []
            for audio in self.audios:
                item = QListWidgetItem(self.listWidget_audios)
                item.setText(audio['title'])
                item.setCheckState(Qt.Unchecked)
                item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
                items.append(item)
            self.items = items
            self._enable_calculate()
            self._enable_select_all()
        else:
            self._disable_calculate()
            self._disable_select_all()
    
    def calculate(self):
        checked = []
        for i, item in enumerate(self.items):
            if self._get_check_state(item):
                checked.append(self.audios[i])
        self.label_amount_output.setText(
            str(len(checked))
        )
        self.label_size_output.setText(
            sum_bytes(*[audio['size'] for audio in checked])
        )
        self.label_duration_output.setText(
            sum_duration(*[audio['duration'] for audio in checked])
        )
    
    @staticmethod
    def _get_check_state(item):
        return item.checkState() == Qt.Checked
    
    def select_all(self):
        check_state = self.checkBox_select_all.isChecked()
        if check_state:
            for item in self.items:
                item.setCheckState(Qt.Checked)
        else:
            for item in self.items:
                item.setCheckState(Qt.Unchecked)

    def clean_audios_list(self):
        self.listWidget_audios.clear()
    
    def clean_total(self):
        self.label_amount_output.setText('0')
        self.label_size_output.setText('0 B')
        self.label_duration_output.setText('0:00:00')
