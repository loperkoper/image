#This script locates the image stickman.png in the region we give it and tell you if it can see it

from pyautogui import * 
import pyautogui 
import time 
import keyboard 
import random
import win32api, win32con
sleep(5)
try:
    if pyautogui.locateOnScreen('account.png') != None:
            pyautogui.click('account.png')
            sleep(0.5)
except:
    sleep(2)
    if pyautogui.locateOnScreen('account.png') != None:
            pyautogui.click('account.png')
            sleep(0.5)
try:

    if pyautogui.locateOnScreen('account2.png') != None:
            pyautogui.click('account2.png')
            sleep(0.5)
except:
    sleep(2)
    if pyautogui.locateOnScreen('account2.png') != None:
            pyautogui.click('account2.png')
            sleep(0.5)

try:

    if pyautogui.locateOnScreen('account3.png', confidence=0.8) != None:
            pyautogui.click('account3.png')
            sleep(1.5)
except:
    sleep(2)
    if pyautogui.locateOnScreen('account3.png', confidence=0.8) != None:
            pyautogui.click('account3.png')
            sleep(1.5)
sleep(2)
keyboard.press('1')
keyboard.release('1')
sleep(2)
try:
    x = 379
    y = 212
    pyautogui.moveTo( x , y , duration = 0.1)

    if pyautogui.locateOnScreen('account4.png') != None:
            pyautogui.click('account4.png')
            pyautogui.click('account4.png')
            sleep(1.5)
except:
    x = 379
    y = 212
    pyautogui.moveTo( x , y , duration = 0.1)
    sleep(2)
    if pyautogui.locateOnScreen('account4.png', confidence=0.8) != None:
            pyautogui.click('account4.png')
            pyautogui.click('account4.png')
            sleep(1.5)
def make_account():
    i = 2
    while i < 22:
        try:

            if pyautogui.locateOnScreen('account5.png') != None:
                    pyautogui.click('account5.png')
                    sleep(1)
        except:
            sleep(2)
            if pyautogui.locateOnScreen('account5.png') != None:
                    pyautogui.click('account5.png')
                    sleep(1)
        try:

            if pyautogui.locateOnScreen('account2.png') != None:
                    pyautogui.click('account2.png')
                    sleep(1)
        except:
            sleep(2)
            if pyautogui.locateOnScreen('account2.png') != None:
                    pyautogui.click('account2.png')
                    sleep(1)

        try:

            if pyautogui.locateOnScreen('account3.png', confidence=0.8) != None:
                    pyautogui.click('account3.png')
                    sleep(1.5)
        except:
            sleep(2)
            if pyautogui.locateOnScreen('account3.png', confidence=0.8) != None:
                    pyautogui.click('account3.png')
                    sleep(1.5)
        sleep(1)
        i = str(i)
        pyautogui.typewrite(i, interval = 0.02)
        i = int(i)
        sleep(3)
        try:
            x = 379
            y = 212
            pyautogui.moveTo( x , y , duration = 0.1)
            sleep(0.5)
            if pyautogui.locateOnScreen('account4.png', confidence=0.8) != None:
                    pyautogui.click('account4.png')
                    pyautogui.click('account4.png')
                    sleep(1.5)
        except:
            sleep(2)
            if pyautogui.locateOnScreen('account4.png', confidence=0.8) != None:
                    pyautogui.click('account4.png')
                    sleep(1.5)
        i = i+1
#make_account()
while 1:
    time.sleep(0.4)
    if pyautogui.locateOnScreen('close.png') != None:
            pyautogui.click('close.png')
            #print("I can see so click")
            time.sleep(0.5)
    elif pyautogui.locateOnScreen('Untitled.png', confidence=0.9) != None:
        try:
            pyautogui.click('Untitled.png')
            print("I can see so click")
            time.sleep(0.5)
        except:
            pass
    elif pyautogui.locateOnScreen('captcha.png') != None: 
        pyautogui.keyDown("ctrl")
        pyautogui.press('r')
        pyautogui.keyUp("ctrl")
        print("I can see so refresh")
        time.sleep(0.5)
    else:
        print("not yet")
        time.sleep(0.5)
