import pyautogui 
import time
f = open('word', 'r')
count = 0

for word in f : 
    pyautogui.typewrite(word)
    pyautogui.press('enter')


