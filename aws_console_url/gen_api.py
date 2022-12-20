# -*- coding: utf-8 -*-

"""
Automatically generate the api.py file
"""

import importlib
from pathlib import Path
from aws_console_url.builder import Builder

dir_here = Path(__file__).absolute().parent
dir_srv = dir_here / "srv"
path_api_py = dir_here / "api.py"

for path in dir_srv.glob("*.py"):
    if path.name == "__init__.py":
        continue
    module_name = path.stem
    module = importlib.import_module(f"aws_console_url.srv.{module_name}")

subclasses = sorted(
    Builder.__subclasses__(),
    key=lambda subclass: subclass.__module__,
)
module_and_class_and_service_list = []
for subclass in subclasses:
    module_name = subclass.__module__.split(".")[-1]
    class_name = subclass.__name__
    service_name = subclass.SERVICE_NAME
    module_and_class_and_service_list.append((module_name, class_name, service_name))

lines = [
    "# -*- coding: utf-8 -*-",
    "",
    "import typing as T",
    "import dataclasses",
    "",
]

for module_name, class_name, _ in module_and_class_and_service_list:
    lines.append(f"from .srv.{module_name} import {class_name}")

lines.extend(
    [
        "",
        "",
        "@dataclasses.dataclass",
        "class AWSConsole:",
        "    is_us_gov_cloud: bool = dataclasses.field(default=False)",
        "    aws_account_id: T.Optional[str] = dataclasses.field(default=None)",
        "    aws_region: T.Optional[str] = dataclasses.field(default=None)",
        "",
    ]
)

for module_name, class_name, service_name in module_and_class_and_service_list:
    lines.append(f"    @property")
    lines.append(f"    def {module_name}(self) -> {class_name}:")
    lines.append(f"        return {class_name}(aws_service=\"{service_name}\")")
    lines.append("")

path_api_py.write_text("\n".join(lines))
