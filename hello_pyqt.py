# from PyQt5.QtGui import QA
from typing import Optional, Union
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QLayout,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
from PyQt5 import QtCore
import sys


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Hello World from PyQt")
        self.setCentralWidget(MultiplyWidget())


class Multiplier:
    def __init__(self) -> None:
        self.num = 2

    def multiply(self) -> int:
        self.num *= self.num
        return self.num


class MultiplyWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.multiplier = Multiplier()

        self.doMultiplyButton = self.make_multiply_button()
        self.resultDisplay = QLabel(str(self.multiplier.num))

        layout = self._get_layout()
        self.setLayout(layout)

    def _get_layout(self) -> QLayout:
        layout = QVBoxLayout()

        layout.addWidget(self.doMultiplyButton)
        layout.addWidget(self.resultDisplay)
        return layout

    def make_multiply_button(self) -> QWidget:
        button = QPushButton("Square It!")
        button.clicked.connect(self.on_multiply_button_clicked)
        return button

    def on_multiply_button_clicked(self) -> None:
        self.multiplier.multiply()
        self.update_result_display()

    def update_result_display(self) -> None:
        self.resultDisplay.setText(str(self.multiplier.num))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec_()
