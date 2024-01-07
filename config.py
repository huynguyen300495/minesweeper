
import platform


# Get more detailed information, especially useful for Unix-like OS
detailed_os_name = platform.system()

if detailed_os_name == "Darwin":
    EASY_LEFT   = 1230
    EASY_TOP    = 815
    EASY_WIDTH  = 1124
    EASY_HEIGHT = 902
else:
    EASY_LEFT   = 942
    EASY_TOP    = 524
    EASY_WIDTH  = 677
    EASY_HEIGHT = 540
