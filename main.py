from PyQt5.QtWidgets import * #QWidget, QApplication
from PyQt5.QtGui import * #QPainter, QPainterPath
from PyQt5.QtCore import * #Qt
import sys
from sketch_viewer import SketchViewer
from image_viewer import ImageViewer

class SGui(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.sketchWidget = SketchViewer()
        self.sketchWidget.setFixedSize(512, 512)

        self.sketchWidgetBox = QGroupBox()
        self.sketchWidgetBox.setTitle('Sketch Pad')
        vbox_sketch = QVBoxLayout()
        vbox_sketch.addWidget(self.sketchWidget)
        self.sketchWidgetBox.setLayout(vbox_sketch)



        self.feedbackWidgetBox = QGroupBox()
        self.feedbackWidgetBox.setTitle('Visual Feedback')

        self.feedbackWidget = ImageViewer()
        self.feedbackWidget.setFixedSize(512, 512)

        vbox_feedback = QVBoxLayout()
        vbox_feedback.addWidget(self.feedbackWidget)
        self.feedbackWidgetBox.setLayout(vbox_feedback)

        hbox = QHBoxLayout()
        hbox.addWidget(self.sketchWidgetBox)
        hbox.addWidget(self.feedbackWidgetBox)
        self.setLayout(hbox)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SGui()
    window.setWindowTitle('SketchTester')
    #window.setWindowFlags(window.windowFlags() & ~Qt.WindowMaximizeButtonHint)   # fix window siz
    window.show()
    sys.exit(app.exec_())