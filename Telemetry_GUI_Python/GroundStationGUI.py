# ----------------------------------------------------------------------------------------------------------------------------------
# -- tkinter
from tkinter import *
# -- PIL 
from PIL import ImageTk, Image
# -- Serial
import serial
# -- To Detect Availabe ComPort
import serial.tools.list_ports
# -- Time
import time
# -- Continuous Thread
import continuous_threading
# ----------------------------------------------------------------------------------------------------------------------------------
#                                                  Main Window
# ----------------------------------------------------------------------------------------------------------------------------------

# -- Creating main window widget
mainWindow = Tk()
# -- Configuring window
mainWindow.title("Ground Station: Telemetry")
# -- Main Window Dimensions
mainWindow.geometry("1150x500") 
# -- main Window Icon



# ----------------------------------------------------------------------------------------------------------------------------------
# -- Event Looping
mainWindow.mainloop() 
# ----------------------------------------------------------------------------------------------------------------------------------