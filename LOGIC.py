from random import randint
import machine
from time import sleep
def choice(x,lcd):   
    if x == 0:
          lcd.clear()
          lcd.putstr("TXT File {}".format(x+1))
          sleep(2)
    elif x == 1:
          lcd.clear()
          lcd.putstr("TXT File {}".format(x+1))
          sleep(2)
    elif x == 2:
          lcd.clear()
          lcd.putstr("TXT File {}".format(x+1))
          sleep(2)        
    elif x == 3:
          lcd.clear()
          lcd.putstr("TXT File {}".format(x+1))
          sleep(2)
    elif x == 4:
          lcd.clear()
          lcd.putstr("TXT File {}".format(x+1))
          sleep(2)     

def choose(x, lcd):
    
    if x == 10:
        lcd.clear()
        lcd.putstr("Opening:        TXT File 1")
        sleep(randint(1,4))
        lcd.clear()
        f = open ('/TXT_File1.txt','r')
        t = f.read()
        f.close()
        lcd.putstr(t)
    
    elif x == 11:
        lcd.clear()
        lcd.putstr("Opening:        TXT File 2")
        sleep(randint(1,4))
        lcd.clear()
        f = open ('/TXT_File2.txt','r')
        t = f.read()
        f.close()
        lcd.putstr(t)
    
    elif x == 12:
        lcd.clear()
        lcd.putstr("Opening:        TXT File 3")
        sleep(randint(1,4))
        lcd.clear()
        f = open ('/TXT_File3.txt','r')
        t = f.read()
        f.close()
        lcd.putstr(t)
    
    elif x == 13:
        lcd.clear()
        lcd.putstr("Opening:        TXT File 4")
        sleep(randint(1,4))
        lcd.clear()
        f = open ('/TXT_File4.txt','r')
        t = f.read()
        f.close()
        lcd.putstr(t)
    
    elif x == 14:
        lcd.clear()
        lcd.putstr("Opening:        TXT File 5")
        sleep(randint(1,4))
        lcd.clear()
        f = open ('/TXT_File5.txt','r')
        t = f.read()
        f.close()
        lcd.putstr(t)
        
def previous (x,lcd):
    lcd.clear()
    x -= 10
    sleep(0.75)
    
def reboot(lcd):
    lcd.clear()
    i = randint(1,4)
    Time = 0
    while Time <= i:
        lcd.clear()
        lcd.putstr("  Restarting.")
        sleep(0.3)
        lcd.clear()
        lcd.putstr("  Restarting..")
        sleep(0.3)
        lcd.clear()
        lcd.putstr("  Restarting...")
        sleep(0.3)
        Time += 1 
    machine.reset()