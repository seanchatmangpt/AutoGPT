# Import necessary libraries
import unittest


# Define test class
class Test(unittest.TestCase):
    # Define test method
    def test(self):
        # Define input
        input = "Final testing and debugging"

        # Define expected output
        expected_output = "Final testing and debugging"

        # Compare input and expected output
        self.assertEqual(input, expected_output)


# Run tests
if __name__ == "__main__":
    unittest.main()
