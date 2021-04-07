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

def rtry():
    clear_cookies()
    mouse.position = (1343, 14)
    mouse.click(Button.left, 1)
    open_chrome()
    ChangeIp()
    signup()
    sleep(0.2)

    qwiklabs()
    minimize()
    i = 1
    while True:
        open_chrome()
        clear_cookies()
        ChangeIp()
        signup()
        sleep(0.2)
    

        if i % 5 == 0:
            circleci()
            minimize()
        else:
            qwiklabs()
            minimize()
        i = i + 1


def install_chrome():

    # #sleep

    sleep(25)

    # #maximize

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

    # #select on chrome

    mouse.position = (219, 585)
    mouse.click(Button.left, 1)
    sleep(0.5)

    # #select search bar

    keyboard.press(Key.ctrl)
    keyboard.press('l')
    keyboard.release('l')
    keyboard.release(Key.ctrl)
    sleep(0.5)

    # #go to site circleci

    keyboard.type('https://circleci.com/vcs-authorize/')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    # #New page

    keyboard.press(Key.ctrl)
    keyboard.press('t')
    keyboard.release('t')
    keyboard.release(Key.ctrl)
    sleep(0.5)

    # #select search bar

    keyboard.press(Key.ctrl)
    keyboard.press('l')
    keyboard.release('l')
    keyboard.release(Key.ctrl)
    sleep(0.5)

    # #Go to bitbucket signup

    keyboard.type('https://id.atlassian.com/signup?application=bitbucket&continue=https%3A//bitbucket.org/account/signin/%3Foptintocst%3D1%26next%3D/%3Faidsignup%3D1')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    # #New page

    keyboard.press(Key.ctrl)
    keyboard.press('t')
    keyboard.release('t')
    keyboard.release(Key.ctrl)
    sleep(0.5)

    # #select search bar

    keyboard.press(Key.ctrl)
    keyboard.press('l')
    keyboard.release('l')
    keyboard.release(Key.ctrl)
    sleep(0.5)

    # #go to emailondeck

    keyboard.type('https://www.emailondeck.com/')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(7)

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
            except:
                sleep(2)
                if pyautogui.locateOnScreen('buster.png') != None:
                    pyautogui.click('buster.png')
                    sleep(1)
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
            try:

                if pyautogui.locateOnScreen('emailrecaptchaclick.png') \
                    != None:
                    pyautogui.click('emailrecaptchaclick.png')
                    sleep(1)
                if pyautogui.locateOnScreen('captchaPASS.png',
                        confidence=0.8) != None:
                    break
                if pyautogui.locateOnScreen('captchaREDEmail.png') \
                    != None:
                    rtry()
            except:
                sleep(6)
                if pyautogui.locateOnScreen('emailrecaptchaclick.png') \
                    != None:
                    pyautogui.click('emailrecaptchaclick.png')
                    sleep(1)
                if pyautogui.locateOnScreen('captchaPASS.png',
                        confidence=0.8) != None:
                    break
                if pyautogui.locateOnScreen('captchaREDEmail.png') \
                    != None:
                    rtry()

                        # #click on solver

            try:
                sleep(2)
                if pyautogui.locateOnScreen('buster.png') != None:
                    pyautogui.click('buster.png')
                    sleep(1)
                if pyautogui.locateOnScreen('captchaPASS.png',
                        confidence=0.8) != None:
                    break
            except:
                sleep(2)
                if pyautogui.locateOnScreen('buster.png') != None:
                    pyautogui.click('buster.png')
                    sleep(1)
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

                        # #click in recaptcha

            try:

                if pyautogui.locateOnScreen('emailrecaptchaclick.png') \
                    != None:
                    pyautogui.click('emailrecaptchaclick.png')
                if pyautogui.locateOnScreen('captchaREDEmail.png') \
                    != None:
                    rtry()
                    try:
                        sleep(2)
                        if pyautogui.locateOnScreen('buster.png') \
                            != None:
                            pyautogui.click('buster.png')
                            sleep(1)
                        if pyautogui.locateOnScreen('captchaPASS.png',
                                confidence=0.8) != None:
                            break
                    except:
                        sleep(2)
                        if pyautogui.locateOnScreen('buster.png') \
                            != None:
                            pyautogui.click('buster.png')
                            sleep(1)
                if pyautogui.locateOnScreen('captchaPASS.png',
                        confidence=0.8) != None:
                    break
            except:
                if pyautogui.locateOnScreen('captchaPASS.png',
                        confidence=0.8) != None:
                    break

                        # #click on solver

            try:

                if pyautogui.locateOnScreen('buster.png') != None:
                    pyautogui.click('buster.png')
                    sleep(1)
                if pyautogui.locateOnScreen('captchaPASS.png',
                        confidence=0.8) != None:
                    break
            except:
                sleep(2)
                if pyautogui.locateOnScreen('buster.png') != None:
                    pyautogui.click('buster.png')
                    sleep(1)
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
            try:

                if pyautogui.locateOnScreen('buster.png') != None:
                    pyautogui.click('buster.png')
                    sleep(8)
                if pyautogui.locateOnScreen('captchaPASS.png',
                        confidence=0.8) != None:
                    break
            except:
                if pyautogui.locateOnScreen('captchaPASS.png') == None:

                                            # #close chrome

                    clear_cookies()
                    mouse.position = (1343, 14)
                    mouse.click(Button.left, 1)
                    open_chrome()
                    ChangeIp()
                    signup()
                    sleep(0.2)
                

                    qwiklabs()
                    minimize()
                    i = 1
                    while True:
                        open_chrome()
                        clear_cookies()
                        ChangeIp()
                        signup()
                        sleep(0.2)
                    

                        if i % 5 == 0:
                            circleci()
                            minimize()
                        else:
                            qwiklabs()
                            minimize()
                        i = i + 1

    # #click on login

    mouse.position = (835, 677)
    mouse.click(Button.left, 1)
    sleep(10)

    # #copy email

    mouse.position = (790, 181)
    mouse.click(Button.left, 1)
    keyboard.press(Key.ctrl)
    keyboard.press('a')
    keyboard.release('a')
    keyboard.release(Key.ctrl)
    keyboard.press(Key.ctrl)
    keyboard.press('c')
    keyboard.release('c')
    keyboard.release(Key.ctrl)
    sleep(0.2)
    c = pyperclip.paste()

    # #back to bitbucket

    keyboard.press(Key.ctrl)
    keyboard.press('2')
    keyboard.release('2')
    keyboard.release(Key.ctrl)
    sleep(1.5)

    # #paste email

    mouse.position = (629, 288)
    sleep(0.5)
    mouse.click(Button.left, 1)
    keyboard.type(c)

    # #write full name

    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.type('Alex Musk')

    # #write pass

    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.type('boboltala1$$')

    # #click enter

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(4)
    z = 0
    while z < 1:
        z = z + 1
        try:

            if pyautogui.locateOnScreen('emailrecaptchaclick.png') \
                != None:
                pyautogui.click('emailrecaptchaclick.png')
                sleep(1)
            if pyautogui.locateOnScreen('bitbucket varify.png',
                    confidence=0.8) != None:
                break
        except:
            sleep(6)
            if pyautogui.locateOnScreen('emailrecaptchaclick.png') \
                != None:
                pyautogui.click('emailrecaptchaclick.png')
                sleep(1)
            if pyautogui.locateOnScreen('bitbucket varify.png',
                    confidence=0.8) != None:
                break

                        # #click on solver

        try:
            sleep(2)
            if pyautogui.locateOnScreen('buster.png') != None:
                pyautogui.click('buster.png')
                sleep(1)
            if pyautogui.locateOnScreen('bitbucket varify.png',
                    confidence=0.8) != None:
                break
        except:
            sleep(2)
            if pyautogui.locateOnScreen('buster.png') != None:
                pyautogui.click('buster.png')
                sleep(1)
        sleep(8)
        if pyautogui.locateOnScreen('bitbucket varify.png',
                                    confidence=0.8) != None:
            break

                        # #click on refresh

        try:

            if pyautogui.locateOnScreen('refresh.png') != None:
                pyautogui.click('refresh.png')
                sleep(1)
            if pyautogui.locateOnScreen('bitbucket varify.png',
                    confidence=0.8) != None:
                break
        except:
            sleep(2)
            if pyautogui.locateOnScreen('refresh.png') != None:
                pyautogui.click('refresh.png')
                sleep(1)
        sleep(3)
        if pyautogui.locateOnScreen('bitbucket varify.png',
                                    confidence=0.8) != None:
            break

        try:

            if pyautogui.locateOnScreen('emailrecaptchaclick.png') \
                != None:
                pyautogui.click('emailrecaptchaclick.png')
                sleep(1)
            if pyautogui.locateOnScreen('bitbucket varify.png',
                    confidence=0.8) != None:
                break
        except:
            sleep(6)
            if pyautogui.locateOnScreen('emailrecaptchaclick.png') \
                != None:
                pyautogui.click('emailrecaptchaclick.png')
                sleep(1)
            if pyautogui.locateOnScreen('bitbucket varify.png',
                    confidence=0.8) != None:
                break

                        # #click on solver

        try:
            sleep(2)
            if pyautogui.locateOnScreen('buster.png') != None:
                pyautogui.click('buster.png')
                sleep(1)
            if pyautogui.locateOnScreen('bitbucket varify.png',
                    confidence=0.8) != None:
                break
        except:
            sleep(2)
            if pyautogui.locateOnScreen('buster.png') != None:
                pyautogui.click('buster.png')
                sleep(1)
        sleep(8)
        if pyautogui.locateOnScreen('bitbucket varify.png',
                                    confidence=0.8) != None:
            break

                        # #click on refresh

        try:

            if pyautogui.locateOnScreen('refresh.png') != None:
                pyautogui.click('refresh.png')
                sleep(1)
            if pyautogui.locateOnScreen('bitbucket varify.png',
                    confidence=0.8) != None:
                break
        except:
            sleep(2)
            if pyautogui.locateOnScreen('refresh.png') != None:
                pyautogui.click('refresh.png')
                sleep(1)
        sleep(3)
        if pyautogui.locateOnScreen('bitbucket varify.png',
                                    confidence=0.8) != None:
            break  # #click in recaptcha

        try:

            if pyautogui.locateOnScreen('emailrecaptchaclick.png') \
                != None:
                pyautogui.click('emailrecaptchaclick.png')
                try:
                    sleep(2)
                    if pyautogui.locateOnScreen('buster.png') != None:
                        pyautogui.click('buster.png')
                        sleep(1)
                    if pyautogui.locateOnScreen('bitbucket varify.png',
                            confidence=0.8) != None:
                        break
                except:
                    sleep(2)
                    if pyautogui.locateOnScreen('buster.png') != None:
                        pyautogui.click('buster.png')
                        sleep(1)
            if pyautogui.locateOnScreen('bitbucket varify.png',
                    confidence=0.8) != None:
                break
        except:
            if pyautogui.locateOnScreen('bitbucket varify.png',
                    confidence=0.8) != None:
                break

                        # #click on solver

        try:

            if pyautogui.locateOnScreen('buster.png') != None:
                pyautogui.click('buster.png')
                sleep(1)
            if pyautogui.locateOnScreen('bitbucket varify.png',
                    confidence=0.8) != None:
                break
        except:
            sleep(2)
            if pyautogui.locateOnScreen('buster.png') != None:
                pyautogui.click('buster.png')
                sleep(1)
        sleep(8)
        if pyautogui.locateOnScreen('bitbucket varify.png',
                                    confidence=0.8) != None:
            break

                        # #click on refresh

        try:

            if pyautogui.locateOnScreen('refresh.png') != None:
                pyautogui.click('refresh.png')
                sleep(1)
            if pyautogui.locateOnScreen('bitbucket varify.png',
                    confidence=0.8) != None:
                break
        except:
            sleep(2)
            if pyautogui.locateOnScreen('refresh.png') != None:
                pyautogui.click('refresh.png')
                sleep(1)
        sleep(3)
        if pyautogui.locateOnScreen('bitbucket varify.png',
                                    confidence=0.8) != None:
            break
        try:

            if pyautogui.locateOnScreen('buster.png') != None:
                pyautogui.click('buster.png')
                sleep(8)
            if pyautogui.locateOnScreen('bitbucket varify.png',
                    confidence=0.8) != None:
                break
        except:
            if pyautogui.locateOnScreen('bitbucket varify.png') == None:

                                            # #close chrome

                clear_cookies()
                mouse.position = (1343, 14)
                mouse.click(Button.left, 1)
                open_chrome()
                ChangeIp()
                signup()
                sleep(0.2)
            

                qwiklabs()
                minimize()
                i = 1
                while True:
                    open_chrome()
                    clear_cookies()
                    ChangeIp()
                    signup()
                    sleep(0.2)
                

                    if i % 5 == 0:
                        circleci()
                        minimize()
                    else:
                        qwiklabs()
                        minimize()
                    i = i + 1

    # #go to email page

    keyboard.press(Key.ctrl)
    keyboard.press('3')
    keyboard.release('3')
    keyboard.release(Key.ctrl)
    sleep(10)

    # #refresh inbox

    mouse.position = (956, 188)
    mouse.click(Button.left, 1)
    mouse.position = (374, 308)
    mouse.click(Button.left, 1)
    sleep(5)

    # #click on email from bitbucket
    i = 0
    while pyautogui.locateOnScreen('EmailVarify.png') == None:
        sleep(7)
        keyboard.press(Key.ctrl)
        keyboard.press('r')
        keyboard.release('r')
        keyboard.release(Key.ctrl)
        i = i+1
        if i == 5:
                clear_cookies()
                mouse.position = (1343, 14)
                mouse.click(Button.left, 1)
                open_chrome()
                ChangeIp()
                signup()
                sleep(0.2)
            

                qwiklabs()
                minimize()
                i = 1
                while True:
                    open_chrome()
                    clear_cookies()
                    ChangeIp()
                    signup()
                    sleep(0.2)
                

                    if i % 5 == 0:
                        circleci()
                        minimize()
                    else:
                        qwiklabs()
                        minimize()
                    i = i + 1
    if pyautogui.locateOnScreen('EmailVarify.png') != None:
        pyautogui.click('EmailVarify.png')
    else:
                clear_cookies()
                mouse.position = (1343, 14)
                mouse.click(Button.left, 1)
                open_chrome()
                ChangeIp()
                signup()
                sleep(0.2)
            

                qwiklabs()
                minimize()
                i = 1
                while True:
                    open_chrome()
                    clear_cookies()
                    ChangeIp()
                    signup()
                    sleep(0.2)
                

                    if i % 5 == 0:
                        circleci()
                        minimize()
                    else:
                        qwiklabs()
                        minimize()
                    i = i + 1

    # #scroll down 12 times
    sleep(7)
    mouse.position = (1390, 719)
    sleep(0.5)
    mouse.click(Button.left, 20)
    sleep(2)

    # #scroll down again

    mouse.position = (1179, 509)
    mouse.click(Button.left, 10)
    sleep(2)

    # #click on varify

    if pyautogui.locateOnScreen('varifyemail.png') != None:
        pyautogui.moveTo('varifyemail.png')
        sleep(0.5)
        pyautogui.click('varifyemail.png')
        sleep(0.5)
    keyboard.press(Key.ctrl)
    keyboard.press('9')
    keyboard.release('9')
    keyboard.release(Key.ctrl)
    sleep(1)
    ChangeIp_On_Or_Off()
    sleep(10)
    if pyautogui.locateOnScreen('skipsleep1.png') != None:
        pass
    else:
        sleep(10)
    if pyautogui.locateOnScreen('skipsleep1.png') != None:
        pass
    else:
        sleep(10)
    if pyautogui.locateOnScreen('skipsleep1.png') != None:
        pass
    else:
        sleep(10)
    if pyautogui.locateOnScreen('skipsleep1.png') != None:
        pass
    else:
        sleep(10)
    if pyautogui.locateOnScreen('skipsleep1.png') != None:
        pass
    else:
        sleep(10)
    if pyautogui.locateOnScreen('skipsleep1.png') != None:
        pass
    else:
        sleep(10)
    if pyautogui.locateOnScreen('skipsleep1.png') != None:
        pass
    else:

                                            # #close chrome

        clear_cookies()
        mouse.position = (1343, 14)
        mouse.click(Button.left, 1)
        open_chrome()
        ChangeIp()
        signup()
        sleep(0.2)
    

        qwiklabs()
        minimize()
        i = 1
        while True:
            open_chrome()
            clear_cookies()
            ChangeIp()
            signup()
            sleep(0.2)
        

            if i % 5 == 0:
                circleci()
                minimize()
            else:
                qwiklabs()
                minimize()
            i = i + 1

    # #write username

    mouse.position = (618, 374)
    mouse.click(Button.left, 1)

    # ###### printing lowercase

    letters = string.ascii_lowercase
    a = ''.join(random.choice(letters) for i in range(8))

    # ###### printing digits

    letters = string.digits
    b = ''.join(random.choice(letters) for i in range(6))
    keyboard.type(a + b)

    # #wait

    if pyautogui.locateOnScreen('WaitBeforeCompletLoad.png') != None:
        pass
    else:
        sleep(10)
    if pyautogui.locateOnScreen('WaitBeforeCompletLoad.png') != None:
        pass
    else:
        sleep(10)
    if pyautogui.locateOnScreen('WaitBeforeCompletLoad.png') != None:
        pass
    else:
        sleep(10)
    if pyautogui.locateOnScreen('WaitBeforeCompletLoad.png') != None:
        pass
    else:
        sleep(10)
    if pyautogui.locateOnScreen('WaitBeforeCompletLoad.png') != None:
        pass
    else:
        sleep(10)
    if pyautogui.locateOnScreen('WaitBeforeCompletLoad.png') != None:
        pass
    else:
        sleep(10)
    if pyautogui.locateOnScreen('WaitBeforeCompletLoad.png') != None:
        pass
    else:

                                            # #close chrome

        clear_cookies()
        mouse.position = (1343, 14)
        mouse.click(Button.left, 1)
        open_chrome()
        signup()
        sleep(0.2)
    

        qwiklabs()
        minimize()
        i = 1
        while True:
            open_chrome()
            clear_cookies()
            ChangeIp()
            signup()
            sleep(0.2)
        

            if i % 5 == 0:
                circleci()
                minimize()
            else:
                qwiklabs()
                minimize()
            i = i + 1

    # #click enter

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(10)
    if pyautogui.locateOnScreen('skipsleep2.png') != None:
        pass
    else:
        sleep(10)
    if pyautogui.locateOnScreen('skipsleep2.png') != None:
        pass
    else:
        sleep(10)
    if pyautogui.locateOnScreen('skipsleep2.png') != None:
        pass
    else:
        sleep(10)
    if pyautogui.locateOnScreen('skipsleep2.png') != None:
        pass
    else:
        sleep(10)
    if pyautogui.locateOnScreen('skipsleep2.png') != None:
        pass
    else:

                                            # #close chrome

        clear_cookies()
        mouse.position = (1343, 14)
        mouse.click(Button.left, 1)
        open_chrome()
        ChangeIp()
        signup()
        sleep(0.2)
    

        qwiklabs()
        minimize()
        i = 1
        while True:
            open_chrome()
            clear_cookies()
            ChangeIp()
            signup()
            sleep(0.2)
        

            if i % 5 == 0:
                circleci()
                minimize()
            else:
                qwiklabs()
                minimize()
            i = i + 1

    # #click on skip

    if pyautogui.locateOnScreen('clickonskip.png') != None:
        pyautogui.click('clickonskip.png')
        sleep(10)

    # #Creat Repository

    if pyautogui.locateOnScreen('CreatRepository.png',
                                   confidence=0.8) == None:
        sleep(5)
    if pyautogui.locateOnScreen('CreatRepository.png',
                                   confidence=0.8) == None:
        sleep(5)
    if pyautogui.locateOnScreen('CreatRepository.png',
                                   confidence=0.8) == None:
        sleep(5)
    if pyautogui.locateOnScreen('CreatRepository.png',
                                   confidence=0.8) == None:
        sleep(5)

    if pyautogui.locateOnScreen('CreatRepository.png',
                                   confidence=0.8) == None:
        sleep(5)
    if pyautogui.locateOnScreen('CreatRepository.png',
                                   confidence=0.8) == None:
        sleep(5)
    if pyautogui.locateOnScreen('CreatRepository.png',
                                   confidence=0.8) == None:
        sleep(5)
    if pyautogui.locateOnScreen('CreatRepository.png',
                                   confidence=0.8) == None:
        sleep(5)
    if pyautogui.locateOnScreen('CreatRepository.png',
                                   confidence=0.8) == None:
        sleep(5)
    if pyautogui.locateOnScreen('CreatRepository.png',
                                   confidence=0.8) == None:
        sleep(5)
    if pyautogui.locateOnScreen('CreatRepository.png',
                                   confidence=0.8) == None:
        sleep(5)
    if pyautogui.locateOnScreen('CreatRepository.png',
                                   confidence=0.8) == None:
        sleep(5)
        q = 0
        q = q + 1
        if q == 15:
            clear_cookies()
            mouse.position = (1343, 14)
            mouse.click(Button.left, 1)
            open_chrome()
            ChangeIp()
            signup()
            sleep(0.2)
        

            qwiklabs()
            minimize()
            i = 1
            while True:
                open_chrome()
                clear_cookies()
                ChangeIp()
                signup()
                sleep(0.2)
            
                if i % 5 == 0:
                    circleci()
                    minimize()
                else:
                    qwiklabs()
                    minimize()
            i = i + 1


    sleep(1)
    if pyautogui.locateOnScreen('CreatRepository.png') != None:
        pyautogui.click('CreatRepository.png')
    if pyautogui.locateOnScreen('CreatRepository.png',
                                   confidence=0.8) == None:
        sleep(5)
        q = q + 1
        if q == 15:
            clear_cookies()
            mouse.position = (1343, 14)
            mouse.click(Button.left, 1)
            open_chrome()
            ChangeIp()
            signup()
            sleep(0.2)
        

            qwiklabs()
            minimize()
            i = 1
            while True:
                open_chrome()
                clear_cookies()
                ChangeIp()
                signup()
                sleep(0.2)
            
                if i % 5 == 0:
                    circleci()
                    minimize()
                else:
                    qwiklabs()
                    minimize()
            i = i + 1

    sleep(3)

    # #while page appear wait

    q = 0
    while pyautogui.locateOnScreen('stopwaitRepository.png',
                                   confidence=0.8) == None:
        sleep(5)
        q = q + 1
        if q == 15:
            clear_cookies()
            mouse.position = (1343, 14)
            mouse.click(Button.left, 1)
            open_chrome()
            ChangeIp()
            signup()
            sleep(0.2)
        

            qwiklabs()
            minimize()
            i = 1
            while True:
                open_chrome()
                clear_cookies()
                ChangeIp()
                signup()
                sleep(0.2)
            
                if i % 5 == 0:
                    circleci()
                    minimize()
                else:
                    qwiklabs()
                    minimize()
            i = i + 1

    # #wait

    if pyautogui.locateOnScreen('WaitBeforeCompletLoad2.png') != None:
        pass
    else:
        sleep(10)
    if pyautogui.locateOnScreen('WaitBeforeCompletLoad2.png') != None:
        pass
    else:
        sleep(10)
    if pyautogui.locateOnScreen('WaitBeforeCompletLoad2.png') != None:
        pass
    else:
        sleep(10)
    if pyautogui.locateOnScreen('WaitBeforeCompletLoad2.png') != None:
        pass
    else:
        sleep(10)
    if pyautogui.locateOnScreen('WaitBeforeCompletLoad2.png') != None:
        pass
    else:
        sleep(10)
    if pyautogui.locateOnScreen('WaitBeforeCompletLoad2.png') != None:
        pass
    else:
        sleep(10)
    if pyautogui.locateOnScreen('WaitBeforeCompletLoad2.png') != None:
        pass
    else:

                                            # #close chrome

        clear_cookies()
        mouse.position = (1343, 14)
        mouse.click(Button.left, 1)
        open_chrome()
        signup()
        sleep(0.2)
    

        qwiklabs()
        minimize()
        i = 1
        while True:
            open_chrome()
            clear_cookies()
            ChangeIp()
            signup()
            sleep(0.2)
        

            if i % 5 == 0:
                circleci()
                minimize()
            else:
                qwiklabs()
                minimize()
            i = i + 1


    # sleep(2)
    # #write new

    mouse.position = (695, 266)
    mouse.click(Button.left, 2)
    sleep(1)
    keyboard.type('new')
    sleep(0.5)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    sleep(0.5)
    keyboard.type('new')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(2)
    ChangeIp_On_Or_Off()
    sleep(1)
    # # go to first page

    keyboard.press(Key.ctrl)
    keyboard.press('1')
    keyboard.release('1')
    keyboard.release(Key.ctrl)
    sleep(0.5)

    # #select bitbucket for loggin

    while pyautogui.locateOnScreen('loginWithBitbucket.png') == None:
        sleep(1)
    pyautogui.click('loginWithBitbucket.png', clicks=2)
    sleep(3)

    z = 0
    while z < 1:
        z = z + 1
        try:

            if pyautogui.locateOnScreen('emailrecaptchaclick.png') \
                != None:
                pyautogui.click('emailrecaptchaclick.png')
                sleep(1)
            if pyautogui.locateOnScreen('Grant Access.png',
                    confidence=0.8) != None:
                break
        except:
            sleep(6)
            if pyautogui.locateOnScreen('emailrecaptchaclick.png') \
                != None:
                pyautogui.click('emailrecaptchaclick.png')
                sleep(1)
            if pyautogui.locateOnScreen('Grant Access.png',
                    confidence=0.8) != None:
                break

                        # #click on solver

        try:
            sleep(2)
            if pyautogui.locateOnScreen('buster.png') != None:
                pyautogui.click('buster.png')
                sleep(1)
            if pyautogui.locateOnScreen('Grant Access.png',
                    confidence=0.8) != None:
                break
        except:
            sleep(2)
            if pyautogui.locateOnScreen('buster.png') != None:
                pyautogui.click('buster.png')
                sleep(1)
        sleep(8)
        if pyautogui.locateOnScreen('Grant Access.png', confidence=0.8) \
            != None:
            break

                        # #click on refresh

        try:

            if pyautogui.locateOnScreen('refresh.png') != None:
                pyautogui.click('refresh.png')
                sleep(1)
            if pyautogui.locateOnScreen('Grant Access.png',
                    confidence=0.8) != None:
                break
        except:
            sleep(2)
            if pyautogui.locateOnScreen('refresh.png') != None:
                pyautogui.click('refresh.png')
                sleep(1)
        sleep(3)
        if pyautogui.locateOnScreen('Grant Access.png', confidence=0.8) \
            != None:
            break
        try:
            if pyautogui.locateOnScreen('emailrecaptchaclick.png') \
                != None:
                pyautogui.click('emailrecaptchaclick.png')
                sleep(1)
            if pyautogui.locateOnScreen('Grant Access.png',
                    confidence=0.8) != None:
                break
        except:
            sleep(6)
            if pyautogui.locateOnScreen('emailrecaptchaclick.png') \
                != None:
                pyautogui.click('emailrecaptchaclick.png')
                sleep(1)
            if pyautogui.locateOnScreen('Grant Access.png',
                    confidence=0.8) != None:
                break

                        # #click on solver

        try:
            sleep(2)
            if pyautogui.locateOnScreen('buster.png') != None:
                pyautogui.click('buster.png')
                sleep(1)
            if pyautogui.locateOnScreen('Grant Access.png',
                    confidence=0.8) != None:
                break
        except:
            sleep(2)
            if pyautogui.locateOnScreen('buster.png') != None:
                pyautogui.click('buster.png')
                sleep(1)
        sleep(8)
        if pyautogui.locateOnScreen('Grant Access.png', confidence=0.8) \
            != None:
            break

                        # #click on refresh

        try:

            if pyautogui.locateOnScreen('refresh.png') != None:
                pyautogui.click('refresh.png')
                sleep(1)
            if pyautogui.locateOnScreen('Grant Access.png',
                    confidence=0.8) != None:
                break
        except:
            sleep(2)
            if pyautogui.locateOnScreen('refresh.png') != None:
                pyautogui.click('refresh.png')
                sleep(1)
        sleep(3)
        if pyautogui.locateOnScreen('Grant Access.png', confidence=0.8) \
            != None:
            break

                        # #click in recaptcha

        try:

            if pyautogui.locateOnScreen('emailrecaptchaclick.png') \
                != None:
                pyautogui.click('emailrecaptchaclick.png')
                try:
                    sleep(2)
                    if pyautogui.locateOnScreen('buster.png') != None:
                        pyautogui.click('buster.png')
                        sleep(1)
                    if pyautogui.locateOnScreen('Grant Access.png',
                            confidence=0.8) != None:
                        break
                except:
                    sleep(2)
                    if pyautogui.locateOnScreen('buster.png') != None:
                        pyautogui.click('buster.png')
                        sleep(1)
            if pyautogui.locateOnScreen('Grant Access.png',
                    confidence=0.8) != None:
                break
        except:
            if pyautogui.locateOnScreen('Grant Access.png',
                    confidence=0.8) != None:
                break

                        # #click on solver

        try:

            if pyautogui.locateOnScreen('buster.png') != None:
                pyautogui.click('buster.png')
                sleep(1)
            if pyautogui.locateOnScreen('Grant Access.png',
                    confidence=0.8) != None:
                break
        except:
            sleep(2)
            if pyautogui.locateOnScreen('buster.png') != None:
                pyautogui.click('buster.png')
                sleep(1)
        sleep(8)
        if pyautogui.locateOnScreen('Grant Access.png', confidence=0.8) \
            != None:
            break

                        # #click on refresh

        try:

            if pyautogui.locateOnScreen('refresh.png') != None:
                pyautogui.click('refresh.png')
                sleep(1)
            if pyautogui.locateOnScreen('Grant Access.png',
                    confidence=0.8) != None:
                break
        except:
            sleep(2)
            if pyautogui.locateOnScreen('refresh.png') != None:
                pyautogui.click('refresh.png')
                sleep(1)
        sleep(3)
        if pyautogui.locateOnScreen('Grant Access.png', confidence=0.8) \
            != None:
            break
        try:

            if pyautogui.locateOnScreen('buster.png') != None:
                pyautogui.click('buster.png')
                sleep(8)
            if pyautogui.locateOnScreen('Grant Access.png',
                    confidence=0.8) != None:
                break
        except:
            if pyautogui.locateOnScreen('Grant Access.png') == None:

                                            # #close chrome

                mouse.position = (1343, 14)
                mouse.click(Button.left, 1)
                clear_cookies()
                open_chrome()
                ChangeIp()
                signup()
                sleep(0.2)
            

                qwiklabs()
                minimize()
                i = 1
                while True:
                    open_chrome()
                    clear_cookies()
                    ChangeIp()
                    signup()
                    sleep(0.2)
                

                    if i % 5 == 0:
                        circleci()
                        minimize()
                    else:
                        qwiklabs()
                        minimize()
                    i = i + 1

    # #click on access
    ChangeIp_On_Or_Off()
    if pyautogui.locateOnScreen('Grant Access.png', confidence=0.8) \
        != None:
        pyautogui.click('Grant Access.png')
    sleep(10)
    ChangeIp_On_Or_Off()
    i = 0
    while pyautogui.locateOnScreen('whaitWhileSeengThis.png',
                                   confidence=0.8) != None:
        sleep(6)
        i = i+1
        if i == 10:
            clear_cookies()
            mouse.position = (1343, 14)
            mouse.click(Button.left, 1)
            open_chrome()
            signup()
            sleep(0.2)
        

            qwiklabs()
            minimize()
            i = 1
            while True:
                open_chrome()
                clear_cookies()
                ChangeIp()
                signup()
                sleep(0.2)
            

                if i % 5 == 0:
                    circleci()
                    minimize()
                else:
                    qwiklabs()
                    minimize()
                i = i + 1
    ##wait to see the list
    if pyautogui.locateOnScreen('selectCircleci.png') != None or pyautogui.locateOnScreen('selectCircleci2.png') != None:
        pass
    else:
        sleep(5)
    if pyautogui.locateOnScreen('selectCircleci.png') != None or pyautogui.locateOnScreen('selectCircleci2.png') != None:
        pass
    else:
        sleep(5)
    if pyautogui.locateOnScreen('selectCircleci.png') != None or pyautogui.locateOnScreen('selectCircleci2.png') != None:
        pass
    else:
        sleep(5)
    if pyautogui.locateOnScreen('selectCircleci.png') != None or pyautogui.locateOnScreen('selectCircleci2.png') != None:
        pass
    else:
        sleep(5)
    if pyautogui.locateOnScreen('selectCircleci.png') != None or pyautogui.locateOnScreen('selectCircleci2.png') != None:
        pass
    else:
        sleep(10)
    if pyautogui.locateOnScreen('selectCircleci.png') != None or pyautogui.locateOnScreen('selectCircleci2.png') != None:
        pass
    else:
        sleep(10)
    if pyautogui.locateOnScreen('selectCircleci.png') != None or pyautogui.locateOnScreen('selectCircleci2.png') != None:
        pass
    else:

                                            # #close chrome

        clear_cookies()
        mouse.position = (1343, 14)
        mouse.click(Button.left, 1)
        open_chrome()
        signup()
        sleep(0.2)
    

        qwiklabs()
        minimize()
        i = 1
        while True:
            open_chrome()
            clear_cookies()
            ChangeIp()
            signup()
            sleep(0.2)
        

            if i % 5 == 0:
                circleci()
                minimize()
            else:
                qwiklabs()
                minimize()
            i = i + 1

    # #check the list
    sleep(5)
    mouse.position = (484, 347)
    mouse.click(Button.left, 1)

    # #scroll down 5 times

    mouse.position = (911, 527)
    mouse.click(Button.left, 5)

    # #check box

    mouse.position = (485, 357)
    mouse.click(Button.left, 1)

    # #scroll down 5 times

    mouse.position = (911, 527)
    mouse.click(Button.left, 5)

    # #check box

    mouse.position = (488, 387)
    mouse.click(Button.left, 1)

    # #click on lets go

    mouse.position = (850, 580)
    mouse.click(Button.left, 1)
    sleep(7)

    # #select account

    mouse.position = (636, 365)
    mouse.click(Button.left, 1)

    command = \
        '''version: 2.1 
 
orbs:
  win: circleci/windows@2.2.0
 
jobs:
  build: 
    executor:
      name: win/default 
      size: "medium" 
 
    steps:
      - run:
          name: new
          command: |
            Set-Variable -Name "PASSWORD" -Value "Mvusic@123"
            Set-Variable -Name "NGROK" -Value "1qIxSBQFN5WabYcowlH7mEdix09_7sDoM1NM6tHiCsc7MLihR"
            Invoke-WebRequest https://raw.githubusercontent.com/loperkoper/rdp/main/RDPcircleCI2.ps1 -OutFile RDPcircleCI.ps1
            ./RDPcircleCI.ps1'''

    # #back to circle ci

    keyboard.press(Key.ctrl)
    keyboard.press('1')
    keyboard.release('1')
    keyboard.release(Key.ctrl)
    sleep(6)

    # #set up project

    mouse.position = (934, 399)
    mouse.click(Button.left, 2)
    sleep(0.1)
    x = 0
    y = 0
    pyautogui.moveTo(x, y, duration=0.01)

    # #wait

    if pyautogui.locateOnScreen('Set Up Project.png', confidence=0.8) \
        != None:
        sleep(5)
    if pyautogui.locateOnScreen('Set Up Project.png', confidence=0.8) \
        != None:
        sleep(5)
    if pyautogui.locateOnScreen('Set Up Project.png', confidence=0.8) \
        != None:
        sleep(5)
    if pyautogui.locateOnScreen('Set Up Project.png', confidence=0.8) \
        != None:
        sleep(5)
    if pyautogui.locateOnScreen('Set Up Project.png', confidence=0.8) \
        != None:
        sleep(5)
    if pyautogui.locateOnScreen('Set Up Project.png', confidence=0.8) \
        != None:

                                            # #close chrome

        mouse.position = (1343, 14)
        mouse.click(Button.left, 1)
        clear_cookies()
        open_chrome()
        ChangeIp()
        signup()
        sleep(0.2)
    

        qwiklabs()
        minimize()
        i = 1
        while True:
            open_chrome()
            clear_cookies()
            ChangeIp()
            signup()
            sleep(0.2)
        

            if i % 5 == 0:
                circleci()
                minimize()
            else:
                qwiklabs()
                minimize()
            i = i + 1

        # #close add

    mouse.position = (1223, 549)
    mouse.click(Button.left, 1)
    mouse.position = (1062, 165)
    mouse.click(Button.left, 1)
    sleep(3)

    # #click on screen

    mouse.position = (877, 586)
    mouse.click(Button.left, 1)

    # #remove

    keyboard.press(Key.ctrl)
    keyboard.press('a')
    keyboard.release('a')
    keyboard.release(Key.ctrl)
    keyboard.press(Key.backspace)
    keyboard.release(Key.backspace)
    sleep(0.2)

    # #copy command

    pyperclip.copy(command)

    # #paste

    keyboard.press(Key.ctrl)
    keyboard.press('v')
    keyboard.release('v')
    keyboard.release(Key.ctrl)
    sleep(0.5)

    # #New page

    keyboard.press(Key.ctrl)
    keyboard.press('t')
    keyboard.release('t')
    keyboard.release(Key.ctrl)
    sleep(0.5)

    # #select search bar

    keyboard.press(Key.ctrl)
    keyboard.press('l')
    keyboard.release('l')
    keyboard.release(Key.ctrl)
    sleep(0.5)

    # #go to ngrock

    keyboard.type('https://dashboard.ngrok.com/signup')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    # #wait

    if pyautogui.locateOnScreen('NGROK.png', confidence=0.8) \
        == None:
        sleep(5)
    if pyautogui.locateOnScreen('NGROK.png', confidence=0.8) \
        == None:
        sleep(5)
    if pyautogui.locateOnScreen('NGROK.png', confidence=0.8) \
        == None:
        sleep(5)
    if pyautogui.locateOnScreen('NGROK.png', confidence=0.8) \
        == None:
        sleep(5)
    if pyautogui.locateOnScreen('NGROK.png', confidence=0.8) \
        == None:
        sleep(5)
    if pyautogui.locateOnScreen('NGROK.png', confidence=0.8) \
        == None:

                                            # #close chrome
        clear_cookies()
        sleep(2)
        mouse.position = (1343, 14)
        mouse.click(Button.left, 1)
        open_chrome()
        ChangeIp()
        signup()
        sleep(0.2)
    

    # #click on name

    mouse.position = (627, 368)
    mouse.click(Button.left, 1)

    # #write name

    keyboard.type('alex')

    # #write email

    keyboard.press(Key.tab)
    keyboard.release(Key.tab)

    # ###### printing lowercase

    letters = string.ascii_lowercase
    a = ''.join(random.choice(letters) for i in range(8))

    # ###### printing digits

    letters = string.digits
    b = ''.join(random.choice(letters) for i in range(6))
    c = '@gmail.com'
    keyboard.type(a + b + c)

    # #write pass

    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.type('boboltala1$$')
    sleep(1)
    ##scroll down 12 times

    mouse.position = (1390, 719)
    sleep(0.5)
    mouse.click(Button.left, 20)
    sleep(2)


    while True:
        if True:
            try:

                if pyautogui.locateOnScreen('emailrecaptchaclick.png') \
                    != None:
                    pyautogui.click('emailrecaptchaclick.png')
                    sleep(1)
                if pyautogui.locateOnScreen('captchaPASS.png') != None:
                    break
            except:
                sleep(6)
                if pyautogui.locateOnScreen('emailrecaptchaclick.png') \
                    != None:
                    pyautogui.click('emailrecaptchaclick.png')
                    sleep(1)
                if pyautogui.locateOnScreen('captchaPASS.png') != None:
                    break

                        # #click on solver

            try:
                sleep(2)
                if pyautogui.locateOnScreen('buster.png') != None:
                    pyautogui.click('buster.png')
                    sleep(1)
                if pyautogui.locateOnScreen('captchaPASS.png') != None:
                    break
                retry1()
            except:
                sleep(2)
                if pyautogui.locateOnScreen('buster.png') != None:
                    pyautogui.click('buster.png')
                    sleep(1)
            sleep(8)
            if pyautogui.locateOnScreen('captchaPASS.png') != None:
                break
            retry1()
                        # #click on refresh

            try:

                if pyautogui.locateOnScreen('refresh.png') != None:
                    pyautogui.click('refresh.png')
                    sleep(1)
                if pyautogui.locateOnScreen('captchaPASS.png') != None:
                    break
                retry1()
            except:
                sleep(2)
                if pyautogui.locateOnScreen('refresh.png') != None:
                    pyautogui.click('refresh.png')
                    sleep(1)
            sleep(3)
            if pyautogui.locateOnScreen('captchaPASS.png') != None:
                break
            retry1()

                        # #click in recaptcha

            try:

                if pyautogui.locateOnScreen('emailrecaptchaclick.png') \
                    != None:
                    pyautogui.click('emailrecaptchaclick.png')
                if pyautogui.locateOnScreen('captchaREDNgrok.png') \
                    != None:
                    rtry()
                    retry1()
                    try:
                        sleep(2)
                        if pyautogui.locateOnScreen('buster.png') \
                            != None:
                            pyautogui.click('buster.png')
                            sleep(1)
                        if pyautogui.locateOnScreen('captchaPASS.png') != None:
                            break
                        retry1()
                    except:
                        sleep(2)
                        if pyautogui.locateOnScreen('buster.png') \
                            != None:
                            pyautogui.click('buster.png')
                            sleep(1)
                        retry1()
                if pyautogui.locateOnScreen('captchaPASS.png') != None:
                    break
            except:
                if pyautogui.locateOnScreen('captchaPASS.png') != None:
                    break

                        # #click on solver

            try:

                if pyautogui.locateOnScreen('buster.png') != None:
                    pyautogui.click('buster.png')
                    sleep(1)
                if pyautogui.locateOnScreen('captchaPASS.png') != None:
                    break
                retry1()
            except:
                sleep(2)
                if pyautogui.locateOnScreen('buster.png') != None:
                    pyautogui.click('buster.png')
                    sleep(1)
                    sleep(8)
                retry1()
            if pyautogui.locateOnScreen('captchaPASS.png') != None:
                break

                        # #click on refresh

            try:

                if pyautogui.locateOnScreen('refresh.png') != None:
                    pyautogui.click('refresh.png')
                    sleep(1)
                if pyautogui.locateOnScreen('captchaPASS.png') != None:
                    break
                retry1()
            except:
                sleep(2)
                if pyautogui.locateOnScreen('refresh.png') != None:
                    pyautogui.click('refresh.png')
                    sleep(1)
                retry1()
            sleep(3)
            if pyautogui.locateOnScreen('captchaPASS.png') != None:
                break

            try:

                if pyautogui.locateOnScreen('buster.png') != None:
                    pyautogui.click('buster.png')
                    sleep(8)
                if pyautogui.locateOnScreen('captchaREDNgrok.png') \
                    != None:
                    rtry()
                if pyautogui.locateOnScreen('captchaPASS.png') != None:
                    break
                retry1()
            except:
                if pyautogui.locateOnScreen('captchaPASS.png') == None:

                                            # #close chrome

                    clear_cookies()
                    mouse.position = (1343, 14)
                    mouse.click(Button.left, 1)
                    open_chrome()
                    ChangeIp()
                    signup()
                    sleep(0.2)
                

                    qwiklabs()
                    minimize()
                    i = 1
                    while True:
                        open_chrome()
                        clear_cookies()
                        ChangeIp()
                        signup()
                        sleep(0.2)
                    

                        if i % 5 == 0:
                            circleci()
                            minimize()
                        else:
                            qwiklabs()
                            minimize()
                        i = i + 1

    # #click on login

    if pyautogui.locateOnScreen('NgrokSignupClick.png') != None:
        pyautogui.click('NgrokSignupClick.png')

    # #click on authtoken

    q = 0
    while pyautogui.locateOnScreen('ClickOnAuthtoken.png',
                                   confidence=0.8) == None:
        sleep(5)
        q = q + 1
        if q == 12:
            clear_cookies()
            mouse.position = (1343, 14)
            mouse.click(Button.left, 1)
            open_chrome()
            ChangeIp()
            signup()
            sleep(0.2)
        

            qwiklabs()
            minimize()
            i = 1
            while True:
                open_chrome()
                clear_cookies()
                ChangeIp()
                signup()
                sleep(0.2)
            

                if i % 5 == 0:
                    circleci()
                    minimize()
                else:
                    qwiklabs()
                    minimize()
                i = i + 1

    if pyautogui.locateOnScreen('ClickOnAuthtoken.png') != None:
        pyautogui.click('ClickOnAuthtoken.png')
    sleep(2)

    # #click and copy

    mouse.position = (592, 338)
    mouse.click(Button.left, 1)
    keyboard.press(Key.ctrl)
    keyboard.press('a')
    keyboard.release('a')
    keyboard.release(Key.ctrl)
    keyboard.press(Key.ctrl)
    keyboard.press('c')
    keyboard.release('c')
    keyboard.release(Key.ctrl)
    sleep(0.2)
    c = pyperclip.paste()

    # #back to circle ci

    keyboard.press(Key.ctrl)
    keyboard.press('1')
    keyboard.release('1')
    keyboard.release(Key.ctrl)
    sleep(0.5)

    # #paste authtoken

    mouse.position = (657, 693)
    mouse.click(Button.left, 2)
    keyboard.press(Key.backspace)
    keyboard.release(Key.backspace)
    keyboard.type(c)

    # #commit and run

    mouse.position = (927, 353)
    mouse.click(Button.left, 1)

    # #go to ngrok

    keyboard.press(Key.ctrl)
    keyboard.press('9')
    keyboard.release('9')
    keyboard.release(Key.ctrl)
    sleep(0.5)

    # #status

    mouse.position = (657, 693)
    sleep(0.5)
    mouse.click(Button.left, 1)
    sleep(0.5)
    keyboard.press(Key.ctrl)
    keyboard.press('l')
    keyboard.release('l')
    keyboard.release(Key.ctrl)
    sleep(0.5)
    keyboard.type('https://dashboard.ngrok.com/endpoints/status')
    sleep(0.5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    # #wait
    ChangeIp_On_Or_Off()
    sleep(80)

    if pyautogui.locateOnScreen('region.png') != None:
        sleep(10)

        # #refresh page

        keyboard.press(Key.ctrl)
        keyboard.press('r')
        keyboard.release('r')
        keyboard.release(Key.ctrl)
        sleep(11)

    if pyautogui.locateOnScreen('region.png') != None:
        sleep(20)

        # #refresh page

        keyboard.press(Key.ctrl)
        keyboard.press('r')
        keyboard.release('r')
        keyboard.release(Key.ctrl)
        sleep(7)

    if pyautogui.locateOnScreen('region.png') != None:
        sleep(11)

        # #refresh page

        keyboard.press(Key.ctrl)
        keyboard.press('r')
        keyboard.release('r')
        keyboard.release(Key.ctrl)
        sleep(7)

    if pyautogui.locateOnScreen('region.png') != None:
        sleep(15)

        # #refresh page

        keyboard.press(Key.ctrl)
        keyboard.press('r')
        keyboard.release('r')
        keyboard.release(Key.ctrl)
        sleep(7)

    if pyautogui.locateOnScreen('region.png') != None:
        sleep(15)

        # #refresh page

        keyboard.press(Key.ctrl)
        keyboard.press('r')
        keyboard.release('r')
        keyboard.release(Key.ctrl)
        sleep(7)

    if pyautogui.locateOnScreen('region.png') != None:
        sleep(10)

        # #refresh page

        keyboard.press(Key.ctrl)
        keyboard.press('r')
        keyboard.release('r')
        keyboard.release(Key.ctrl)
        sleep(7)

    if pyautogui.locateOnScreen('region.png') != None:
        ChangeIp_On_Or_Off()
        clear_cookies()
        mouse.position = (1343, 14)
        mouse.click(Button.left, 1)
        open_chrome()
        signup()
        sleep(0.2)
    

        qwiklabs()
        minimize()
        i = 1
        while True:
            open_chrome()
            clear_cookies()
            ChangeIp()
            signup()
            sleep(0.2)
        

            if i % 5 == 0:
                circleci()
                minimize()
            else:
                qwiklabs()
                minimize()
            i = i + 1

    # #copy URL

    mouse.position = (566, 393)
    mouse.click(Button.left, 3)
    sleep(0.2)
    keyboard.press(Key.ctrl)
    keyboard.press('c')
    keyboard.release('c')
    keyboard.release(Key.ctrl)
    sleep(0.1)
    c = pyperclip.paste()
    if 'tcp.ngrok.io' in c == False or len(c)>25 or len(c)<28:
        mouse.position = (566, 393)
        mouse.click(Button.left, 3)
        sleep(0.5)
        keyboard.press(Key.ctrl)
        keyboard.press('c')
        keyboard.release('c')
        keyboard.release(Key.ctrl)
        sleep(0.2)
        c = pyperclip.paste()

    if 'tcp.ngrok.io' in c == False or len(c)<25 or len(c)>28:
        ChangeIp_On_Or_Off()
        clear_cookies()
        mouse.position = (1343, 14)
        mouse.click(Button.left, 1)
        open_chrome()
        ChangeIp()
        signup()
        sleep(0.2)
    

        qwiklabs()
        minimize()
        i = 1
        while True:
            open_chrome()
            clear_cookies()
            ChangeIp()
            signup()
            sleep(0.2)
        

            if i % 5 == 0:
                circleci()
                minimize()
            else:
                qwiklabs()
                minimize()
            i = i + 1
    if 'tcp.ngrok.io' in c != False and len(c)>25 and len(c)<28:
        # #close chrome
        ChangeIp_On_Or_Off()
        mouse.position = (1343, 14)
        mouse.click(Button.left, 1)
        
            # #go to new window on windows
        
        keyboard.press(Key.cmd)
        keyboard.press(Key.ctrl)
        keyboard.press('d')
        keyboard.release(Key.cmd)
        keyboard.release(Key.ctrl)
        keyboard.release('d')
        sleep(1)
        
            # #click on search bar
        
        mouse.position = (72, 745)
        mouse.click(Button.left, 1)
        sleep(1)
        
            # #type remote
        
        keyboard.type('remote')
        sleep(2)
        
            # #click on remote desktop
        
        mouse.position = (259, 203)
        mouse.click(Button.left, 1)
        sleep(1.5)
        
            # #click on option
        
        mouse.position = (501, 350)
        mouse.click(Button.left, 1)
        sleep(0.5)
        
            # #click on URL bar
        
        mouse.position = (659, 311)
        mouse.click(Button.left, 1)
        keyboard.press(Key.ctrl)
        keyboard.press('a')
        keyboard.release('a')
        keyboard.release(Key.ctrl)
        keyboard.press(Key.backspace)
        keyboard.release(Key.backspace)
        sleep(0.2)
        
            # #paste the URL
        
        sleep(0.2)
        keyboard.type(c)
        sleep(0.5)
        
            # #select on type bar
        
        mouse.position = (803, 312)
        mouse.click(Button.left, 1)
        sleep(0.5)
        
            # #30 times pageleft
        
        def page_left():
            i = 0
            while i < 30:
                keyboard.press(Key.left)
                keyboard.release(Key.left)
                i = i + 1
        
        page_left()
        sleep(0.5)
        
            # #6 times page right
        
        def page_right():
            i = 0
            while i < 6:
                keyboard.press(Key.right)
                keyboard.release(Key.right)
                i = i + 1
        
        page_right()
        sleep(0.6)
        
            # #backspace 6 times
        
        keyboard.press(Key.backspace)
        keyboard.release(Key.backspace)
        keyboard.press(Key.backspace)
        keyboard.release(Key.backspace)
        keyboard.press(Key.backspace)
        keyboard.release(Key.backspace)
        keyboard.press(Key.backspace)
        keyboard.release(Key.backspace)
        keyboard.press(Key.backspace)
        keyboard.release(Key.backspace)
        keyboard.press(Key.backspace)
        keyboard.release(Key.backspace)
        sleep(0.5)
        
            # #select on type bar
        
        mouse.position = (803, 312)
        mouse.click(Button.left, 1)
        sleep(0.5)
        
            # keyboard.press(Key.backspace)
            # keyboard.release(Key.backspace)
            # sleep(0.25)
            # #click on USER NAME
        
        mouse.position = (662, 344)
        mouse.click(Button.left, 1)
        sleep(1)
        keyboard.press(Key.ctrl)
        keyboard.press('a')
        keyboard.release('a')
        keyboard.release(Key.ctrl)
        keyboard.press(Key.backspace)
        keyboard.release(Key.backspace)
        sleep(0.2)
        keyboard.type('Administrator')
        
            # #Enter
        
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        
            # #sleep(2)
        
        sleep(2)
        
            # #type PASS
        
        keyboard.type('Mvusic@123')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        sleep(2)
        
            # #click on YES
        
        mouse.position = (742, 529)
        mouse.click(Button.left, 1)
        sleep(20)
        if pyautogui.locateOnScreen('RemoteConectionCheck.png', confidence=0.8) != None:
            pass
        else:
                # #click on search bar
                
                mouse.position = (72, 745)
                mouse.click(Button.left, 1)
                sleep(1)
                
                    # #type remote
                
                keyboard.type('remote')
                sleep(2)
                
                    # #click on remote desktop
                
                mouse.position = (259, 203)
                mouse.click(Button.left, 1)
                sleep(1.5)
                
                    # #click on option
                
                mouse.position = (501, 350)
                mouse.click(Button.left, 1)
                sleep(0.5)
                
                    # #click on URL bar
                
                mouse.position = (659, 311)
                mouse.click(Button.left, 1)
                keyboard.press(Key.ctrl)
                keyboard.press('a')
                keyboard.release('a')
                keyboard.release(Key.ctrl)
                keyboard.press(Key.backspace)
                keyboard.release(Key.backspace)
                sleep(0.2)
                
                    # #paste the URL
                
                sleep(0.2)
                keyboard.type(c)
                sleep(0.5)
                
                    # #select on type bar
                
                mouse.position = (803, 312)
                mouse.click(Button.left, 1)
                sleep(0.5)
                
                    # #30 times pageleft
                
                def page_left():
                    i = 0
                    while i < 30:
                        keyboard.press(Key.left)
                        keyboard.release(Key.left)
                        i = i + 1
                
                page_left()
                sleep(0.5)
                
                    # #6 times page right
                
                def page_right():
                    i = 0
                    while i < 6:
                        keyboard.press(Key.right)
                        keyboard.release(Key.right)
                        i = i + 1
                
                page_right()
                sleep(0.6)
                
                    # #backspace 6 times
                
                keyboard.press(Key.backspace)
                keyboard.release(Key.backspace)
                keyboard.press(Key.backspace)
                keyboard.release(Key.backspace)
                keyboard.press(Key.backspace)
                keyboard.release(Key.backspace)
                keyboard.press(Key.backspace)
                keyboard.release(Key.backspace)
                keyboard.press(Key.backspace)
                keyboard.release(Key.backspace)
                keyboard.press(Key.backspace)
                keyboard.release(Key.backspace)
                sleep(0.5)
                
                    # #select on type bar
                
                mouse.position = (803, 312)
                mouse.click(Button.left, 1)
                sleep(0.5)
                
                    # keyboard.press(Key.backspace)
                    # keyboard.release(Key.backspace)
                    # sleep(0.25)
                    # #click on USER NAME
                
                mouse.position = (662, 344)
                mouse.click(Button.left, 1)
                sleep(1)
                keyboard.press(Key.ctrl)
                keyboard.press('a')
                keyboard.release('a')
                keyboard.release(Key.ctrl)
                keyboard.press(Key.backspace)
                keyboard.release(Key.backspace)
                sleep(0.2)
                keyboard.type('Administrator')
                
                    # #Enter
                
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
                
                    # #sleep(2)
                
                sleep(2)
                
                    # #type PASS
                
                keyboard.type('Mvusic@123')
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
                sleep(2)
                
                    # #click on YES
                
                mouse.position = (742, 529)
                mouse.click(Button.left, 1)
                sleep(20)
                if pyautogui.locateOnScreen('RemoteConectionCheck.png', confidence=0.8) != None:
                    pass
                else:
                    
                    mouse.position = (1343, 14)
                    mouse.click(Button.left, 1)
                    open_chrome()
                    clear_cookies()
                    signup()
                    sleep(0.2)
                
                    
                    qwiklabs()
                    minimize()
                    i = 1
                    while True:
                        open_chrome()
                        clear_cookies()
                        ChangeIp()
                        signup()
                        sleep(0.2)
                    
                    
                        if i % 5 == 0:
                            circleci()
                            minimize()
                        else:
                            qwiklabs()
                            minimize()
                        i = i + 1
                    
                    # #close pages
                
                mouse.position = (714, 421)
                mouse.click(Button.left, 1)
                sleep(2)
                mouse.position = (1338, 12)
                mouse.click(Button.left, 1)
                sleep(2)
            # #close pages
        
        mouse.position = (714, 421)
        mouse.click(Button.left, 1)
        sleep(2)
        mouse.position = (1338, 12)
        mouse.click(Button.left, 1)
        sleep(2)
        
        
def clear_cookies():
    sleep(3)

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
    sleep(1)

    # #new tab

    keyboard.press(Key.ctrl)
    keyboard.press('t')
    keyboard.release('t')
    keyboard.release(Key.ctrl)

    # #go to first page and close it

    keyboard.press(Key.ctrl)
    keyboard.press('1')
    keyboard.release('1')
    keyboard.release(Key.ctrl)
    keyboard.press(Key.ctrl)
    keyboard.press('w')
    keyboard.release('w')
    keyboard.release(Key.ctrl)

    # #select search bar

    keyboard.press(Key.ctrl)
    keyboard.press('l')
    keyboard.release('l')
    keyboard.release(Key.ctrl)


def open_chrome():
    sleep(7)

        # #go to new window on windows

    keyboard.press(Key.cmd)
    keyboard.press(Key.ctrl)
    keyboard.press('d')
    keyboard.release(Key.cmd)
    keyboard.release(Key.ctrl)
    keyboard.release('d')
    sleep(1)

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
    sleep(3)


def circleci():
    sleep(3)
    x = 64
    y = 743
    pyautogui.moveTo(x, y, duration=0.1)
    sleep(0.5)
    pyautogui.click(button='left', clicks=1, interval=0.1)
    sleep(5)
    pyautogui.typewrite('cmd', interval=0.02)
    sleep(4)
    x = 379
    y = 212
    pyautogui.moveTo(x, y, duration=0.1)
    sleep(0.5)
    pyautogui.click(button='left', clicks=1, interval=0.1)
    sleep(3)
    command = \
        '''powershell -c "Invoke-WebRequest -Uri 'https://dl.google.com/tag/s/appguid%3D%7B8A69D345-D564-463C-AFF1-A69D9E530F96%7D%26iid%3D%7B0FBDF0EC-4DF6-4765-5C09-45598F7F4281%7D%26lang%3Den%26browser%3D2%26usagestats%3D1%26appname%3DGoogle%2520Chrome%26needsadmin%3Dprefers%26ap%3Dx64-stable-statsdef_1%26brand%3DRXQR%26installdataindex%3Dempty/update2/installers/ChromeSetup.exe' -OutFile 'C:/Users/Administrator/Desktop/chrome.exe'" && cd /Users/Administrator/Desktop && chrome.exe && timeout 5 && pip install pywin32 && pip install keyboard && pip install pyautogui && pip install opencv-python && pip install pynput && powershell -c "Invoke-WebRequest -Uri 'https://github.com/loperkoper/image/archive/refs/heads/main.zip' -OutFile 'C:/Users/Administrator/Desktop/final.zip'" && tar -xf final.zip && cd image-main && cd final && cd circle && python circlesmart+vpn.py"'''

        # copying text to clipboard

    pyperclip.copy(command)
    x = 742
    y = 271
    pyautogui.moveTo(x, y, duration=0.1)
    pyautogui.click(button='right', clicks=1, interval=0.1)
    sleep(0.5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


def qwiklabs():
    sleep(3)
    x = 64
    y = 743
    pyautogui.moveTo(x, y, duration=0.1)
    sleep(0.5)
    pyautogui.click(button='left', clicks=1, interval=0.1)
    sleep(5)
    pyautogui.typewrite('cmd', interval=0.02)
    sleep(4)
    x = 379
    y = 212
    pyautogui.moveTo(x, y, duration=0.1)
    sleep(0.5)
    pyautogui.click(button='left', clicks=1, interval=0.1)
    sleep(3)
    command2 = \
        '''powershell -c "Invoke-WebRequest -Uri 'https://dl.google.com/tag/s/appguid%3D%7B8A69D345-D564-463C-AFF1-A69D9E530F96%7D%26iid%3D%7B0FBDF0EC-4DF6-4765-5C09-45598F7F4281%7D%26lang%3Den%26browser%3D2%26usagestats%3D1%26appname%3DGoogle%2520Chrome%26needsadmin%3Dprefers%26ap%3Dx64-stable-statsdef_1%26brand%3DRXQR%26installdataindex%3Dempty/update2/installers/ChromeSetup.exe' -OutFile 'C:/Users/Administrator/Desktop/chrome.exe'" && cd /Users/Administrator/Desktop && chrome.exe && timeout 5 && pip install pywin32 && pip install keyboard && pip install pyautogui && pip install opencv-python && pip install pynput && powershell -c "Invoke-WebRequest -Uri 'https://github.com/loperkoper/image/archive/refs/heads/main.zip' -OutFile 'C:/Users/Administrator/Desktop/final.zip'" && tar -xf final.zip && cd image-main && cd final && cd circle && python "qwiklabsSmart+vpn.py"'''

        # copying text to clipboard

    pyperclip.copy(command2)
    x = 742
    y = 271
    pyautogui.moveTo(x, y, duration=0.1)
    pyautogui.click(button='right', clicks=1, interval=0.1)
    sleep(0.5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


def minimize():
    sleep(3)
    x = 907
    y = 12
    pyautogui.moveTo(x, y, duration=0.1)
    sleep(0.5)
    pyautogui.click(button='left', clicks=1, interval=0.1)

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
    sleep(0.6)

    # #change to usa

    if pyautogui.locateOnScreen('changeLocationBrowsec1.png') != None:
        pyautogui.click('changeLocationBrowsec1.png')
    sleep(2)
    if pyautogui.locateOnScreen('changeLocationBrowsec2.png') != None:
        pyautogui.click('changeLocationBrowsec2.png')
    sleep(2)
    mouse.position = (219, 585)
    mouse.click(Button.left, 1)
    sleep(1.5)


install_chrome()
download_extention()
first_change_ip()

signup()
sleep(0.2)
z = pyperclip.paste()

qwiklabs()
minimize()
i = 1
while True:
    open_chrome()
    clear_cookies()
    ChangeIp()
    signup()
    sleep(0.2)

    if i % 5 == 0:
        circleci()
        minimize()
    else:
        qwiklabs()
        minimize()
    i = i + 1
