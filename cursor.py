import pyautogui

def left_click(x,y):
    x_coor = 644 + ((x-1) * 56)
    y_coor = 438 +((y-1) * 56)

    pyautogui.moveTo(x_coor, y_coor)  
    pyautogui.doubleClick(button='left')


def right_click(x,y):
    x_coor = 644 + ((x-1) * 56)
    y_coor = 438 +((y-1) * 56)

    pyautogui.moveTo(x_coor, y_coor) 
    pyautogui.click(button='right')






