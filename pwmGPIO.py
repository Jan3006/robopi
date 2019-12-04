import time
#import RPi.GPIO as GPIO
import pigpio
import os

#PIN VARIABLEN
STEP0 = 12
STEP1 = 13
f = "1"
d = "500000"
print("Starte pigpio...\n")
pi = pigpio.pi()

pi.set_mode(STEP0, pigpio.OUTPUT)
pi.set_mode(STEP1, pigpio.OUTPUT)

print("Starte PWM GPIOPIN 12/13\n")

pi.hardware_PWM(STEP0, 2, 500000)
pi.hardware_PWM(STEP1, int(f), int(d))

try:
	while  int(f)>=0:
		print("f: " + str(f) + " d: " + str(d))
		f = input("\n[GPIO Pin 13(f)]: ")
		#d = input("\n[GPIO Pin 13(d)]: ")
		if int(f)>=0 and int(d) >= 0:
			pi.hardware_PWM(STEP1, int(f), int("500000"))
except KeyboardInterrupt:
	print("\nStop pigpio")
finally:
	print("Stop PWM GPIOPIN 12/13\n")
	pi.hardware_PWM(STEP0, 5, 0)
	pi.hardware_PWM(STEP1, 5, 0)
	print("Stop pigpio\nStop")
	pi.stop()