from machine import I2C, Pin
from time import sleep
from random import randint
from pico_i2c_lcd import I2cLcd
from LOGIC import choice, choose, reboot, previous
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)

I2C_ADDR = i2c.scan()[0]

lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)
led = Pin(25, Pin.OUT)

select = Pin(18, Pin.IN, Pin.PULL_DOWN)
enter = Pin(17, Pin.IN, Pin.PULL_DOWN)
back = Pin(16, Pin.IN, Pin.PULL_DOWN)

sleep(2)
lcd.putstr("   Welcome to\n    Pico-OS!")
sleep(5)
lcd.clear()
lcd.putstr("   Created By\n     FJay01")
sleep(3)
lcd.clear()


x = -1
lcd.putstr("Press Button To      Start!")
while True:  
    if select.value():
        led.toggle()
        sleep(0.75)
        led.toggle()
        x += 1
        print (x)
        choice(x,lcd)
        sleep(0.2)
        choice(x,lcd)
    elif x == 5:
        x = 0
        choice(x, lcd)
        
    if enter.value():
        led.toggle()
        sleep(1)
        led.toggle()
        x += 10
        print (x)
        choose(x, lcd)
        
    if back.value():
        led.toggle()
        sleep(0.75)
        led.toggle()
        if x > 9:
            x -= 10
            lcd.clear()
            sleep(0.2)
            i = randint(1,4)
            Time = 0
            while Time <= i:
                lcd.clear()
                lcd.putstr(" Going Back.")
                sleep(0.3)
                lcd.clear()
                lcd.putstr(" Going Back..")
                sleep(0.3)
                lcd.clear()
                lcd.putstr(" Going Back...")
                sleep(0.3)
                lcd.clear()
                lcd.putstr(" Going Back....")
                sleep(0.3)
                Time += 1 
            choice(x,lcd)
        elif x < 10:
            reboot(lcd)