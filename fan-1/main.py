#
# rshell --buffer-size=100 -p /dev/ttyACM0 -a
#

from machine import Pin, PWM
import time

chip_pins = [4, 5, 6, 7]
pwms = []

D=25

def setupPin(p):
	pin = Pin(p, mode=Pin.OUT, pull=Pin.PULL_UP)
	pwm = PWM(pin)
	pwm.freq(25000)
	return pwm

def setFanDuty(pwm, duty):
	if duty<0:
		duty=0
	if duty>100:
		duty = 100
	d = int(duty/100*65535)
	pwm.duty_u16(d)

for X in chip_pins:
	pwms.append(setupPin(X))

for pwm in pwms:
	setFanDuty(pwm, D)

while True:
	time.sleep(1)
