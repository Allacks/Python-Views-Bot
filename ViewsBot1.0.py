import webbrowser   #You may have to install these modules
import time
import os

num = 1
while (num > 0):
    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')   #obviously you have to insert the link here. Just between the ''
    time.sleep(25)
    os.system("taskkill /im chrome.exe /f") #If chrome is not your main browser, you have to change the main browser to chrome or insert the process name of your main browser between the " "! Else your PC might crash after 10 minutes
    time.sleep(2)
    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')   #insert the link here between the '' too
    time.sleep(21) 
    os.system("taskkill /im chrome.exe /f") #If chrome is not your main browser, you have to change the main browser to chrome or insert the process name of your main browser between the " "!
    time.sleep(3)
    
'''If youtube does not count these views,
just increase the times. But remember: 
They have to be differently so the algorithm does 
not identifies it as a bot!
Also the times have to be over 21 so the video runs atleast 20 seconds!
Else Youtube does not count it as view'''