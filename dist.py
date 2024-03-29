# Libraries
import RPi.GPIO as GPIO
import time
from time import sleep

# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

# set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24

red = 16
green = 21
blue = 20

# set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

red_p = GPIO.PWM(red, 50)
red_p.start(0)

blue_p = GPIO.PWM(blue, 50)
blue_p.start(0)

green_p = GPIO.PWM(green, 50)
green_p.start(0)


def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
    return distance


if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print("Measured Distance = %.1f cm" % dist)
            while dist > 9.0:
                GPIO.output(blue, 0)
                GPIO.output(red, 0)
                for dc in range(0, 101, 5):
                    green_p.ChangeDutyCycle(dc)
                    time.sleep(0.01)
                for dc in range(100, -1, -5):
                    green_p.ChangeDutyCycle(dc)
                    time.sleep(0.01)
                dist = distance()
            while 5.0 < dist < 9.0:
                print("abi")
                GPIO.output(red, 0)
                for dc in range(0, 101, 5):
                    green_p.ChangeDutyCycle(dc)
                    blue_p.ChangeDutyCycle(dc)
                    time.sleep(0.01)
                for dc in range(100, -1, -5):
                    green_p.ChangeDutyCycle(dc)
                    blue_p.ChangeDutyCycle(dc)
                    time.sleep(0.01)
                dist = distance()
            while dist < 4.9:
                GPIO.output(blue, 0)
                GPIO.output(green, 0)
                for dc in range(0, 101, 5):
                    red_p.ChangeDutyCycle(dc)
                    time.sleep(0.01)
                for dc in range(100, -1, -5):
                    red_p.ChangeDutyCycle(dc)
                    time.sleep(0.01)
                dist = distance()
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
