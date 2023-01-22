from PyQt5 import QtWidgets

class ui_window(object):
    def setup_window(self, window):
        window.setWindowTitle("Airport Finder")
        window.setFixedWidth(700)
        window.setFixedHeight(400)


if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = ui_window()
    ui.setup_window(window)
    window.show()
    sys.exit(app.exec_())
