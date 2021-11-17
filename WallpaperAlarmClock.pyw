import win32api
import time
import ctypes
import datetime as dt
from playsound import playsound

def wallpaper_change(name):
          ctypes.windll.user32.SystemParametersInfoW(20, 0, name , 0)

name  = r"C:\Users\Connor\AppData\Local\Programs\Python\Python38-32\mouse_click\\"
num = "a"
left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
right = win32api.GetKeyState(0x02)  # Right button down = 0 or 1. Button up = -127 or -128


# left and right are random, so this stops false alarms at the startup of the program
if left == 0: left_prev = 0
else: left_prev = 1
if right == 0: right_prev = 0
else: right_prev = 1

played = False
 
while True:
          if dt.datetime.now().hour == 22:
                    if not played:
                              playsound(name + "pill.mp3", False)
                              played = True
                    for i in range(8):
                              right = win32api.GetKeyState(0x02)
                              if right_prev != right and right >=0:
                                        wallpaper_change(name + "1.jpg")  
                                        quit()
                              time.sleep(0.09)
                              num = str(i) + ".jpg"
                              wallpaper_change(name + num) 


          
