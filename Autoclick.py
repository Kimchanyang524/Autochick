import pyautogui as pag
import keyboard

pag.PAUSE = 0.001


def clicker():
    while True:
        pag.doubleClick()
        if keyboard.is_pressed("F10"):
            break


while True:
    if keyboard.is_pressed("F9"):
        clicker()
