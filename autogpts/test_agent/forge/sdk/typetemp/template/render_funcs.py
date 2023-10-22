from typing import Any

from ..environment.typed_environment import environment
from ..environment.typed_native_environment import native_environment


def render_str(source, env=environment, **kwargs) -> str:
    template = env.from_string(source)

    return template.render(**kwargs)


def render_py(source, env=native_environment, **kwargs) -> Any:
    template = env.from_string(source)

    return template.render(**kwargs)
