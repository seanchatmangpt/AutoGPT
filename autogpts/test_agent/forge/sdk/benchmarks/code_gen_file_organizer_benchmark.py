import anyio

from forge.sdk.benchmarks.dev_abilities import write_file

from forge.sdk.utils.create_prompts import create_python
from forge.sdk.utils.file_tools import extract_filename


async def generate_task(task):
    file_name = extract_filename(task)

    await write_file(None, "1", file_name, b"")

    code = await create_python(task)

    await write_file(None, "1", file_name, code.encode())

    run_tests("code_gen_file_organizer_benchmark_test.py")


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
        "Create a file organizer CLI tool in Python that sorts files in a directory based on their file types ("
        "e.g., images, documents, audio) and moves them into these corresponding folders: 'images', 'documents', "
        "'audio'. The entry point will be a python file that can be run this way: python organize_files.py "
        "--directory_path=YOUR_DIRECTORY_PATH"
    )

    steps = await generate_task(task)
    print(steps)


if __name__ == "__main__":
    anyio.run(main)
