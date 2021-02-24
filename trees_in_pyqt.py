# from PyQt5.QtGui import QA
from typing import Optional, Union
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QLayout,
    QMainWindow,
    QPushButton,
    QTableWidgetItem,
    QTreeWidget,
    QTreeWidgetItem,
    QVBoxLayout,
    QWidget,
)
from PyQt5 import QtCore
import sys


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Calculate Widget")
        self.setCentralWidget(CalculateWidget(self))


class Data:
    def __init__(self, startingNumber: int = 2) -> None:
        self.number = startingNumber

    def __str__(self) -> str:
        return str(self.number)


class DataOperator:
    def __init__(self, data: Data) -> None:
        self.data = data

    @property
    def num(self) -> int:
        return self.data.number

    @num.setter
    def num(self, newNumber: int) -> None:
        self.data.number = newNumber


class Multiplier(DataOperator):
    def multiply(self) -> int:
        self.num *= self.num
        return self.num


class Divider(DataOperator):
    def divide(self) -> int:
        self.num = int(self.num / 2)
        return self.num


class CalculateWidget(QTreeWidget):
    def __init__(self, parentWindow: QWidget) -> None:
        super(CalculateWidget, self).__init__(parentWindow)

        self._data = Data()

        self.multiplier = MultiplyWidget(self)
        # # self.divider = DivideWidget(self)
        # self.resultDisplay = ResultDisplayWidget(self)
        # self.addChild(self.resultDisplay)
        # self.addChild(self.multiplier)

    def update_result_display(self) -> None:
        self.resultDisplay.update()


class MultiplyWidget(QTreeWidgetItem):
    def __init__(self, parentCalculatorWidget: CalculateWidget) -> None:
        super().__init__(parentCalculatorWidget, ["Multiply"])

        self.calculatorWidget = parentCalculatorWidget

        self.multiplier = Multiplier(self.calculatorWidget._data)

        self.doMultiplyButton = self.make_multiply_button()

    def make_multiply_button(self) -> None:
        pass

    def on_multiply_button_clicked(self) -> None:
        self.multiplier.multiply()
        self.calculatorWidget.update_result_display()


class ResultDisplayWidget(QTreeWidgetItem):
    def __init__(self, parentCalculatorWidget: CalculateWidget) -> None:
        super().__init__(parentCalculatorWidget)

        self.calculatorWidget = parentCalculatorWidget

        self.resultDisplay = QLabel(str(self.calculatorWidget.data))

    def update(self) -> None:
        self.resultDisplay.setText(str(self.calculatorWidget.data))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec_()
