import keyboard
import time
import mouse
x ='x'

time.sleep(2)

def moveClick(x,y):
    mouse.move(x,y)
    time.sleep(1)
    mouse.click()
    time.sleep(4)
while x == 'x':
    for i in range(5):
        moveClick(885+125*i,645)
        keyboard.write("8")
        time.sleep(2)
    time.sleep(5)
    moveClick(1740,1010)
    mouse.click()
    time.sleep(8)
    moveClick(1190,390)
    time.sleep(5)
    keyboard.press_and_release('f5')
    time.sleep(5)
    x = input('forsett skriv (x): ')




