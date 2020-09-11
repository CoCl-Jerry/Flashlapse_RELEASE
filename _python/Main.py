# import basic libraries
import sys
import time

# import settings
import Settings

# import custom functions
import Commands
import Threads
import Functions
import Call_Thread

# import UI functions
import UI_Update

# import Qt content
from PyQt5.QtWidgets import QMainWindow, QApplication

# import generated UI
import FlashLapse_UI

# global variables
default_dir = "/home/pi/Desktop"
date = time.strftime('%m_%d_%Y')

# create class for Raspberry Pi GUI


class MainWindow(QMainWindow, FlashLapse_UI.Ui_MainWindow):
 # access variables inside of the UI's file

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)  # gets defined in the UI file
        Settings.init(self)
        Call_Thread.sensor_init(self)
        Commands.startup()

        self.Start_spinBox.valueChanged.connect(
            lambda: UI_Update.LED_validate(self))
        self.End_spinBox.valueChanged.connect(
            lambda: UI_Update.LED_validate(self))

        self.lightConfirm_pushButton.clicked.connect(
            lambda: Commands.light_confirm(self))
        self.lightReset_pushButton.clicked.connect(
            lambda: Commands.light_reset(self))

        self.disco_pushButton.clicked.connect(lambda: Commands.disco_run(self))
        self.rainbow_pushButton.clicked.connect(
            lambda: Commands.rainbow_run(self))
        self.sundial_pushButton.clicked.connect(
            lambda: Commands.sundial_run(self))
        self.pulse_pushButton.clicked.connect(lambda: Commands.pulse_run(self))

        self.confirmCycle_pushButton.clicked.connect(
            lambda: Call_Thread.start_cycle(self))

        self.schedulerTest_pushButton.clicked.connect(
            lambda: Call_Thread.schedule_test(self))
        self.schedulerSet_pushButton.clicked.connect(
            lambda: Call_Thread.schedule_run(self))
        self.motorSpeed_slider.valueChanged.connect(
            lambda: Commands.motorSliderChange(self))
        self.motorSpeed_slider.sliderReleased.connect(
            lambda: Commands.motorSliderRelease(self))

        self.clinostatSet_pushButton.clicked.connect(
            lambda: Commands.clinoStart(self))
        self.snapshot_pushButton.clicked.connect(
            lambda: Call_Thread.start_snapshot(self))
        self.liveFeed_pushButton.clicked.connect(
            lambda: Call_Thread.start_livefeed(self))
        self.preview_pushButton.clicked.connect(
            lambda: Call_Thread.start_preview(self))

        self.rotate_pushButton.clicked.connect(
            lambda: Call_Thread.rotate_image(self))

        self.xAxis_horizontalSlider.valueChanged.connect(
            lambda: Functions.zoomSliderChange(self))
        self.xAxis_horizontalSlider.sliderReleased.connect(
            lambda: Call_Thread.start_snapshot(self))

        self.yAxis_horizontalSlider.valueChanged.connect(
            lambda: Functions.zoomSliderChange(self))
        self.yAxis_horizontalSlider.sliderReleased.connect(
            lambda: Call_Thread.start_snapshot(self))

        self.motorConfirm_pushButton.clicked.connect(
            lambda: Commands.motor_rotate(self.motor_spinBox.value()))

        self.imageTitle_lineEdit.textChanged.connect(
            lambda: Functions.IST_Edit(self))
        self.addDate_pushButton.clicked.connect(
            lambda: Functions.add_date(self))
        self.ImageInterval_spinBox.valueChanged.connect(
            lambda: Functions.ICI_Change(self))
        self.imageDuration_spinBox.valueChanged.connect(
            lambda: Functions.ISD_Change(self))
        self.directory_pushButton.clicked.connect(
            lambda: Functions.select_directory(self))

        self.storage_tabWidget.currentChanged.connect(
            lambda: UI_Update.validate_input(self))
        self.startRoutines_pushButton.clicked.connect(
            lambda: Call_Thread.start_sequence(self))

        self.JPG_radioButton.toggled.connect(
            lambda: Functions.img_format(self))
        self.PNG_radioButton.toggled.connect(
            lambda: Functions.img_format(self))

        self.lightingPreset_pushButton.clicked.connect(
            lambda: Functions.start_lighting_preset(self))
        self.MotionPreset_pushButton.clicked.connect(
            lambda: Call_Thread.start_motion_preset(self))

        self.IR_pushButton.clicked.connect(
            lambda: Commands.IR_toggle(self))

        self.log_pushButton.clicked.connect(
            lambda: Functions.sensor_log(self))

        self.sample_spinBox.valueChanged.connect(
            lambda: Functions.sample_change(self))

        self.cyverseDefault_pushButton.clicked.connect(
            lambda: Functions.Cyverse_Save(self))
        self.cyverseConfirm_pushButton.clicked.connect(
            lambda: Call_Thread.CV_authenticate(self))
        try:
            with open(Settings.cyverse_data_path, "r") as fh:
                self.cyverseUsername_lineEdit.setText(
                    fh.readline().strip('\n'))
                self.cyversePassword_lineEdit.setText(
                    fh.readline().strip('\n'))
            fh.close()
        except FileNotFoundError:
            pass


# main function


def main():
    # a new app instance
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()

    # without this, the script exits immediately.
    sys.exit(app.exec_())


# python bit to figure how who started This
if __name__ == "__main__":
    main()
