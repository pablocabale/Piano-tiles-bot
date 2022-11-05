from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def displayMouseInfo():
    while not (keyboard.is_pressed('esc')):
        x, y = pyautogui.position()
        r, g ,b = pyautogui.pixel(x, y)
        positionStr = 'X: {0} Y: {1}  RGB: ({2}, {3}, {4})'.format(str(x).rjust(4), str(y).rjust(4), str(r).rjust(3), str(g).rjust(3), str(b).rjust(3))
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)

def main():
    displayMouseInfo()

main()