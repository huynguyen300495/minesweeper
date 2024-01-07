from config import *
import pyautogui
from PIL import Image, ImageStat
import numpy as np
import pytesseract


def get_screenshot():
    region = (EASY_LEFT, EASY_TOP, EASY_WIDTH, EASY_HEIGHT)
    screenshot = pyautogui.screenshot(region=region)
    screenshot.save('screenshot.png')


def analyze_square(img):
    img_preprocessed = img.convert('L')
    img_preprocessed = img_preprocessed.point(lambda x: 0 if x < 128 else 255, '1')

    text = pytesseract.image_to_string(img_preprocessed, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
    text = text.strip()
    if text.isdigit(): return int(text)

    # No number detected, classify green vs gray
    stat = ImageStat.Stat(img)
    std_dev = stat.stddev

    # If the standard deviation is low, it's likely a gray square
    if np.mean(std_dev) < GRAY_THRESHOLD:
        return 0
    else:
        # Otherwise, it's a green square (unrevealed)
        return '-'



