"""
feathercm.scac
~~~~~~~~~~~~~~

simplified command and control for FeAtHEr-Cm
"""

import supervisor
import board
import neopixel

infoLED = neopixel.NeoPixel(board.NEOPIXEL, 1)
currentMessage = None
command = None
argument = None

def doReload():
    supervisor.reload()

def sba():
    ''' Returns if serial bytes are available and sets an LED'''
    global infoLED
    if supervisor.runtime.serial_bytes_available:
        infoLED = (0,0,50)
        val = True
    else:
        infoLED = (50,0,0)
        val = False
    return val

def listen():
    global currentMessage
    global command
    global argument
    currentMessage = input().strip()
    # If valid, separate into command and argument
    parts = currentMessage.split(" ",1)
    if len(parts) == 2:
        (command, argument) = parts
    else:
        command = parts[0]
        argument = None

def transmitList(data):
    for i in data:
        s = ''
        for j in i:
            s += str(j) + ' '
        print(s + '\r')

# Command lists
def cRun(argString):
    if argString == None:
        print(f'I need information')
    else:
        print('running something')

def cHelp(argString):
    import gc
    gc.collect()
    print(gc.mem_free())

# Command list
commands = ["run", "help"]
functions = [cRun, cHelp]
cmdDict = {commands[i]:functions[i] for i in range(0,len(commands))}
