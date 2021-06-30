
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
