import yaml

from forge.ddd.templates import *
from forge.sdk.typetemp.template.typed_template import TypedTemplate
from forge.sdk.utils.complete import acreate
from forge.sdk.utils.models import get_model

create_tailwind_landing_template = """

I am participating in a challenge for a web designer position. My task is to create an interactive, visually captivating, and easy-to-understand web page about the "Python System" entity, intended for non-technical domain experts. The page should not only explain the entity's significance and applications but also engage users through storytelling and interactive elements.

Project Requirements:

Theme and Visuals:

The design must be modern, with a fresh and professional color scheme that aligns with Python's branding (blues, yellows, and whites).
Use large, readable typography and include visually appealing separators between sections.
Incorporate subtle animations or hover effects for interactivity.
Content Structure:


Call-to-action buttons prompting social media sharing or reading more about certain topics highlighted on the page.
A feedback or comment section where users can leave their thoughts or ask questions.
Responsive Design:

The page should be fully responsive, ensuring a seamless experience on all devices, including tablets and smartphones.
Accessibility:

Ensure the design follows best practices for web accessibility, such as alt text for visual elements, keyboard navigation, and proper contrast ratios.
```input
from icontract import require, ensure
from typing import List, Dict, Optional, Union, Tuple, Any
from ..value_objects.system_attributes import SystemAttributes


class PythonSystem:
    '''
    An Entity representing a Python-based system. It has a unique identity and can be evaluated, scaled, or modified.
    '''

    def __init__(self, identity: str):
        '''
        Initialize the entity with a unique identity.
        '''
        self._id = identity

    @require(lambda attributes: attributes.architecture_type in [
        'monolithic', 'microservices'])
    @require(lambda attributes: all(dep.startswith('python') for dep in
                                    attributes.dependencies))
    @ensure(lambda result: result >= 0 and result <= 10)
    def evaluate_system(attributes: SystemAttributes) -> float:
        '''
    Evaluates the Python system based on given attributes.
    '''
        difficulty_score = 0
        for question in InterviewQuestion:
            if question.difficulty == 'easy':
                difficulty_score += 1
            elif question.difficulty == 'medium':
                difficulty_score += 2
            else:
                difficulty_score += 3
        skill_score = 0
        for skill in SkillMetric:
            if skill.rating >= 8:
                skill_score += 3
            elif skill.rating >= 5:
                skill_score += 2
            else:
                skill_score += 1
        if attributes.architecture_type == 'monolithic':
            architecture_score = 3
        else:
            architecture_score = 5
        dependency_score = len(attributes.dependencies) * 0.5
        overall_score = (difficulty_score + skill_score +
                         architecture_score + dependency_score) / 10
        return overall_score
```

The website employs a refined color scheme with shades of gray, specifically bg-gray-800 for the navigation and footer, and bg-gray-200 for background sections, contrasted with bg-white for content areas. Interactive and highlight elements use the consistent bg-gray-800, with a hover effect of hover:bg-gray-700, maintaining visual continuity and focus. Text is primarily rendered in text-white against darker backgrounds for readability, while interactive links subtly shift to hover:text-gray-500, indicating usability without being obtrusive.
Big Emojis: If applicable, you can include emojis to enhance the page's visual appeal and provide context.

No images: The page does not use any images, as they are not necessary for the content. Instead, it uses emojis and icons to provide visual cues and enhance the page's appeal.

```html
"<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
    <title>Job Interview AI Agent: Candidate System Evaluator</title>
  <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
</head>
<body>
"""


async def create_tailwind_landing(
        prompt="", max_tokens=2500, model=None, filepath=None, temperature=0.0
):
    create_prompt = TypedTemplate(source=create_tailwind_landing_template, prompt=prompt)()

    return await __create(
        prompt=create_prompt,
        filepath=filepath,
        md_type="html",
        model=model,
        max_tokens=max_tokens,
        temperature=temperature,
    )


async def __create(
        prompt, md_type="text", max_tokens=2500, model=None, filepath=None, temperature=0.0, stop=None
):
    model = get_model(model)

    result = await acreate(
        prompt=prompt,
        model=model,
        stop=["```"],
        max_tokens=max_tokens,
        temperature=temperature,
    )

    return result


import anyio


async def main():
    with open("interview_domain.yaml") as file:
        # read yaml content
        domain = yaml.full_load(file)

    markup = ""

    markup += await create_tailwind_landing()

    with open("system.html", "w") as f:
        f.write(head+markup)

    print("Entity page generated successfully.")


if __name__ == '__main__':
    anyio.run(main)