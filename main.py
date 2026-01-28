import sys
from PySide6.QtWidgets import QApplication
from cryptqt.gui.QT_gui import MyWidget

def main():
    app = QApplication(sys.argv)

    window = MyWidget()
    window.resize(800, 600)
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
