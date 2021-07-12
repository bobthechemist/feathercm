
import supervisor
import board
from .settings import *
from .data import data

# Base functions

def initFunc(*argv):
    '''Default initialization function

    Featherwing module should override this function, although it doesn't have to.
    '''
    return 'No Featherwing initialization function found.'

def rebootFunc(*argv):
    '''Reboots the potentiostat
    '''
    supervisor.reload()

commandList += ["init", "reboot"]
functionList += [initFunc, rebootFunc]


def init(featherwing):
    '''Starts feather-cm
    '''
    mergeDict(makeCommandDict(commandList, functionList))
    response = commandDict['init'](featherwing)
    respond(response)

def sba():
    '''Checks if a command is available on the serial line
    '''
    return supervisor.runtime.serial_bytes_available

def listen():
    '''Starts listening to the serial line

    If a command is present, read the line, check if it is a valid command, execute the command and return the response.
    '''
    global command, argument
    if sba():
        currentMessage = input().strip()
        parts = currentMessage.split(" ", 1)
        if len(parts) == 2:
            (command, argument) = parts
        else:
            command = parts[0]
            argument = None
        if commandValidQ():
            response = commandDict[command](argument)
        else:
            response = "Invalid command"
        respond(response)

def commandValidQ():
    '''Checks if the latest command is valid
    '''
    return command in commandDict.keys()

def respond(response):
    ''' Posts a response
    '''
    if type(response) is str:
        print(response)
    elif type(response) is data:
        for i in response.processData():
            print(i)
    elif type(response) is list:
        for i in response:
            print(i)
    else:
        print(f"I cannot handle type: {type(response)}.")

# Support functions

def analogWriteValue(x):
    '''Returns the 'correct' 12-bit integer value that generates the expected voltage
    for the input value.  To perform this calibration, measure the actual voltage (with DVM) at
    A0 with respect to A0 setting.  Best results are obtained for voltages under 2.0.  Find the
    absolute error and convert that to an A0 adjustment value. Find the best fit line between A0 (x axis)
    and A0 adjustment value (y axis).

    Note: the M4 cannot handle rail-to-rail and output is limited to 0.1 to 3.2
    '''
    slope = 1.005747
    intercept = 28.3129
    if x < intercept:
        raise ValueError(f"Analog output value must be greater than {intercept}.")
    elif not 124 <= x <= 3972:
        raise ValueError(f"Requested value is outside of the range possible with M4.")
    return int(x * slope - intercept)

def analogWrite(pin, value):
    '''Writes to an analog pin after correcting for calibration curve adjustments and switching
    value from 12 bit to 16 bit.
    '''
    val = analogWriteValue(value) << 4
    #print(f'sending {val}')
    pin.value = val
    return None

def analogWriteVoltage(pin, value, vground = True):
    '''Writes to an analog pin the requested voltage after correcting for calibration curve
    adjustments.  Will correct for virtual ground if requested.
    '''
    val = value
    if vground:
        val += feathercmSettings["virtualGround"]
    val = val/feathercmSettings["maxVoltage"] * 4096
    val = analogWriteValue(val)
    #print(f'sending {val}')
    pin.value = val << 4
    return None

def analogRead(pin, n = 8):
    ''' Reads an analog pin and adjusts the value according to a linear calibration.  Allows
    rapid signal averaging and returns the value as 12-bit.  Currently, errors seem to be on the
    order of +/- 5 mV.
    '''
    slope = 1.000405 # Consider putting calibration data in the settings file
    intercept = -12.7531
    val = 0
    for i in range(n):
        val += pin.value >> 4 # convert to 12-bit
    val = val/n
    return int(val * slope + intercept)

def toVoltage(reading, vground = True):
    '''Convert a 12-bit reading into a voltage.  Setting vground = False will return 0 to 3.3 V,
    a true value will return -1.65 to +1.65 V
    '''
    val = reading/4096 * feathercmSettings["maxVoltage"]
    if vground:
        val -= feathercmSettings["virtualGround"]

    return val

