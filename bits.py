import time
import RPi.GPIO as GPIO

GPIO.cleanup()

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7,GPIO.OUT)

try:
        while True:
                # "On"
                GPIO.output(7,GPIO.HIGH)
                time.sleep(1)

        	# "Off"
                GPIO.output(7,GPIO.LOW)
                time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
    
