import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QSlider
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.is_day_mode = True
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(600, 400, 300, 200)

        self.setWindowOpacity(0.7)

        vbox = QVBoxLayout()

        self.time_label.setAlignment(Qt.AlignCenter)
        self.toggle_button = QPushButton("Switch to Night Mode", self)
        self.toggle_button.clicked.connect(self.toggle_mode)

        self.opacity_slider = QSlider(Qt.Horizontal, self)
        self.opacity_slider.setMinimum(30)
        self.opacity_slider.setMaximum(100)
        self.opacity_slider.setValue(70)
        self.opacity_slider.setTickInterval(10)
        self.opacity_slider.setTickPosition(QSlider.TicksBelow)
        self.opacity_slider.valueChanged.connect(self.change_opacity)

        vbox.addWidget(self.time_label)
        vbox.addWidget(self.toggle_button)
        vbox.addWidget(self.opacity_slider)
        self.setLayout(vbox)

        font_id = QFontDatabase.addApplicationFont("DS-DIGIT.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family, 150)
        self.time_label.setFont(my_font)

        self.update_stylesheet()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.update_time()

    def update_stylesheet(self):
        if self.is_day_mode:
            self.time_label.setStyleSheet("font-size: 150px; color: #227037;")
            self.setStyleSheet("background-color: white;")
            self.toggle_button.setText("Switch to Night Mode")
            self.toggle_button.setStyleSheet("background-color: #227037; color: white; font-size: 20px; padding: 10px;")
        else:
            self.time_label.setStyleSheet("font-size: 150px; color: #A0A0A0;")
            self.setStyleSheet("background-color: #2C2C2C;")
            self.toggle_button.setText("Switch to Day Mode")
            self.toggle_button.setStyleSheet("background-color: #A0A0A0; color: black; font-size: 20px; padding: 10px;")

    def toggle_mode(self):
        self.is_day_mode = not self.is_day_mode
        self.update_stylesheet()

    def change_opacity(self, value):
        self.setWindowOpacity(value / 100)

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss")
        self.time_label.setText(current_time)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())
