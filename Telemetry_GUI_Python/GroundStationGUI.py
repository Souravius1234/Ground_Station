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
#                                       Serial Communication Initialization
# ----------------------------------------------------------------------------------------------------------------------------------

# -- [Step 1] -> Detect availabe ComPort and Initialize Serial Communication
ports = serial.tools.list_ports.comports()
for port, desc, hwid in sorted(ports):
        ComPortAvailable = port
#       print for debugging        
        #print(ComPortAvailable)

# -- [Step 2] -> Initialize Serial Communication
dataFromSerial = serial.Serial(ComPortAvailable,9600, timeout = 1) 

# To hold raw telemetry data [directly from serial]
global rawData
# ----------------------------------------------------------------------------------------------------------------------------------
#                                               Frame and Labels
# ----------------------------------------------------------------------------------------------------------------------------------

# -- First layer of main Window [Label Frames: Controls, Logo, Exit]
frame_First_Layer = Frame(mainWindow, width = 1150, height = 250, relief = "raised")
frame_First_Layer.grid(row = 0, column = 0, columnspan=3)
# -- [Label Frame: Controls]
frame_Controls = LabelFrame(frame_First_Layer, text = "Controls",borderwidth = 2,relief = "raised",padx = 5,pady = 5)
frame_Controls.grid(row = 0, column = 0, padx = 25, pady = 25)
# -- [Label Frame: Logo]
# -- Image
imgLogo = ImageTk.PhotoImage(Image.open("logo_Lalit_Kumar.png"))
labelLogoImg = Label(image = imgLogo)
# -- Frame
LebelLogo = Label(frame_First_Layer, text = "l",borderwidth = 2,relief = "flat", height = 130, width = 850,image = imgLogo)
LebelLogo.grid(row = 0, column = 1, padx = 1, pady = 40) 
# -- [Label Frame: Exit]
frameExit = LabelFrame(frame_First_Layer, text = "Exit",borderwidth = 2,relief = "raised",padx = 5,pady = 5)
frameExit.grid(row = 0, column = 2, padx = 25, pady = 25) 

# -- [Label: Port Availabe Display]
label_port = Label(frame_Controls, text = "Port :", width = 4, height = 1)
label_port.grid(row = 1, column = 0)
# -- Display Connected ComPort
label_port = Label(frame_Controls, text = ComPortAvailable, width = 6, height = 1)
label_port.grid(row = 1, column = 1)

# -- Second layer of main Window [Label Frames: Telemetry Data]
frame_Second_Layer = Frame(mainWindow, width = 1150, height = 250)
frame_Second_Layer.grid(row = 1, column = 0, columnspan=3)
# -- Telemetry Data Name Fields
# -- GPS FIX
labelName_GPSFix = Label(frame_Second_Layer, text = "GPS Fix :", width = 14, height = 1, anchor="w")
labelName_GPSFix.grid(row = 0, column = 0)
# -- GPS QUALITY
labelName_GPSQuality = Label(frame_Second_Layer, text = "GPS Quality :", width = 14, height = 1, anchor="w")
labelName_GPSQuality.grid(row = 1, column = 0)
# -- GPS SATELLITES
labelName_GPSSats = Label(frame_Second_Layer, text = "GPS Satellites :", width = 14, height = 1, anchor="w")
labelName_GPSSats.grid(row = 2, column = 0)
# -- GPS SPEED
labelName_GPSSpeed = Label(frame_Second_Layer, text = "GPS Speed (m/s) :", width = 14, height = 1, anchor="w")
labelName_GPSSpeed.grid(row = 3, column = 0)
# -- GPS LATITUDE
labelName_GPSLatitude = Label(frame_Second_Layer, text = "GPS Latitude :", width = 14, height = 1, anchor="w")
labelName_GPSLatitude.grid(row = 0, column = 2, padx = 8)
# -- GPS LONGITUDE
labelName_GPSLongitude = Label(frame_Second_Layer, text = "GPS Longitude :", width = 14, height = 1, anchor="w")
labelName_GPSLongitude.grid(row = 1, column = 2, padx = 8)
# -- GPS ALTITUDE
labelName_GPSAltitude = Label(frame_Second_Layer, text = "GPS Altitude (m) :", width = 14, height = 1, anchor="w")
labelName_GPSAltitude.grid(row = 2, column = 2, padx = 8)
# -- TEMPERATURE
labelName_Temperature = Label(frame_Second_Layer, text = "Temperature (°C) :", width = 14, height = 1, anchor="w")
labelName_Temperature.grid(row = 0, column = 5, padx = 8)
# -- BAROMETRIC ALTITUDE
labelName_BaroAltitude = Label(frame_Second_Layer, text = "Altitude (m) :", width = 14, height = 1, anchor="w")
labelName_BaroAltitude.grid(row = 1, column = 5, padx = 8)
# -- VOLTAGE LEVEL 3V
labelName_3vLevel = Label(frame_Second_Layer, text = "3v Level (v) :", width = 14, height = 1, anchor="w")
labelName_3vLevel.grid(row = 2, column = 5, padx = 8)
# -- VOLTAGE LEVEL 5V
labelName_5vLevel = Label(frame_Second_Layer, text = "5v Level (v) :", width = 14, height = 1, anchor="w")
labelName_5vLevel.grid(row = 3, column = 5, padx = 8)
# -- Orientation X
labelName_Xaxis = Label(frame_Second_Layer, text = "X Axis:", width = 8, height = 1, anchor="w")
labelName_Xaxis.grid(row = 0, column = 7, padx = 8)
# -- Orientation Y
labelName_Yaxis = Label(frame_Second_Layer, text = "Y Axis:", width = 8, height = 1, anchor="w")
labelName_Yaxis.grid(row = 1, column = 7, padx = 8)
# -- Orientation Z
labelName_Zaxis = Label(frame_Second_Layer, text = "Z Axis:", width = 8, height = 1, anchor="w")
labelName_Zaxis.grid(row = 2, column = 7, padx = 8)

