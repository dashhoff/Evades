import cv2
import numpy as np
import pyautogui
import time

# Установка значения порога сравнения
THRESHOLD = 0.7

# Загрузка изображения объекта
object_image = cv2.imread(r'C:\Users\mlavo\Desktop\Evades\Gats\Enemy.png', cv2.IMREAD_COLOR)

# Уменьшение разрешения объекта (по желанию)
# object_image = cv2.resize(object_image, (новая_ширина, новая_высота))

# Определение размера объекта
h, w, _ = object_image.shape
object_center_x, object_center_y = w // 2, h // 2

pyautogui.FAILSAFE = True

while True:
    # Снимок экрана
    screenshot = pyautogui.screenshot()

    # Преобразование в массив numpy и RGB формат
    screenshot_np = np.array(screenshot)
    screenshot_rgb = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2RGB)

    # Поиск объекта
    result = cv2.matchTemplate(screenshot_rgb, object_image, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= THRESHOLD)

    # Перемещение мыши к центру объекта, если найден
    if len(loc[0]) > 0:
        max_loc = (loc[1][0], loc[0][0])  # Находим первое совпадение
        center_x, center_y = max_loc[0] + object_center_x, max_loc[1] + object_center_y
        pyautogui.moveTo(center_x, center_y)