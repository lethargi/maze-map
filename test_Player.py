import unittest as ut
import numpy as np

from Player import Player

class TestPlayer(ut.TestCase):
    def test_Given_player_When_move_Then_position_changes_as_expected(self):
        start_position = np.array([0, 0])
        player = Player(start_position)

        expected_position = np.array([0,-1])

        player.move("w")

        self.assertTrue(np.array_equal(player.position, expected_position))

    def test_Given_player_When_move_multiple_times_Then_number_of_past_positions_are_as_expected(self):
        start_position = np.array([0, 0])
        player = Player(start_position)

        movements = "wasd"

        for m in list(movements):
            player.move(m)

        self.assertEqual(len(player.past_positions), len(movements))

