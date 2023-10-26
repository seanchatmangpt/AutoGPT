from typing import NamedTuple, List

from forge.CodeGenerationHypothesisGeneratorAGI import CodeAttributes, CodeGenerationHypothesisGeneratorAGI
from forge.CodeGenerationInformationNeedsSatisficingChecker import CodeGenerationInformationNeedsSatisficingChecker


# Define a JobInterviewAttributes named tuple for storing job interview code-related information
class JobInterviewAttributes(NamedTuple):
    languages: List[str]
    problem_domain: str
    complexity_level: str
    duration: int  # Time allowed to solve the problem in minutes


from forge.sdk.utils.create_prompts import create_python
import anyio


class ExpertJobInterviewSourceCodeExampleGeneratingAGI:
    async def generate_example(self, attributes: JobInterviewAttributes) -> str:
        # Utilize insights from Fluent Python for Python-specific optimizations
        hypothesis = ""

        if "python" in attributes.languages:
            hypothesis = "The code will be Pythonic and leverage Python's rich feature set for an optimized solution. "

        # Utilize insights from The Pragmatic Programmer for best practices
        hypothesis += "The code will follow best practices in software development, as suggested by The Pragmatic Programmer. "

        # Adding problem-specific hypothesis
        hypothesis += f"The problem domain is {attributes.problem_domain} and the complexity level is {attributes.complexity_level}. "

        # If duration is provided, consider it in the hypothesis
        if attributes.duration:
            hypothesis += f"The candidate should ideally solve the problem within {attributes.duration} minutes. "

        # Generate the example code based on this hypothesis
        example_code = await create_python(hypothesis)  # Assuming create_python generates code based on the hypothesis

        return example_code


# Asynchronous main function
async def main():
    job_interview_attributes = JobInterviewAttributes(
        language=["Python"],
        problem_domain="Data Structures",
        complexity_level="Medium",
        duration=30  # 30 minutes
    )

    generator = ExpertJobInterviewSourceCodeExampleGeneratingAGI()
    example_code = await generator.generate_example(job_interview_attributes)

    print(example_code)



# Asynchronous main function
async def main():
    # Generate Hypothesis for a Next.js app with FastAPI backend
    code_attributes = CodeAttributes(
        language="JavaScript",
        problem_statement="Creating a Next.js app with FastAPI backend",
        performance_requirements="Highly responsive UI",
        readability_requirements="High",
        domain="Web Development"
    )
    code_attributes2 = CodeAttributes(
        language="Python",
        problem_statement="FastAPI backend",
        performance_requirements="low-latency API",
        readability_requirements="High",
        domain="Web Development"
    )
    hypothesis_gen = CodeGenerationHypothesisGeneratorAGI()
    hypothesis_js = hypothesis_gen.generate_hypothesis(code_attributes)
    hypothesis_py = hypothesis_gen.generate_hypothesis(code_attributes2)
    print(f"Hypothesis: {hypothesis_js}")
    print(f"Hypothesis: {hypothesis_py}")

    # Generate Job Interview Example for Full-stack development
    job_interview_attributes = JobInterviewAttributes(
        languages=["JavaScript", "Python"],
        problem_domain=hypothesis_py,
        complexity_level="Medium",
        duration=60  # 60 minutes
    )
    job_interview_gen = ExpertJobInterviewSourceCodeExampleGeneratingAGI()
    job_interview_example = await job_interview_gen.generate_example(job_interview_attributes)
    print(f"Job Interview Example: {job_interview_example}")

    # Check Satisficing
    checker = CodeGenerationInformationNeedsSatisficingChecker()
    result = checker.check_satisficing(
        "Create a Next.js app with FastAPI backend",
        [job_interview_example],  # Assuming this contains the generated code
        {"Domain": "Web Development", "Languages": ["JavaScript", "Python"]}
    )
    if result["satisficed"]:
        print("The code generated satisfies the user's needs.")
    else:
        print("The code generated does not satisfy the user's needs. Feedback:", result["feedback"])

# Run the asynchronous main function
if __name__ == "__main__":
    anyio.run(main)
