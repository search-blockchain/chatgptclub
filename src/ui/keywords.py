
from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget)

class KeywordsDlg(QDialog):
    def __init__(self, parent=None):
        super(KeywordsDlg, self).__init__(parent)

        self.originalPalette = QApplication.palette()

        check = []
        check.append("check")
        check.append("uncheck")
        checkComboBox = QComboBox()
        checkComboBox.addItems(check)
        checkComboBox = QLabel("&Check:")
       





        


        




