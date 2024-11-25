from hal import hal_servo as SERVO
from hal import hal_adc as ADC
import time


def main():
    SERVO.init()
    ADC.init()

    while(True):
        reading = ADC.get_adc_value(1)
        angle = (-180 * reading/ 1023) + 180
        print("Angle = ", round(angle,0))
        SERVO.set_servo_position(angle)
        time.sleep(0.5)
        #SERVO.set_servo_position(180)
        time.sleep(0.5)



# Main entry point
if __name__ == "__main__":
    main()