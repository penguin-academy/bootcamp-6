print("Hello World")
 
import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setwarnings(False) # Ignorar las advertencias
GPIO.setmode(GPIO.BOARD)    # Usar la numeración física
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Iniciar el pin 8
 
while True:
    GPIO.output(8, GPIO.HIGH)    # Se enciende la LED
    sleep(1)  # Se queda encendido 1 segundo
    GPIO.output(8, GPIO.LOW)     # Se apaga la LED
    sleep(1)  # Se queda apagado 1 segundo