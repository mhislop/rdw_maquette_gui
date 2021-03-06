from seeders.TrafficLightSetSeeder import TrafficLightSetSeeder
from classes.TrafficLightSet import TrafficLightSet
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import RPi.GPIO as GPIO
import time
import board
import busio
from digitalio import Direction
from adafruit_mcp230xx.mcp23017 import MCP23017
import threading
import boot 
import matrix.boot

# MCP config
i2c = busio.I2C(board.SCL, board.SDA)
mcp = MCP23017(i2c)

# GUI config
root = Tk()
root.title("GUI Maquette")
root.resizable(False, False)
window_height = 700
window_width = 700

# Center window on screen
def center_screen():
    global screen_height, screen_width, x_cordinate, y_cordinate

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
center_screen()

# Set background
bg_image = Image.open("/home/pi/Desktop/rdw_maquette_gui/images/Kruispunt.png")
bg_image = bg_image.resize((700, 700))
bg_image = ImageTk.PhotoImage(bg_image)

canvas_bg = Canvas(root, width=700, height=700)
canvas_bg.pack(fill = "both", expand = False)
canvas_bg.create_image(0, 0, image=bg_image, anchor="nw")

traffic_light_sets = TrafficLightSetSeeder()

# Setup GPIO pins for output
def setup_pins():
    # Setup GPIO pins
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    for set in traffic_light_sets:
        if set.uses_mcp is False:
            GPIO.setup(set.green_GPIO, GPIO.OUT)
            GPIO.setup(set.yellow_GPIO, GPIO.OUT)
            GPIO.setup(set.red_GPIO, GPIO.OUT)
            # Activate green on all traffic lights
            GPIO.output(set.green_GPIO, GPIO.LOW)
            GPIO.output(set.yellow_GPIO, GPIO.LOW)
            GPIO.output(set.red_GPIO, GPIO.HIGH)
        else:
            mcp.get_pin(set.green_GPIO).direction = Direction.OUTPUT
            mcp.get_pin(set.yellow_GPIO,).direction = Direction.OUTPUT
            mcp.get_pin(set.red_GPIO).direction = Direction.OUTPUT
            # Activate green on all traffic lights
            mcp.get_pin(set.green_GPIO).value = False
            mcp.get_pin(set.yellow_GPIO).value = False
            mcp.get_pin(set.red_GPIO).value = True

# Button click event
def toggle_traffic_light(set_number):
    for set in traffic_light_sets:
        if set.set_number == set_number:
            if set.is_green_active:
                # Switch traffic light to red #

                # Turn of green light
                if set.uses_mcp is False:
                    GPIO.output(set.green_GPIO, GPIO.LOW)
                else:
                    mcp.get_pin(set.green_GPIO).value = False

                # Turn on yellow light for 2 seconds
                if set.uses_mcp is False:
                    GPIO.output(set.yellow_GPIO, GPIO.HIGH)
                else:
                    mcp.get_pin(set.yellow_GPIO).value = True
                time.sleep(2)

                # Create new traffic light button to update UI
                traffic_light_sets[set_number].active_image = PhotoImage(file="/home/pi/Desktop/rdw_maquette_gui/images/yellow_light.png")
                traffic_light_button = Button(root)
                traffic_light_button.config(image=set.active_image)
                traffic_light_button.pack()
                canvas_bg.create_window(set.coordinates[0], set.coordinates[1], anchor="nw", window=traffic_light_button)
               
                # Turn on red light
                if set.uses_mcp is False:
                    GPIO.output(set.yellow_GPIO, GPIO.LOW)
                else:
                    mcp.get_pin(set.yellow_GPIO).value = False

                if set.uses_mcp is False:
                    GPIO.output(set.red_GPIO, GPIO.HIGH)
                else:
                    mcp.get_pin(set.red_GPIO).value = True
                set.is_green_active = False

                # Update UI 
                traffic_light_sets[set_number].active_image = PhotoImage(file="/home/pi/Desktop/rdw_maquette_gui/images/red_light.png")
                pack_button(set)

                print("Verkeerslichtset {} staat op rood".format(set_number))
            else:
                # Switch traffic light to green #
                if set.uses_mcp is False:
                    GPIO.output(set.red_GPIO, GPIO.LOW)
                else:
                    mcp.get_pin(set.red_GPIO).value = False

                if set.uses_mcp is False:
                    print("groen gaat aan")
                    print(set.green_GPIO)
                    GPIO.output(set.green_GPIO, GPIO.HIGH)
                else:
                    mcp.get_pin(set.green_GPIO).value = True

                # Update UI
                traffic_light_sets[set_number].active_image = PhotoImage(file="/home/pi/Desktop/rdw_maquette_gui/images/green_light.png")
                set.is_green_active = True
                pack_button(set)

                print("Verkeerslichtset {} staat op groen".format(set_number))

# Runs when traffic light is clicked
def traffic_light_click(linked_to):
    t1 = threading.Thread(target=toggle_traffic_light, args=[linked_to[0]])
    t2 = threading.Thread(target=toggle_traffic_light, args=[linked_to[1]])
    t1.start()
    t2.start()


# Create traffic light button
def pack_button(set):
    traffic_light_button = Button(root, command=lambda:traffic_light_click(set.linked_to))
    traffic_light_button.config(image=set.active_image)
    traffic_light_button.pack()
    canvas_bg.create_window(set.coordinates[0], set.coordinates[1], anchor="nw", window=traffic_light_button) 

# Setup traffic light buttons on canvas
def setup_buttons():
    for x in range(8):
        set = traffic_light_sets[x]
        pack_button(set)
        
# Initialize
matrix.boot.start()
setup_pins()
setup_buttons()
root.mainloop()

