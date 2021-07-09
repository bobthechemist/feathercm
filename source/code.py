"""
code
~~~~

The main routine for FeAtHEr.Cm
"""

# Import only one module from feathercm
#import feathercm.echem as f
import feathercm.base as base
import board
from analogio import AnalogIn, AnalogOut
from time import sleep

#f.init(f.FEATHERWING)
#while True:
#    f.listen()


ctl = AnalogOut(board.A0)
vdb = AnalogIn(board.A4)
vd = AnalogIn(board.A5)
volt = AnalogIn(board.A2)
curr = AnalogIn(board.A3)



while True:
    base.analogWriteVoltage(ctl, 1.5, vground=True)
    myVoltage = base.toVoltage(base.analogRead(volt),vground=True)
    myCurrent = base.toVoltage(base.analogRead(curr),vground=True)
    print(f'volt: {round(myVoltage,3)}, curr: {round(myCurrent,3)}')
    sleep(1)





