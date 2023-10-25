# Feature: Implement automated testing for Python code.
# Scenario: The system should be able to run automated tests on the Python code.

import unittest


# Define a function to run the tests
def run_tests():
    """Run all tests in the current module."""
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(__name__)
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    return result


# Define a test class to be run by the test runner
class TestAutomatedTesting(unittest.TestCase):
    """Test case for automated testing functionality."""

    # Define test methods
    def test_addition(self):
        """Test that addition works correctly."""
        self.assertEqual(1 + 1, 2)

    def test_subtraction(self):
        """Test that subtraction works correctly."""
        self.assertEqual(5 - 3, 2)

    def test_multiplication(self):
        """Test that multiplication works correctly."""
        self.assertEqual(2 * 3, 6)


# Run the tests when the module is executed directly
if __name__ == "__main__":
    run_tests()
