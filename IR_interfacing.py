import RPi.GPIO as IO
import time
IO.setwarnings(False)
IO.setmode(IO.BCM)


IO.setup(14,IO.IN) #GPIO 14 -> IR sensor as input
count=0

while 1:

    if(IO.input(14)==True): #object is detected
        count=count+1
        print(count)
