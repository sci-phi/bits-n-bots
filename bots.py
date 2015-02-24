import time
import RPi.GPIO as GPIO

GPIO.cleanup()

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7,GPIO.OUT)

servo = GPIO.PWM(7,50)
servo.start(7.5)

try:
        while True:
                # Zero Degrees
                servo.ChangeDutyCycle(7.5)
                time.sleep(1)

                # 90 Degrees (Neutral)
                servo.ChangeDutyCycle(12.5)
                time.sleep(1)

        	# 180 Degrees
                servo.ChangeDutyCycle(2.5)
                time.sleep(1)

except KeyboardInterrupt:
    servo.stop()
    GPIO.cleanup()
    
