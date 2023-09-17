import cv2
import numpy as np
import pyautogui
import time

#x, y, width, height = 40, 90, 1860, 910

pyautogui.FAILSAFE = True
time.sleep(1)
#x = pyautogui.position()
#print(x)

#Изображение объекта 
object_image = cv2.imread(r'C:\Users\mlavo\Desktop\Evades/Den.png', cv2.IMREAD_COLOR)


while True:
    #Скрин
    screenshot = pyautogui.screenshot()

    #Массив и преобразовка
    screenshot_np = np.array(screenshot)
    #screenshot_rgb = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2RGB)

    #Поиск
    result = cv2.matchTemplate(screenshot_np, object_image, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    #Двигаем мышь
    if max_val > 0.7:
        h, w, _ = object_image.shape
        center_x, center_y = max_loc[0] + w // 2, max_loc[1] + h // 2
        pyautogui.moveTo(center_x, center_y)