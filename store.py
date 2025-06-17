import pyautogui

pyautogui.position()

c = True

while c == True:
    f = True
    u = True
    n = True
    skull = pyautogui.locateOnScreen('skull.png')
    pyautogui.moveTo(skull, duration=1)
    pyautogui.click()
    while f == True:
        try:
            fisheye = pyautogui.locateOnScreen('clickerheroes_fisheye.png')
            pyautogui.moveTo(fisheye, duration=1)
            pyautogui.click()
        except:
            break   
    while u == True:
        try:
            upgrade = pyautogui.locateOnScreen('bluesliver.png')
            pyautogui.moveTo(upgrade, duration=1)
            pyautogui.click()       
        except:
            break
    while n == True:
        try:
            nextarea = pyautogui.locateOnScreen('exclamation')
            pyautogui.moveTo(nextarea, duration=1)
            pyautogui.click()       
        except:
            break