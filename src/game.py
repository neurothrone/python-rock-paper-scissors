from src.enums import Move, Winner
from src.players import HumanPlayer, ComputerPlayer


class Game:
    """Class representing the Rock, Paper, Scissors game."""

    def __init__(self):
        """Initialize the game with players and scores."""
        self.human_player = HumanPlayer()
        self.computer_player = ComputerPlayer()
        self.player_score = 0
        self.computer_score = 0

    @staticmethod
    def determine_winner(player_move: Move, computer_move: Move) -> Winner:
        """
        Determine the winner of a round.
        
        Args:
            player_move: The move chosen by the player.
            computer_move: The move chosen by the computer.
        
        Returns:
            Winner: Winner.PLAYER if player wins, Winner.COMPUTER if computer wins, Winner.DRAW if it's a draw.
        """
        if player_move == computer_move:
            return Winner.DRAW

        winning_combinations = {
            (Move.ROCK, Move.SCISSORS),
            (Move.SCISSORS, Move.PAPER),
            (Move.PAPER, Move.ROCK)
        }

        if (player_move, computer_move) in winning_combinations:
            return Winner.PLAYER
        else:
            return Winner.COMPUTER

    @staticmethod
    def display_round_result(player_move: Move, computer_move: Move, winner: Winner) -> None:
        """
        Display the result of a round.
        
        Args:
            player_move: The move chosen by the player.
            computer_move: The move chosen by the computer.
            winner: The winner of the round (Winner.PLAYER, Winner.COMPUTER, or Winner.DRAW).
        """
        print(f"\nYou chose: {player_move.value}")
        print(f"Computer chose: {computer_move.value}")

        if winner == Winner.DRAW:
            print("It's a draw!")
        elif winner == Winner.PLAYER:
            print("You win this round!")
        else:
            print("Computer wins this round!")

    def run(self) -> None:
        """Run the main game loop until either player or computer reaches a score of 3."""
        print("Welcome to Rock, Paper, Scissors!")
        print("First to score 3 points wins the game.")

        while self.player_score < 3 and self.computer_score < 3:
            print(f"\nScore - You: {self.player_score}, Computer: {self.computer_score}")

            player_move = self.human_player.get_move()
            computer_move = self.computer_player.get_move()
            winner = self.determine_winner(player_move, computer_move)

            self.display_round_result(player_move, computer_move, winner)

            if winner == Winner.PLAYER:
                self.player_score += 1
            elif winner == Winner.COMPUTER:
                self.computer_score += 1

        print("\n" + "=" * 30)
        print(f"Final Score - You: {self.player_score}, Computer: {self.computer_score}")

        if self.player_score > self.computer_score:
            print("Congratulations! You won the game!")
        else:
            print("Game over! Computer won the game!")