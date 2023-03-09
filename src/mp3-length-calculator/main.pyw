from sys import argv
from PySide6.QtWidgets import QApplication
from interface.window import Window


def main():
    app = QApplication(argv)
    window = Window()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
