import sys

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (QApplication,
                             QWidget,
                             QLineEdit,
                             QPushButton,
                             QLabel,
                             QGridLayout,
                             QSizePolicy,
                             QRadioButton,
                             )

from inn_generator import InnGenerator


class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 300)
        label = QLabel('Main App', parent=self)


class InnGen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('UA INN Generator')
        self.setWindowIcon(QIcon(''))
        self.window_width, self.window_height = 300, 300
        self.setFixedSize(self.window_width, self.window_height)

        layout = QGridLayout()
        self.setLayout(layout)

        labels = {}
        self.lineEdits = {}

        labels['Birthdate'] = QLabel('Birthdate')
        labels['Birthdate'].setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        self.lineEdits['Birthdate'] = QLineEdit('21-06-1990')
        layout.addWidget(labels['Birthdate'], 0, 0, 1, 1)
        layout.addWidget(self.lineEdits['Birthdate'], 0, 1, 1, 3)

        button_login = QPushButton('Generate', clicked=self.generate_inn)
        layout.addWidget(button_login, 2, 3, 1, 1)

        self.radio_men = QRadioButton("Male", self)
        self.radio_men.click()
        self.radio_girl = QRadioButton("Female", self)
        layout.addWidget(self.radio_men, 1, 0, 1, 1)
        layout.addWidget(self.radio_girl, 1, 2, 1, 2)

        self.inn = QLineEdit()
        layout.addWidget(self.inn, 2, 0, 1, 3)

    def generate_inn(self):
        birthdate = self.lineEdits['Birthdate'].text()
        if self.radio_men.isChecked():
            male = 1
        else:
            male = 0
        self.inn.setText(str(InnGenerator(birthdate, male).generate_inn()))


app = QApplication(sys.argv)
innGen = InnGen()
innGen.show()
sys.exit(app.exec())
