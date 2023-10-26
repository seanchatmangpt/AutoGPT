from typing import NamedTuple

from forge.sdk.utils.create_prompts import create_python


# Define a CodeAttributes named tuple for storing code-related information
class CodeAttributes(NamedTuple):
    language: str
    problem_statement: str
    performance_requirements: str
    readability_requirements: str
    domain: str


class CodeGenerationHypothesisGeneratorAGI:
    def generate_hypothesis(self, attributes: CodeAttributes) -> str:
        # Utilize insights from Fluent Python for Python-specific optimizations
        hypothesis = ""
        if attributes.language.lower() == "python":
            hypothesis = "The code will be Pythonic and take advantage of Python-specific features for readability and performance. "

        # Utilize insights from The Pragmatic Programmer for best practices
        hypothesis += "The code will be modular and maintainable, as advocated by The Pragmatic Programmer. "

        # Adding problem-specific hypothesis
        hypothesis += f"For the specific problem of {attributes.problem_statement}, the code will aim to fulfill the following performance requirements: {attributes.performance_requirements} and readability requirements: {attributes.readability_requirements}. "

        # Mention the domain if it adds value to the hypothesis
        if attributes.domain:
            hypothesis += f"This will be particularly tailored for the {attributes.domain} domain."

        return hypothesis


import anyio

async def main():
    code_attributes = CodeAttributes(
        language="Python",
        problem_statement="sorting an array",
        performance_requirements="O(n log n)",
        readability_requirements="high",
        domain="algorithmic tasks"
    )

    generator = CodeGenerationHypothesisGeneratorAGI()
    hypothesis = generator.generate_hypothesis(code_attributes)

    code = await create_python(hypothesis)

    print(code)


if __name__ == '__main__':
    anyio.run(main)
