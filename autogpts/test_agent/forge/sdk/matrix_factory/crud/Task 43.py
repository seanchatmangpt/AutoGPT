# Import the necessary modules
import unittest
import requests


# Define the test class
class LoadTestingSystemTest(unittest.TestCase):
    # Define the setUp method to initialize necessary variables
    def setUp(self):
        self.url = "http://www.example.com"
        self.num_requests = 100

    # Define the test method
    def test_load_testing(self):
        # Make 100 requests to the specified URL
        for i in range(self.num_requests):
            response = requests.get(self.url)
            # Assert that the response is successful
            self.assertEqual(response.status_code, 200)


# Run the tests
if __name__ == "__main__":
    unittest.main()
