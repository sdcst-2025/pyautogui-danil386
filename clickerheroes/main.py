import pyautogui
import time

def main():

    pyautogui.FAILSAFE = True
    print("starting")
    for i in range (0,10):
        print(".")
        time.sleep(1)
    print("Go")

def click():
    try:
        skull = pyautogui.locateOnScreen('skull.png')
        pyautogui.moveTo(skull, duration=1)
        for i in range (0,75):
            pyautogui.click()
        print("clicked!")
    except:
        print("error")

def upgrade():
    try:
        upgrade = pyautogui.locateOnScreen('bluesliver.png', grayscale = False, confidence = 0.996)
        pyautogui.moveTo(upgrade, duration=1)
        pyautogui.click()
        print("upgraded!")
        ux = 'u1'
        return ux
    except:
        print("no upgrade available")
        ux = 'u2'
        return ux

def nextarea():
    try:
        nextarea = pyautogui.locateOnScreen('nextarea.png', region = [980, 345, 25, 15], grayscale = False, confidence = 0.6)
        pyautogui.moveTo(nextarea, duration =1)
        for i in range (0,7):
            pyautogui.click()
    except:
        print("next level unavailable")
        n = False   

def heropower():
    hp1 = pyautogui.click(x = 250, y = 620)
    print("power 1 acquired")
    hp2 = pyautogui.click(x = 285, y = 620)
    print("power 2 acquired")

def herospecials():
    try:
        herospecials = pyautogui.locateOnScreen('herospecials.png', grayscale = False, confidence = 0.8)
        pyautogui.moveTo(herospecials, duration = 1)
        pyautogui.click()
    except:
        print("no specials available")
        hs = False

def hire():
    try:
        hire = pyautogui.locateOnScreen('hire.png', grayscale = False, confidence = 0.996)
        pyautogui.moveTo(hire, duration = 1)
        pyautogui.click()
    except:
        print("no heroes available for hire")
        h = False

def scroll():
    try:
        scroll = pyautogui.locateOnScreen('scroll.png', grayscale = False)
        pyautogui.moveTo(scroll, duration = 1)
        for i in range (0,5):
            pyautogui.click()
    except:
        print("not possible to scroll at the moment")

def boss():
    try:
        pyautogui.locateOnScreen('bossclock.png', grayscale = False, confidence = 0.8)
        for i in (0,8):
            click()
        nextarea()
        time.sleep(5)
        try:
            pyautogui.locateOnScreen('bossclock.png', grayscale = False, confidence = 0.8)
            try:
                pastarea = pyautogui.locateOnScreen('pastarea.png', region = [865, 345, 25, 15], grayscale = False, confidence = 0.6)
                pyautogui.moveTo(pastarea, duration =1)
                pyautogui.click()
            except:
                print("past level unavailable")
            u = True
            hp = True
            ux = 1
            while u == True:
                ux = float(ux)
                click()
                uoption = upgrade()
                print(uoption)
                if uoption == 'u1':
                    ux = ux+1
                    print(ux)
                elif uoption == 'u2':
                    ux = ux + 0
                    print(ux)
                if ux == 25:
                    print("Yay! 25 Levels")
                    u=False
                else:
                    u=True
                time.sleep(3)
            while hp == True:
                for i in range (0,50):
                    click()
                heropower()
                hp = False
                time.sleep(3)
            bx = 'b1'
            hx = 'h1'
            o = [bx,hx]
            return o
        except:
            print("boss defeated")
    except:
        print("no bosses at the moment")

main()
c = True
u = True
hp = True
while c == True:
    pyautogui.FAILSAFE = True
    u = True
    hp = True
    click()
    time.sleep(5)
    hire()
    ux = 1
    while u == True:
        ux = float(ux)
        click()
        nextarea()
        uoption = upgrade()
        print(uoption)
        if uoption == 'u1':
            ux = ux+1
            print(ux)
        elif uoption == 'u2':
            ux = ux + 0
            print(ux)
        if ux == 30:
            print("Yay! Level 30")
            u=False
        else:
            u=True
        time.sleep(3)
        bossoutput = boss()
        try:
            bx = bossoutput[0]
            hx = bossoutput[1]
            if bx == 'b1':
                u = False
            else:
                u = True
            if hx == 'h1':
                hp = False
            else:
                hp= True
        except:
            u = True
            hp = True
    scroll()
    while hp == True:
        for i in range (0,50):
            click()
        heropower()
        hp = False
    nextarea()
    time.sleep(3)


