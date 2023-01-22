from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTabWidget, QGridLayout, QLabel, QWidget, QVBoxLayout


class ui_window(object):
    def setup_window(self, window):
        window.setWindowTitle("Airport Finder")
        window.setFixedWidth(700)
        window.setFixedHeight(400)
        self.setup_tabs()
    def setup_tabs(self):
        self.centralWidget = QWidget(window)
        self.centralWidget.setFixedWidth(700)
        self.centralWidget.setFixedHeight(400)
        self.tabWidget = QTabWidget(self.centralWidget)
        self.tabWidget.setFixedWidth(700)
        self.tabWidget.setFixedHeight(400)
        self.findAirportsTab = QWidget()
        self.tabWidget.addTab(self.findAirportsTab, "Find")
        self.savedAirportsTab = QWidget()
        self.tabWidget.addTab(self.savedAirportsTab, "Saved")
        self.control_airport_tab()
    def control_airport_tab(self):
        self.titleDescLabel = QLabel(self.findAirportsTab)
        self.titleDescLabel.setText("Airport Description:")
        self.titleDescLabel.move(350, 60)
        self.titleDescLabel.setStyleSheet("font-size: 20pt")
        self.titleLabel = QLabel(self.findAirportsTab)
        self.titleLabel.setText("Salt Lake City International Airport")
        self.titleLabel.move(180, 0)
        self.titleLabel.setStyleSheet("font-weight: bold; font-size: 22pt")
        self.descLabel = QLabel(self.findAirportsTab)
        self.descLabel.setText(" Salt Lake City International Airport is a civil-military airport \n located about 4 miles west of Downtown Salt Lake City,  \n Utah, in the United States. The airport is the closest\n commercial airport for more than 2.5 million people and is\n within a 30-minute drive of nearly 1.3 million jobs.")
        self.descLabel.move(260, 100)
        self.descLabel.setStyleSheet("font-size: 13.5pt")



if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = ui_window()
    ui.setup_window(window)
    window.show()
    sys.exit(app.exec_())
