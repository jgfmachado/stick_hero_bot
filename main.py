'''
A "not so great" bot that plays Stick Hero.
Requires scrcpy to stream your phone, or an emulator perhaps.
Also requires opencv installed through pip.
'''

import pyautogui
import time
import subprocess
import math

def main():
    level = 1
    while True:
        location_hero = locate_center_on_image("stick_hero_bot\\hero.png")
        location_goal = locate_center_on_image("stick_hero_bot\\goal.png")
        
        print(f"Level: {level}")
        distance = location_goal.x - location_hero.x
        print(f"Distance: {distance}px")
        duration = math.ceil(distance*1.188)
        print(f"Duration: {duration}ms")

        exec("adb shell input touchscreen swipe 500 500 500 500 " + str(duration))

        time.sleep(2.5)

        level += 1

# returns the center position, on the screen, of a given image
def locate_center_on_image(img):
    return pyautogui.locateCenterOnScreen(img, confidence = 0.9)

# execute shell commands
def exec(command):
    subprocess.run(command, shell=True)

if __name__ == "__main__":
    main()