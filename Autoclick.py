import pyautogui as pag
import keyboard

pag.PAUSE = 0.001

print("F8 to right click")
print("F9 to left click")
print("F10 to stop")
print("F11 to exit")


def clicker():
    while True:
        pag.doubleClick()
        if keyboard.is_pressed("F10"):
            break

def rightclicker():
    while True:
        pag.rightClick()
        if keyboard.is_pressed("F10"):
            break


while True:
    if keyboard.is_pressed("F9"):
        clicker()
    if keyboard.is_pressed("F8"):
        rightclicker()
    if keyboard.is_pressed("F11"):
        break
