import time 
from time import sleep
import pyautogui
from pynput import keyboard
from pynput.keyboard import Key, KeyCode
import threading
import pyautogui

isSpamming = False
isThreadStopped = False
isSpamStopped = False

def spam():
    global isSpamming, isThreadStopped, isSpamStopped

    text = input("\nEnter some text to spam: ")
    interval = float(input("Enter the interval: "))
    amount = int(input("Enter the amount of messages: "))
    while amount:
        if isSpamming:
            pyautogui.write(text)
            pyautogui.hotkey('enter')

        if isThreadStopped or isSpamStopped:
            break

        amount -= 1
        sleep(interval)

    if isSpamStopped:
        isSpamStopped = False
        spam()

def on_press(key):
    global isSpamming, isThreadStopped, isSpamStopped

    if key == Key.tab: 
        isSpamming = not isSpamming
    if key == Key.ctrl:
        isSpamStopped = True

def on_release(key):
    global isThreadStopped

    if key == Key.esc:
        isThreadStopped = True
        exit()

th1 = threading.Thread(target = spam)
th1.start()

with keyboard.Listener(on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
