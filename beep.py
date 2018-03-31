import RPi.GPIO as GPIO
import time

BuzzerPin = 11


def setup():
    GPIO.setmode(GPIO.BOARD)  # Numbers GPIOs by physical location
    GPIO.setup(BuzzerPin, GPIO.OUT)  # Set pins' mode is output
    GPIO.output(BuzzerPin, GPIO.HIGH)
    print("beep starting")


def on():
    GPIO.output(BuzzerPin, GPIO.LOW)


def off():
    GPIO.output(BuzzerPin, GPIO.HIGH)


def beep(x):
    on()
    time.sleep(x)
    off()
    time.sleep(x)


def loop():
    while True:
        beep(0.5)


def destroy():
    GPIO.output(BuzzerPin, GPIO.HIGH)  # Set BuzzerPin pin to High
    GPIO.cleanup()  # Release resource


if __name__ == '__main__':  # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be executed.
        destroy()
