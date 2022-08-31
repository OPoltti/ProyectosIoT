import RPi.GPIO as GPIO
import time
import threading
import sys #Libreria que permite finalizar programa con sys.exit()
from time import sleep
from firebase import firebase

firebase=firebase.FirebaseApplication('https://iot-bombadejeringa-default-rtdb.firebaseio.com',None)
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

pin_A1 = 29 # pinA1
pin_A2 = 31 
pin_ENA = 33 #PWM
pin_B1 = 36
pin_B2 = 38
pin_ENB = 35 #PWM

GPIO.setup(pin_A1, GPIO.OUT)
GPIO.setup(pin_A2, GPIO.OUT)
GPIO.setup(pin_ENA, GPIO.OUT)
GPIO.setup(pin_B1, GPIO.OUT)
GPIO.setup(pin_B2, GPIO.OUT)
GPIO.setup(pin_ENB, GPIO.OUT)

#w=float(input("Ingrese velocidad: "))
#w=0.01 # Regula la velocidad de giro del motor       
result1=firebase.get('/VOLUMEN/VOLUMEN',None)
result2=firebase.get('/CALIBRACION/Posicion',None)
result=firebase.get('/VELOCIDAD/VELOCIDAD',None)
#def loop():
if (result==1):
               w=0.01 #flujo 1.67ml/s
if (result==2):
               w=0.055 #flujo 0.32 ml/s
if (result==3):
               w=0.1  #flujo 0.18 ml/s
def loop1(): 
            i=1
            a=13#int(input("ingrese limite a"))
            while (i <=a and result1 == 1): 
                i += 1
                print("contador",i)
                GPIO.output(pin_ENA,GPIO.HIGH)
                GPIO.output(pin_A1,GPIO.HIGH)
                GPIO.output(pin_A2,GPIO.LOW)
                GPIO.output(pin_ENB,GPIO.HIGH)
                GPIO.output(pin_B1,GPIO.HIGH)
                GPIO.output(pin_B2,GPIO.LOW)
                time.sleep(w)
                
                GPIO.output(pin_ENA,GPIO.HIGH)
                GPIO.output(pin_A1,GPIO.LOW)
                GPIO.output(pin_A2,GPIO.HIGH)
                GPIO.output(pin_ENB,GPIO.HIGH)
                GPIO.output(pin_B1,GPIO.HIGH)
                GPIO.output(pin_B2,GPIO.LOW)
                time.sleep(w)
                
                GPIO.output(pin_ENA,GPIO.HIGH)
                GPIO.output(pin_A1,GPIO.LOW)
                GPIO.output(pin_A2,GPIO.HIGH)
                GPIO.output(pin_ENB,GPIO.HIGH)
                GPIO.output(pin_B1,GPIO.LOW)
                GPIO.output(pin_B2,GPIO.HIGH)
                time.sleep(w)
                
                GPIO.output(pin_ENA,GPIO.HIGH)
                GPIO.output(pin_A1,GPIO.HIGH)
                GPIO.output(pin_A2,GPIO.LOW)
                GPIO.output(pin_ENB,GPIO.HIGH)
                GPIO.output(pin_B1,GPIO.LOW)
                GPIO.output(pin_B2,GPIO.HIGH)                
                time.sleep(w)
                #break
                #while (i == a):
                #   sys.exit()
thread1=threading.Thread(target=loop1)
thread1.start()
loop1()

def loop12(): 
            i=1
            c=26#int(input("ingrese limite a"))
            while (i <=c and result1 == 2): 
                i += 1
                print("contador",i)
                GPIO.output(pin_ENA,GPIO.HIGH)
                GPIO.output(pin_A1,GPIO.HIGH)
                GPIO.output(pin_A2,GPIO.LOW)
                GPIO.output(pin_ENB,GPIO.HIGH)
                GPIO.output(pin_B1,GPIO.HIGH)
                GPIO.output(pin_B2,GPIO.LOW)
                time.sleep(w)
                
                GPIO.output(pin_ENA,GPIO.HIGH)
                GPIO.output(pin_A1,GPIO.LOW)
                GPIO.output(pin_A2,GPIO.HIGH)
                GPIO.output(pin_ENB,GPIO.HIGH)
                GPIO.output(pin_B1,GPIO.HIGH)
                GPIO.output(pin_B2,GPIO.LOW)
                time.sleep(w)
                
                GPIO.output(pin_ENA,GPIO.HIGH)
                GPIO.output(pin_A1,GPIO.LOW)
                GPIO.output(pin_A2,GPIO.HIGH)
                GPIO.output(pin_ENB,GPIO.HIGH)
                GPIO.output(pin_B1,GPIO.LOW)
                GPIO.output(pin_B2,GPIO.HIGH)
                time.sleep(w)
                
                GPIO.output(pin_ENA,GPIO.HIGH)
                GPIO.output(pin_A1,GPIO.HIGH)
                GPIO.output(pin_A2,GPIO.LOW)
                GPIO.output(pin_ENB,GPIO.HIGH)
                GPIO.output(pin_B1,GPIO.LOW)
                GPIO.output(pin_B2,GPIO.HIGH)                
                time.sleep(w)
                #break
                #while (i == a):
                #   sys.exit()
