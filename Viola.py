import keyboard
import pyautogui
import time

pyautogui.FAILSAFE = True

# Определите координаты центра экрана
screen_width, screen_height = pyautogui.size()
center_x, center_y = screen_width // 2, screen_height // 2

# Задайте скорость, с которой будут отправляться нажатия клавиш (по желанию).
time.sleep(0.5)
print(pyautogui.position())
#Мышь

def main():
    while True:
        # Получите текущее положение курсора мыши
        mouse_x, mouse_y = pyautogui.position()

        # Определите направление движения курсора относительно центра экрана
        if mouse_x < center_x:
            pyautogui.keyUp('right')
            pyautogui.keyDown('left')
        elif mouse_x > center_x:
            pyautogui.keyDown('right')
            pyautogui.keyDown('right')

        if mouse_y < center_y:
            pyautogui.keyUp('down')
            pyautogui.keyDown('up')
        elif mouse_y > center_y:
            pyautogui.keyUp('up')
            pyautogui.keyDown('down')

        #if mouse_y < 960 and mouse_y > 640:
            #pyautogui.keyUp('down')
            #pyautogui.keyUp('up')

if __name__ == "__main__":
    main()

#Клавиатура
'''
while True:
    key_event = keyboard.read_event()
    if key_event.event_type == keyboard.KEY_DOWN:
        if key_event.name == 'W':
            keyboard.press_and_release('up')
        elif key_event.name == 'A':
            keyboard.press_and_release('left')
        elif key_event.name == 'S':
            keyboard.press_and_release('down')
        elif key_event.name == 'D':
            keyboard.press_and_release('right')
'''