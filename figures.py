import os
import math

import sys
# Подключаем модули QApplication и QLabel
from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtGui import QPainter, QBrush
from PySide2.QtCore import Qt, QPoint


class Figure:
    def __init__(self, x=0, y=0, w=0, h=0):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
    
    def perimeter(self):
        raise NotImplementedError
    
    def square(self):
        raise NotImplementedError

    
class Rectangle(Figure):
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def square(self):
        return self.width * self.height


class Ellipse(Figure):
    def perimeter(self):
        return 2 * math.pi * math.sqrt((self.width ** 2 + self.height ** 2) / 4)

    def square(self):
        return math.pi * self.width * self.height

# Импортируйте свой файл с фигурами


class FigureWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Рисовалка фигур')
        self.__figures = []
        
    def set_figures(self, figures):
        self.__figures = figures
        
    def paintEvent(self, event):
        
        painter = QPainter(self)
        reset_brush = painter.brush()
        
        for figure in self.__figures:
            if not isinstance(figure, Figure):
                continue
            
            if isinstance(figure, Rectangle):
                painter.setBrush(QBrush(Qt.red))
                painter.drawRect(figure.x, figure.y, figure.width, figure.height)
                continue
            
            if isinstance(figure, Ellipse):
                painter.setBrush(QBrush(Qt.green))
                painter.drawEllipse(figure.x, figure.y, figure.width, figure.height)
                continue

            # if isinstance(figure, CloseFigure):
            #     painter.setBrush(QBrush(Qt.blue))
            #
            #     points = []
            #     for point in figure:
            #         points.append(QPoint(point['x'], point['y']))
            #     painter.drawPolygon(points)
            #     continue


if __name__ == '__main__':

    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = './platforms'
    app = QApplication(sys.argv)
    figure_widget = FigureWidget()

    # Создайте список фигур
    figures = [Rectangle(20, 30, 400, 200), Ellipse(20, 250, 400, 200)]

    figure_widget.set_figures(figures)

    figure_widget.show()
    sys.exit(app.exec_())
