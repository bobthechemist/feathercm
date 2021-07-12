"""
code
~~~~

The main routine for FeAtHEr.Cm
"""

# Import only one module from feathercm
#import feathercm.echem as f
import board
from analogio import AnalogIn, AnalogOut
import time
import feathercm.echem as f

f.init(f.FEATHERWING)
print(f.instrument.samplingFrequency)
f.instrument.scanrate = 0.1
f.instrument.setSamplingFrequency()
print(f.instrument.samplingFrequency)



#f.init(f.FEATHERWING)
#while True:
#    f.listen()

'''
ctl = AnalogOut(board.A0)
vdb = AnalogIn(board.A4)
vd = AnalogIn(board.A5)
volt = AnalogIn(board.A2)
curr = AnalogIn(board.A3)

base.analogWriteVoltage(ctl,.5, vground=True)

while True:
    myVoltage = base.toVoltage(base.analogRead(volt),vground=True)
    myCurrent = base.toVoltage(base.analogRead(curr),vground=True)
    print(f'before volt: {round(myVoltage,3)}, curr: {round(myCurrent,3)}')
    sleep(1)
'''





