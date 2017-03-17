#Last Edited by Jean Brack 2/20/17
#!/usr/bin/python
import time
# Import the Raspberry Pi GPIO libraries that
# allow us to connect the Raspberry Pi to
# other physical devices via the General
# Purpose Input-Output (GPIO) pins
import RPi.GPIO as GPIO
import os
GPIO.setwarnings(False)
# Now we need to set-up the General Purpose
# Input-Ouput (GPIO) pins
# Clear the current set-up so that we can
# start from scratch
GPIO.cleanup()
# Set up the GPIO library to use Raspberry Pi
# board pin numbers
GPIO.setmode(GPIO.BOARD)
# Set Pin 16 on the GPIO header to act as
# the output port to control forward movement on RIGHTWHEEL
LIGHT=7
OFFDELAY=.0001
ONDELAY=.01
Motor1=10
Motor2=8
GPIO.setup(LIGHT,GPIO.OUT)
GPIO.setup(Motor1,GPIO.OUT)
GPIO.setup(Motor2,GPIO.OUT)
GPIO.output(LIGHT,GPIO.LOW)
GPIO.output(Motor1,GPIO.LOW)
GPIO.output(Motor2,GPIO.LOW)
cmd = 'mpg123 /home/pi/sounds/Be*.mp3 > /dev/null 2>/dev/null &'
os.system(cmd)
try:
        OFFDELAY=.011
        ONDELAY=.01
        counter=100
        while counter > 0:
                time.sleep(OFFDELAY)
                GPIO.output(Motor1,GPIO.LOW)
                GPIO.output(Motor2,GPIO.HIGH)
                GPIO.output(LIGHT,GPIO.HIGH)
                time.sleep(ONDELAY)
                GPIO.output(Motor1,GPIO.LOW)
                GPIO.output(Motor2,GPIO.LOW)
                GPIO.output(LIGHT,GPIO.LOW)
                counter = counter - 1
	OFFDELAY=.009
	ONDELAY=.01
	counter=100
	while counter > 0:
		time.sleep(OFFDELAY)
		GPIO.output(Motor1,GPIO.LOW)
		GPIO.output(Motor2,GPIO.HIGH)
		GPIO.output(LIGHT,GPIO.HIGH)
		time.sleep(ONDELAY)
		GPIO.output(Motor1,GPIO.LOW)
		GPIO.output(Motor2,GPIO.LOW)
		GPIO.output(LIGHT,GPIO.LOW)
		counter = counter - 1
	OFFDELAY=.007
	ONDELAY=.01
	counter=500
        while counter > 0:
                time.sleep(OFFDELAY)
                GPIO.output(Motor1,GPIO.LOW)
                GPIO.output(Motor2,GPIO.HIGH)
                GPIO.output(LIGHT,GPIO.HIGH)
                time.sleep(ONDELAY)
                GPIO.output(Motor1,GPIO.LOW)
                GPIO.output(Motor2,GPIO.LOW)
                GPIO.output(LIGHT,GPIO.LOW)
                counter = counter - 1
        OFFDELAY=.009
        ONDELAY=.01
        counter=100
        while counter > 0:
                time.sleep(OFFDELAY)
                GPIO.output(Motor1,GPIO.LOW)
                GPIO.output(Motor2,GPIO.HIGH)
                GPIO.output(LIGHT,GPIO.HIGH)
                time.sleep(ONDELAY)
                GPIO.output(Motor1,GPIO.LOW)
                GPIO.output(Motor2,GPIO.LOW)
                GPIO.output(LIGHT,GPIO.LOW)
                counter = counter - 1
	OFFDELAY=.011
	ONDELAY=.01
        counter=100
        while counter > 0:
                time.sleep(OFFDELAY)
                GPIO.output(Motor1,GPIO.LOW)
                GPIO.output(Motor2,GPIO.HIGH)
                GPIO.output(LIGHT,GPIO.HIGH)
                time.sleep(ONDELAY)
                GPIO.output(Motor1,GPIO.LOW)
                GPIO.output(Motor2,GPIO.LOW)
                GPIO.output(LIGHT,GPIO.LOW)
                counter = counter - 1
except KeyboardInterrupt:
        #call("echo Hello World", shell=True)
        print "Please, oh please let me keep moving."
        GPIO.output(Motor1,GPIO.LOW)
        GPIO.output(Motor2,GPIO.LOW)
        import os
        cmd = '/home/pi/bin/lo'
        os.system(cmd)
