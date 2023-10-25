import anyio

from forge.sdk.benchmarks.dev_abilities import write_file
from forge.sdk.utils.complete import acreate

from forge.sdk.utils.create_prompts import create_python
from forge.sdk.utils.file_tools import extract_filename


async def generate_task(task):
    file_name = extract_filename(task)

    await write_file(None, "1", file_name, b"")

    gherkin = await acreate(
        task
        + "\nConvert to 4 Gherkin Features. Include examples to ensure correct results ```gherkin",
        temperature=1.2,
        max_tokens=500,
        stop=["```"],
    )

    code = await create_python(gherkin + task)

    await write_file(None, "1", file_name, code.encode())

    run_tests("code_gen_url_shortener_benchmark_test.py")


def run_tests(test_file):
    import subprocess
    import sys

    try:
        output = subprocess.check_output([sys.executable, test_file])
        print(output)
        assert b"OK" in output
        return True
    except subprocess.CalledProcessError:
        return False


async def main():
    task = (
        "Build a basic URL shortener using a python CLI. Here are the specifications.\n\nFunctionality: The "
        "program should have two primary functionalities.\n\nShorten a given URL.\nRetrieve the original URL from "
        "a shortened URL.\n\nCLI: The command-line interface should accept a URL as its first input. It should be "
        "able to determine if the url is a shortened url or not. If the url is not shortened, it will display ONLY "
        "the shortened url, otherwise, it will display ONLY the original unshortened URL. Afterwards, "
        "it should prompt the user for another URL to process.\n\nTechnical specifications:\nBuild a file called "
        "url_shortener.py. This file will be called through command lines.\n\nEdge cases:\nFor the sake of "
        "simplicity, there will be no edge cases, you can assume the input is always correct and the user "
        "immediately passes the shortened version of the url he just shortened.\n\nYou will be expected to create "
        "a python file called url_shortener.py that will run through command lines by using python "
        "url_shortener.py.\n\nThe url_shortener.py will be tested this way:\n```\nimport unittest\nfrom "
        "url_shortener import shorten_url, retrieve_url\n\nclass TestURLShortener(unittest.TestCase):\n    "
        "def test_url_retrieval(self):\n        # Shorten the URL to get its shortened form\n        shortened_url "
        "= shorten_url('https://www.example.com')\n\n        # Retrieve the original URL using the shortened URL "
        "directly\n        retrieved_url = retrieve_url(shortened_url)\n\n        self.assertEqual(retrieved_url, "
        "'https://www.example.com', \"Retrieved URL does not match the original!\")\n\nif __name__ == "
        '"__main__":\n    unittest.main()\n```'
    )

    steps = await generate_task(task)
    print(steps)


if __name__ == "__main__":
    anyio.run(main)
