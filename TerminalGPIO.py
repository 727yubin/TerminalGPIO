import sys
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

pin_no = int(sys.argv[1])
dur = int(sys.argv[2])

GPIO.setup(pin_no, GPIO.OUT)

GPIO.output(pin_no, GPIO.LOW)

GPIO.output(pin_no, GPIO.HIGH)
time.sleep(dur)
GPIO.output(pin_no, GPIO.LOW)

GPIO.cleanup()