# -- Third layer of main Window [Frame: Indicators, Raw Data, others ]
frame_Third_Layer = Frame(mainWindow, width = 1150, height = 250)
frame_Third_Layer.grid(row = 2, column = 0, columnspan=3)

# -- [Label Frame: Raw Telemetry Data]
Labelframe_RawData = LabelFrame(frame_Third_Layer, text = "Raw Telemetry Data", width = 50, height = 1)
Labelframe_RawData.grid(row = 0, column = 0, padx = 25, pady = 20)
# -- Raw Data
labelName_RawData = Label(Labelframe_RawData, text = "<,data,>", width = 80, height = 2, anchor="center")
labelName_RawData.grid(row = 0, column = 0)   

# ----------------------------------------------------------------------------------------------------------------------------------
#                                                       Functions
# ----------------------------------------------------------------------------------------------------------------------------------

# Start reading and displaying Telemetry Data
def startTelemetry():    
#   Update Start/Stop indicator Color [START = GREEN lightish Shade #00E600]
    button_StartStopIndicator = Button(frame_Controls, width = 2, height = 1, bg = "#00E600")
    button_StartStopIndicator.grid(row = 0, column = 2)
#   Telemetry variables           
    global receivedTelemetry
    receivedTelemetry = dataFromSerial.readline().decode('windows-1252')
#   Removing \r\n from the end of the received data     
    receivedTelemetry = receivedTelemetry.rstrip("\r\n")
    global rawData
    rawData = receivedTelemetry
#   Print Raw Telemetry for debugging    
    #print(receivedTelemetry)
    global splitData
    splitData = receivedTelemetry.split(",")
#   Print Split data for debugging
   #print(splitData)
    if len(splitData) > 1:
        if (splitData[0] == "<") and (splitData[17] == ">"):
