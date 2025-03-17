from enum import Enum
from typing import Any
import logging
from dataclasses import dataclass, field


@dataclass
class StateHandlerMixin:
    command: str
    expl: str
    stand_alone: bool = field(repr=False, default=True)

class BaseState:
    def __init__(self, state: Enum):
        self.state = state

    def list_cmds(self):
        for cmd in self.state:
            print(f"\t {cmd.command}: {cmd.expl}")

    def test_cmds(self):
        self.list_cmds()
        return 'all ok'