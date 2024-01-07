from config import *
import pyautogui

def get_screenshot():
    region = (EASY_LEFT, EASY_TOP, EASY_WIDTH, EASY_HEIGHT)
    screenshot = pyautogui.screenshot(region=region)
    screenshot.save('screenshot.png')

