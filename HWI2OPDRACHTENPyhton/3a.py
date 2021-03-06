
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

#import GPIO as GPIO

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
GPIO.setup(14, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)


while True: # Run forever
 GPIO.output(8, GPIO.HIGH) # Turn on
 GPIO.output(14, GPIO.HIGH) # Turn on
 sleep(1) # Sleep for 1 second
 sleep(1) # Sleep for 1 second

 GPIO.output(8, GPIO.LOW) # Turn off
 GPIO.output(14, GPIO.LOW) # Turn off
 sleep(1) # Sleep for 1 second
 sleep(1) # Sleep for 1 second

