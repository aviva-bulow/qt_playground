# from PyQt5.QtGui import QA
from typing import List, Optional, Union
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


class CalculateWidget(QWidget):
    def __init__(self, parent: Optional["QWidget"],) -> None:
        super().__init__(parent=parent)

        self._data = Data()

        self.calculateWidgetTree = CalculateWidgetTree(self)
        self.calculateWidgetTree.itemPressed.connect(self.on_tree_item_click)
        self.resultDisplay = ResultDisplayWidget(self)
        self.setLayout(self._get_layout())

    def _get_layout(self) -> QLayout:
        layout = QVBoxLayout()

        layout.addWidget(self.calculateWidgetTree)
        layout.addWidget(self.resultDisplay)
        return layout

    def on_tree_item_click(self, item: "ClickableWidgetItem", column) -> None:
        self.calculateWidgetTree.on_click(item, column)
        self.resultDisplay.update()


class CalculateWidgetTree(QTreeWidget):
    def __init__(self, parentWindow: QWidget) -> None:
        super(CalculateWidgetTree, self).__init__(parentWindow)

        self._data = parentWindow._data

        self.multiplier = MultiplyWidget(self)
        self.divider = DivideWidget(self)

    def update_result_display(self) -> None:
        self.resultDisplay.update()

    def on_click(self, item: "ClickableWidgetItem", column: int) -> None:
        item.on_click()


class ClickableWidgetItem(QTreeWidgetItem):
    def __init__(self, parent: QTreeWidgetItem, columnNameList: List[str]) -> None:
        super().__init__(parent, columnNameList)

    def on_click(self) -> None:
        pass


class MultiplyWidget(ClickableWidgetItem):
    def __init__(self, parentCalculatorWidget: CalculateWidget) -> None:
        super().__init__(parentCalculatorWidget, ["Multiply"])

        self.multiplier = Multiplier(parentCalculatorWidget._data)

    def on_click(self) -> None:
        self.multiplier.multiply()


class DivideWidget(ClickableWidgetItem):
    def __init__(self, parentCalculatorWidget: CalculateWidget) -> None:
        super().__init__(parentCalculatorWidget, ["Divide"])

        self.divider = Divider(parentCalculatorWidget._data)

    def on_click(self) -> None:
        self.divider.divide()


class ResultDisplayWidget(QWidget):
    def __init__(self, parentCalculatorWidget: CalculateWidget) -> None:
        super().__init__(parentCalculatorWidget)

        self.calculatorWidget = parentCalculatorWidget

        self.resultDisplay = QLabel(str(self.calculatorWidget._data))
        layout = QVBoxLayout()
        layout.addWidget(self.resultDisplay)
        self.setLayout(layout)

    def update(self) -> None:
        self.resultDisplay.setText(str(self.calculatorWidget._data))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec_()
