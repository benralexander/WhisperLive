from enum import Enum
from typing import Any
import logging
from dataclasses import dataclass, field







@dataclass
class StateHandlerMixin:
    command: str
    expl: str
    stand_alone: bool = field(repr=False, default=True)

class Capitalization(StateHandlerMixin,Enum):
    NO_CHANGE = 'reset', 'do not modify the capitalization as provided by the model'
    CAP_FIRST_CHAR = 'cap', 'letter the first letter of the succeeding word', False
    ALL_CAPS_ON = 'all caps on', 'capitalize every letter of the succeeding phrase'
    ALL_CAPS_OFF = 'all caps off', 'do not capitalize every letter of the succeeding phrase'
    NO_CAP_ON = 'no caps on', 'present all letters as lowercase'


class BaseState:
    def __init__(self, state: Enum):
        self.state = state

    def list_cmds(self):
        for cmd in self.state:
            print(f"\t {cmd.value.cmd}: {cmd.value.expl}")




class Cap:
    def __init__(self,
                 capitalization: Capitalization = None,
                 punctuation: Punctuation = None):



class Punctuation(Enum):
    NO_CHANGE = 0
    RETAIN_PUNCTUATION = 1
    REMOVE_PUNCTUATION = 2


class State:
    def __init__(self,
                 capitalization: Capitalization = None,
                 punctuation: Punctuation = None):
        """
        initialize the state.  If no parameters are set, then assume the user wants to write a program

        :type punctuation: object
        """
        self.capitalization = capitalization if capitalization is not None else Capitalization.NO_CHANGE
        self.punctuation = punctuation if punctuation is not None else Punctuation.NO_CHANGE
        if self.mode_is_empty():
            self.programmer_mode()


    def mode_is_empty(self) -> bool:
        """
        are all the states default?

        :rtype: object
        """
        return self.capitalization == Capitalization.NO_CHANGE and \
                self.punctuation == Punctuation.RETAIN_PUNCTUATION


    def programmer_mode(self) -> None:
        self.capitalization = Capitalization.ALL_CAPS_OFF
        self.punctuation = Punctuation.REMOVE_PUNCTUATION


    def communication_mode(self) -> None:
        self.capitalization = Capitalization.NO_CHANGE
        self.punctuation = Punctuation.NO_CHANGE


    def list_commands(self) -> None:
        """
        Remind the user of all possible commands
        """




