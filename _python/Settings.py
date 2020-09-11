import serial
import time
import UI_Update
import Adafruit_DHT


def init(self):

    global base_Connected
    base_Connected = True

    try:
        global ASD
        ASD = serial.Serial('/dev/ttyS0', 9600)

    except:
        UI_Update.desync(self)

    global DHT_SENSOR
    DHT_SENSOR = Adafruit_DHT.DHT22

    global humidity
    humidity = 0

    global temperature
    temperature = 0

    global commands_list
    commands_list = []

    global send_commands_list
    send_commands_list = []

    global current_CMD
    current_CMD = ""

    global cyverseUsername
    cyverseUsername = ""

    global cyversePassword
    cyversePassword = ""

    global cycle_running
    cycle_running = False

    global IR_stat
    IR_stat = False

    global cycle_time
    cycle_time = 60

    global sch_running
    sch_running = False

    global log_sensor
    log_sensor = False

    global test_running
    test_running = False

    global clino_running
    clino_running = False

    global timelapse_running
    timelapse_running = False

    global cyverse_authenticated
    cyverse_authenticated = False

    global angle_1
    angle_1 = 0
    global angle_2
    angle_2 = 0
    global delay_1
    delay_1 = 0
    global delay_2
    delay_2 = 0

    global rpm
    RPM = 5

    global rotation
    rotation = 2

    global AOI_X
    AOI_X = 0
    global AOI_Y
    AOI_Y = 0
    global AOI_W
    AOI_W = 1
    global AOI_H
    AOI_H = 1

    global sample_time
    sample_time = 1

    global livetime
    livetime = 1
    global x_resolution
    x_resolution = 2464
    global y_resolution
    y_resolution = 2464

    global sequence_name
    sequence_name = ""

    global default_dir
    default_dir = "/home/pi/Desktop"

    global date
    date = time.strftime('%m_%d_%Y')

    global cyverse_data_path
    cyverse_data_path = "../_temp/.cyverse_data.txt"

    global prelog_dir
    prelog_dir = "/home/pi/Desktop/sensor_log/"

    global log_dir
    log_dir = "/home/pi/Desktop/sensor_log/" + date

    global full_dir
    full_dir = ""

    global interval
    interval = 10

    global duration
    duration = 1

    global total
    total = 6

    global image_format
    image_format = 1

    global current
    current = 0

    global storage_mode
    storage_mode = 0

    global file_list
    file_list = []

    global file
    file = ""

    global current_image
    current_image = ""

    global germinationColor
    germinationColor = 0

    global germinationDirection
    germinationDirection = 0

    global cycleTime
    cycleTime = 24

    global stripLength
    stripLength = 5

    global gravitropism_wait
    gravitropism_wait = 120

    global rotateAmount
    rotateAmount = 90

    global rotateDelay
    rotateDelay = 120

    global motionPreset_mode
    lightingPreset_mode = 0

    global lightingPreset_running
    lightingPreset_running = False

    global motionPreset_running
    motionPreset_running = False

    global cpuserial
    f = open('/proc/cpuinfo', 'r')
    for line in f:
        if line[0:6] == 'Serial':
            cpuserial = line[10:26]
    f.close()
    print(cpuserial)

    global link
    link = ""
