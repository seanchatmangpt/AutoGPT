import requests

from forge.sdk.abilities.registry import ability, AbilityParameter


@ability(
    name="fetch_webpage",
    description="Retrieve the content of a webpage",
    parameters=[
        AbilityParameter(name="url", description="Webpage URL", type="string", required=True)
    ],
    output_type="string",
)
async def fetch_webpage(agent, task_id: str, url: str) -> str:
    response = requests.get(url)
    return response.text
