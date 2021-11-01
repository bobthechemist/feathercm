import supervisor
import board
from .data import data
from analogio import AnalogOut, AnalogIn
from digitalio import DigitalInOut, Direction


commandList = []
functionList = []
commandDict = {}
command = None
argument = None
instrument = None # Here the instruction/method is stored globally

# NOTE: At some point, this must be reconciled and merged with base, which is too pstat-centric at the moment.
def makeCommandDict(commands, functions):
    ''' Create a dictionary from arguments
    '''
    return {commands[i]:functions[i] for i in range(0,len(commands))}


def mergeDict(newDict):
    ''' Merges the passed dictionary into the global dictionary.
    There is no checking of key overlap at present.  Currently using this 'feature' to overload the base initialization command.  Not sure if this is necessary.
    '''
    global commandDict
    commandDict.update(newDict)
    return None

def initFunc(*argv):
    '''Default initialization function

    Featherwing module should override this function, although it doesn't have to.
    '''
    return 'No Featherwing initialization function found.'

def rebootFunc(*argv):
    '''Reboots the instrument
    '''
    supervisor.reload()

def validCommandFunc(*argv):
    '''Returns valid command list
    TODO: allow for help description
    '''
    retval = f'valid commands are: {list(set(commandList))}'
    try:
        retval = dir(commandDict[argv[0]])
        retval = 'Waiting to include this functionality'
    except KeyError:
        pass
    return retval

commandList += ['init', 'reboot', '?']
functionList += [initFunc, rebootFunc, validCommandFunc]



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
    if type(response) in [str, int, float]:
        print(response)
    # Appropriate only for echem, which is probably OK, but data class should probably be echemdata class
    elif type(response) is data:
        for i in response.processData():
            print(i)
    elif type(response) is list:
        for i in response:
            print(i)
    elif type(response) is float:
        print(f'{response:.3f}')
    else:
        print(f"I cannot handle type: {type(response)}.")