thread12=threading.Thread(target=loop12)
thread12.start()
loop12()

def loop13(): 
            i=1
            d=39#int(input("ingrese limite a"))
            while (i <=d and result1 == 3): 
                i += 1
                print("contador",i)
                GPIO.output(pin_ENA,GPIO.HIGH)
                GPIO.output(pin_A1,GPIO.HIGH)
                GPIO.output(pin_A2,GPIO.LOW)
                GPIO.output(pin_ENB,GPIO.HIGH)
                GPIO.output(pin_B1,GPIO.HIGH)
                GPIO.output(pin_B2,GPIO.LOW)
                time.sleep(w)
                
                GPIO.output(pin_ENA,GPIO.HIGH)
                GPIO.output(pin_A1,GPIO.LOW)
                GPIO.output(pin_A2,GPIO.HIGH)
                GPIO.output(pin_ENB,GPIO.HIGH)
                GPIO.output(pin_B1,GPIO.HIGH)
                GPIO.output(pin_B2,GPIO.LOW)
                time.sleep(w)
                
                GPIO.output(pin_ENA,GPIO.HIGH)
                GPIO.output(pin_A1,GPIO.LOW)
                GPIO.output(pin_A2,GPIO.HIGH)
                GPIO.output(pin_ENB,GPIO.HIGH)
                GPIO.output(pin_B1,GPIO.LOW)
                GPIO.output(pin_B2,GPIO.HIGH)
                time.sleep(w)
                
                GPIO.output(pin_ENA,GPIO.HIGH)
                GPIO.output(pin_A1,GPIO.HIGH)
                GPIO.output(pin_A2,GPIO.LOW)
                GPIO.output(pin_ENB,GPIO.HIGH)
                GPIO.output(pin_B1,GPIO.LOW)
                GPIO.output(pin_B2,GPIO.HIGH)                
                time.sleep(w)
                #break
                #while (i == a):
                #   sys.exit()
thread13=threading.Thread(target=loop13)
thread13.start()
loop13()

def loop14(): 
            i=1
            e=52#int(input("ingrese limite a"))
            while (i <=e and result1 == 4): 
                i += 1
                print("contador",i)
                GPIO.output(pin_ENA,GPIO.HIGH)
                GPIO.output(pin_A1,GPIO.HIGH)
                GPIO.output(pin_A2,GPIO.LOW)
                GPIO.output(pin_ENB,GPIO.HIGH)
                GPIO.output(pin_B1,GPIO.HIGH)
                GPIO.output(pin_B2,GPIO.LOW)
                time.sleep(w)
                
                GPIO.output(pin_ENA,GPIO.HIGH)
                GPIO.output(pin_A1,GPIO.LOW)
                GPIO.output(pin_A2,GPIO.HIGH)
                GPIO.output(pin_ENB,GPIO.HIGH)
                GPIO.output(pin_B1,GPIO.HIGH)
                GPIO.output(pin_B2,GPIO.LOW)
                time.sleep(w)
                
                GPIO.output(pin_ENA,GPIO.HIGH)
                GPIO.output(pin_A1,GPIO.LOW)
                GPIO.output(pin_A2,GPIO.HIGH)
                GPIO.output(pin_ENB,GPIO.HIGH)
                GPIO.output(pin_B1,GPIO.LOW)
                GPIO.output(pin_B2,GPIO.HIGH)
                time.sleep(w)
                
                GPIO.output(pin_ENA,GPIO.HIGH)
                GPIO.output(pin_A1,GPIO.HIGH)
                GPIO.output(pin_A2,GPIO.LOW)
                GPIO.output(pin_ENB,GPIO.HIGH)
                GPIO.output(pin_B1,GPIO.LOW)
                GPIO.output(pin_B2,GPIO.HIGH)                
                time.sleep(w)
                #break
                #while (i == a):
                #   sys.exit()
