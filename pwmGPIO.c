#include <stdio.h>
#include <pigpio.h>

int main()
{
	int INPUT = 0;
	int OUTPUT = 1;
	
	int STEP0 = 12;
	int STEP1 = 13;
	
	int f = 1;
	int d = 500000;

	printf("Starte pigpio...\n");
	if(gpioInitialise() < 0) return -1;

	gpioSetMode(STEP0, OUTPUT);
	gpioSetMode(STEP1, OUTPUT);
	gpioSetMode(23, OUTPUT);

	printf("Starte PWM GPIOPIN 12/13\n");
	gpioHardwarePWM(STEP0, 2, 500000);
	gpioHardwarePWM(STEP1, f, 500000);
	gpioWrite(23, 1);
	while(f>=0){
		printf("f: %d ", f);
		printf("d: %d", d);
		printf("\n[GPIO Pin 13(f)]: ");
		scanf("%d", &f);
		if(f>=0&&d>=0) gpioHardwarePWM(STEP1, f, 500000);
	}

	printf("Stop PWM GPIOPIN 12/13\n");
	gpioHardwarePWM(STEP0, 0, 0);
	gpioHardwarePWM(STEP1, 0, 0);
	gpioWrite(23, 0);

	printf("Stop pigpio\n");
	gpioTerminate();

	return 0;
}
