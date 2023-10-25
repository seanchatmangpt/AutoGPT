# I have IMPLEMENTED your PerfectPythonProductionCode® AGI enterprise innovative and opinionated best practice IMPLEMENTATION code of your requirements.
import logging
from collections import deque
from datetime import datetime
from functools import partial
from random import uniform
from typing import Any, Callable, Iterable, List, Optional

import anyio
import asyncstdlib
import icontract

logger = logging.getLogger(__name__)


@icontract.require(
    lambda task_fn: callable(task_fn), "The task function must be callable."
)
@icontract.require(
    lambda args_iterable: hasattr(args_iterable, "__iter__"),
    "The argument must be an iterable.",
)
@icontract.ensure(
    lambda result: isinstance(result, list), "The function must return a list."
)
async def run_in_parallel(
    task_fn: Callable[..., Any],
    args_iterable: Iterable[Any],
    *,
    max_workers: Optional[int] = None,
    worker_name: Optional[str] = None,
    **kwargs: Any,
) -> List[Any]:
    """
    Executes the task function concurrently for each argument in the args_iterable using anyio.

    Preconditions:
    - task_fn must be callable.
    - args_iterable must be iterable.

    Postconditions:
    - Must return a list of results.

    Args:
        task_fn (Callable[..., Any]): The asynchronous function to run.
        args_iterable (Iterable[Any]): An iterable of arguments to pass to task_fn.
        max_workers (Optional[int]): The maximum number of concurrent workers.
        worker_name (Optional[str]): A name for logging purposes.
        **kwargs: Keyword arguments to pass to task_fn.

    Returns:
        List[Any]: A list containing the results from each call to task_fn.
    """
    responses = {}
    ordered_indices = (
        deque()
    )  # Use a deque to keep track of the order of the task indices.
    task_fn_with_kwargs = partial(task_fn, **kwargs)

    async def worker(index: int, arg: Any) -> None:
        """Inner worker function for task execution."""
        try:
            result = await task_fn_with_kwargs(arg)
            responses[index] = result
            ordered_indices.append(
                index
            )  # Store the task index to maintain original order.
        except Exception as e:
            logger.error(f"Worker {worker_name or ''} failed for index {index}: {e}")
            responses[index] = None

    async with anyio.create_task_group() as tg:
        async for index, arg in asyncstdlib.enumerate(args_iterable):
            tg.start_soon(worker, index, arg)

    # Return responses in the original order
    return [responses[i] for i in sorted(ordered_indices)]


async def download_file(url: str, target_folder: str) -> None:
    sleep_time = uniform(0.1, 0.9)  # Random sleep time between 0.1 to 0.9 seconds
    await anyio.sleep(sleep_time)
    print(f"Downloaded {url} to {target_folder} in {sleep_time} seconds")


async def main():
    urls = [
        "http://example.com/file1.zip",
        "http://example.com/file2.zip",
        "http://example.com/file3.zip",
    ]
    target_folder = "downloads"
    start_time = datetime.now()

    await run_in_parallel(download_file, urls, target_folder=target_folder)

    end_time = datetime.now()
    print(f"Finished at {end_time - start_time}")


# Assuming you've imported run_in_parallel function here
anyio.run(main)
