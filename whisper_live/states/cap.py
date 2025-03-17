from enum import Enum
from whisper_live.shared_types import StateHandlerMixin,BaseState
import logging
from dataclasses import dataclass, field




class Capitalization(StateHandlerMixin, Enum):
    NO_CHANGE = 'reset', 'do not modify the capitalization as provided by the model'
    CAP_FIRST_CHAR = 'cap', 'letter the first letter of the succeeding word', False
    ALL_CAPS_ON = 'all caps on', 'capitalize every letter of the succeeding phrase'
    ALL_CAPS_OFF = 'all caps off', 'do not capitalize every letter of the succeeding phrase'
    NO_CAP_ON = 'no caps on', 'present all letters as lowercase'

class Cap(BaseState):

    def __init__(self):
        self.capitalization = Capitalization
        super().__init__( self.capitalization )

    def capitalization_class(self) :
        return

    def initiaize(self):
        return 'we can init'
