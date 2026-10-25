import pyautogui
import time

while True:
    # Captura a posição atual do mouse
    pos = pyautogui.position()
    print(pos)   # Exibe no terminal
    time.sleep(1)
