import unittest
from src.enums import Move, Winner


class TestEnums(unittest.TestCase):
    """Test cases for the enums used in the game."""

    def test_move_enum_values(self):
        """Test that Move enum has the expected values."""
        self.assertEqual(Move.ROCK.value, "rock")
        self.assertEqual(Move.PAPER.value, "paper")
        self.assertEqual(Move.SCISSORS.value, "scissors")
        self.assertEqual(len(Move), 3)

    def test_winner_enum_values(self):
        """Test that Winner enum has the expected values."""
        self.assertEqual(Winner.PLAYER.value, "player")
        self.assertEqual(Winner.COMPUTER.value, "computer")
        self.assertEqual(Winner.DRAW.value, "draw")
        self.assertEqual(len(Winner), 3)

    def test_move_enum_comparison(self):
        """Test that Move enum values can be compared correctly."""
        self.assertEqual(Move.ROCK, Move.ROCK)
        self.assertNotEqual(Move.ROCK, Move.PAPER)
        self.assertNotEqual(Move.ROCK, Move.SCISSORS)

    def test_winner_enum_comparison(self):
        """Test that Winner enum values can be compared correctly."""
        self.assertEqual(Winner.PLAYER, Winner.PLAYER)
        self.assertNotEqual(Winner.PLAYER, Winner.COMPUTER)
        self.assertNotEqual(Winner.PLAYER, Winner.DRAW)


if __name__ == "__main__":
    unittest.main()
