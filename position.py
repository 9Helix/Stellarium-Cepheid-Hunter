import pyautogui as pag
from time import sleep
import keyboard
from turtle import *

fps=60
stop=0
Screen().setup(250, 80)
colormode(255)
bgcolor(5,5,5)
title('Cursor Position')
color(255,255,255)
ht()
speed(0)
while not stop:
    pu()
    goto(0,-10)
    pd()
    clear()
    x=str(pag.position())
    x=x.replace('Point','')
    write(x,move=False,align='center',font=('Calibri',20,'normal'))   
    pu()
    goto(0,-10)
    pd()
    if keyboard.is_pressed('p'):
        print(x)
    if keyboard.is_pressed('q'):
        stop=1
    #sleep(1/fps)

