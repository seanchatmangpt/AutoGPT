import yaml
from loguru import logger
from munch import Munch

from lchop.context.agent_context import AgentContext
from lchop.context.browser_context import BrowserContext
from lchop.context.state_context import StateContext
from lchop.context.step_context import StepContext
from lchop.context.template_context import TemplateContext

class WorkContext:
    globals()

    def __init__(
        self,
        step_ctx: StepContext,
        template_ctx: TemplateContext,
        browser_ctx: BrowserContext,
        agent_ctx: AgentContext,
        state_ctx: StateContext,
    ):
        self.step_ctx = step_ctx
        self.template_ctx = template_ctx
        self.browser_ctx = browser_ctx
        self.agent_ctx = agent_ctx
        self.state_ctx = state_ctx
        self.global_params = Munch()
        logger.info("WorkContext initialized.")


async def inject_steps(workflow_config, work_ctx):
    logger.info("Attempting to identify and execute 'load_workflow' steps...")

    load_workflow_indices = [
        index
        for index, step in enumerate(workflow_config.workflow)
        if step.name == "load_workflow"
    ]

    if not load_workflow_indices:
        logger.info("'load_workflow' steps not found. Skipping injection.")
        return

    for index in reversed(load_workflow_indices):
        step = workflow_config.workflow[index]
        filepath = step.params.get("path")

        if not filepath:
            logger.error("'load_workflow' step found, but no filepath specified.")
            raise ValueError("YAML path for 'load_workflow' is not specified.")

        try:
            with open(filepath, "r") as stream:
                new_workflow_config = Munch.fromDict(yaml.safe_load(stream))
                logger.info(f"Successfully loaded new workflow from {filepath}")

            workflow_config.workflow[index : index + 1] = new_workflow_config[
                "workflow"
            ]
            logger.info(
                f"Injection complete. 'load_workflow' step at index {index} replaced by steps from {filepath}"
            )

        except Exception as e:
            logger.error(
                f"Failed to load or inject new workflow from {filepath}. Exception: {str(e)}"
            )
            raise Exception(f"Failed to load or inject new workflow. Aborting.") from e


async def exe_step(step_config, work_ctx):
    func_name = None
    if hasattr(step_config, "func"):
        func_name = step_config.func
    else:
        func_name = step_config.name
    func_desc = step_config.get("description", "No Description")

    logger.info(f"Executing {func_name}: {func_desc}")

    implementation = work_ctx.step_ctx.steps[func_name]
    global_params = work_ctx.global_params
    params = step_config.get("params", {})
    params["work_ctx"] = work_ctx
    params.update(work_ctx.__dict__)
    params.update(global_params)
    result = await implementation(**params)

    logger.info(f"Step {func_name} completed with result: {result}")

    work_ctx.step_ctx.results[func_name] = result
    work_ctx.step_ctx.results_list.append(result)

    return result


async def exe_workflow(workflow_config, work_ctx):
    logger.info("Starting workflow execution.")

    await inject_steps(workflow_config, work_ctx)

    for step_config in workflow_config.workflow:
        step_result = await exe_step(step_config, work_ctx)

        if not step_result["success"]:
            logger.error(
                f"Step {step_config['name']} ({step_config['func']}) failed. Stopping workflow."
            )
            return False

    logger.info(f"Results: {len(work_ctx.step_ctx.results.keys())}")
    logger.info("Workflow execution completed.")
    return True


async def load_workflow(work_ctx=None, filepath=None, yaml_string=None):
    if not work_ctx:
        work_ctx = default_work_context()
    if not filepath and not yaml_string:
        raise ValueError("Either filepath or yaml_string must be specified.")
    if yaml_string:
        workflow_config = Munch.fromDict(yaml.safe_load(yaml_string))
        work_ctx.global_params.update(workflow_config.get("global_params", {}))
        return await exe_workflow(workflow_config, work_ctx)
    with open(filepath, "r") as stream:
        try:
            workflow_config = Munch.fromDict(yaml.safe_load(stream))
            work_ctx.global_params.update(workflow_config.get("global_params", {}))
            return await exe_workflow(workflow_config, work_ctx)
        except yaml.YAMLError as e:
            logger.error(f"Error loading YAML file: {e}")


def default_work_context():
    return WorkContext(
        StepContext(),
        TemplateContext(),
        BrowserContext(),
        AgentContext(),
        StateContext(),
    )
