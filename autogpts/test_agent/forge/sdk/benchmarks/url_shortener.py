# url_shortener.py

# Importing necessary modules
import sys
import unittest


# Defining the shorten_url function
def shorten_url(url):
    """Shortens a given URL and returns the shortened URL.

    Args:
        url (str): The URL to be shortened.

    Returns:
        str: The shortened URL.
    """
    # Checking if the URL is already shortened
    if url.startswith("http://t.cn/"):
        return url

    # Shortening the URL
    shortened_url = "http://t.cn/" + url[-7:]

    return shortened_url


# Defining the retrieve_url function
def retrieve_url(shortened_url):
    """Retrieves the original URL from a shortened URL and returns it.

    Args:
        shortened_url (str): The shortened URL to be retrieved.

    Returns:
        str: The original unshortened URL.
    """
    # Checking if the URL is already shortened
    if not shortened_url.startswith("http://t.cn/"):
        return shortened_url

    # Retrieving the original URL
    original_url = shortened_url[11:]

    return original_url


# Defining the main function
def main():
    """The main function that runs the CLI for the URL shortener program."""
    # Getting the URL from the command line
    url = sys.argv[1]

    # Shortening the URL
    shortened_url = shorten_url(url)

    # Retrieving the original URL
    original_url = retrieve_url(shortened_url)

    # Displaying the appropriate output based on the input
    if shortened_url == original_url:
        print("The shortened URL is:", shortened_url)
    else:
        print("The original URL is:", original_url)

    # Prompting the user for another URL
    url = input("Enter another URL to process: ")


# Running the main function
if __name__ == "__main__":
    main()


# Writing tests for the functions
class TestURLShortener(unittest.TestCase):
    """A class that contains tests for the shorten_url and retrieve_url functions."""

    def test_shorten_url(self):
        """Tests the shorten_url function."""
        # Shortening a URL
        shortened_url = shorten_url("https://www.example.com")

        # Checking if the shortened URL is correct
        self.assertEqual(
            shortened_url, "http://t.cn/1234567", "Shortened URL is incorrect!"
        )

    def test_retrieve_url(self):
        """Tests the retrieve_url function."""
        # Retrieving the original URL
        original_url = retrieve_url("http://t.cn/1234567")

        # Checking if the original URL is correct
        self.assertEqual(
            original_url, "https://www.example.com", "Retrieved URL is incorrect!"
        )


# Running the tests
unittest.main()
