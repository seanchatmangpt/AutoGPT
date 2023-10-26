from dataclasses import dataclass
from typing import List

import yaml

from forge.sdk.typetemp.template.typed_template import TypedTemplate
from forge.sdk.utils.complete import acreate
from forge.sdk.utils.create_prompts import __create
from forge.sdk.utils.models import get_model
from gen_entities import generate_reporting_system_entities
from gen_web_crud import generate_web_crud



@dataclass
class FlaskAppTemplate(TypedTemplate):
    entities: List[str] = None
    to: str = "./app.py"
    source = """
from flask import Flask, render_template
{% for entity in entities %}
from web.routes.{{ entity }}Routes import app as {{ entity.lower() }}_app
{% endfor %}

app = Flask(__name__)

{% for entity in entities %}
app.register_blueprint({{ entity.lower() }}_app, url_prefix='/{{ entity.lower() }}')
{% endfor %}

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    """


def generate_app():

    # open yaml file
    with open("interview_domain.yaml") as file:
        # read yaml content
        entities = yaml.full_load(file)

    entity_names = [entity.get("name") for entity in entities["entities"]]

    generate_reporting_system_entities(entity_names)

    # Generate web CRUD interfaces
    generate_web_crud(entity_names)

    # Create Flask App using the defined entities
    flask_app_template = FlaskAppTemplate(entities=entity_names)
    flask_app_template()

    # create_init_files()

    print("Flask app generated successfully.")


def main():
    # Run the function to generate the Flask app
    generate_app()


create_tailwind_landing_template = """
Generate a sophisticated and polished Tailwind CSS landing page that is intended as a  sample 
for a position in web development. The landing page should be optimized for high conversion rates and be 
tailored for a platform that offers an AI-based service. 

Incorporate the following elements:

1. A fixed navigation bar at the top, including links to Home, Features, Testimonials, and Contact Us.
  
2. A hero section that captivates attention and provides a brief overview of what the AI-based service does. Include a compelling headline and a strong call-to-action button.

3. A Features section that uses cards to showcase at least three key features of the service. Each card
 should have an icon, a headline, and a short description.

4. A Testimonials section featuring quotes from satisfied customers to build credibility. Display at least 
three testimonials and include an image for each person giving the testimonial, if possible.

5. A Footer that includes basic contact information, social media links, and any legal disclaimers or privacy policy links.

For each of these sections, employ modern UI/UX principles such as contrasting colors for readability, 
consistent spacing and padding, and mobile responsiveness. Aim to create a design that is both visually 
appealing and highly functional to impress


# Venture Capital Domain Model

# Entities represent objects with a distinct identity that carries significance within the Venture Capital ecosystem.
entities:
  - name: Startup
    definition: An Entity representing a startup company seeking funding. It has a unique identity, business model, and funding requirements.
  
  - name: VentureCapitalist
    definition: An Entity representing an individual or firm that provides capital to startups with high growth potential in exchange for equity, or partial ownership of the company.

  - name: InvestmentRound
    definition: An Entity that represents a stage of financing where multiple investors provide capital to a startup, typically in exchange for equity.

# Value Objects represent elements with attributes but no distinct identity.
value_objects:
  - name: InvestmentTerms
    definition: A Value Object encapsulating the terms of an investment, including equity offer, valuation, and amount invested.
    properties:
      - name: equity_percentage
        type: float
      - name: valuation
        type: float
      - name: capital_invested
        type: float

  - name: StartupProfile
    definition: A Value Object representing a comprehensive overview of a startup's business model, team, and market opportunity.
    properties:
      - name: business_model_description
        type: str
      - name: team_members
        type: List[str]
      - name: market_size
        type: float

# Business functions for Entities and Value Objects in the Venture Capital domain.
business_functions:
  - entity: VentureCapitalist
    name: evaluateInvestment
    parameters:
      - parameter: startup
        type: Startup
      - parameter: terms
        type: InvestmentTerms
    definition: Assesses the viability and potential return on an investment in a particular startup based on the specified terms.
    contract:
      pre:
        - condition: "lambda startup, terms: startup is not None"
        - condition: "lambda startup, terms: terms is not None"
      post:
        - condition: "lambda result: result is not None"

  - entity: Startup
    name: seekInvestment
    parameters:
      - parameter: investment_round
        type: InvestmentRound
    definition: Initiates a process to secure funding from potential investors in a specific investment round.
    contract:
      pre:
        - condition: "lambda investment_round: investment_round is not None"
      post:
        - condition: "lambda result: result is not None"

# Additional information or metadata relevant to the domain.
additional_info:
  important_note: In the Venture Capital Domain, interactions between entities involve high-stakes investment decisions. Thus, due diligence and rigorous assessment practices are integral to the business functions defined here. Business functions adhere to a Design by Contract (DbC) approach to ensure each function's integrity and the validity of its interactions.

  domain_description: "In the realm of Venture Capital, we facilitate the symbiotic growth of innovative startups and investment entities. Startups can articulate their value propositions, growth potential, and funding requirements, attracting investors aligned with their vision. Venture capitalists, angel investors, and investment firms can explore a plethora of vetted, high-potential startups to diversify their investment portfolios, contribute to groundbreaking innovations, and achieve substantial returns on investment. Through structured investment rounds, transparent communication, and strategic guidance, we forge lasting partnerships between investors and entrepreneurs, fueling economic growth and technological advancement."

```input
{{prompt}}
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Venture Capital</title>
  <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
</head>
<body>"""


async def create_tailwind_landing(
    prompt, max_tokens=2500, model=None, filepath=None, temperature=0.9
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
  <title>Venture Capital Management GPT</title>
  <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
</head>
<body>"""
    markup += landing

    with open("index.html", "w") as f:
        f.write(markup)

    print("Landing page generated successfully.")


if __name__ == '__main__':
    anyio.run(main)

