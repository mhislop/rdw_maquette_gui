import time
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import sh1106
from gpiozero import DistanceSensor
import threading

devicedistance = 0.205
device2distance = 0.21

start_time_1 = 0
end_time_1 = 0

start_time_2 = 0
end_time_2 = 0

def speedmas1():
    serial = i2c(port=1, address=0x3C)
    device = sh1106(serial)
    sensor1 = DistanceSensor(echo=12, trigger=25)
    sensor2 = DistanceSensor(echo=23, trigger=24)

    while True:
        time.sleep(0.1)
        if sensor1.distance < 0.30:
            global start_time_1
            start_time_1 = time.time()
            print("1ste aan")
        if start_time_1 > 0 and sensor2.distance < 0.30:
            print("2nd aan")
            global end_time_1
            end_time_1 = time.time()
            if start_time_1 > 0 and end_time_1 > 0:
                time_lapsed = end_time_1 - start_time_1
                speed_calc = round(100 * (devicedistance2 / time_lapsed))
                speed_display = str(speed_calc) + " CM/S"
                print(time_lapsed)
                print(speed_display)

                with canvas(device) as draw:
                    draw.rectangle(device.bounding_box, outline="white", fill="Black")
                    draw.text((30,25), speed_display, fill="white")
                start_time_1 = 0
                end_time_1 = 0

def speedmas2():
    serial = i2c(port=1, address=0x3D)
    device = sh1106(serial)
    sensor3 = DistanceSensor(echo=16, trigger=20)
    sensor4 = DistanceSensor(echo=8, trigger=7)

    while True:
        time.sleep(0.1)
        if sensor3.distance < 0.30:
            global start_time_2
            start_time_2 = time.time()
            print("3de aan")
        if start_time_2 > 0 and sensor4.distance < 0.30:
            print("4de aan")
            global end_time_2
            end_time_2 = time.time()
            if start_time_2 > 0 and end_time_2 > 0:
                time_lapsed = end_time_2 - start_time_2
                speed_calc = round(100 * (devicedistance / time_lapsed))
                speed_display = str(speed_calc) + " CM/S"
                print(time_lapsed)
                print(speed_display)

                with canvas(device) as draw:
                    draw.rectangle(device.bounding_box, outline="white", fill="Black")
                    draw.text((30,25), speed_display, fill="white")
                start_time_2 = 0
                end_time_2 = 0

def start():
    t1 = threading.Thread(target=speedmas1)
    t1.start()
    print("Matrixbord 1 geactiveerd")
    t2 = threading.Thread(target=speedmas2)
    t2.start()
    print("Matrixbord 2 geactiveerd")
