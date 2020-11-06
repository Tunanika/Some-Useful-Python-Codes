#from pyautogui import*
import pyautogui
import time
import keyboard
#import random
from pynput.mouse import Button, Controller


Mouse = Controller()
print('The current pointer position is {0}'.format(
    Controller().position))


while keyboard.is_pressed('q') == False:

    
        Mouse.position = (126.1171875, 765.875)
        Mouse.press(Button.left)
        Mouse.release(Button.left)
        print(Mouse.position)

        time.sleep(0.5)
   
        Mouse.position = (213.8671875, 765.875)
        Mouse.press(Button.left)
        Mouse.release(Button.left)
        print(Mouse.position)

        time.sleep(0.5)

        Mouse.position = (332.71484375, 765.875)
        Mouse.press(Button.left)
        Mouse.release(Button.left)
        print(Mouse.position)

        time.sleep(0.5)
   
        Mouse.position = (413.4453125, 765.875)
        Mouse.press(Button.left)
        Mouse.release(Button.left)
        print(Mouse.position)

        time.sleep(0.5)
