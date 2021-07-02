"""
feathercm.data
~~~~~~~~~~~~~~

data class for FeAtHEr-Cm
"""
#gfrom .base import *
from .settings import *

class data:
    def toVoltage(self, value):
        """Convert raw value to a voltage
        """
        mv = feathercmSettings["maxVoltage"]
        mr = feathercmSettings["maxReading"]
        vg = feathercmSettings["virtualGround"]
        return (value * mv)/mr - vg

    def toInvertedVoltage(self,value):
        """Convert raw value to a voltage
        """
        mv = feathercmSettings["maxVoltage"]
        mr = feathercmSettings["maxReading"]
        vg = feathercmSettings["virtualGround"]
        return -((value * mv)/mr - vg)

    def toCurrent(self, value):
        """Convert raw value to a current
        """
        return self.toVoltage(value)/feathercmSettings["currentFollowerResistor"]

    def toSelf(self, value):
        """Convert raw value into a time, possibly useful for prefix conversion"""
        return value

    def toReading(self,voltage):
        mv = feathercmSettings["maxVoltage"]
        mr = feathercmSettings["maxReading"]
        vg = feathercmSettings["virtualGround"]
        return int(mr*(voltage+vg)//mv)

    def __init__(self, *argv):
        self.validUnits = ["Current", "Voltage", "InvertedVoltage", "None"]
        self.unitFuncs = [self.toCurrent, self.toVoltage, self.toInvertedVoltage, self.toSelf]
        self.unitDict = {self.validUnits[i]:self.unitFuncs[i] for i in range(0,len(self.validUnits))}
        self.vals = [[10000,10000],[32768,32768]]
        self.dim = []
        self.storedUnits = 'raw'
        self.maxlength = 1000
        for arg in argv:
            if arg in self.validUnits:
                self.dim.append(arg)
            else:
                self.dim.append("None")

    def fromRaw(self, which, value):
        """Converts a reading into a value"""
        return self.unitDict[which](value)

    def processData(self):
        """Converts reading data into values"""
        newvals = []
        for i in self.vals:
            newvals.append([self.fromRaw(self.dim[0],i[0]),self.fromRaw(self.dim[1],i[1])])
        return newvals

    def append(self, item):
        """Appends item onto val"""
        self.vals.append(item)
