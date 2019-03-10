from picamera import PiCamera
from gpiozero import Button
from time import sleep
import os
import sys
#import flickr_api
#if FLICKR:
    #import flickr


camera = PiCamera()
btn = Button(23, hold_time=2)
btn2 = Button(24, hold_time=2)

camera.start_preview()
i = 0
v = 0

while True:
    images = []
    if btn.is_pressed:
        i += 1
        camera.capture('/home/pi/Desktop/Projects/ThotShot/images/image%s.png' % i)
        print("image",i)

    if btn.is_held:
        v += 1
        camera.start_recording('/home/pi/Desktop/Projects/ThotShot/images/vido%s.h264' % v)
        print("video start")
        sleep(15)
        camera.stop_recording()
        print("video stop",v)
        
        
        

    if btn2.is_pressed:
        camera.stop_preview()
        
    #for image_name in images:
        #if FLICKR:
            #os.remove(image_name)

    
        
