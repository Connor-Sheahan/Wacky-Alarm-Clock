# Wacky-Alarm-Clock

Just like any other alarm clock, this program sounds a custom alarm when the set time arrives; however, this script also messes with your desktop background to create (harmless) chaos!

Basically, I came up with this when I was bored and got curious about how one could detect mouse clicks and change desktop backgrounds in Python. At the time, I kept forgetting to take my medication at the appropriate time, so I thought it would be a fun project to code my own alarm clock and make it really wacky.

For this script to work, there requires some setup: 

a) Firstly the script should be in a folder (mine was named "mouse_click" as seen in the code); the path in the code must be set to be the same as the path to this folder. 

b) Secondly, the mp3 file acting as the alarm sound must also be in the folder, and the name in the code must match the name of the audio file. 

c) Thirdly the images you want your desktop background to cycle through must also be in the folder, and they should be named as numbers like so: "1.jpg", "2.jpg", "3.jpg", etc... 

d) Finally, you must update the for loop in the code to match the amount of image files you are using. 

Now, when the time comes (specified in the code), the program will play the mp3 file and switch the desktop background repeatedly between the images in the folder. To stop this chaos, all you need to do is right click and the  program will stop running!

Note: If you want this program to work automatically every day, it must be manually set to run on startup (put a shortcut of the file in "AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup")

Have fun!
