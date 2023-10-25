import anyio

from forge.sdk.benchmarks.dev_abilities import write_file

from forge.sdk.utils.create_prompts import create_python
from forge.sdk.utils.file_tools import extract_filename


async def generate_task(task):
    file_name = extract_filename(task)

    await write_file(None, "1", file_name, b"")

    code = await create_python(task)

    await write_file(None, "1", file_name, code.encode())

    run_tests("code_gen_password_generator_benchmark_test.py")


def run_tests(test_file):
    import subprocess
    import sys

    try:
        output = subprocess.check_output([sys.executable, test_file])
        print(output)
        assert b"OK" in output
    except subprocess.CalledProcessError:
        return False


async def main():
    task = (
        "Create a random password generator. The password should have between 8 and 16 characters and should "
        "contain at least one letter, number and symbol. The password should be printed to the console. The entry "
        "point will be a python file that can be run this way: python password_generator.py [--len x] where x is "
        "the length of the password. If no length is specified, the password should be 8 characters long. The "
        "password_generator can also be imported as a module and called as password = "
        "password_generator.generate_password(len=x). Any invalid input should raise a ValueError."
    )

    steps = await generate_task(task)
    print(steps)


if __name__ == "__main__":
    anyio.run(main)
