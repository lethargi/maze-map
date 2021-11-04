from enum import Enum
from typing import Tuple

import numpy as np


MOVEMENT_DICTIONARY = {
        "w": np.array([0, -2]),
        "a": np.array([-2, 0]),
        "s": np.array([0, 2]),
        "d": np.array([2, 0]),
        }


class Player:
    def __init__(self, start_position : np.ndarray):
        self.position = start_position
        self.past_positions = []

    def move(self, direction: str):
        ## TODO remove later
        if direction not in MOVEMENT_DICTIONARY.keys():
            raise Exception("Unrecognized movement")
        self.past_positions.append(self.position)
        self.position += MOVEMENT_DICTIONARY[direction]
