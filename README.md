# Rock. Paper. Scissors. Combat Protocol Engaged.

A minimalistic CLI skirmish between carbon-based free will and cold, algorithmic chance.

## Project Structure

The project is organized into a package structure to improve testability, structure, and readability:

- `src/`: Source code package
    - `enums.py`: Contains the `Move` and `Winner` enums.
    - `players.py`: Contains the `Player` abstract base class and its implementations (`HumanPlayer` and
      `ComputerPlayer`).
    - `game.py`: Contains the `Game` class with methods for game logic (`determine_winner`, `display_round_result`, and
      `run`).
- `tests/`: Unit tests package
    - `test_game.py`: Tests for the `Game` class.
    - `test_players.py`: Tests for the `Player` implementations.
    - `test_enums.py`: Tests for the enums.
    - `run_tests.py`: Script to run all tests.
- `main.py`: The main entry point for the game.

## How to Play

1. Launch the game from your shell of choice:
   ```
   python main.py
   ```

2. Choose your weapon: Rock, Paper, or Scissors.
   Your opponent? A silicon-based entity with no concept of mercy.

3. First to 3 points wins. Ties delay the inevitable.

## Rules

- Rock pulverizes Scissors.
- Scissors shred Paper.
- Paper smothers Rock like a passive-aggressive email.

Same move? Nobody wins. Nobody loses. Just tension.

## Features

- Enum-powered move system. Because strings are for amateurs.
- Type hints so strong they practically compile themselves.
- Modular and readable, like a well-organized armory.
- Game logic packed into a `Game` class. No globals, no chaos.
- Tests included. Because bugs are worse than losing.

## Running Tests

To verify everything still functions in this realm:

```
python tests/run_tests.py
```

If the tests pass, sleep well. If not, fix it or be defeated by your own creation.
