from picographics import PicoGraphics,DISPLAY_INKY_PACK
from machine import Pin

frontLED=22
buttonA=12
buttonB=13
buttonC=14
buttonUp=15
buttonDown=11

display = PicoGraphics(display=DISPLAY_INKY_PACK)
ScreenWidth, ScreenHeight = display.get_bounds()

def clear():
    display.set_pen(15)
    display.rectangle(0,0,ScreenWidth,ScreenHeight)
    #display.clear()
    display.update()