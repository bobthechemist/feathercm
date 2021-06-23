import board
import digitalio
import time
import neopixel
from analogio import AnalogIn, AnalogOut
from digitalio import DigitalInOut, Direction, Pull
import feathercm as f
import feathercm.echem
import busio
import feathercm.data
import supervisor
import feathercm.scac as scac
import gc


button = DigitalInOut(board.D5)
button.direction = Direction.INPUT
button.pull = Pull.UP
led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT
ec = feathercm.echem.sweep(board.A0, board.A2, board.A3)

while True:
    if scac.sba():
        scac.listen()
        if scac.command in scac.commands:
            print('found\r')
            scac.cmdDict[scac.command](scac.argument)
        else:
            print('not found\r')
        #if scac.command == "run":
        #    out = ec.doSweep()
        #    scac.transmitList(out.processData())
            #for i in out.processData():
            #    print(f'{i[0]} {i[1]}')

    if not button.value:
        supervisor.reload()
