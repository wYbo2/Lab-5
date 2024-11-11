import RPi.GPIO as GPIO #import RPi.GPIO module
import time
from time import sleep


from hal import hal_led as led
from hal import hal_lcd as LCD
from hal import hal_dc_motor as dc_motor
from hal import hal_buzzer as buzzer
from hal import hal_servo as servo
import version as ver


def init():
    GPIO.setmode(GPIO.BCM) #choose BCM mode
    GPIO.setwarnings(False)
    GPIO.setup(22,GPIO.IN) #set GPIO 22 as input
    #GPIO.setmode(GPIO.BCM)  # choose BCM mode
    #GPIO.setwarnings(False)
    GPIO.setup(24, GPIO.OUT) 
     # set GPIO 24 as output

def read_slide_switch():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(22,GPIO.IN) 
    ret = 0
    
    if GPIO.input(22):
        ret = 1
    return ret

def blink_led(delay):
    # Led Blink
    led.init()

    led.set_output(0, 1)
    time.sleep(delay)

    led.set_output(0, 0)
    time.sleep(delay)

    led.set_output(0, 1)
    time.sleep(delay)

    led.set_output(0, 0)
    time.sleep(delay)


def main():
    #blink_led(1)
    y = 1
    while True:
        x = read_slide_switch()
        print(x)
        if x==1:
            blink_led(0.2)
            y = 1
        elif x ==0 and y%2 == 1:
            start_time=time.time()
            while (time.time()-start_time)<5:
                blink_led(0.1)
                y = 2
            
            
        
    
## Main entry point
if __name__ == "__main__":
    main()