thread14=threading.Thread(target=loop14)
thread14.start()
loop14()

def loop15(): 
            i=1
            f=66#int(input("ingrese limite a"))
            while (i <=f and result1 == 5): 
                i += 1
                print("contador",i)
                GPIO.output(pin_ENA,GPIO.HIGH)
                GPIO.output(pin_A1,GPIO.HIGH)
                GPIO.output(pin_A2,GPIO.LOW)
                GPIO.output(pin_ENB,GPIO.HIGH)
                GPIO.output(pin_B1,GPIO.HIGH)
                GPIO.output(pin_B2,GPIO.LOW)
                time.sleep(w)
                
                GPIO.output(pin_ENA,GPIO.HIGH)
                GPIO.output(pin_A1,GPIO.LOW)
                GPIO.output(pin_A2,GPIO.HIGH)
                GPIO.output(pin_ENB,GPIO.HIGH)
                GPIO.output(pin_B1,GPIO.HIGH)
                GPIO.output(pin_B2,GPIO.LOW)
                time.sleep(w)
                
                GPIO.output(pin_ENA,GPIO.HIGH)
                GPIO.output(pin_A1,GPIO.LOW)
                GPIO.output(pin_A2,GPIO.HIGH)
                GPIO.output(pin_ENB,GPIO.HIGH)
                GPIO.output(pin_B1,GPIO.LOW)
                GPIO.output(pin_B2,GPIO.HIGH)
                time.sleep(w)
                
                GPIO.output(pin_ENA,GPIO.HIGH)
                GPIO.output(pin_A1,GPIO.HIGH)
                GPIO.output(pin_A2,GPIO.LOW)
                GPIO.output(pin_ENB,GPIO.HIGH)
                GPIO.output(pin_B1,GPIO.LOW)
                GPIO.output(pin_B2,GPIO.HIGH)                
                time.sleep(w)
                #break
                #while (i == a):
                #   sys.exit()
thread15=threading.Thread(target=loop15)
thread15.start()
loop15()

def loop2():

            j=1
            b=66#int(input("ingrese limite b"))
            while (j <=b and result2 == 1 ):
                j = j +1
                print("contadoooor",j)
                GPIO.output(pin_ENA,GPIO.LOW)
                GPIO.output(pin_A1,GPIO.LOW)
                GPIO.output(pin_A2,GPIO.LOW)
                GPIO.output(pin_ENB,GPIO.HIGH)
                GPIO.output(pin_B1,GPIO.HIGH)
                GPIO.output(pin_B2,GPIO.LOW)
                time.sleep(w)
                
                GPIO.output(pin_ENA,GPIO.HIGH)
                GPIO.output(pin_A1,GPIO.HIGH)
                GPIO.output(pin_A2,GPIO.LOW)
                GPIO.output(pin_ENB,GPIO.LOW)
                GPIO.output(pin_B1,GPIO.LOW)
                GPIO.output(pin_B2,GPIO.LOW)
                time.sleep(w)
                
                GPIO.output(pin_ENA,GPIO.LOW)
                GPIO.output(pin_A1,GPIO.LOW)
                GPIO.output(pin_A2,GPIO.LOW)
                GPIO.output(pin_ENB,GPIO.HIGH)
                GPIO.output(pin_B1,GPIO.LOW)
                GPIO.output(pin_B2,GPIO.HIGH)
                time.sleep(w)
                
                GPIO.output(pin_ENA,GPIO.HIGH)
                GPIO.output(pin_A1,GPIO.LOW)
                GPIO.output(pin_A2,GPIO.HIGH)
                GPIO.output(pin_ENB,GPIO.LOW)
                GPIO.output(pin_B1,GPIO.LOW)
                GPIO.output(pin_B2,GPIO.LOW)
                time.sleep(w)
                #    sys.exit()
thread2=threading.Thread(target=loop2)
thread2.start()
loop2()
#GPIO.cleanup()