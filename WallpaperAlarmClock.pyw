import win32api
import time
import ctypes
import datetime as dt
from playsound import playsound

# Changes the wallpaper to the image file at the specified path
def wallpaper_change(name): 
          ctypes.windll.user32.SystemParametersInfoW(20, 0, name , 0)

# Initializing Variables
name  = r"C:\Users\Connor\AppData\Local\Programs\Python\Python38-32\mouse_click\\"
num = "a"
left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
right = win32api.GetKeyState(0x02)  # Right button down = 0 or 1. Button up = -127 or -128
left_prev = 0
right_prev = 0
played = False

# left and right are random on intialization, so this stops false alarms at the startup of the program
if left == 0: 
          left_prev = 0
else: 
          left_prev = 1
if right == 0: 
          right_prev = 0
else: 
          right_prev = 1
 
while True:
          # Checks if the specified time has arrived for the alarm to go off 
          if dt.datetime.now().hour == 22: 

                    # Stops the audio file from playing multple times
                    if not played: 
                              playsound(name + "pill.mp3", False)
                              played = True

                    # Cycles through the image files while changing the desktop background
                    for i in range(8): 

                              # Program stops on right click
                              right = win32api.GetKeyState(0x02)
                              if right_prev != right and right >=0:
                                        wallpaper_change(name + "1.jpg")  # resets background to defaul original background (assuming the original is in the folder as "1.jpg" 
                                        quit()
                                        
                              time.sleep(0.09)
                              num = str(i) + ".jpg"  # For the program to cycle through the images correctly, image files should be name "1.jpg", "2.jpg", "3.jpg", etc
                              wallpaper_change(name + num) 


          
