from __future__ import annotations

from typing import TYPE_CHECKING

import random

from components.base_component import BaseComponent

if TYPE_CHECKING:
    from entity import Actor

class Talker(BaseComponent):
    parent: Actor

    def __init__(self, exclamations):
        self.exclamations = exclamations

    def exclaim(self):
        self.engine.message_log.add_message(
            f"{self.parent.name}: \"{random.choice(self.exclamations)}\""
        )

class Silent(Talker):
    def __init__(self):
        pass

toad_exclamations = [
    'Nice weather today!',
    'What a nice day to be a toad...',
    'Toad!',
    'I ought to eat some more seedcakes.',
    'I\'m just toading about.',
]