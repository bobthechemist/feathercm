'''
Settings dictionaries for the various instruments
Intended to be imported with `from .allsettings import <dict> as settings`
'''

# Board settings
specSettings = {
    "NP": 10, # Time series number of points
    "FR": 2, # Time series collection frequency
    "DT": 'active'
}

specDescriptions = {
    "NP": "Number of points",
    "FR": "Collection frequency",
    "DT": "Detector: 'active', 'passive' or 'tia'"
}
