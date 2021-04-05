#!/usr/bin/python
# -*- coding: utf-8 -*-

# import os
# os.system('cmd /c "cd Desktop && cd chrome signup && qwiklabs.com - Chrome.lnk"')
# pip install pywin32 && pip install keyboard && pip install pyautogui && pip install opencv-python && pip install pynput

import pyautogui
from time import sleep
import webbrowser
from pynput.mouse import Button, Controller
mouse = Controller()
from pynput.keyboard import Key, Controller
keyboard = Controller()
import pyautogui
import pyperclip
from time import sleep
import random
import string
sleep(5)
if pyautogui.locateOnScreen('captchaRED.png', confidence=0.8) != None:
   pyautogui.click('captchaRED.png')
   sleep(1)
