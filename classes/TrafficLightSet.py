from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class TrafficLightSet:
    def __init__(this, set_number, green_GPIO, yellow_GPIO, red_GPIO, coordinates, uses_mcp):
        this.set_number = set_number
        this.green_GPIO = green_GPIO
        this.yellow_GPIO = yellow_GPIO
        this.red_GPIO = red_GPIO
        this.coordinates = coordinates
        this.uses_mcp = uses_mcp
        this.is_green_active = False
        this.active_image = PhotoImage(file="/home/pi/Desktop/maquette_gui/images/red_light.png")

