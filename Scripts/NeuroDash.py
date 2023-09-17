import cv2
import numpy as np
import pyautogui

# Создайте список изображений, которые вы хотите найти
image_paths = [
    r'C:\Users\mlavo\Desktop\Evades\img.png',
    r'C:\Users\mlavo\Desktop\Evades\img1.png',
    # Добавьте пути к другим изображениям здесь
]

# Определите регион скриншота
x, y, width, height = 825, 425, 300, 300

while True:
    for image_path in image_paths:
        # Загрузите изображение объекта, который вы хотите найти
        object_image = cv2.imread(image_path)

        # Сделайте скриншот заданной области экрана
        screenshot = pyautogui.screenshot(region=(x, y, width, height))
        screen_image = np.array(screenshot)

        # Преобразуйте изображение в формат BGR (OpenCV)
        screen_image = cv2.cvtColor(screen_image, cv2.COLOR_RGB2BGR)

        # Попытайтесь найти объект на скриншоте
        result = cv2.matchTemplate(screen_image, object_image, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8  # Порог совпадения (может потребоваться настройка)

        # Найдите местоположение объекта
        loc = np.where(result >= threshold)

        for pt in zip(*loc[::-1]):
            # Обведите найденный объект красным прямоугольником
            cv2.rectangle(screen_image, pt, (pt[0] + object_image.shape[1], pt[1] + object_image.shape[0]), (0, 0, 255), 1)

        # Отобразите скриншот с обводкой объекта
        cv2.imshow('Object Detection', screen_image)

        # Ожидайте нажатия клавиши 'q' для выхода
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Закройте окно и освободите ресурсы
cv2.destroyAllWindows()