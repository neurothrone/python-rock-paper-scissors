#!/usr/bin/env python3

import unittest
import sys
import os

# Add the parent directory to the path so that the tests can import from src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import all test modules
from tests.test_game import TestGame
from tests.test_players import TestComputerPlayer, TestHumanPlayer
from tests.test_enums import TestEnums


def run_tests():
    """Run all the tests."""
    # Create a test suite
    test_suite = unittest.TestSuite()

    # Add all test cases to the suite
    test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestGame))
    test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestComputerPlayer))
    test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestHumanPlayer))
    test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestEnums))

    # Run the tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)

    # Return the result
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
