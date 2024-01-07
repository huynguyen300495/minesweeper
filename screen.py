from config import *
import pyautogui
from PIL import Image, ImageStat
import numpy as np
import pytesseract
from collections import Counter


def get_screenshot():
    region = (EASY_LEFT, EASY_TOP, EASY_WIDTH, EASY_HEIGHT)
    screenshot = pyautogui.screenshot(region=region)
    screenshot.save('screenshot.png')


def analyze_square(img):
    img_preprocessed = img.convert('L')
    img_preprocessed = img_preprocessed.point(lambda x: 0 if x < 128 else 255, '1')

    text = pytesseract.image_to_string(img_preprocessed, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
    text = text.strip()
    if text.isdigit(): 
        if text == '7': return 1
        return int(text)

    # No number detected, classify green vs gray
    pixels = list(img.getdata())
    color_count = Counter(pixels)
    most_common_color = color_count.most_common(1)[0][0]

    # Handle both RGB and RGBA formats
    if len(most_common_color) == 4:
        r, g, b, _ = most_common_color  # Ignore the alpha channel
    else:
        r, g, b = most_common_color
        
    if g > r and g > b:
        return '-'
    return 0



