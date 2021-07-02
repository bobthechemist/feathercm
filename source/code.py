"""
code
~~~~

The main routine for FeAtHEr.Cm
"""

# Import only one module from feathercm
import feathercm.echem as f


f.init(f.FEATHERWING)

while True:
    f.listen()
