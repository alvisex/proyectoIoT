import RPi.GPIO as GPIO
import SimpleMFRC522
import time
import wiringpi

io     = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_PINS)
reader = SimpleMFRC522.SimpleMFRC522()
blanco =''
io.pinMode(7,io.OUTPUT)
try:
  print("Por Favor Deslisa la Tarjeta")
  id,text = reader.read()
  io.digitalWrite(7,io.HIGH)
  time.sleep(0.5)
  if(text == blanco):
    print ("Esta Tarjeta Esta Vacia")
    io.digitalWrite(7,io.LOW)
  else:
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

finally:
  GPIO.cleanup()
