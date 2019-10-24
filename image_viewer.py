from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

import numpy as np
import time
import cv2


class ImageViewer(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.image = None
        self.show()

    def paintEvent(self,event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.fillRect(event.rect(), Qt.white)

        if self.image is not None:
            q_img = QImage(self.image.tostring(), self.img_size, self.img_size, QImage.Format_RGB888)
            painter.drawImage(0, 0, q_img)

        painter.end()

    def update_image(self, img_path):
        img = cv2.imread(img_path, cv2.IMREAD_COLOR)
        destRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        destRGB = cv2.resize(destRGB, (self.img_size, self.img_size))
        self.image = destRGB
        self.update()

    def reset(self):
        self.image = None
        self.update()