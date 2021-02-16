import pyautogui as pa 
import time
time.sleep(5)
f = open("beehive.txt",'r')
for word in f :
    pa.typewrite(word)
    pa.press("enter")
