from pyautogui import*
import pyautogui
import time
import keyboard
#import random
from pynput.mouse import Button, Controller




Mouse = Controller()
print('The current pointer position is {0}'.format(
    Controller().position))

while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(132.578125,  540.88671875)[0] == 0:
        Mouse.position = (132.578125, 540.88671875)
        Mouse.press(Button.left)
        time.sleep(0.01)
        Mouse.release(Button.left)

    if pyautogui.pixel(227.29296875, 540.88671875)[0] == 0:
        Mouse.position = (227.29296875, 540.88671875)
        Mouse.press(Button.left)
        time.sleep(0.01)
        Mouse.release(Button.left)

    if pyautogui.pixel(332.71484375, 540.88671875)[0] == 0:
        Mouse.position = (332.71484375, 540.88671875)
        Mouse.press(Button.left)
        time.sleep(0.01)
        Mouse.release(Button.left)

    if pyautogui.pixel(459, 540.88671875)[0] == 0:
        Mouse.position = (450, 540.88671875)
        Mouse.press(Button.left)
        time.sleep(0.01)
        Mouse.release(Button.left)