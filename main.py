import utils
import badge
import time
from machine import Pin  

led=Pin(utils.frontLED, Pin.OUT)
led.off()

def buttonA_pressed(change):
    led.toggle()
    time.sleep(0.1)
    led.toggle()
    badge.loadBadge()

def buttonB_pressed(change):
    led.toggle()
    time.sleep(0.1)
    led.toggle()
    badge.loadSignup()

def buttonC_pressed(change):
    led.toggle()
    time.sleep(0.1)
    led.toggle()
    badge.loadMobile()

def buttonUp_pressed(change):
    led.toggle()
    time.sleep(0.1)
    led.toggle()
    utils.clear()

def buttonDown_pressed(change):
    led.toggle()
    time.sleep(0.1)
    led.toggle()
    loadIntro()

def NotWritten():
    display=utils.display
    utils.clear()
    display.set_pen(0)
    display.text("Button not Impletmented Yet", 10, 10)
    display.update()

buttonA=Pin(utils.buttonA,Pin.IN,Pin.PULL_DOWN)
buttonA.irq(handler=buttonA_pressed, trigger=Pin.IRQ_FALLING)
buttonB=Pin(utils.buttonB,Pin.IN,Pin.PULL_DOWN)
buttonB.irq(handler=buttonB_pressed, trigger=Pin.IRQ_FALLING)
buttonC=Pin(utils.buttonC,Pin.IN,Pin.PULL_DOWN)
buttonC.irq(handler=buttonC_pressed, trigger=Pin.IRQ_FALLING)
buttonUp=Pin(utils.buttonUp,Pin.IN,Pin.PULL_DOWN)
buttonUp.irq(handler=buttonUp_pressed, trigger=Pin.IRQ_FALLING)
buttonDown=Pin(utils.buttonDown,Pin.IN,Pin.PULL_DOWN)
buttonDown.irq(handler=buttonDown_pressed, trigger=Pin.IRQ_FALLING)

def main():
    badge.loadIntro()
    
if __name__ == '__main__':
    main()
