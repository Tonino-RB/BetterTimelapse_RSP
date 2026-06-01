import time 
from picamera2 import Picamera2
import piCamSettings as settings
import captureTimelapse as capture
import timelapse
#Start PiCamera with settings
picam2 = Picamera2()
config = settings.configuration(picam2) #Change setting in settings script
picam2.configure(config)
# Start camera
picam2.start()

# Let sensor warm up
time.sleep(2)



try:
    while True:
        dir="/home/tonino/Documents/timelapse"
        capture.takeTimelapse(picam2, dir)
        timelapse.create_timelapse(dir, dir, 30)
        time.sleep(5)
        # do work
        #1 - set up camera
        #2 - capture image
        #3 - Stop recording
        #4 - Process image
        #5 - Save Timelapse
        #6 - Send a notification

except KeyboardInterrupt :
    print("Stopped by user")