import Settings
import Commands
import os
from PyQt5.QtGui import QImage, QPixmap


def LED_validate(self):
    if(self.Start_spinBox.value() >= self.End_spinBox.value()):
        self.lightConfirm_pushButton.setEnabled(False)
    else:
        self.lightConfirm_pushButton.setEnabled(True)


def desync(self):
    error_img = QImage("../_image/Error.png")
    self.Image_Frame.setPixmap(QPixmap(error_img))
    self.Control_Tab.setEnabled(False)
    self.Misc_Frame.setEnabled(False)


def CV_authenticating(self):
    self.storage_tabWidget.setEnabled(False)
    self.cyverseConfirm_pushButton.setText(
        "Authenticating CyVerse Credentials...")


def CV_authenticated(self):
    self.storage_tabWidget.setEnabled(True)
    if Settings.cyverse_authenticated:
        self.cyverseConfirm_pushButton.setText(
            "CyVerse Credentials Authentication Successful")
    else:
        self.cyverseConfirm_pushButton.setText(
            "CyVerse Credentials Authentication Failed")
    validate_input(self)


def cycle_update(self):
    if Settings.cycle_running:
        self.confirmCycle_pushButton.setText("TERMINATE")
    else:
        self.confirmCycle_pushButton.setText("CONFIRM")
        Commands.deploy_lights(Settings.commands_list)


def test_update(self):
    if Settings.test_running:
        self.schedulerTest_pushButton.setText("TERMINATE")
        self.clinostatSet_pushButton.setEnabled(False)
    else:
        self.schedulerTest_pushButton.setText("Test Cycle")
        self.clinostatSet_pushButton.setEnabled(True)


def schedule_update(self):
    if Settings.sch_running:
        self.schedulerSet_pushButton.setText("TERMINATE")
        self.clinostatSet_pushButton.setEnabled(False)
    else:
        self.schedulerSet_pushButton.setText("Set Cycle")
        self.clinostatSet_pushButton.setEnabled(True)


def imaging_disable(self):
    self.Misc_Frame.setEnabled(False)


def imaging_enable(self):
    self.Misc_Frame.setEnabled(True)


def timelapse_update(self):
    if Settings.timelapse_running:
        if(Settings.storage_mode):
            self.startRoutines_pushButton.setText(
                "End CLOUD Sequence")
        else:
            self.startRoutines_pushButton.setText(
                "End LOCAL Sequence")
        self.Misc_Frame.setEnabled(False)
    else:
        if(Settings.storage_mode):
            self.startRoutines_pushButton.setText("Start CLOUD Sequence")
        else:
            self.startRoutines_pushButton.setText("Start LOCAL Sequence")
        self.Misc_Frame.setEnabled(True)
        self.Progress_Label.setText(
            "Progress: 0/" + str(Settings.total))
        self.Progress_Bar.setValue(0)


def lightingPreset_update(self):
    self.lightingPreset_tabWidget.setEnabled(
        not Settings.lightingPreset_running)
    if not Settings.lightingPreset_running:
        Commands.light_reset(self)


def motionPreset_update(self):
    self.motionPreset_tabWidget.setEnabled(
        not Settings.motionPreset_running)


def update_frame(self, file):
    self.Misc_Frame.setEnabled(True)
    temp_img = QImage(file)
    self.Progress_Label.setText(
        "Progress: " + str(Settings.current + 1) + "/" + str(Settings.total))
    self.Progress_Bar.setValue(Settings.current + 1)
    self.Image_Frame.setPixmap(QPixmap(temp_img))


def update_frame_alt(self, file):
    self.Misc_Frame.setEnabled(True)
    temp_img = QImage(file)
    self.Image_Frame.setPixmap(QPixmap(temp_img))
    if(Settings.image_format):
        os.system("gpicview ../_temp/preview.jpg")
    else:
        os.system("gpicview ../_temp/preview.png")


def update_frame_snap(self, file):
    self.Misc_Frame.setEnabled(True)
    temp_img = QImage(file)
    self.Image_Frame.setPixmap(QPixmap(temp_img))


def validate_input(self):
    if internet():
        self.Cyverse_frame.setEnabled(True)
    else:
        self.Cyverse_frame.setEnabled(False)

    Settings.total = int((Settings.duration * 60) / Settings.interval)
    if(Settings.total > 0 and len(Settings.sequence_name) != 0):
        self.startRoutines_pushButton.setEnabled(True)
    else:
        self.startRoutines_pushButton.setEnabled(False)
    self.Progress_Label.setText(
        "Progress: " + str(Settings.current) + "/" + str(Settings.total))
    if(self.storage_tabWidget.currentIndex() == 1 and Settings.cyverse_authenticated):
        Settings.storage_mode = 1
        self.startRoutines_pushButton.setText("Start CLOUD Sequence")
    else:
        Settings.storage_mode = 0
        self.startRoutines_pushButton.setText("Start LOCAL Sequence")


def sensor_update(self):
    self.temperatureData_label.setText(
        "TEMP={0:0.1f}°C".format(Settings.temperature))
    self.humidityData_label.setText(
        "HMD={0:0.1f}%".format(Settings.humidity))
