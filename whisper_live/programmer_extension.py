from enum import Enum
import logging
import threading
import string
from pynput.keyboard import Key, Controller






class Programmer():
    def __init__(self,development_mode: bool = True,
                 punctuation_suppressed: bool = True):
        self.logger = logging.getLogger(__name__)
        self.development_mode = development_mode
        self.punctuation_suppressed = punctuation_suppressed
        self.keyboard = Controller() if not self.development_mode else None

        logging.info('initialized Programmer mode')

    def look_for_directives(self, last_text: str = "") -> bool:
        """
        Look to see if the user is trying to specify a command.  If so, be willing to change
        the state of the program.  If the command is built into a string of text, then return
        a Boolean indicating that continued processing is necessary.  If not, return a False
        to indicate that no further processing is necessary.

        :param last_text:
        :type last_text:
        """



    def output(self,last_text:str):
        if  self.development_mode:
            print(f"{last_text}")
        else:
            self.keyboard.type(last_text)

