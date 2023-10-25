from forge.sdk.abilities.registry import ability, AbilityParameter
from radon.raw import analyze
from radon.metrics import h_visit
from radon.metrics import mi_visit

from textwrap import dedent


from radon.complexity import cc_visit

from forge.sdk.utils.complete import create
from forge.sdk.utils.py_module import PyModule


def get_cyclomatic_complexity(source_code: str) -> dict:
    """
    Returns the Cyclomatic Complexity of the given source code.
    """
    return {func.name: func.complexity for func in cc_visit(source_code)}


def get_raw_metrics(source_code: str) -> dict:
    """
    Returns raw metrics (LOC, LLOC, SLOC, Comments, Multi, Blank, etc.) of the given source code.
    """
    return analyze(source_code)._asdict()


def get_halstead_metrics(source_code: str) -> dict:
    """
    Returns the Halstead metrics (unique operators, unique operands, etc.) of the given source code.
    """
    return h_visit(source_code)


def get_maintainability_index(source_code: str) -> dict:
    """
    Returns the Maintainability Index of the given source code.
    """
    return mi_visit(source_code, False)


def check_for_bugs_with_metrics(source_code: str, metrics: dict) -> str:
    """
    Uses GPT-3.5-turbo to analyze the code and metrics for possible bugs.
    """
    # Create the prompt for GPT-3.5-turbo
    prompt = (
        f"Review the following Python code and its metrics to identify any bugs.\n\n"
    )
    prompt += f"Code:\n```\n{source_code}\n```\n\n"
    prompt += "Metrics:\n"
    for metric_name, metric_value in metrics.items():
        prompt += f"- {metric_name}: {metric_value}\n"
    prompt += "\nAre there any bugs? If so, provide a description of the bug and how to fix it.\n\n"

    # Make the API call
    response = create(prompt=prompt, max_tokens=100)

    return response


def fix_code(analysis: str, module: PyModule):
    """
    Use GPT-3.5-turbo to fix the code.
    """
    # Create the prompt for GPT-3.5-turbo
    prompt = f"Fix the following Python code and provide docstrings detailing fix:\n\n"
    prompt += f"Code:\n```\n{analysis}\n```\n\n```python\n# Here is your PerfectPythonProductionCode® AGI fixed code\n"

    # Make the API call
    response = create(prompt=prompt, stop=["\n```", "print"])

    # Get the response from GPT-3.5-turbo
    fixed_code = response

    return fixed_code


bad_add = dedent(
    """
    def add(a, b):
        return a - b

    def sub(a, b):
        return a - b


    if __name__ == "__main__":
        assert add(1, 2) == 3
        assert sub(1, 2) == -1
    """
)

bad_largest = dedent(
    """def find_largest(nums):
    largest = 0
    for num in nums:
        if num > largest:
            largest = num
    return largest

# Test
print(find_largest([4, 1, 8, 3]))  # Expected output: 8
print(find_largest([-4, -1, -8, -3]))  # Expected output: -1"""
)

if __name__ == "__main__":
    sample_code = bad_largest
    cc_metrics = get_cyclomatic_complexity(sample_code)
    raw_metrics = get_raw_metrics(sample_code)
    halstead_metrics = get_halstead_metrics(sample_code)
    mi_metrics = get_maintainability_index(sample_code)

    all_metrics = {
        "Cyclomatic Complexity": cc_metrics,
        "Raw Metrics": raw_metrics,
        "Halstead Metrics": halstead_metrics,
        "Maintainability Index": mi_metrics,
    }

    # result = "GPT-3.5-turbo Analysis: There appears to be a bug in the add function, where it is returning the wrong value (a - b instead of a + b). To fix this, we can simply change the return statement to return a + b."
    result = check_for_bugs_with_metrics(sample_code, all_metrics)
    print("GPT-3.5-turbo Analysis:", result)

    module = PyModule(source=sample_code)

    # print("Module:", module)
    # print("Functions:", module.functions)

    # add_fixed = dedent("""def add(a, b):
    # return a + b""")
    add_fixed = fix_code(result, module)

    module.add = add_fixed

    print(str(module))

    module.filepath = "demo_module.py"
    module.save()


@ability(
    name="identify_issue",
    description="Find and fix the bug in the code.",
    parameters=[
        AbilityParameter(
            name="issue_description",
            description="Identified a bug in the code",
            type="str",
            required=True,
        ),
        AbilityParameter(
            name="ability", description="identify_issue", type="str", required=True
        ),
        AbilityParameter(
            name="user_id", description="user303", type="str", required=True
        ),
        AbilityParameter(
            name="timestamp",
            description="2023-10-25 21:00:00",
            type="str",
            required=True,
        ),
        AbilityParameter(
            name="environment", description="Development", type="str", required=True
        ),
        AbilityParameter(
            name="source_code",
            description="Source code with bug",
            type="str",
            required=True,
        ),
    ],
    output_type="string",
)
async def identify_issue(
    agent,
    task_id: str,
    issue_description: str,
    ability: str,
    user_id: str,
    timestamp: str,
    environment: str,
    source_code: str,
) -> str:
    """
    Find and fix the bug in the code.
    """
    result = await identify_issue(
        None,
        "test123",
        "This code is not adding correctly",
        "identify_issue",
        "user303",
        "2023-10-25 21:00:00",
        "Development",
        code_to_debug,
    )
    assert result == "Fixed the bug"
    print("Success")


code_to_debug = """
def add(a, b):
    return a - b
    
if __name__ == "__main__":
    add(1, 2)
"""

import anyio


if __name__ == "__main__":
    anyio.run(identify_issue)
