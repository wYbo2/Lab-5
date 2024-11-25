import time
from hal import hal_lcd as LCD


def main():
    #initialise LCD
    lcd = LCD.lcd()
    lcd.lcd_clear()

    while(True):
        local_time = time.localtime() # get struct_time 
        time_string = time.strftime("%H:%M:%S", local_time)
        date_string = time.strftime("%d-%m-%Y", local_time)
        print(time_string)
        print(date_string)
        lcd.lcd_display_string(time_string, 1)
        lcd.lcd_display_string(date_string, 2)
        time.sleep(1)


# Main entry point
if __name__ == "__main__":
    main()
