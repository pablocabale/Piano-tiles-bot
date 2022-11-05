from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

def click(x,y,pressedTime):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(pressedTime)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def displayMouseInfo():
    while not (keyboard.is_pressed('esc')):
        x, y = pyautogui.position()
        r, g ,b = pyautogui.pixel(x, y)
        positionStr = 'X: {0} Y: {1}  RGB: ({2}, {3}, {4})'.format(str(x).rjust(4), str(y).rjust(4), str(r).rjust(3), str(g).rjust(3), str(b).rjust(3))
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)

def playPianoTiles():
    position1 = [750, 650]
    position2 = [875, 650]
    position3 = [1000, 650]
    position4 = [1125, 650]
    positions = [position1, position2, position3, position4]
    pressedTime = 0.01
    while not (keyboard.is_pressed('esc')):
        for position in positions:
            if pyautogui.pixel(position[0], position[1])[0] == 0:
                click(position[0], position[1], pressedTime)

def main():
    playPianoTiles()

<<<<<<< HEAD
main()

#displayMouseInfo()
=======
#main()

displayMouseInfo()
>>>>>>> main
