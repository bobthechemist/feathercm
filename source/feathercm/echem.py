"""
feathercm.echem
~~~~~~~~~~~~~~~

This module contains functions and classes used in electrochemical measurements
"""
from .base import *
from .settings import *
from analogio import AnalogIn
from analogio import AnalogOut
import time
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


    def controlOn(self):
        if self.controlActive:
            raise(RuntimeError("Control pin already active. Bailing because this shouldn't happen."))
        else:
            self.control = AnalogOut(self.controlPin)
            self.controlActive = True

    def controlOff(self):
        if not self.controlActive:
            raise(RuntimeError("Control pin is not active. Bailing because this shouldn't happen."))
        else:
            self.control.deinit()
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
        self.scanrate = 1 # V/s
        self.samplingFrequency = 10 # Hz
        self.ns = 1000000000 # simple definition
        super().__init__(control, voltage, current)

    def setParameter(self, param, value):
        # Parameter checks should go here. Not sure why I cannot use dict
        if param == "SR":
            self.scanrate = value
        elif param == "ST":
            self.startPotential = value
        elif param == "EN":
            self.endPotential = value
        elif param == "SW":
            self.switchPotential = value
        elif param == "SF":
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
        """ Perform a CV sweep """
        # Helper functions
        p = lambda a,b: 1 if a < b else -1 # Return direction
        c = lambda a,b,d: (a < b) if (d == 1) else (b < a) # Should continue?
        # Create place to store data
        d = data("InvertedVoltage", "Current")

        # [?] Do we assume potentials/scanrate are legit?

        # Turn on the control pin and set the initial potential
        self.controlOn()
        currPotential = self.startPotential
        self.control.value = d.toReading(currPotential)
        # Fixed quiet time
        time.sleep(0.5)
        d.append([self.voltage.value, self.current.value])
        nsr = self.scanrate / self.ns # Gets used frequently
        # Start the forward scan
        cp = p(self.startPotential,self.switchPotential) # Gets used frequently
        sampleTime = self.ns / self.samplingFrequency # Gets used frequently
        tbegin = time.monotonic_ns()
        lastSample = tbegin # Start sampling at the same time
        while c(currPotential, self.switchPotential, cp):
            currPotential = self.startPotential + cp * (time.monotonic_ns()-tbegin) * nsr
            self.control.value = d.toReading(currPotential)
            if time.monotonic_ns() > lastSample +sampleTime:
                d.append([self.voltage.value, self.current.value])
                lastSample = time.monotonic_ns()
        # Set up reverse scan
        tswitch = time.monotonic_ns()
        cp = p(self.switchPotential, self.endPotential) # Update
        while c(currPotential, self.endPotential, cp):
            currPotential = self.switchPotential +cp * (time.monotonic_ns()-tswitch) * nsr
            self.control.value = d.toReading(currPotential)
            if time.monotonic_ns() > lastSample +sampleTime:
                d.append([self.voltage.value, self.current.value])
                lastSample = time.monotonic_ns()
        # Turn off control
        self.controlOff()

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
commandList += ['init','go', 'test', 'set', 'get']
functionList += [initFunc, goFunc, testFunc, setFunc, getFunc]
