import pyautogui

pyautogui.position()

f = True


while f == True:
    fisheye = pyautogui.locateOnScreen('clickerheroes_fisheye.png')
    pyautogui.moveTo(fisheye, duration=1)
    pyautogui.click()