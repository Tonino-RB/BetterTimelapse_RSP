import RPi.GPIO as GPIO
from picamera2 import Picamera2
import time
import subprocess as sub
import sys

BUTTON_PIN = 16
GPIO.setmode(GPIO.BCM)
photoCount = 1
prevState = GPIO.HIGH
GPIO.setup(BUTTON_PIN,GPIO.IN, pull_up_down=GPIO.PUD_UP)
# Initialize camera
picam2 = Picamera2()

# Configure still capture mode
config = picam2.create_still_configuration()
picam2.configure(config)

# Start camera
picam2.start()

# Let sensor warm up
time.sleep(2)

try :
    while True :
        time.sleep(0.05)
        state = GPIO.input(BUTTON_PIN)
        if state == GPIO.LOW :
            print("low")
            if prevState != state : #S'assure que la prise de photo ne se déclanche qu'une seule fois, même si long press
                print("END SWITCH TOUCHED")
                # Capture image
                filename = "image" + str(photoCount) + ".jpg"
                picam2.capture_file(filename)
                print(filename + " taken")
                photoCount += 1
                time.sleep(0.1)
            pressTime = time.time()
            while state == GPIO.LOW :
                time.sleep(0.1)
                pressDelta = time.time()
                pressDuration = pressDelta - pressTime
                print(pressDuration)
                if pressDuration > 2 :
                    command = ["python3", "/home/tonino/Documents/timelapse.py"]
                    sub.run(command)
                    GPIO.cleanup()
                    print("GPIO CLEANED")
                    print("print over")
                    sys.exit()
                state = GPIO.input(BUTTON_PIN)
        else:
            print("NOT PRESSED")
        prevState = state #Mémorise l'état
except KeyboardInterrupt:
    GPIO.cleanup()
