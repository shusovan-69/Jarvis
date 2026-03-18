from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPainter, QColor, QPen
from PyQt6.QtCore import Qt, QTimer
import sys
import math


class JarvisUI(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Jarvis")
        self.setGeometry(800, 350, 300, 300)

        self.angle = 0
        self.state = "idle"

        self.timer = QTimer()
        self.timer.timeout.connect(self.animate)
        self.timer.start(30)

    def animate(self):
        self.angle += 2
        self.update()

    def set_listening(self):
        self.state = "listening"

    def set_thinking(self):
        self.state = "thinking"

    def set_idle(self):
        self.state = "idle"

    def paintEvent(self, event):

        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        center_x = self.width() / 2
        center_y = self.height() / 2

        if self.state == "listening":
            color = QColor(0, 200, 255)

        elif self.state == "thinking":
            color = QColor(255, 200, 0)

        else:
            color = QColor(100, 100, 100)

        pen = QPen(color)
        pen.setWidth(4)

        painter.setPen(pen)

        radius = 80

        painter.drawEllipse(
            int(center_x - radius),
            int(center_y - radius),
            radius * 2,
            radius * 2
        )

        for i in range(8):

            angle = math.radians(self.angle + i * 45)

            x = center_x + math.cos(angle) * radius
            y = center_y + math.sin(angle) * radius

            painter.drawEllipse(int(x), int(y), 6, 6)


def create_ui():

    app = QApplication(sys.argv)

    ui = JarvisUI()
    ui.show()

    return app, ui