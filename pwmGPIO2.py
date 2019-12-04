import pigpio

#PIN VARIABLEN
STEP0 = 12
f = 1
d = 500000


def init():
	print("Starte pigpio...\n")
	pi = pigpio.pi()
	pi.set_mode(STEP0, pigpio.OUTPUT)
	pi.set_mode(STEP1, pigpio.OUTPUT)
	return pi

def set(pi,pf):
	pi.hardware_PWM(STEP1, pf, d)

def stop(pi):
	pi.hardware_PWM(STEP0, 5, 0)
	print("Stop pigpio\nStop")
	pi.stop()