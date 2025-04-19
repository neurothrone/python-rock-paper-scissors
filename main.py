#!/usr/bin/env python3

from src.game import Game


if __name__ == "__main__":
    try:
        game = Game()
        game.run()
    except KeyboardInterrupt:
        print("\nGame interrupted. Goodbye!")
