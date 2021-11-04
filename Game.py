from typing import Tuple

import numpy as np

from Player import Player
from Map import Map

from copy import copy

import pygame as pg

class Game:
    def __init__(self, map_size: Tuple[int, int]):
        self.map_size = map_size
        self.map = Map().make_maze(*map_size)[1]
        self.player = Player(np.array((1,1)))

    def draw_map(self):
        current_map = copy(self.map)
        current_map[self.player.position[1], self.player.position[0]] = 9
        formatted_map = current_map[1::2,1::2]
        return formatted_map
