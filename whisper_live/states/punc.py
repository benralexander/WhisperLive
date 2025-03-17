from enum import Enum
from whisper_live.shared_types import StateHandlerMixin,BaseState
import logging
from dataclasses import dataclass, field




class Punctuation(StateHandlerMixin,Enum):
    NO_CHANGE = 'reset', 'do not modify the capitalization as provided by the model'
    RETAIN_PUNCTUATION =  'retain punctuation', 'retain all punctuation the model suggests'
    REMOVE_PUNCTUATION =  'no punctuation', 'return results stripped of all punctuation'


class Punc(BaseState):

    def __init__(self):
        self.punctuation = Punctuation
        super().__init__( self.punctuation )


    def initiaize(self):
        return 'we can init'
