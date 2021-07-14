"""
feathercm.echem
~~~~~~~~~~~~~~~

This module contains functions and classes used in electrochemical measurements
"""
from .base import *
from .settings import *
from analogio import AnalogOut, AnalogIn
from digitalio import DigitalInOut, Direction
import time
import gc
from .data import data

class base:
    """Base class for electrochemical measurements
    """

    def __init__(self, control, voltage, current):
        """Settings are stored in a global config file (settings.py)
        """
        # TODO: Add error checking and default values
        self.controlPin = control
        self.controlActive = False
        self.control = None
        # I don't think we want the control pin to always be active
        #self.control = AnalogOut(control)
        self.voltage = AnalogIn(voltage)
        self.current = AnalogIn(current)
        # Use builtin for indicator
        self.led = DigitalInOut(board.D13)
        self.led.direction = Direction.OUTPUT


    def controlOn(self):
        if self.controlActive:
            raise(RuntimeError("Control pin already active. Bailing because this shouldn't happen."))
        else:
            try:
                self.control.deinit()
            except AttributeError:
                pass
            self.control = AnalogOut(self.controlPin)
            self.controlActive = True

    def controlOff(self):
        if not self.controlActive:
            raise(RuntimeError("Control pin is not active. Bailing because this shouldn't happen."))
        else:
            self.control.deinit()
            self.control = AnalogIn(self.controlPin)
            self.controlActive = False

    def scanrateCheck(self, scanrate):
        min = feathercmSettings["minimumScanrate"]
        max = feathercmSettings["maximumScanrate"]
        if not (scanrate >= min and scanrate <= max):
            raise(RuntimeError("{} is not a valid scan rate".format(scanrate)))

    def voltageCheck(self, voltage):
        mv = feathercmSettings["maxVoltage"]
        vg = feathercmSettings["virtualGround"]
        if not ( (voltage + vg) <= mv and (voltage + vg) ) >= 0:
            raise(RuntimeError("Voltage ({}) is out of range.".format(voltage)))

class sweep(base):
    def __init__(self,control, voltage, current):
        self.startPotential = -0.5 # Potentials in V
        self.switchPotential = 0.5
        self.endPotential = -0.5
        self.scanrate = 0.5 # V/s
        self.samplingFrequency = None
        self.setSamplingFrequency() # Hz
        self.ns = 10**9 # simple definition
        super().__init__(control, voltage, current)

    def setSamplingFrequency(self):
        '''Calculates the sampling frequency that results in 1024 points for the CV
        '''
        vt = abs(self.switchPotential - self.startPotential) + abs(self.endPotential - self.switchPotential)
        minval = feathercmSettings["minimumFrequency"]
        maxval = feathercmSettings["maximumFrequency"]
        numPoints = feathercmSettings["dataSize"]
        self.samplingFrequency =  min(maxval, max(minval,(numPoints * self.scanrate / vt)))


    def setParameter(self, param, value):
        # Parameter checks should go here. Not sure why I cannot use dict
        if param is "SR":
            self.scanrate = value
        elif param is "ST":
            self.startPotential = value
        elif param is "EN":
            self.endPotential = value
        elif param is "SW":
            self.switchPotential = value
        elif param is "SF":
            self.samplingFrequency = value
        else:
            raise NameError("Problem with parameter")


    def getParameter(self, param):
        params = {
            "SR": self.scanrate,
            "ST": self.startPotential,
            "EN": self.endPotential,
            "SW": self.switchPotential,
            "SF": self.samplingFrequency
        }
        if param in params:
            res = str(params[param])
        else:
            res = "NA"
        return res

    def doSweep(self):
        '''Next gen CV sweep
        '''
        # Inform user of sweep start
        self.led.value = True

        # clean up memory
        gc.collect()
        d = data("InvertedVoltage", "Current")
        self.controlOn()
        currPotential = self.startPotential
        analogWriteVoltage(self.control,currPotential)
        # Fixed quiet time
        time.sleep(0.5)
        lastPotlChange = 0
        lastCurrChange = 0
        initDirection = 1 if self.switchPotential > self.startPotential else -1
        tStart = time.monotonic_ns()
        tCurrent = tStart
        tSwitch = tStart + 10**9 * abs(self.startPotential - self.switchPotential)/self.scanrate
        tEnd = tSwitch + 10**9 * abs(self.endPotential - self.switchPotential)/self.scanrate
        doneQ = False
        potlDelta = 10**9/feathercmSettings["maximumFrequency"]
        self.setSamplingFrequency()
        currDelta = 10**9/self.samplingFrequency
        while not doneQ:
            if time.monotonic_ns() - lastPotlChange > potlDelta:
                # Change potential
                if time.monotonic_ns() < tSwitch:
                    currPotential = (time.monotonic_ns() - tStart)* \
                        initDirection*self.scanrate/10**9 + \
                        self.startPotential
                else:
                    currPotential = (time.monotonic_ns() - tSwitch)*(-1)* \
                        initDirection*self.scanrate/10**9 + self.switchPotential
                analogWriteVoltage(self.control, currPotential)
                lastPotlChange = time.monotonic_ns()
            if time.monotonic_ns() - lastCurrChange > currDelta:
                d.append([analogRead(self.voltage), analogRead(self.current)])
                lastCurrChange = time.monotonic_ns()
            doneQ = time.monotonic_ns() > tEnd
        # Turn off control
        self.controlOff()

        self.led.value = False

        return d




# Board module should identify itself
FEATHERWING = "echem"

# Functions needed for the board
def initFunc(*argv):
    global instrument
    instrument = sweep(board.A0, board.A2, board.A3)
    return f'I have initialized {argv[0]}'

def goFunc(*argv):
    global instrument
    out = instrument.doSweep()
    return out

def testFunc(*argv):
    time.sleep(5)
    return [1.2,2.4]

def setFunc(*argv):
    global instrument
    res = str(argv)
    if argv[0] is None:
        res = "Choose from scan rate (SR), start potential (ST), switch potential (SW), end potential (EN) or sampling frequency (SF)."
    else:
        # Split argument
        par = argv[0].split(" ", 1)
        if par[0] in ('SR', 'ST', 'SW', 'EN', 'SF'):
            res = f'I will set {par[0]} to {par[1]}.'
            instrument.setParameter(par[0],float(par[1]))
        else:
            res = f'{par[1]} Valid parameters are: SR, ST, SW, EN, and SF.'
    return res

def getFunc(*argv):
    global instrument
    res = str(argv)
    if argv[0] is None:
        res = "Choose from scan rate (SR), start potential (ST), switch potential (SW), end potential (EN) or sampling frequency (SF)."
    else:
        res = instrument.getParameter(argv[0])
    return res


# Names of commands and their associated functions
# IMPT: Append to these variables.
commandList += ['init','go', 'test', 'set', 'get', 'current']
functionList += [initFunc, goFunc, testFunc, setFunc, getFunc, setCurrentMultFunc]
