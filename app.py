import pyautogui
from time import sleep
import datetime
from datetime import datetime
import os


datahora = datetime.now()
datahora = datahora.strtime('%H.%M.#S')

pyautogui.PAUSE = 3

while True:
    datahora = datetime.now()
    datahora1 = datahora.strftime('%H.%M.#S')
    print(datahora1)
    sleep(1)
    os.system("cls")
    if datahora1 > str('09:50:00'):
        pyautogui.click(315,752)
        pyautogui.click(1196,83)
        pyautogui.press('enter',presses=2)
        pyautogui.click(57,446)
        pyautogui.click(799,667)
        break
pyautogui.alert(text='Ponto Batido.', title='', button='OK')