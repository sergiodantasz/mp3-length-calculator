# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QGridLayout,
    QGroupBox, QLabel, QLineEdit, QListView,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(450, 450)
        MainWindow.setMinimumSize(QSize(450, 450))
        MainWindow.setMaximumSize(QSize(450, 450))
        font = QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_path = QLabel(self.centralwidget)
        self.label_path.setObjectName(u"label_path")
        self.label_path.setMaximumSize(QSize(28, 16777215))

        self.gridLayout_2.addWidget(self.label_path, 0, 0, 1, 1)

        self.lineEdit_path_output = QLineEdit(self.centralwidget)
        self.lineEdit_path_output.setObjectName(u"lineEdit_path_output")
        self.lineEdit_path_output.setReadOnly(True)

        self.gridLayout_2.addWidget(self.lineEdit_path_output, 0, 1, 1, 2)

        self.horizontalSpacer = QSpacerItem(308, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 0, 1, 2)

        self.pushButton_choose_path = QPushButton(self.centralwidget)
        self.pushButton_choose_path.setObjectName(u"pushButton_choose_path")
        self.pushButton_choose_path.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.pushButton_choose_path, 1, 2, 1, 1)

        self.listWidget_audios = QListWidget(self.centralwidget)
        self.listWidget_audios.setObjectName(u"listWidget_audios")
        self.listWidget_audios.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.listWidget_audios.setResizeMode(QListView.Adjust)

        self.gridLayout_2.addWidget(self.listWidget_audios, 2, 0, 1, 3)

        self.checkBox_select_all = QCheckBox(self.centralwidget)
        self.checkBox_select_all.setObjectName(u"checkBox_select_all")

        self.gridLayout_2.addWidget(self.checkBox_select_all, 3, 0, 1, 3)

        self.pushButton_calculate = QPushButton(self.centralwidget)
        self.pushButton_calculate.setObjectName(u"pushButton_calculate")

        self.gridLayout_2.addWidget(self.pushButton_calculate, 4, 0, 1, 3)

        self.groupBox_total = QGroupBox(self.centralwidget)
        self.groupBox_total.setObjectName(u"groupBox_total")
        self.groupBox_total.setAlignment(Qt.AlignCenter)
        self.groupBox_total.setFlat(True)
        self.gridLayout = QGridLayout(self.groupBox_total)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_amount = QLabel(self.groupBox_total)
        self.label_amount.setObjectName(u"label_amount")
        self.label_amount.setMaximumSize(QSize(53, 16777215))

        self.gridLayout.addWidget(self.label_amount, 0, 0, 1, 1)

        self.label_amount_output = QLabel(self.groupBox_total)
        self.label_amount_output.setObjectName(u"label_amount_output")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_amount_output.sizePolicy().hasHeightForWidth())
        self.label_amount_output.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_amount_output, 0, 1, 1, 1)

        self.label_size = QLabel(self.groupBox_total)
        self.label_size.setObjectName(u"label_size")

        self.gridLayout.addWidget(self.label_size, 1, 0, 1, 1)

        self.label_size_output = QLabel(self.groupBox_total)
        self.label_size_output.setObjectName(u"label_size_output")
        sizePolicy.setHeightForWidth(self.label_size_output.sizePolicy().hasHeightForWidth())
        self.label_size_output.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_size_output, 1, 1, 1, 1)

        self.label_duration = QLabel(self.groupBox_total)
        self.label_duration.setObjectName(u"label_duration")
        self.label_duration.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.label_duration, 2, 0, 1, 1)

        self.label_duration_output = QLabel(self.groupBox_total)
        self.label_duration_output.setObjectName(u"label_duration_output")
        sizePolicy.setHeightForWidth(self.label_duration_output.sizePolicy().hasHeightForWidth())
        self.label_duration_output.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_duration_output, 2, 1, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_total, 5, 0, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MP3 Length Calculator", None))
        self.label_path.setText(QCoreApplication.translate("MainWindow", u"Path:", None))
        self.lineEdit_path_output.setPlaceholderText(QCoreApplication.translate("MainWindow", u"The directory containing the audios.", None))
        self.pushButton_choose_path.setText(QCoreApplication.translate("MainWindow", u"Choose path", None))
        self.checkBox_select_all.setText(QCoreApplication.translate("MainWindow", u"Select all", None))
        self.pushButton_calculate.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.groupBox_total.setTitle(QCoreApplication.translate("MainWindow", u"Total", None))
        self.label_amount.setText(QCoreApplication.translate("MainWindow", u"Amount:", None))
        self.label_amount_output.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_size.setText(QCoreApplication.translate("MainWindow", u"Size:", None))
        self.label_size_output.setText(QCoreApplication.translate("MainWindow", u"0 B", None))
        self.label_duration.setText(QCoreApplication.translate("MainWindow", u"Duration:", None))
        self.label_duration_output.setText(QCoreApplication.translate("MainWindow", u"0:00:00", None))
    # retranslateUi

