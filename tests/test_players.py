import unittest
from unittest.mock import patch, MagicMock
from src.enums import Move
from src.players import ComputerPlayer, HumanPlayer


class TestComputerPlayer(unittest.TestCase):
    """Test cases for the ComputerPlayer class."""

    def setUp(self):
        """Set up a new ComputerPlayer instance for each test."""
        self.computer_player = ComputerPlayer()

    def test_get_move_returns_valid_move(self):
        """Test that get_move returns a valid Move enum value."""
        move = self.computer_player.get_move()
        self.assertIn(move, list(Move))

    @patch("random.choice")
    def test_get_move_uses_random_choice(self, mock_choice):
        """Test that get_move uses random.choice to select a move."""
        mock_choice.return_value = Move.ROCK
        move = self.computer_player.get_move()
        mock_choice.assert_called_once()
        self.assertEqual(move, Move.ROCK)


class TestHumanPlayer(unittest.TestCase):
    """Test cases for the HumanPlayer class."""

    def setUp(self):
        """Set up a new HumanPlayer instance for each test."""
        self.human_player = HumanPlayer()

    def test_display_move_options(self):
        """Test that display_move_options prints the correct information."""
        with patch("builtins.print") as mock_print:
            self.human_player.display_move_options()
            # Check that print was called with the expected messages
            mock_print.assert_any_call("\nChoose your move:")
            mock_print.assert_any_call("1. Rock")
            mock_print.assert_any_call("2. Paper")
            mock_print.assert_any_call("3. Scissors")

    @patch("builtins.input", return_value="1")
    def test_get_valid_input_valid(self, mock_input):
        """Test that get_valid_input returns the correct value for valid input."""
        choice = self.human_player.get_valid_input()
        self.assertEqual(choice, 1)
        mock_input.assert_called_once()

    @patch("builtins.input", side_effect=["invalid", "4", "0", "1"])
    @patch("builtins.print")  # Mock print to avoid output during tests
    def test_get_valid_input_invalid(self, mock_print, mock_input):
        """Test that get_valid_input handles invalid input correctly."""
        choice = self.human_player.get_valid_input()
        self.assertEqual(choice, 1)
        self.assertEqual(mock_input.call_count, 4)

    def test_get_move(self):
        """Test that get_move calls the appropriate methods and returns the correct move."""
        # Mock the display_move_options and get_valid_input methods
        self.human_player.display_move_options = MagicMock()
        self.human_player.get_valid_input = MagicMock(return_value=1)

        move = self.human_player.get_move()

        # Verify that the methods were called
        self.human_player.display_move_options.assert_called_once()
        self.human_player.get_valid_input.assert_called_once()

        # Verify that the correct move was returned
        self.assertEqual(move, Move.ROCK)


if __name__ == "__main__":
    unittest.main()
