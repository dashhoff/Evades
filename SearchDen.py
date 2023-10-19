import cv2
import numpy as np
import pyautogui
import time
from numba import jit

#825, 425, 300, 300
# Размеры и положение региона, который вы снимаете
region_x, region_y, region_width, region_height = 600, 400, 600, 500

# Изменения координат объекта, найденные на скриншоте, к координатам на основном экране
@jit(fastmath = True, NoPython = True, NoGIL = True)
def convert_coordinates(x, y):
    global region_x, region_y
    return x + region_x, y + region_y

pyautogui.FAILSAFE = True

# Изображение объекта 
object_image = cv2.imread(r'C:\Users\mlavo\Desktop\Evades\Img\Den.png', cv2.IMREAD_COLOR)

jit(fastmath = True, NoPython = True, NoGIL = True)
while True:
    timer = time.perf_counter()
    # Скрин
    screenshot = pyautogui.screenshot(region=(region_x, region_y, region_width, region_height))

    # Массив и преобразовка
    screenshot_np = np.array(screenshot)
    screenshot_rgb = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2RGB)

    # Поиск
    result = cv2.matchTemplate(screenshot_rgb, object_image, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # Двигаем мышь
    if max_val > 0.7:
        h, w, _ = object_image.shape
        center_x, center_y = convert_coordinates(max_loc[0] + w // 2, max_loc[1] + h // 2)
        pyautogui.moveTo(center_x, center_y)

    print(time.perf_counter() - timer)
