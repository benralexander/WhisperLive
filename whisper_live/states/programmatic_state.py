from enum import Enum
from typing import Any
import logging
from whisper_live.shared_types import StateHandlerMixin,BaseState
from whisper_live.states.cap import Capitalization





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




