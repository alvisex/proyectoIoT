import RPi.GPIO as GPIO
import SimpleMFRC522
import time
import wiringpi

io     = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_PINS)
reader = SimpleMFRC522.SimpleMFRC522()
blanco =''
txtt = '123'
io.pinMode(7,io.OUTPUT)
try:
  print("Por Favor Deslisa la Tarjeta")
  id,text = reader.read()
  io.digitalWrite(7,io.HIGH)
  time.sleep(0.5)
  if(text == txtt):
    print('joder')
  elif(text == 123):
    print('es numero')
    #print(text)
    print("\n \n")
    print("-----------------------")
    print(" B I E N V E N I D O ")
    print("----------------------")
    print("\n \n")
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17,GPIO.OUT,initial=GPIO.LOW)
    GPIO.output(17, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(17, GPIO.LOW)
  else:
    print('No esta comparando')
    print(text)
    print(txtt)

finally:
  GPIO.cleanup()