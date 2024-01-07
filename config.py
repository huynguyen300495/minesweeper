import platform


# Get OS information
detailed_os_name = platform.system()

if detailed_os_name == "Darwin":
    EASY_LEFT   = 1230
    EASY_TOP    = 815
    EASY_WIDTH  = 1124
    EASY_HEIGHT = 902
    GRAY_THRESHOLD = 4.5

else:
    EASY_LEFT   = 942
    EASY_TOP    = 524
    EASY_WIDTH  = 677
    EASY_HEIGHT = 540
    GRAY_THRESHOLD = 9.0

EASY_X = 10  # The number of squares horizontally
EASY_Y = 8   # The number of squares vertically


# Colors
LIGHT_GREEN = (170, 215, 81, 255)
DARK_GREEN  = (162, 209, 73, 255)
LIGHT_GRAY  = (229, 194, 159, 255)
DARK_GRAY   = (215, 184, 153, 255)

COLOR_ONE   = (25, 118, 210, 255)
COLOR_TWO   = (56, 142, 60, 255)
COLOR_THREE = (211, 47, 47, 255)
COLOR_FOUR  = (123, 31, 162, 255)

