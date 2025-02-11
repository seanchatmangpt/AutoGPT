from dataclasses import dataclass

import yaml


from forge.sdk.lchop.context.task_context import register_task
from forge.sdk.typetemp.template.typed_template import TypedTemplate


@dataclass
class NewTypedTemplate(TypedTemplate):
    message: str = None
    source = "Hello, {{ message }}"


@register_task
async def type_temp(work_ctx, message="Hello, World!", **kwargs):
    temp = NewTypedTemplate(message=message)
    return {"success": True, "results": f"Successfully templated: {temp()}"}


@register_task
async def generate_task_code_from_workflow(
    work_ctx, workflow_path, task_code_path, **kwargs
):
    with open(workflow_path, "r") as stream:
        workflow_config = yaml.safe_load(stream)

    rendered = work_ctx.template_ctx.render_file_template(
        "/Users/candacechatman/dev/linkml-projects/matrix-factory/src/lchop/tasks/task_function_template.j2",
        workflow=workflow_config.get("workflow"),
    )

    with open(task_code_path, "w") as f:
        f.write(rendered)

    return {
        "success": True,
        "results": f"Successfully generated code in {task_code_path}",
    }
