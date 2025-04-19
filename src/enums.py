import enum


class Move(enum.Enum):
    """Enum representing the possible moves in Rock, Paper, Scissors."""
    ROCK = "rock"
    PAPER = "paper"
    SCISSORS = "scissors"


class Winner(enum.Enum):
    """Enum representing the possible outcomes of a round."""
    PLAYER = "player"
    COMPUTER = "computer"
    DRAW = "draw"
