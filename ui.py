from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTabWidget, QGridLayout, QLabel, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import *


class ui_window(object):
    def setup_window(self, window):
        window.setWindowTitle("Airport Finder")
        window.setFixedWidth(1050)
        window.setFixedHeight(600)
        self.setup_tabs()
    def setup_tabs(self):
        self.centralWidget = QWidget(window)
        self.centralWidget.setFixedWidth(1050)
        self.centralWidget.setFixedHeight(600)
        self.tabWidget = QTabWidget(self.centralWidget)
        self.tabWidget.setFixedWidth(1050)
        self.tabWidget.setFixedHeight(600)
        self.findAirportsTab = QWidget()
        self.tabWidget.addTab(self.findAirportsTab, "Find")
        self.savedAirportsTab = QWidget()
        self.tabWidget.addTab(self.savedAirportsTab, "Saved")
        self.control_airport_tab()
    def control_airport_tab(self):
        self.titleDescLabel = QLabel(self.findAirportsTab)
        self.titleDescLabel.setText("Airport Description:")
        self.titleDescLabel.move(700, 60)
        self.titleDescLabel.setStyleSheet("font-size: 22pt")
        self.titleLabel = QLabel(self.findAirportsTab)
        self.titleLabel.setText("Salt Lake City International Airport")
        self.titleLabel.move(320, 0)
        self.titleLabel.setStyleSheet("font-weight: bold; font-size: 25pt")
        self.descLabel = QLabel(self.findAirportsTab)
        self.descLabel.setText(" Salt Lake City International Airport is a civil-military airport \n located about 4 miles west of Downtown Salt Lake City,  \n Utah, in the United States. The airport is the closest\n commercial airport for more than 2.5 million people and is\n within a 30-minute drive of nearly 1.3 million jobs.\n SLC is the 20th busiest airport in North America and the\n 47th busiest in the world. More than 300 flights depart daily\n to 90 nonstop destinations. SLC is currently undergoing a\n $4 billion redevelopment program, the first phase of\n which opened in September of 2020. The project is being\n funded by nuser fees--primarily by airlines serving\n SLC--as well as savings, car rental fees, passenger\n facility charges and airport revenue bonds. ")
        self.descLabel.move(600, 100)
        self.descLabel.setStyleSheet("font-size: 15pt")
        self.all_buttons()
    def all_buttons(self):
        self.webButton = QPushButton(self.findAirportsTab)
        self.webButton.setText("Open Website")
        self.webButton.move(597, 350)
        self.saveButton = QPushButton(self.findAirportsTab)
        self.saveButton.setText("Save")
        self.saveButton.move(597, 380)
        self.nextButton = QPushButton(self.findAirportsTab)
        self.nextButton.setText("Next")
        self.nextButton.move(940, 410)
        self.backButton = QPushButton(self.findAirportsTab)
        self.backButton.setText("Back")
        self.backButton.move(597, 410)
        self.show_img()

    def show_img(self):
        labelOne = QLabel(self.findAirportsTab)
        pixmapOne = QPixmap('./App-Pics/SLCINT1')
        labelOne.setPixmap(pixmapOne)
        labelOne.setScaledContents(True)
        labelOne.setFixedWidth(357)
        labelOne.setFixedHeight(237)
        labelOne.move(30, 45)
        labelTwo = QLabel(self.findAirportsTab)
        pixmapTwo = QPixmap('./App-Pics/SLCINT2')
        labelTwo.setPixmap(pixmapTwo)
        labelTwo.setScaledContents(True)
        labelTwo.setFixedWidth(169)
        labelTwo.setFixedHeight(225)
        labelTwo.move(400, 45)
        labelThree = QLabel(self.findAirportsTab)
        pixmapThree = QPixmap('./App-Pics/SLCmap')
        labelThree.setPixmap(pixmapThree)
        labelThree.setScaledContents(True)
        labelThree.setFixedWidth(370)
        labelThree.setFixedHeight(214)
        labelThree.move(30, 290)
        labelFour= QLabel(self.findAirportsTab)
        pixmapFour = QPixmap('./App-Pics/SLC_the_falls')
        labelFour.setPixmap(pixmapFour)
        labelFour.setScaledContents(True)
        labelFour.setFixedWidth(143)
        labelFour.setFixedHeight(214)
        labelFour.move(426, 290)








if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = ui_window()
    ui.setup_window(window)
    window.show()
    sys.exit(app.exec_())
