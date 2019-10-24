from PyQt5.QtWidgets import * #QWidget, QApplication
from PyQt5.QtCore import * #Qt
from PyQt5.QtGui import *
import numpy as np
from canvas import Canvas
import cv2

class SketchViewer(QWidget):
    def __init__( self, win_size=512, img_size=512, interactive=True):
        QWidget.__init__(self)
        self.points = []
        self.nps = 512
        self.scale = 1
        self.isPressed = False
        self.pos = QPoint(0, 0)
        self.scale = win_size / float(img_size)
        self.brushWidth = int(2 * self.scale)
        nc = 3
        self.canvas = Canvas(img_size=img_size, scale=self.scale, nc=nc, pen_width=self.brushWidth)
        self.rgb_color = 0
        self.show()

    def round_point(self, pnt):
        x = int(np.round(pnt.x()))
        y = int(np.round(pnt.y()))
        return QPoint(x, y)

    def mousePressEvent(self, event):
        self.pos = self.round_point(event.pos())
        if event.button() == Qt.LeftButton:
            self.isPressed = True

    def mouseMoveEvent(self, event):
        self.pos = self.round_point(event.pos())
        if self.isPressed:
            self.points.append(self.pos)
            self.canvas.update(self.points, self.rgb_color)
            self.update()

    def mouseReleaseEvent(self, event):
        self.pos = self.round_point(event.pos())
        if self.isPressed:
            self.points.append(self.pos)
            self.canvas.update(self.points, self.rgb_color)
            self.isPressed = False
            self.points.clear()
            self.update()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.fillRect(event.rect(), Qt.white)
        painter.setRenderHint(QPainter.Antialiasing)
        im = self.canvas.get_img()

        if im is not None:
            bigim = cv2.resize(im, (self.nps, self.nps))
            qImg = QImage(bigim.tostring(), self.nps, self.nps, QImage.Format_RGB888)
            painter.drawImage(0, 0, qImg)
