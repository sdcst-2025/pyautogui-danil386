import pyautogui

pyautogui.position()

skull = pyautogui.locateOnScreen('skull.png')
pyautogui.moveTo(skull, duration=1)
pyautogui.click()
