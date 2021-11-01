from .specbase import *
from .allsettings import specSettings as settings
from .allsettings import specDescriptions as descriptions
from time import monotonic_ns
import random

FEATHERWING = "spec"

# Pin designations (in echem, we set up a class.  Here, I do not think it is necessary)
source = DigitalInOut(board.D12)
source.direction = Direction.OUTPUT
indicator = DigitalInOut(board.D13)
indicator.direction = Direction.OUTPUT

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
        source.value = True
    else:
        source.value = False
    return f'Turning source {onoff}.'

def readFunc(*argv):
    options = ['tia', 'passive', 'active']
    pins = {'tia':tia, 'passive':passive, 'active':active}
    if argv[0] in options:
        return toVoltage(pins[argv[0]].value)
    else:
        return f'Valid options are {options}'

def setFunc(*argv):
    '''description'''
    if argv[0] is None:
        res = 'Choose from: ' + ', '.join([f'{descriptions[i]} ({i})' for i in descriptions.keys()]) + '.'
    else:
        # Split argument
        par = argv[0].split(" ", 1)
        par[0] = par[0].upper()
        if par[0] in settings.keys():
            res = f'I will set {par[0]} to {par[1]}.'
            settings[par[0]] = par[1]
        else:
            res = f'{par[1]} Valid parameters are: ' + ', '.join([f'{list(descriptions.keys())}'])
    return res

def getFunc(*argv):
    ''' Get current value for a parameter. Do not include a parameter for a list of possibilities.'''
    if argv[0] is None:
        res = 'Choose from: ' + ', '.join([f'{descriptions[i]} ({i})' for i in descriptions.keys()]) + '.'
    else:
        uargv = argv[0].upper()
        if uargv in settings.keys():
            res = settings[uargv]
        else:
            res = f'No such parameter {uargv}'
    return res

def timeSeriesFunc(*argv):
    ''' Collects a time series of measurements. '''
    # Abort if detector incorrect
    if not settings['DT'] in ['active', 'passive', 'tia']:
        return f'{settings["DT"]} is not a valid detector.'
    detector = globals()[settings['DT']]
    # Make sure source is on
    source.value = True
    data = []
    i = 0
    timeDelta = 10**9/float(settings['FR'])
    lastTime = monotonic_ns()
    indicator.value = True
    while len(data) < int(settings["NP"]):
        currentTime = monotonic_ns()
        if (currentTime - lastTime) > timeDelta:
            data.append([i,detector.value])
            lastTime = currentTime
            i = i + 1
    indicator.value = False
    source.value = False
    return data




# Names of commands and their associated functions
# IMPT: Append to these variables.
commandList += ['init', 'source', 'read', 'set', 'get', 'go']
functionList += [initFunc, sourceFunc, readFunc, setFunc, getFunc, timeSeriesFunc]
