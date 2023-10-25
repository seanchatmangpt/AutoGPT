# Import the necessary modules
import unittest


# Define the test class
class TestForms(unittest.TestCase):
    # Define the setUp method to initialize any necessary variables
    def setUp(self):
        self.forms = ["form1", "form2", "form3"]

    # Define the test method to test the length of the forms list
    def test_forms_length(self):
        self.assertEqual(len(self.forms), 3)

    # Define the test method to test if a specific form is in the forms list
    def test_specific_form(self):
        self.assertIn("form2", self.forms)


# Run the tests
if __name__ == "__main__":
    unittest.main()
