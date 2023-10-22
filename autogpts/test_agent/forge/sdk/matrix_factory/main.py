import time

from lchop.context.work_context import default_work_context, load_workflow

from lchop.tasks.gen_email_tasks import *

async def main():
    work_ctx = default_work_context()

    await load_workflow(work_ctx, "workflow.yaml")
    print(work_ctx.task_ctx.results)


if __name__ == "__main__":
    import asyncio

    # start and end time in seconds
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f"Time elapsed: {end - start}")
