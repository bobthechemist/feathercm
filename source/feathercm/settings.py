commandList = []
functionList = []
commandDict = {}
command = None
argument = None
instrument = None # Here the instruction/method is stored globally

# Board settings
feathercmSettings = {
    "currentFollowerResistor": 15000,
    "maxVoltage": 3.3,
    "maxReading": 65536,
    "virtualGround": 1.65,
    "minimumScanrate": 0.1,
    "maximumScanrate": 2.0,
    "minimumFrequency": 1,
    "maximumFrequency": 500
}

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
