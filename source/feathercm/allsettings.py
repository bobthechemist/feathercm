'''
Settings dictionaries for the various instruments
Intended to be imported with `from .allsettings import <dict> as settings`
'''

# Board settings
specSettings = {
    "NP": 100, # Time series number of points
    "FR": 2 # Time series collection frequency
}

specDescriptions = {
    "NP": "Number of points",
    "FR": "Collection frequency"
}
