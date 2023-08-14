import pyautogui
import time
import keyboard
import threading
import os

def aceitarPartida():
    while True:
        btn_aceitar =pyautogui.locateCenterOnScreen('Screenshot_1.png',confidence=0.5)

        if btn_aceitar:
            pyautogui.click(btn_aceitar.x, btn_aceitar.y)
            print('botão encontrado')
            break
        else:
            time.sleep(5)
            print('Procurando o botão')

def pararScript():
    while True:
        if keyboard.is_pressed('esc'):
            os._exit(0)

threading.Thread(target=aceitarPartida).start()
threading.Thread(target=pararScript).start()