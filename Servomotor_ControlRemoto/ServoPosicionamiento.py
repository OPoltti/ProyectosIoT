from gpiozero import Servo
import math
from time import sleep 
from firebase import firebase
firebase = firebase.FirebaseApplication('https://seguidorsolarporiot-feria-default-rtdb.firebaseio.com', None)
import RPi.GPIO as GPIO

from gpiozero.pins.pigpio import PiGPIOFactory

factory=PiGPIOFactory()
servo = Servo(18, min_pulse_width=0.5/1000, max_pulse_width=5.0/1000, pin_factory=factory)
servoh = Servo(4, min_pulse_width=0.5/1000, max_pulse_width=5.0/1000, pin_factory=factory)

try:    
    while True:
            fun = firebase.get('/Funcionamiento/Modo/','')
            if(fun=='MANUAL'):
                ang_vertical = firebase.get('/Movimiento/ang_vertical/','') 
                a=ang_vertical*4/9+180
                servo.value=math.sin(math.radians(a))
            
                ang_horizontal = firebase.get('/Movimiento/ang_horizontal/','') 
                b=ang_horizontal*4/9+180
                servoh.value=math.sin(math.radians(b))
            
            if(fun=='AUTOMATICO'):
                ldr1= firebase.get('/LDRS/1','')
                ldr2= firebase.get('/LDRS/2','')
                ldr3= firebase.get('/LDRS/3','')
                ldr4= firebase.get('/LDRS/4','')
                
                servohLimitHigh=170
                servohLimitLow=10
                
                servovLimitHigh=170
                servovLimitLow=10
                
                w=10
                
                PT=(ldr1+ldr3)/2                
                PB=(ldr2+ldr4)/2
                PI=(ldr1+ldr2)/2
                PD=(ldr3+ldr4)/2
                DH=(PT-PB)
                DV=(PI-PD)
                
                if(abs(DV)<=w):
                    servoh=None
                    if(DV>10):
                        servoh.value=math.sin(math.radians(servo.value-2))
                    if(servo.value>servovLimitHigh):
                        servo.value=servovLimitHigh
                        delay(10)
                    else(servoh.value=math.sin(math.radians(servo.value+2))):
                    if(servo<servovLimitLow):
                        servo.value=servoLimitLow
                        delay(10)
                        
except KeyboardInterrupt:
    pulso.stop()
    GPIO.cleanup()      