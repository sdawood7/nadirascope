#!/usr/bin/python
import sys
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

StepPins = [17,27,22,23]

for pin in StepPins:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin, False)

Seq = [[1,0,0,1],
       [1,0,0,0],
       [1,1,0,0],
       [0,1,0,0],
       [0,1,1,0],
       [0,0,1,0],
       [0,0,1,1],
       [0,0,0,1]]

StepCount = len(Seq)

WaitTime = 1/float(1000) #1 milliseconds

StepCounter = 0

if len(sys.argv) > 1:
    numSteps = int(sys.argv[1])
    print("Turning " + str(numSteps) + " Steps")
    if numSteps < 0:
        StepDir = -1
    else:
        StepDir = 1

    for i in range(0, abs(numSteps)):
        for pin in range(0,len(StepPins)):
            pinOut = False if Seq[(i%len(Seq)) * StepDir][pin] == 0 else True
            GPIO.output(StepPins[pin], pinOut)
            time.sleep(WaitTime)
        for pin in range(0, len(StepPins)):
            GPIO.output(StepPins[pin], False)
