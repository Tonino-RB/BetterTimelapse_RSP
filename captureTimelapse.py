import RPi.GPIO as GPIO
import time
import subprocess as sub



def takeTimelapse(picam2, directory):
    #Initiate button
    BUTTON_PIN = 16
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_PIN,GPIO.IN, pull_up_down=GPIO.PUD_UP)

    sub.run(["mkdir", "-p", directory]) #Create directory if it doesn't exist
    prevState = GPIO.HIGH
    finnished = False
    photoCount = 1
    while finnished !=True :
        time.sleep(0.05)
        state = GPIO.input(BUTTON_PIN)
        if state == GPIO.LOW :
            print("low")
            if prevState != state : #S'assure que la prise de photo ne se déclanche qu'une seule fois, même si long press
                print("END SWITCH TOUCHED")
                # Capture image
                filename = directory + "/image" + str(photoCount) + ".jpg"
                picam2.capture_file(filename)
                print(filename + " taken")
                photoCount += 1
                time.sleep(0.1)
            pressTime = time.time()
            while state == GPIO.LOW and finnished != True :
                time.sleep(0.1)
                pressDelta = time.time()
                pressDuration = pressDelta - pressTime
                print(pressDuration)
                if pressDuration > 2 :
                    finnished = True
  
                if finnished == True :
                    GPIO.cleanup()
                    print("GPIO CLEANED")
                    print("print over")
                else :
                    state = GPIO.input(BUTTON_PIN)
        else:
            print("NOT PRESSED")
        prevState = state #Mémorise l'état
