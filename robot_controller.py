import RPi.GPIO as GPIO
import time

class Robot:
    def __init__(self):
        # Initialize the GPIO pins for motor control
        # Replace PIN_A and PIN_B with the actual GPIO pin numbers on your Raspberry Pi
        self.PIN_A = 0
        self.PIN_B = 1
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.PIN_A, GPIO.OUT)
        GPIO.setup(self.PIN_B, GPIO.OUT)

    def move_forward(self):
        GPIO.output(self.PIN_A, GPIO.HIGH)
        GPIO.output(self.PIN_B, GPIO.LOW)

    def move_backward(self):
        GPIO.output(self.PIN_A, GPIO.LOW)
        GPIO.output(self.PIN_B, GPIO.HIGH)

    def stop(self):
        GPIO.output(self.PIN_A, GPIO.LOW)
        GPIO.output(self.PIN_B, GPIO.LOW)

    def cleanup(self):
        GPIO.cleanup()
