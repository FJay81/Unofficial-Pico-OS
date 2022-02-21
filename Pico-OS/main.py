from machine import I2C, Pin
from time import sleep
from pico_i2c_lcd import I2cLcd
from LOGIC import choice

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)

I2C_ADDR = i2c.scan()[0]

lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)
led = Pin(25, Pin.OUT)
select = Pin(14, Pin.IN, Pin.PULL_DOWN)
x = -1
lcd.putstr("Press Button To      Start")
while True:  
    if select.value():
        led.toggle()
        sleep(0.75)
        led.toggle()
        x += 1
        print (x)
        choice(x,lcd)
    
    
    elif x > 5:
        x = 0
        print(x)
        choice(x,lcd)