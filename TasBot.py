import pyautogui
import time
from numba import jit

# Задержка перед началом работы бота (дайте игре время для загрузки)
time.sleep(0.5)
pyautogui.center

# Функции для нажатия клавиш W, A, S, D
def press_w():
    print('Снизу')
    pyautogui.moveTo(960, 640)
    # pyautogui.keyDown('w')
    # pyautogui.keyUp('w')


def press_a():
    print('Справа')
    pyautogui.moveTo(860, 540)
    # pyautogui.keyDown('a')
    # pyautogui.keyUp('a')

def press_s():
    print('Сверху')
    pyautogui.moveTo(960, 440)
    # pyautogui.keyDown('s')
    # pyautogui.keyUp('s')

def press_d():
    print('Слева')
    pyautogui.moveTo(1060, 540)
    # pyautogui.keyDown('d')
    # pyautogui.keyUp('d')


# Функция для обнаружения врага и получения его координат
jit(fastmath = True, NoPython = True, NoGIL = True)
def detect_enemy_coordinates():
    locate_enemy = pyautogui.locateOnScreen(r'C:\Users\mlavo\Desktop\Evades\Img\Enemy.png', confidence=0.7, region=(825, 425, 300, 300))
    if locate_enemy:
        enemy_x = locate_enemy.left + locate_enemy.width / 2
        enemy_y = locate_enemy.top + locate_enemy.height / 2
        return enemy_x, enemy_y
    else:
        return None

# Основной цикл бота
jit(fastmath = True, NoPython = True, NoGIL = True)
while True:
    timer = time.perf_counter()
    enemy_coordinates = detect_enemy_coordinates()  # Получаем координаты врага

    if enemy_coordinates:
        character_x, character_y = pyautogui.size()  # Получаем размер экрана (для определения координат персонажа в центре)
        character_x /= 2
        character_y /= 2

        enemy_x, enemy_y = enemy_coordinates

        # Определяем направление движения врага относительно персонажа и нажимаем соответствующую клавишу
        if enemy_x > character_x:
            press_a()  # Враг справа, двигаемся влево
        else:
            press_d()  # Враг слева, двигаемся вправо

        if enemy_y > character_y:
            press_w()  # Враг снизу, двигаемся вверх
        else:
            press_s()  # Враг сверху, двигаемся вниз
    else:
        pyautogui.moveTo(960, 540)
        # Если враг не обнаружен, можно добавить другую логику или оставить пустым
        pass

    print(time.perf_counter() - timer)