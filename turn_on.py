import argparse
import RPi.GPIO as GPIO

# Get RGB colors from command line arguments.
parser = argparse.ArgumentParser(description = 'Add a little color to your life.')
parser.add_argument('color', metavar='color', type=str, nargs=1,
                   help='A color value of red, green, blue, or off.')
args = parser.parse_args()

# LED pin mapping.
red = 11
green = 13
blue = 12

# GPIO Setup.
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

# Clear all existing color values.
GPIO.output(red, 0)
GPIO.output(green, 0)
GPIO.output(blue, 0)

# Set individual colors.
if args.color[0] == 'red':
    print(red, "red")
    GPIO.output(red, 1)
elif args.color[0] == 'green':
    GPIO.output(green, 1)
    print("green on")
elif args.color[0] == 'blue':
    print(blue, "blue")
    GPIO.output(blue, 1)
