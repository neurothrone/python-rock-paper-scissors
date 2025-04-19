import random
from abc import ABC, abstractmethod
from src.enums import Move


class Player(ABC):
    """Abstract base class for players in the game."""

    @abstractmethod
    def get_move(self) -> Move:
        """
        Get the player's move.

        Returns:
            Move: The chosen move.
        """
        pass


class HumanPlayer(Player):
    """Human player implementation."""

    @staticmethod
    def display_move_options() -> None:
        """
        Display the available move options to the user.
        """
        print("\nChoose your move:")
        for i, move in enumerate(Move, 1):
            print(f"{i}. {move.value.capitalize()}")

    @staticmethod
    def get_valid_input() -> int:
        """
        Get and validate user input.

        Returns:
            int: A valid choice (1-3) from the user.
        """
        while True:
            try:
                choice = int(input("Enter the number of your choice (1-3): "))
                if 1 <= choice <= 3:
                    return choice
                else:
                    print("Invalid choice. Please enter a number between 1 and 3.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def get_move(self) -> Move:
        """
        Get the human player's choice of move.

        Returns:
            Move: The player's chosen move.
        """
        self.display_move_options()
        choice = self.get_valid_input()
        return list(Move)[choice - 1]


class ComputerPlayer(Player):
    """Computer player implementation."""

    def get_move(self) -> Move:
        """
        Generate a random move for the computer.

        Returns:
            Move: The computer's randomly chosen move.
        """
        return random.choice(list(Move))
