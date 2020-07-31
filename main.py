'''
A bot for Stick Hero
Requires scrcpy to stream your phone, or an emulator perhaps
Also requires opencv installed through pip
'''

import pyautogui
import time

#pyautogui.displayMousePosition()
#pyautogui.screenshot('screenshot.png')

def main():
    while True:
        location_hero = locate_center_on_image("stick_hero_bot\\hero.png")
        location_goal = locate_center_on_image("stick_hero_bot\\goal.png")
        pyautogui.moveTo(location_hero)
        print(location_hero.x)
        print(location_goal.x)
        
        distance = location_goal.x - location_hero.x
        duration = 0.001 * distance
        mouse_click(duration)

        time.sleep(4)

def mouse_click(duration):
    pyautogui.mouseDown()
    time.sleep(duration)
    pyautogui.mouseUp()

def locate_center_on_image(img):
    return pyautogui.locateCenterOnScreen(img, confidence = 0.9)


if __name__ == "__main__":
    main()