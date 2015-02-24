import time
import RPi.GPIO as GPIO

GPIO.cleanup()

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7,GPIO.OUT)

GPIO.setup(12,GPIO.OUT)
#GPIO.output(12,GPIO.HIGH)

servo = GPIO.PWM(7,50)
servo.start(7.5)

try:
        while True:
                # Zero Degrees
                GPIO.output(12,GPIO.HIGH)
                servo.ChangeDutyCycle(2.5)

                GPIO.output(12,GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(12,GPIO.LOW)
                time.sleep(0.5)
                

                # 90 Degrees (Neutral)
                servo.ChangeDutyCycle(7.5)

                GPIO.output(12,GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(12,GPIO.LOW)
                time.sleep(0.5)
                

        	# 180 Degrees
                servo.ChangeDutyCycle(12.5)
                
                GPIO.output(12,GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(12,GPIO.LOW)
                time.sleep(0.5)
                

except KeyboardInterrupt:
    servo.stop()
    GPIO.cleanup()
    