#       Displaying Received Data        
        #   Data_1 = GPS_Fix
            labelVal_GPSFix = Label(frame_Second_Layer, text = splitData[1], width = 12, height = 1, anchor="w", relief = "sunken" )
            labelVal_GPSFix.grid(row = 0, column = 1)
        #   Data_2 = GPS_Quality
            labelVal_GPSQuality = Label(frame_Second_Layer, text = splitData[2], width = 12, height = 1, anchor="w", relief = "sunken" )
            labelVal_GPSQuality.grid(row = 1, column = 1)
        #   Data_3 = GPS_Satellites
            labelVal_GPSSats = Label(frame_Second_Layer, text = splitData[3], width = 12, height = 1, anchor="w", relief = "sunken" )
            labelVal_GPSSats.grid(row = 2, column = 1)
        #   Data_4 = GPS_Speed
            labelVal_GPSSpeed = Label(frame_Second_Layer, text = splitData[4], width = 12, height = 1, anchor="w", relief = "sunken" )
            labelVal_GPSSpeed.grid(row = 3, column = 1)
        #   Data_5 = GPS_Latitude
            labelVal_GPSLatitude = Label(frame_Second_Layer, text = splitData[5], width = 12, height = 1, anchor="w", relief = "sunken" )
            labelVal_GPSLatitude.grid(row = 0, column = 3)
        #   Data_6 = GPS_Longitude
            labelVal_GPSLongitude = Label(frame_Second_Layer, text = splitData[6], width = 12, height = 1, anchor="w", relief = "sunken" )
            labelVal_GPSLongitude.grid(row = 1, column = 3)
        #   Data_7 = GPS_Altitude
            labelVal_GPSAltitude = Label(frame_Second_Layer, text = splitData[7], width = 12, height = 1, anchor="w", relief = "sunken" )
            labelVal_GPSAltitude.grid(row = 2, column = 3)
        #   Data_8 = GPS_Latitude_Direction (Heading)
            labelVal_GPSLati_Dir = Label(frame_Second_Layer, text = splitData[8], width = 12, height = 1, anchor="w", relief = "sunken" )
            labelVal_GPSLati_Dir.grid(row = 0, column = 4)
        #   Data_9 = GPS_Longitude_Direction (Heading)
            labelVal_GPSLong_Dir = Label(frame_Second_Layer, text = splitData[9], width = 12, height = 1, anchor="w", relief = "sunken" )
            labelVal_GPSLong_Dir.grid(row = 1, column = 4)
        #   Data_10 = Temperature
            labelVal_Temperature = Label(frame_Second_Layer, text = splitData[10], width = 12, height = 1, anchor="w", relief = "sunken" )
            labelVal_Temperature.grid(row = 0, column = 6)
        #   Data_11 = Altitude
            labelVal_BaroAltitude = Label(frame_Second_Layer, text = splitData[11], width = 12, height = 1, anchor="w", relief = "sunken" )
            labelVal_BaroAltitude.grid(row = 1, column = 6)
        #   Data_12 = Voltage Level 3v
            labelVal_3vLevel = Label(frame_Second_Layer, text = splitData[12], width = 12, height = 1, anchor="w", relief = "sunken" )
            labelVal_3vLevel.grid(row = 2, column = 6)
        #   Data_13 = Voltage Level 5v
            labelVal_5vLevel = Label(frame_Second_Layer, text = splitData[13], width = 12, height = 1, anchor="w", relief = "sunken" )
            labelVal_5vLevel.grid(row = 3, column = 6)
        #   Data_14 = Orientation X Axis
            labelVal_Xaxis = Label(frame_Second_Layer, text = splitData[14], width = 12, height = 1, anchor="w", relief = "sunken" )
            labelVal_Xaxis.grid(row = 0, column = 8)
        #   Data_15 = Orientation Y Axis
            labelVal_Yaxis = Label(frame_Second_Layer, text = splitData[15], width = 12, height = 1, anchor="w", relief = "sunken" )
            labelVal_Yaxis.grid(row = 1, column = 8)    
        #   Data_16 = Orientation Z Axis
            labelVal_Zaxis = Label(frame_Second_Layer, text = splitData[16], width = 12, height = 1, anchor="w", relief = "sunken" )
            labelVal_Zaxis.grid(row = 2, column = 8)
        #   Raw Data
            labelName_RawData = Label(Labelframe_RawData, text = rawData, width = 80, height = 2, anchor="center")
            labelName_RawData.grid(row = 0, column = 0)
        #   Update Readings Every 1 seconds    
            time.sleep(1)                         

    else:
        #print("Data Error")
    #   Raw Data [Error Message]
        labelName_RawData = Label(Labelframe_RawData, text = "Telemetry Error", width = 80, height = 2, anchor="center")
        labelName_RawData.grid(row = 0, column = 0)         

# To pause the continuous thread [thread_ShowData]
def stopTelemetry():
#   pause the Continuous Thread (startTelemetry())    
    thread_ShowData.stop()
#   Update Start/Stop indicator Color [STOP = RED]
    button_StartStopIndicator = Button(frame_Controls, width = 2, height = 1, bg = "red")
    button_StartStopIndicator.grid(row = 0, column = 2)
#   Enable Exit Button
    button_Exit = Button(frameExit, text = "Exit", width = 4, height = 1, command = mainWindow.quit, state = "active")
    button_Exit.grid(row = 0, column = 0)           

# Continuous thread to keep reading and displaying the serial data
thread_ShowData = continuous_threading.PausableThread(startTelemetry)

# To disable the Exit Button when the Start button is pressed
def disableExitButton():
    #   Disable Exit Button (Done when Start button is clicked)    
        button_Exit = Button(frameExit, text = "Exit", width = 4, height = 1, command = mainWindow.quit, state = "disabled")
        button_Exit.grid(row = 0, column = 0)

