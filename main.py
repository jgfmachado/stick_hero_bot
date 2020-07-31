'''
A bot for Stick Hero
Requires scrcpy to stream your phone, or an emulator perhaps
Also requires opencv installed through pip
'''

import pyautogui
import time
import subprocess
import numpy as np
import math

#pyautogui.displayMousePosition()
#pyautogui.screenshot('screenshot.png')

def main():
    while True:
        location_hero = locate_center_on_image("stick_hero_bot\\hero.png")
        location_goal = locate_center_on_image("stick_hero_bot\\goal.png")
        #pyautogui.moveTo(location_hero)
        print(location_hero.x)
        print(location_goal.x)
        
        distance = location_goal.x - location_hero.x
        duration = int(math.floor(distance + np.log(distance) * np.log(distance)))
        #duration = 0.001 * distance
        #mouse_click(duration)

        exec("adb shell input touchscreen swipe 500 500 500 500 " + str(duration))

        time.sleep(3)

def mouse_click(duration):
    pyautogui.mouseDown()
    time.sleep(duration)
    pyautogui.mouseUp()

def locate_center_on_image(img):
    return pyautogui.locateCenterOnScreen(img, confidence = 0.9)

# execute shell commands
def exec(command):
    subprocess.run(command, shell=True)

if __name__ == "__main__":
    main()