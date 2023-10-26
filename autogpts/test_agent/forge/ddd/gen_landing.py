import yaml

from forge.ddd.templates import *
from forge.sdk.typetemp.template.typed_template import TypedTemplate
from forge.sdk.utils.complete import acreate
from forge.sdk.utils.models import get_model

create_tailwind_landing_template = """
Generate a sophisticated and polished Tailwind CSS landing page that is intended as a job interview sample 
for a position in web development. The landing page should be optimized for high conversion rates and be 
tailored for a platform that offers an AI-based job interview coaching service. 

Incorporate the following elements:

1. A fixed navigation bar at the top, including links to Home, Features, Testimonials, and Contact Us.

2. A hero section that captivates attention and provides a brief overview of what the AI-based job interview 
coaching service does. Include a compelling headline and a strong call-to-action button.

3. A Features section that uses cards to showcase at least three key features of the service. Each card
 should have an icon, a headline, and a short description.

4. A Testimonials section featuring quotes from satisfied customers to build credibility. Display at least 
three testimonials and include an image for each person giving the testimonial, if possible.

5. A Footer that includes basic contact information, social media links, and any legal disclaimers or privacy policy links.

For each of these sections, employ modern UI/UX principles such as contrasting colors for readability, 
consistent spacing and padding, and mobile responsiveness. Aim to create a design that is both visually 
appealing and highly functional to impress during the job interview.


```input
{{prompt}}
```

```html
"""


async def create_tailwind_landing(
        prompt, max_tokens=2500, model=None, filepath=None, temperature=0.0
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

    landing = await create_tailwind_landing(domain["additional_info"]["site_description"])

    markup = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Job Interview AI Agent</title>
  <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
</head>
<body>"""
    markup += landing

    with open("index.html", "w") as f:
        f.write(markup)

    print("Landing page generated successfully.")


if __name__ == '__main__':
    anyio.run(main)