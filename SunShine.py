import GPIOdetail
import SunShineClient as SC
import RPi.GPIO as GPIO
from time import sleep

def control_steer(outchannel, inchannel):
	# 设置简易操作舵机的函数
	GPIOdet = GPIOdetail.GPIOs()
	if GPIOdet.search(value=outchannel).Mode == 'IN':
	    GPIO.setup(outchannel, GPIO.OUT, initial=0)
	
	pwm = GPIO.PWM(outchannel, 50)
	GPIO.add_event_detect(inchannel, GPIO.FALLING)
	pwm.start(0)
	for i in range(0, 181, 1):
            pwm.ChangeDutyCycle(2.5+10*i/180)
            sleep(0.01)
            if GPIO.event_detected(inchannel):
                print("I am event_detecter:", GPIO.event_detected(inchannel))
                sleep(0.05)
                break
			
	pwm.stop()
	GPIO.cleanup(outchannel)
	
def control_led(outchannel, inchannel):
	# 设置点亮LED灯的函数
	GPIOdet = GPIOdetail.GPIOs()
	if GPIOdet.search(value=outchannel).Mode == 'IN':
	    GPIO.setup(outchannel, GPIO.OUT, initial=0)
	
	GPIO.output(outchannel, 1)
	sleep(1)
	GPIO.output(outchannel, 0)
	
	GPIO.cleanup(outchannel)
	

# 设置用到的引脚号
ledchannel = 16
ltchannel = 20
stchannel = 21

# 设置引脚模式、引脚输入输出状态
GPIO.setmode(GPIO.BCM)
GPIO.setup([ledchannel, stchannel], GPIO.OUT, initial=0)
GPIO.setup(ltchannel, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
	try:
		if GPIO.input(ltchannel):
			sleep(0.1)
			print("Light Sensor IS ", GPIO.input(ltchannel))
			LS_state = "HIGH" if GPIO.input(ltchannel) else "LOW"
			SC.publish("I am Light_Sensor , and I am "+LS_state)
			control_steer(stchannel, ltchannel)
		else:
			sleep(1)
			print("Light Sensor Is Low*_*", GPIO.input(ltchannel))
			LS_state = "HIGH" if GPIO.input(ltchannel) else "LOW"
			SC.publish("I am Light_Sensor , and I am "+LS_state)
			control_led(ledchannel, ltchannel)
	except KeyboardInterrupt:
		break

GPIO.cleanup()
		