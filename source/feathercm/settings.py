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
    "maxReading": 4096,
    "virtualGround": 1.65,
    "minimumScanrate": 0.05,
    "maximumScanrate": 10.0,
    "minimumFrequency": 1,
    "maximumFrequency": 500,
    "dataSize": 512
}

# Do these belong in base?

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

def setCurrentMultFunc(*argv):
    global feathercmSettings
    if argv[0] is None:
        res = f'Current follower currently has {feathercmSettings["currentFollowerResistor"]}'
    else:
        feathercmSettings["currentFollowerResistor"] = argv[0]
        res = f'Set current follower resistance to {feathercmSettings["currentFollowerResistor"]}'
    return res

# Names of commands and their associated functions
# IMPT: Append to these variables.
commandList += ['current']
functionList += [setCurrentMultFunc]
