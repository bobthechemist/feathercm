from .specbase import *


FEATHERWING = "spec"

# Pin designations (in echem, we set up a class.  Here, I do not think it is necessary)
source = DigitalInOut(board.D12)
source.direction = Direction.OUTPUT

tia = AnalogIn(board.A1)
passive = AnalogIn(board.A2)
active = AnalogIn(board.A3)

def toVoltage(value):
    return float(3.3 * value / 65536)

# Functions needed for the board
def initFunc(*argv):
    return f'I have initialized {argv[0]}'

def sourceFunc(*argv):
    onoff = 'off'
    options = ['1', 'on', 'ON']
    if argv[0] in options:
        onoff = 'on'
    return f'Turning source {onoff}.'

def readFunc(*argv):
    options = ['tia', 'passive', 'active']
    pins = {'tia':tia, 'passive':passive, 'active':active}
    if argv[0] in options:
        return toVoltage(pins[argv[0]].value)
    else:
        return f'Valid options are {options}'



# Names of commands and their associated functions
# IMPT: Append to these variables.
commandList += ['init', 'source', 'read']
functionList += [initFunc, sourceFunc, readFunc]