# To initialize the data fields on the startup
def initTelemetryDisplay():
    #   Enable Data Labels on startup    
        labelVal_GPSFix = Label(frame_Second_Layer, text = "--", width = 12, height = 1, anchor="center", relief = "sunken" )
        labelVal_GPSFix.grid(row = 0, column = 1)
    #   Data_2 = GPS_Quality
        labelVal_GPSQuality = Label(frame_Second_Layer, text = "--", width = 12, height = 1, anchor="center", relief = "sunken" )
        labelVal_GPSQuality.grid(row = 1, column = 1)
    #   Data_3 = GPS_Satellites
        labelVal_GPSSats = Label(frame_Second_Layer, text = "--", width = 12, height = 1, anchor="center", relief = "sunken" )
        labelVal_GPSSats.grid(row = 2, column = 1)
    #   Data_4 = GPS_Speed
        labelVal_GPSSpeed = Label(frame_Second_Layer, text = "--", width = 12, height = 1, anchor="center", relief = "sunken" )
        labelVal_GPSSpeed.grid(row = 3, column = 1)
    #   Data_5 = GPS_Latitude
        labelVal_GPSLatitude = Label(frame_Second_Layer, text = "--", width = 12, height = 1, anchor="center", relief = "sunken" )
        labelVal_GPSLatitude.grid(row = 0, column = 3)
    #   Data_6 = GPS_Longitude
        labelVal_GPSLongitude = Label(frame_Second_Layer, text = "--", width = 12, height = 1, anchor="center", relief = "sunken" )
        labelVal_GPSLongitude.grid(row = 1, column = 3)
    #   Data_7 = GPS_Altitude
        labelVal_GPSAltitude = Label(frame_Second_Layer, text = "--", width = 12, height = 1, anchor="center", relief = "sunken" )
        labelVal_GPSAltitude.grid(row = 2, column = 3)
    #   Data_8 = GPS_Latitude_Direction (Heading)
        labelVal_GPSLati_Dir = Label(frame_Second_Layer, text = "--", width = 12, height = 1, anchor="center", relief = "sunken" )
        labelVal_GPSLati_Dir.grid(row = 0, column = 4)
    #   Data_9 = GPS_Longitude_Direction (Heading)
        labelVal_GPSLong_Dir = Label(frame_Second_Layer, text = "--", width = 12, height = 1, anchor="center", relief = "sunken" )
        labelVal_GPSLong_Dir.grid(row = 1, column = 4)
    #   Data_10 = Temperature
        labelVal_Temperature = Label(frame_Second_Layer, text = "--", width = 12, height = 1, anchor="center", relief = "sunken" )
        labelVal_Temperature.grid(row = 0, column = 6)
    #   Data_11 = Altitude
        labelVal_BaroAltitude = Label(frame_Second_Layer, text = "--", width = 12, height = 1, anchor="center", relief = "sunken" )
        labelVal_BaroAltitude.grid(row = 1, column = 6)
    #   Data_12 = Voltage Level 3v
        labelVal_3vLevel = Label(frame_Second_Layer, text = "--", width = 12, height = 1, anchor="center", relief = "sunken" )
        labelVal_3vLevel.grid(row = 2, column = 6)
    #   Data_13 = Voltage Level 5v
        labelVal_5vLevel = Label(frame_Second_Layer, text = "--", width = 12, height = 1, anchor="center", relief = "sunken" )
        labelVal_5vLevel.grid(row = 3, column = 6)
    #   Data_14 = Orientation X Axis
        labelVal_Xaxis = Label(frame_Second_Layer, text = "--", width = 12, height = 1, anchor="center", relief = "sunken" )
        labelVal_Xaxis.grid(row = 0, column = 8)
    #   Data_15 = Orientation Y Axis
        labelVal_Yaxis = Label(frame_Second_Layer, text = "--", width = 12, height = 1, anchor="center", relief = "sunken" )
        labelVal_Yaxis.grid(row = 1, column = 8)    
    #   Data_16 = Orientation Z Axis
        labelVal_Zaxis = Label(frame_Second_Layer, text = "--", width = 12, height = 1, anchor="center", relief = "sunken" )
        labelVal_Zaxis.grid(row = 2, column = 8)     
# ----------------------------------------------------------------------------------------------------------------------------------
#                                                       Buttons
# ----------------------------------------------------------------------------------------------------------------------------------

# -- Start Button
button_Start = Button(frame_Controls, text = "Start", width = 4, height = 1, command = lambda: [thread_ShowData.start(), disableExitButton()])
button_Start.grid(row = 0, column = 0)
# -- Stop Button
button_Stop = Button(frame_Controls, text = "Stop", width = 4, height = 1, command = stopTelemetry)
button_Stop.grid(row = 0, column = 1, padx = 5, pady = 5)
# -- Start/Stop Indicator
button_StartStopIndicator = Button(frame_Controls, text = "", width = 2, height = 1)
button_StartStopIndicator.grid(row = 0, column = 2)
# -- Exit Button
button_Exit = Button(frameExit, text = "Exit", width = 4, height = 1, command = mainWindow.quit)
button_Exit.grid(row = 0, column = 0)

# ----------------------------------------------------------------------------------------------------------------------------------
#                                           Initializing Telemetry Data Fields
# ----------------------------------------------------------------------------------------------------------------------------------

initTelemetryDisplay()

# ----------------------------------------------------------------------------------------------------------------------------------
# -- Event Looping
mainWindow.mainloop() 
# ----------------------------------------------------------------------------------------------------------------------------------