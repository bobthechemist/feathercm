"""
feathercm.exceptions
~~~~~~~~~~~~~~~~~~~~

This module contains the set of exceptions for feathercm
"""

class feathercmError(Exception):
    """Error handling for feathercm"""
    def __init__(self,message):
        self.message = message
