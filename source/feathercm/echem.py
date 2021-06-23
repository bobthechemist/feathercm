"""
feathercm.echem
~~~~~~~~~~~~~~~

This module contains functions and classes used in electrochemical measurements
"""
from .exceptions import feathercmError
from .settings import feathercmSettings
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
            raise(feathercmError("Control pin already active. Bailing because this shouldn't happen."))
        else:
            self.control = AnalogOut(self.controlPin)
            self.controlActive = True

    def controlOff(self):
        if not self.controlActive:
            raise(feathercmError("Control pin is not active. Bailing because this shouldn't happen."))
        else:
            self.control.deinit()
            self.controlActive = False

    def scanrateCheck(self, scanrate):
        min = feathercmSettings["minimumScanrate"]
        max = feathercmSettings["maximumScanrate"]
        if not (scanrate >= min and scanrate <= max):
            raise(feathercmError("{} is not a valid scan rate".format(scanrate)))

    def voltageCheck(self, voltage):
        mv = feathercmSettings["maxVoltage"]
        vg = feathercmSettings["virtualGround"]
        if not ( (voltage + vg) <= mv and (voltage + vg) ) >= 0:
            raise(feathercmError("Voltage ({}) is out of range.".format(voltage)))

class sweep(base):
    def __init__(self,control, voltage, current):
        self.startPotential = -0.5 # Potentials in V
        self.switchPotential = 0.5
        self.endPotential = -0.5
        self.scanrate = 1 # V/s
        self.samplingFrequency = 50 # Hz
        self.ns = 1000000000 # simple definition
        super().__init__(control, voltage, current)

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
