import anyio

from forge.sdk.benchmarks.dev_abilities import write_file

from forge.sdk.utils.create_prompts import create_python
from forge.sdk.utils.file_tools import extract_filename


async def generate_task(task):
    file_name = extract_filename(task)

    await write_file(None, "1", file_name, b"")

    code = await create_python(task)

    await write_file(None, "1", file_name, code.encode())

    run_tests("code_gen_three_sum_benchmark_test.py")


def run_tests(test_file):
    import subprocess
    import sys

    check = b"[0, 1, 2]\n[0, 2, 5]\n[0, 2, 3]\n"
    try:
        output = subprocess.check_output([sys.executable, test_file])
        assert check == output
        return True
    except subprocess.CalledProcessError:
        return False


async def main():
    task = (
        "Create a three_sum function in a file called sample_code.py. Given an array of integers, return indices "
        "of the three numbers such that they add up to a specific target. You may assume that each input would "
        "have exactly one solution, and you may not use the same element twice. Example: Given nums = [2, 7, 11, "
        "15], target = 20, Because nums[0] + nums[1] + nums[2] = 2 + 7 + 11 = 20, return [0, 1, 2]."
    )

    steps = await generate_task(task)
    print(steps)


if __name__ == "__main__":
    anyio.run(main)
