import yaml

from forge.ddd.templates import *
from forge.sdk.typetemp.template.typed_template import TypedTemplate
from forge.sdk.utils.complete import acreate
from forge.sdk.utils.models import get_model

create_tailwind_landing_template = """

Generate a sophisticated and polished Tailwind CSS page 
Imagine you are participating in an expert web designer job interview challenge. Your task is to create a visually engaging web page that effectively represents the essence of the provided Python entity. This web page is intended for non-technical domain experts who are interested in understanding the entity's purpose and significance.

Design a web page with a layout and style that closely resembles the provided template but without including any code 
or technical markup. Replace the template's placeholders with relevant, non-technical content related to the Python 
entity. Your goal is to showcase the entity's importance and uniqueness to the non-technical audience in a visually 
appealing and user-friendly way.

This challenge is an opportunity to demonstrate your web design skills and your ability to communicate complex concepts in a clear and visually appealing manner. The final web page should serve as a concise and informative representation of the Python entity, highlighting its value and significance for non-technical individuals.


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

Styling: Ensure that the styling adheres to modern UI/UX principles. Pay attention to fonts, colors, spacing, and alignment to make the page visually appealing.

Images & Emojis: If applicable, you can include images and emojis to enhance the page's visual appeal and provide context. 

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

    print("Landing page generated successfully.")


if __name__ == '__main__':
    anyio.run(main)