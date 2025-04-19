import unittest
from unittest.mock import patch
from src.enums import Move, Winner
from src.game import Game


class TestGame(unittest.TestCase):
    """Test cases for the Game class."""

    def setUp(self):
        """Set up a new Game instance for each test."""
        self.game = Game()

    def test_determine_winner_draw(self):
        """Test that identical moves result in a draw."""
        for move in Move:
            self.assertEqual(self.game.determine_winner(move, move), Winner.DRAW)

    def test_determine_winner_player_wins(self):
        """Test cases where the player should win."""
        winning_cases = [
            (Move.ROCK, Move.SCISSORS),
            (Move.SCISSORS, Move.PAPER),
            (Move.PAPER, Move.ROCK)
        ]
        for player_move, computer_move in winning_cases:
            self.assertEqual(
                self.game.determine_winner(player_move, computer_move),
                Winner.PLAYER,
                f"Player should win with {player_move} against {computer_move}"
            )

    def test_determine_winner_computer_wins(self):
        """Test cases where the computer should win."""
        winning_cases = [
            (Move.SCISSORS, Move.ROCK),
            (Move.PAPER, Move.SCISSORS),
            (Move.ROCK, Move.PAPER)
        ]
        for player_move, computer_move in winning_cases:
            self.assertEqual(
                self.game.determine_winner(player_move, computer_move),
                Winner.COMPUTER,
                f"Computer should win with {computer_move} against {player_move}"
            )

    @patch("builtins.print")
    def test_display_round_result(self, mock_print):
        """Test that display_round_result prints the correct messages."""
        # Test draw
        self.game.display_round_result(Move.ROCK, Move.ROCK, Winner.DRAW)
        mock_print.assert_any_call("It's a draw!")

        # Test player win
        mock_print.reset_mock()
        self.game.display_round_result(Move.ROCK, Move.SCISSORS, Winner.PLAYER)
        mock_print.assert_any_call("You win this round!")

        # Test computer win
        mock_print.reset_mock()
        self.game.display_round_result(Move.ROCK, Move.PAPER, Winner.COMPUTER)
        mock_print.assert_any_call("Computer wins this round!")


if __name__ == "__main__":
    unittest.main()
