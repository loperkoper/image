#!/usr/bin/python
# -*- coding: utf-8 -*-
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


def test():

    # #wait

    if pyautogui.locateOnScreen('region.png') != None:
        sleep(18)

        # #refresh page

        keyboard.press(Key.ctrl)
        keyboard.press('r')
        keyboard.release('r')
        keyboard.release(Key.ctrl)
        sleep(3)

    if pyautogui.locateOnScreen('region.png') != None:
        sleep(18)

        # #refresh page

        keyboard.press(Key.ctrl)
        keyboard.press('r')
        keyboard.release('r')
        keyboard.release(Key.ctrl)
        sleep(3)

    if pyautogui.locateOnScreen('region.png') != None:
        sleep(18)

        # #refresh page

        keyboard.press(Key.ctrl)
        keyboard.press('r')
        keyboard.release('r')
        keyboard.release(Key.ctrl)
        sleep(3)

    if pyautogui.locateOnScreen('region.png') != None:
        sleep(18)

        # #refresh page

        keyboard.press(Key.ctrl)
        keyboard.press('r')
        keyboard.release('r')
        keyboard.release(Key.ctrl)
        sleep(3)

    if pyautogui.locateOnScreen('region.png') != None:
        sleep(18)

        # #refresh page

        keyboard.press(Key.ctrl)
        keyboard.press('r')
        keyboard.release('r')
        keyboard.release(Key.ctrl)
        sleep(3)

    if pyautogui.locateOnScreen('region.png') != None:
        sleep(18)

        # #refresh page

        keyboard.press(Key.ctrl)
        keyboard.press('r')
        keyboard.release('r')
        keyboard.release(Key.ctrl)
        sleep(3)

    if pyautogui.locateOnScreen('region.png') != None:
        clear_cookies()
        mouse.position = (1343, 14)
        mouse.click(Button.left, 1)
        open_chrome()
        signup()
        sleep(0.2)
        z = pyperclip.paste()
        if len(z) < 35:
            remote_desktop()
            qwiklabs()
            minimize()
        i = 1
        while True:
            open_chrome()
            clear_cookies()
            ChangeIp()
            signup()
            sleep(0.2)
            z = pyperclip.paste()
            if len(z) < 35:
                remote_desktop()
                if i % 5 == 0:
                    circleci()
                    minimize()
                else:
                    qwiklabs()
                    minimize()
                i = i + 1
            else:
                i = i

    # #refresh page

    keyboard.press(Key.ctrl)
    keyboard.press('r')
    keyboard.release('r')
    keyboard.release(Key.ctrl)
    sleep(3)

    # #copy URL

    mouse.position = (566, 393)
    mouse.click(Button.left, 3)
    sleep(0.5)
    keyboard.press(Key.ctrl)
    keyboard.press('c')
    keyboard.release('c')
    keyboard.release(Key.ctrl)
    sleep(0.2)
    c = pyperclip.paste()

    # #close chrome

    mouse.position = (1343, 14)
    mouse.click(Button.left, 1)


test()
