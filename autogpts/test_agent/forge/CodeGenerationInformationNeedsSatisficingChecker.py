import json

from forge.sdk.abilities.code.radon_workbench import fix_code, refactor_code
from forge.sdk.utils.complete import create  # Assuming the path is correct
from forge.sdk.utils.create_prompts import create_python


class CodeGenerationInformationNeedsSatisficingChecker:
    def check_satisficing(self, user_query, code_generation_results, notes):
        mission = '''You are a Code Generation Information Needs Satisficing Checker. 
        Your role is to specifically evaluate the sufficiency of the final code generated in fulfilling a user's 
        original requirement. Your evaluation should consider the bugs, edge cases, accuracy, efficiency, readability, 
        and completeness of the generated code. Unhandled edge cases are not bugs.'''

        output_format = '''Your output will be in JSON format and will consist of two main fields: `feedback` and `satisficed`. `Feedback` will assess whether the generated code is buggy, accurate, efficient, readable, and complete. `Satisficed` will be a Boolean value that signifies whether the generated code meets these criteria (edge cases considered in criteria). List all bugs not edge cases.'''

        prompt = f"{mission}\n\n{output_format}\n\nUser Query: {user_query}\nCode Generation Results: {code_generation_results}\nNotes: {notes}\n\n```json\n"

        feedback = create(prompt=prompt, stop=["```"])

        return json.loads(feedback)

bubble_sort_code = '''
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                return None
                # Swap elements
arr[j], arr[j + 1] = arr[j + 1], arr[j]
'''

import anyio

def main():
    checker = CodeGenerationInformationNeedsSatisficingChecker()

    result = checker.check_satisficing(
        "I need Python code for sorting",
        [bubble_sort_code],
        {"Domain": "Code Generation", "Language": "Python"}
    )


    if result["satisficed"]:
        print("The code generated satisfies the user's needs.")
    else:
        fixed = False
        new_code = bubble_sort_code
        while not fixed:
            new_code = refactor_code(f'{new_code}\nI need help fixing these bugs: {str(result["feedback"]["bugs"])}\n')

            print(new_code)

            result = checker.check_satisficing(
                "I need Python code for sorting",
                [new_code],
                {"Domain": "Code Generation", "Language": "Python"}
            )

            print(result)

            if result["satisficed"]:
                fixed = True
                print("The refactored code generated satisfies the user's needs.")


if __name__ == '__main__':
    main()
