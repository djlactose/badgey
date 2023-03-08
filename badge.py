import utils
import jpegdec

display = utils.display
  
def loadBadge():
    f=open("badge.txt", "r")
    imageX=utils.ScreenWidth-135
    imageY=utils.ScreenHeight-135
    utils.clear()
    display.set_pen(4)
    display.rectangle(0,0,utils.ScreenWidth,28)
    display.set_pen(15)
    display.set_font("bitmap14_outline")
    display.text(f.readline(), int((utils.ScreenWidth-imageX)/2)-20, 0, imageX)
    display.set_pen(0)
    display.set_font("bitmap8")
    display.text(f.readline(), 10, 30, imageX,3)
    display.set_pen(13)
    display.rectangle(0,utils.ScreenHeight-45,utils.ScreenWidth,45)
    display.set_pen(0)
    display.set_font("bitmap6")
    display.text(f.readline(), 10, utils.ScreenHeight-40, imageX)
    display.text(f.readline(), int((utils.ScreenWidth-imageX)/2)-20, utils.ScreenHeight-20, imageX)
    j = jpegdec.JPEG(display)
    if j.open_file("/img/ContactCard.jpg"):
        j.decode(imageX, imageY, jpegdec.JPEG_SCALE_FULL)
    display.update()
    
def loadMobile():
    utils.clear()
    j = jpegdec.JPEG(display)
    if j.open_file("/img/ios.jpg"):
        j.decode(int(((utils.ScreenWidth-116)/2)-83), int(((utils.ScreenHeight/2)-55)/2), jpegdec.JPEG_SCALE_FULL)
    if j.open_file("/img/google.jpg"):
        j.decode(int(((utils.ScreenWidth-116)/2)-83), int(utils.ScreenHeight-(((utils.ScreenHeight/2)+51)/2)), jpegdec.JPEG_SCALE_FULL)
    if j.open_file("/img/MobileQR.jpg"):
        j.decode(utils.ScreenWidth-116, int((utils.ScreenHeight-116)/2), jpegdec.JPEG_SCALE_FULL)
    display.update()
    
def loadSignup():
    utils.clear()
    display.set_pen(0)
    display.set_font("bitmap8")
    display.text("Scan this QR Code for a no obligation risk free 14 Day Free Trial", 87+20, 30,utils.ScreenWidth-87-20)
    j = jpegdec.JPEG(display)
    if j.open_file("/img/signup.jpg"):
        j.decode(10, int((utils.ScreenHeight-87)/2), jpegdec.JPEG_SCALE_FULL)
    display.update()

def loadIntro():
    utils.clear()
    display=utils.display
    j = jpegdec.JPEG(display)
    if j.open_file("/img/badgey.jpg"):
        j.decode(utils.ScreenWidth-110, 0, jpegdec.JPEG_SCALE_FULL)
    display.set_pen(0)
    display.text("Welcome to Badgey!",10,10,utils.ScreenWidth-110)
    display.text("Created by Nick Hernandez",10,utils.ScreenHeight-30,utils.ScreenWidth-110)
    display.update()
    

def main():
    loadBadge()
    
if __name__ == '__main__':
    main()
