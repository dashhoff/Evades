#from _typeshed import AnyStr_co
import PIL
from PIL import ImageGrab
import pyscreenshot as ImageGrab
import cv2
import pyautogui
import os
import keyboard
import math
import numpy as np
from time import sleep
import threading

pyautogui.FAILSAFE = True

#880 480 200 200
sleep(1)
x = pyautogui.position()
print(x)

while True:
    locate_enemy = pyautogui.locateOnScreen(r'C:\Users\mlavo\Desktop\Evades/img.png',confidence=0.8, region = (825,425,300,300))
    if locate_enemy is None:
        print('Нема')
    if locate_enemy is not None:
        print('ДААААААААААААААААААА')
        pyautogui.keyDown('x')

#while (True):
#    img = pyautogui.screenshot(region=(880,480, 200, 200))
#    img.save(r"C:\Users\mlavo\Desktop\Evades\img.png")
#    continue

#sleep(1)
#print (pyautogui.position())
#img = pyautogui.screenshot(region=(600,200, 700, 400))
#img.save(r"C:\Users\mlavo\Desktop\Evades\img.png")


'''
# Определите регион скриншота (левая верхняя точка и размер)
region = (825, 425, 1125, 725)

# Путь к изображению объекта, который нужно найти
object_image_path = r'C:\Users\mlavo\Desktop\Evades/img.png'

while True:
    # Сделать скриншот региона экрана
    screenshot = pyautogui.screenshot(region=region)
    
    # Загрузить изображение объекта
    object_image = cv2.imread(object_image_path)
    
    # Попробовать найти объект на скриншоте
    result = cv2.matchTemplate(np.array(screenshot), object_image, cv2.TM_CCOEFF_NORMED)
    _, _, _, max_loc = cv2.minMaxLoc(result)
    
    threshold = 0.8  # Порог совпадения (может потребоваться настройка)

    if np.max(result) >= threshold:
        # Если объект найден, получите его координаты и нажмите клавишу 'z'
        object_width, object_height = object_image.shape[:-1]
        object_x, object_y = max_loc
        pyautogui.keyDown('x')
        pyautogui.keyDown('x')
        pyautogui.keyDown('x')
        print("Объект найден и нажата клавиша 'x'")
'''


'''
print (pyautogui.size())
pyautogui.moveTo(800, 1080/2, duration = 0.5)
print (pyautogui.position())
pyautogui.click(clicks=1000, interval=0.005)
'''

'''
pyautogui.PAUSE = 0.2
pyautogui.keyDown('d')
sleep(0.5)
pyautogui.keyDown('w')
sleep(0.25)
pyautogui.keyUp('w')
sleep(0.05)
pyautogui.keyDown('s')
sleep(0.035)
pyautogui.keyUp('s')
sleep(0.02)
pyautogui.keyDown('s')
sleep(0.01)
pyautogui.keyUp('s')
sleep(0.5)
pyautogui.keyUp('d')

sleep(0.25)
pyautogui.keyDown('d')
sleep(0.75)
pyautogui.keyDown('s')
sleep(0.05)
pyautogui.keyUp('s')
sleep(0.2)
pyautogui.keyDown('w')
sleep(0.2)
pyautogui.keyUp('d')
pyautogui.keyDown('s')
sleep(0.1)
pyautogui.keyDown('d')
sleep(0.2)
'''