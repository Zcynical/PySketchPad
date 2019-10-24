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
        self.uiSketch = Canvas(img_size=img_size, scale=self.scale, nc=nc, pen_width=self.brushWidth)
        # nc = 3
        # self.uiSketch = UISketch(img_size=512,scale=self.scale,nc=nc,width=self.brushWidth)
        # self.uir = UIRecorder()
        # self.img_size = img_size
        # self.interactive=interactive
        # self.color = QColor(0,0,0)
        #
        self.rgb_color = 0
        #
        # self.setMouseTracking(True)
        # self.frame_id = -1
        # self.image_id = 0
        # self.shadow_image=None
        # self.move(win_size,win_size)
        # self.pos = QPoint(0,0)
        # self.isPressed = False
        # self.show_ui=False #True
        # self.moving = False
        # self.warping = False
        # self.warp_start = None
        # self.warp_end = None
        # self.warp_control_points = []
        # self.prev_brushWidth = None
        # self.scribbling = True
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
        print(self.pos)
        if self.isPressed:
            self.points.append(self.pos)
            self.uiSketch.update(self.points, self.rgb_color)
            self.update()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.fillRect(event.rect(), Qt.white)
        painter.setRenderHint(QPainter.Antialiasing)
        # #self.uiSketch.set_shadow_img(self.shadow_image)
        im = self.uiSketch.get_img()

        if im is not None:
            bigim = cv2.resize(im, (self.nps, self.nps))
            qImg = QImage(bigim.tostring(), self.nps, self.nps, QImage.Format_RGB888)
            painter.drawImage(0, 0, qImg)
