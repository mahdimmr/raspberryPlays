import RPi.GPIO as GPIO
import time

red = 16
green = 21
blue = 20

GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

red_p = GPIO.PWM(red, 50)
red_p.start(0)

blue_p = GPIO.PWM(blue, 50)
blue_p.start(0)

green_p = GPIO.PWM(green, 50)
green_p.start(0)


try:
    for x in range(50):
        green_p.ChangeDutyCycle(x)
        red_p.ChangeDutyCycle(50)
        time.sleep(0.1)

    for x in range(50):
        red_p.ChangeDutyCycle(50 - x)
        green_p.ChangeDutyCycle(50 - x)
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()