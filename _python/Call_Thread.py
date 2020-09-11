import Settings
import Functions
import UI_Update
import Threads


def start_motion_preset(self):
    if not Settings.motionPreset_running:
        try:
            Settings.gravitropism_wait = self.gravitropism_spinBox.value()
            Settings.rotateAmount = self.rotateAmount_spinBox.value()
            Settings.rotateDelay = self.rotateDelay_spinBox.value()
            Settings.motionPreset_mode = self.motionPreset_tabWidget.currentIndex()

            self.MPreset_Thread = Threads.MPreset()
            self.MPreset_Thread.started.connect(
                lambda: UI_Update.motionPreset_update(self))
            self.MPreset_Thread.finished.connect(
                lambda: UI_Update.motionPreset_update(self))
            self.MPreset_Thread.start()

        except Exception as e:
            print(e)
    else:
        Settings.motionPreset_running = False
        UI_Update.motionPreset_update(self)


def start_cycle(self):
    if not Settings.cycle_running:
        try:
            Settings.cycle_time = self.powerCycle_spinBox.value()

            self.Cycle_Thread = Threads.Cycle()
            self.Cycle_Thread.started.connect(
                lambda: UI_Update.cycle_update(self))
            self.Cycle_Thread.start()

        except Exception as e:
            print(e)
    else:
        Settings.cycle_running = False
        UI_Update.cycle_update(self)


def schedule_test(self):
    if not Settings.test_running:
        try:
            Settings.angle_1 = self.rotate1_spinbox.value()
            Settings.angle_2 = self.rotate2_spinbox.value()
            self.Test_Thread = Threads.Test()
            self.Test_Thread.started.connect(
                lambda: UI_Update.test_update(self))
            self.Test_Thread.finished.connect(
                lambda: UI_Update.test_update(self))
            self.Test_Thread.start()
        except Exception as e:
            print(e)
    else:
        Settings.test_running = False
        UI_Update.test_update(self)


def schedule_run(self):
    if not Settings.sch_running:
        try:
            Settings.angle_1 = self.rotate1_spinbox.value()
            Settings.angle_2 = self.rotate2_spinbox.value()
            Settings.delay_1 = self.wait1_spinbox.value()
            Settings.delay_2 = self.wait2_spinbox.value()

            self.Schedule_Thread = Threads.Schedule()
            self.Schedule_Thread.started.connect(
                lambda: UI_Update.schedule_update(self))
            self.Schedule_Thread.start()
        except Exception as e:
            print(e)
    else:
        Settings.sch_running = False
        UI_Update.schedule_update(self)


def start_snapshot(self):
    try:
        Functions.Camera_update(self)
        self.Snap_Thread = Threads.Snap()
        self.Snap_Thread.started.connect(
            lambda: UI_Update.imaging_disable(self))
        self.Snap_Thread.finished.connect(
            lambda: UI_Update.update_frame_snap(self, "../_temp/snapshot.jpg"))
        self.Snap_Thread.start()

    except Exception as e:
        print(e)


def CV_authenticate(self):
    Settings.cyverseUsername = self.cyverseUsername_lineEdit.text()
    Settings.cyversePassword = self.cyversePassword_lineEdit.text()
    try:
        self.Auth_Thread = Threads.Auth()
        self.Auth_Thread.started.connect(
            lambda: UI_Update.CV_authenticating(self))
        self.Auth_Thread.finished.connect(
            lambda: UI_Update.CV_authenticated(self))
        self.Auth_Thread.start()

    except Exception as e:
        print(e)


def start_livefeed(self):
    try:
        Settings.livetime = self.liveFeed_spinBox.value()
        self.livefeed_Thread = Threads.Live()
        self.livefeed_Thread.started.connect(
            lambda: UI_Update.imaging_disable(self))
        self.livefeed_Thread.finished.connect(
            lambda: UI_Update.imaging_enable(self))
        self.livefeed_Thread.start()

    except Exception as e:
        print(e)


def start_preview(self):
    try:
        Functions.Camera_update(self)
        self.Preview_Thread = Threads.Preview()
        self.Preview_Thread.started.connect(
            lambda: UI_Update.imaging_disable(self))
        if(Settings.image_format):
            self.Preview_Thread.finished.connect(
                lambda: UI_Update.update_frame_alt(self, "../_temp/preview.jpg"))
        else:
            self.Preview_Thread.finished.connect(
                lambda: UI_Update.update_frame_alt(self, "../_temp/preview.png"))
        self.Preview_Thread.start()

    except Exception as e:
        print(e)


def rotate_image(self):
    try:
        Functions.Camera_update(self)
        Settings.rotation += 1
        self.Snap_Thread = Threads.Snap()
        self.Snap_Thread.started.connect(
            lambda: UI_Update.imaging_disable(self))
        self.Snap_Thread.finished.connect(
            lambda: UI_Update.update_frame(self, "../_temp/snapshot.jpg"))
        self.Snap_Thread.start()

    except Exception as e:
        print(e)


def start_sequence(self):

    if(Settings.image_format):
        Settings.file = Settings.full_dir + "/" + Settings.sequence_name + "_%04d.jpg"
    else:
        Settings.file = Settings.full_dir + "/" + Settings.sequence_name + "_%04d.png"
    self.Progress_Bar.setMaximum(Settings.total)

    try:
        if not Settings.timelapse_running:
            Functions.Camera_update(self)

            self.Imaging_Thread = Threads.Image()
            self.Imaging_Thread.started.connect(
                lambda: UI_Update.timelapse_update(self))
            self.Imaging_Thread.finished.connect(
                lambda: UI_Update.timelapse_update(self))
            self.Imaging_Thread.capturing.connect(
                lambda: UI_Update.imaging_disable(self))
            self.Imaging_Thread.complete.connect(
                lambda: UI_Update.update_frame(self, Settings.current_image))
            self.Imaging_Thread.start()
        else:
            Settings.timelapse_running = False
            UI_Update.timelapse_update(self)

    except Exception as e:
        print(e)

    if Settings.storage_mode and Settings.cyverse_authenticated:
        try:
            if Settings.cyverse_authenticated:
                print("Starting Cyverse Sync Thread")
                self.Cyverse_Thread = Threads.Cyverse()
                self.Cyverse_Thread.start()

        except Exception as e:
            print(e)


def sensor_init(self):
    try:
        self.Sensor_Thread = Threads.Sensor()
        self.Sensor_Thread.update.connect(
            lambda: UI_Update.sensor_update(self))
        self.Sensor_Thread.start()
    except Exception as e:
        print(e)
