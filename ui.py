from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTabWidget, QGridLayout, QLabel, QWidget, QVBoxLayout


class ui_window(object):
    def setup_window(self, window):
        window.setWindowTitle("Airport Finder")
        window.setFixedWidth(700)
        window.setFixedHeight(400)
        oTabWidget = QTabWidget(window)

        oPage1 = QWidget()
        oLabel1 = QLabel("hello", window)
        oVbox1 = QVBoxLayout()
        oVbox1.addWidget(oLabel1)
        oPage1.setLayout(oVbox1)

        oPage2 = QWidget()
        oPage2.setGeometry(0, 0, 400, 400)

        oTabWidget.addTab(oPage1, "Find")
        oTabWidget.addTab(oPage2, "Saved")


        window.show()




if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = ui_window()
    ui.setup_window(window)
    window.show()
    sys.exit(app.exec_())
