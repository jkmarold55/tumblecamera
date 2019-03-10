def restart():
    timestamp=datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    camera.capture(timestamp+".jpg")
    photofile = "/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload /home/pi/Desktop/Projects/ThotShot/"+timestamp+".jpg "+timestamp+".jpg "
    call([photofile], shell=True)


from picamera import PiCamera
from gpiozero import Button
from subprocess import call
from time import sleep

#import flickr_api
#if FLICKR:
    #import flickr
import datetime



camera = PiCamera()
btn = Button(23, hold_time=2)
btn2 = Button(24, hold_time=2)

camera.start_preview()
camera.rotation = 180
i = 0
v = 0

while True:
    images = []
    
    if btn.is_pressed:
        restart()
        #i += 1
        #camera.capture('/home/pi/Desktop/Projects/ThotShot/images/image%s.png' % i)
        #print("image",i)
            
            

        #camera.capture(timestamp+" .jpg")
        #photofile = "/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload /home/pi/Desktop/Projects/ThotShot/"+timestamp+".jpg "+timestamp+".jpg "
        #call([photofile], shell=True)
            
    if btn.is_held:
        v += 1
        camera.start_recording('/home/pi/Desktop/Projects/ThotShot/images/vido%s.h264' % v)
        print("video start")
        sleep(15)
        camera.stop_recording()
        print("video stop",v)
        
        
        

    if btn2.is_pressed:
        camera.stop_preview()
        


    
