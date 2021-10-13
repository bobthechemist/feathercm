from .specbase import *
from .allsettings import specSettings as settings
from .allsettings import specDescriptiosn as descriptions



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

def setFunc(*argv):
    res = str(argv)
    if argv[0] is None:
        res = 'Choose from: ' + ', '.join([f'{descriptions[i]} ({i})' for i in descriptions.keys()]) + '.'
    else:
        # Split argument
        par = argv[0].split(" ", 1)
        if par[0] in settings.keys():
            res = f'I will set {par[0]} to {par[1]}.'
            settings[par[0]] = par[1]
        else:
            res = f'{par[1]} Valid parameters are: ' + ', '.join([f'{list(descriptions.keys())}])
    return res

def getFunc(*argv):
    res = str(argv)
    if argv[0] is None:
        res = 'Choose from: ' + ', '.join([f'{descriptions[i]} ({i})' for i in descriptions.keys()]) + '.'
    else:
        if argv[0] in settings.keys():
            res = settings[argv[0]]
        else:
            res = f'No such parameter {argv[0]}'
    return res

# Names of commands and their associated functions
# IMPT: Append to these variables.
commandList += ['init', 'source', 'read', 'set', 'get']
functionList += [initFunc, sourceFunc, readFunc, setFunc, getFunc]
