from config import *
import pyautogui
from PIL import Image

def get_screenshot():
    region = (EASY_LEFT, EASY_TOP, EASY_WIDTH, EASY_HEIGHT)
    screenshot = pyautogui.screenshot(region=region)
    screenshot.save('screenshot.png')

def color_equal(color1, color2, tolerance=10):
    return all(abs(c1 - c2) <= tolerance for c1, c2 in zip(color1, color2))


def is_color_approx_equal(color1, color2, tolerance=5):
    return all(abs(c1 - c2) <= tolerance for c1, c2 in zip(color1, color2))

def determine_color(color):
    # Define your colors
    LIGHT_GREEN = (170, 215, 81, 255)
    DARK_GREEN  = (162, 209, 73, 255)
    LIGHT_GRAY  = (229, 194, 159, 255)
    DARK_GRAY   = (215, 184, 153, 255)
    COLOR_ONE   = (25, 118, 210, 255)
    COLOR_TWO   = (56, 142, 60, 255)
    COLOR_THREE = (211, 47, 47, 255)
    COLOR_FOUR  = (123, 31, 162, 255)

    # Check the color and return the corresponding value
    if is_color_approx_equal(color, LIGHT_GREEN) or is_color_approx_equal(color, DARK_GREEN):
        return '-'
    elif is_color_approx_equal(color, LIGHT_GRAY) or is_color_approx_equal(color, DARK_GRAY):
        return '0'
    elif is_color_approx_equal(color, COLOR_ONE):
        return 1
    elif is_color_approx_equal(color, COLOR_TWO):
        return 2
    elif is_color_approx_equal(color, COLOR_THREE):
        return 3
    elif is_color_approx_equal(color, COLOR_FOUR):
        return 4
    return None


def analyze_square(image):
    color_counts = {'-': 0, '0': 0, 1: 0, 2: 0, 3: 0, 4: 0}

    # Iterate over each pixel
    width, height = img.size
    for x in range(width):
        for y in range(height):

            # Get the color of the pixel
            color = img.getpixel((x, y))
            color_class = determine_color(color)
            
            if color_class in color_counts:
                color_counts[color_class] += 1

    # Check for numbers first
    for num in range(1, 5):
        if color_counts[num] >= 10:
            return num

    # Check for '-' or '0'
    if color_counts['-'] >= color_counts['0']:
        return '-'
    else:
        return 0


# Open an image file
with Image.open('screenshot.png') as img:
    result = analyze_square(img)
    print(result)