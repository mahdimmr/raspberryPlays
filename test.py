import RPi.GPIO as GPIO  # import RPi.GPIO module
from time import sleep  # lets us have a delay
import argparse

GPIO.setmode(GPIO.BCM)  # choose BCM or BOARD
GPIO.setwarnings(False)
# parser = argparse.ArgumentParser(description = 'Add a little color to your life.')
# parser.add_argument('color', metavar='color', type=str, nargs=1,
#                    help='A color value of red, green, blue, or off.')
# args = parser.parse_args()
# GPIO.setup(int(args.color[0]), GPIO.OUT, initial=0)  # set GPIO24 as an output
# GPIO.output(int(args.color[0]), 1)
# sleep(1)
#
# GPIO.cleanup()

try:
    # leds = [2, 3, 4, 17, 27, 22, 10, 9, 11, 5, 6, 13, 19, 26, 14, 15, 18, 23, 24, 25, 8, 7, 12, 16, 20, 21]
    leds = [27, 17, 18, 22, 23, 24]
    leds2 = [22, 23, 24]
    leds3 = [27, 17, 18]
    for i in leds:
        GPIO.setup(i, GPIO.OUT, initial=0)

    while True: # set GPIO24 as an output
        for a in range(10):
            for j in leds2:
                GPIO.output(j, 1)  # set GPIO24 to 1/GPIO.HIGH/True
                sleep(float(f"0.0{a}"))
                GPIO.output(j, 0)  # set GPIO24 to 0/GPIO.LOW/Fals
            sleep(.05)
            for b in range(a):
                for k in leds3:
                    GPIO.output(k, 1)
                    sleep(float(f"0.0{a}"))
                    GPIO.output(k, 0)

        #for l in leds:
         #   GPIO.output(l, 1)
          #  sleep(.005)
           # GPIO.output(l, 0)


#leds.reverse()
        #for k in leds:
         #   GPIO.output(k, 0)  # set GPIO24 to 0/GPIO.LOW/False
         #   sleep(.5)
         #   GPIO.output(k, 1)  # set GPIO24 to 1/GPIO.HIGH/True

except KeyboardInterrupt:  # trap a CTRL+C keyboard interrupt
    GPIO.cleanup()

