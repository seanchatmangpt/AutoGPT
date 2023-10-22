import loguru

from fgn.completion.chat import achat
from fgn.completion.complete import acreate
from matrix_factory.afile import write
from matrix_factory.chat_helpers import best_models, ok_models, gpt_4_models


async def create_domain_model_from_yaml(prompt, max_tokens=2500, model="gpt4", filepath=None):
    model = get_model(model)

    yaml_prompt = f"""
    Objective:
    Create a non-anemic Python domain model from a YAML formatted input that describes a module and its features. The
    domain model should embody the Pythonic principles advocated by Luciano Rahmalo in "Fluent Python", the domain-driven
    design insights of Vernon Vaughn from "Implementing Domain Driven Design", and the pragmatic wisdom of David Thomas
    and Andrew Hunt from "The Pragmatic Programmer".

    Sample Input:
    ```yaml
    OnlineContractAdminCapability:
      overview_description: "Welcome to the Contract Administration Capability of My Application."
      features:
        - "Dashboard with Contract Metrics (e.g., approval rates, pending reviews)"
        - "Interactive Contract Query Tool with Natural Language Processing"
        - "Tolerance and Compliance Rule Management"
        - "Stack Management with Label Customization"
        - "Automatic and Manual Tolerance Adjustments"
        - "Contract Health Monitoring and Reporting"
    ```

    Jinja Template:
    ```python
    from dataclasses import dataclass

    @dataclass
    class Contract:
        contract_id: str
        contract_name: str
        metrics: List[ContractMetric]
        approval_rates: List[ApprovalRate]
        pending_reviews: List[PendingReview]
        health_monitor: HealthMonitor
        is_active: bool
        has_been_approved: bool


        def view_metrics(self):
            pass
            
        def user_has_approved(self):
            pass
            
        def close_contract(self):
            pass
            
        etc... 
    ```

    User Requirement Input:
    {prompt}
    
    """
    return await __chat(prompt=yaml_prompt, md_type="python", model=model, max_tokens=max_tokens, filepath=filepath)


async def create_yaml(prompt, max_tokens=2500, model=None):
    model = get_model(model)

    yaml_prompt = f"""
    Objective:
    Transform the given input (whether it's Python code, project documentation, or another form of structured data) into a YAML format.

    GIVEN INPUT:
    {prompt}

    GIVEN OUTPUT:
    """
    return await __create(prompt=yaml_prompt, md_type="python", model=model, max_tokens=max_tokens)


async def create_python(prompt, max_tokens=2500, model=None, filepath=None, temperature=0.0):
    model = get_model(model)

    python_prompt = f"""
Objective:
Transform the given input (whether it's Python code, project documentation, or another form of structured data) 
into PYTHON CODE that aligns with the Pythonic practices Luciano Ramalho would advocate for based on his 
teachings in "Fluent Python". Ensure it's idiomatic, concise, and leverages Python's features effectively.


GIVEN INPUT:
{prompt}

GIVEN OUTPUT:"""
    return await __create(prompt=python_prompt,
                          filepath=filepath, md_type="python",
                          model=model, max_tokens=max_tokens, temperature=temperature)


async def __create(prompt, md_type="text", max_tokens=2500, model=None, filepath=None, temperature=0.0):
    model = get_model(model)

    prompt = f"""{prompt}
```{md_type}
    """

    result = await acreate(prompt=prompt, model=model, stop=["```"], max_tokens=max_tokens, temperature=temperature)
    loguru.logger.info(f"Prompt: {result}")
    loguru.logger.info(f"Result: {result}")

    if filepath:
        await write(contents=result, filename=filepath)

    return result


async def __chat(prompt, md_type="text", max_tokens=2500, model=None, filepath=None, temperature=0.0):
    model = get_model(model)

    prompt = f"""{prompt}
```{md_type}
    """

    result = await achat(prompt=prompt, model=model)
    loguru.logger.info(f"Prompt: {result}")
    loguru.logger.info(f"Result: {result}")

    if filepath:
        await write(contents=result, filename=filepath)

    return result


def round_robin_gpt_4_models():
    idx = 0
    while True:
        yield gpt_4_models[idx % len(gpt_4_models)]
        idx += 1


def round_robin_best_models():
    idx = 0
    while True:
        yield best_models[idx % len(best_models)]
        idx += 1


def round_robin_ok_models():
    idx = 0
    while True:
        yield ok_models[idx % len(ok_models)]
        idx += 1


def get_model(model):
    if model == "best":
        return next(round_robin_best_models())
    elif model == "ok":
        return next(round_robin_ok_models())
    elif not model:
        return next(round_robin_best_models())
    elif model == "gpt4":
        return next(round_robin_gpt_4_models())
    else:
        return model
