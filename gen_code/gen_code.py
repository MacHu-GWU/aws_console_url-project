# -*- coding: utf-8 -*-

"""
Automatically generate the api.py file
"""

import importlib
from pathlib import Path
from jinja2 import Template
from aws_console_url.builder import Builder

dir_here = Path(__file__).absolute().parent
dir_project_root = dir_here.parent
dir_srv = dir_project_root / "aws_console_url" / "srv"

for path in dir_srv.glob("*.py"):
    if path.name == "__init__.py":
        continue
    module_name = path.stem
    module = importlib.import_module(f"aws_console_url.srv.{module_name}")

subclasses = sorted(
    Builder.__subclasses__(),
    key=lambda subclass: subclass.__module__,
)
module_and_class_list = []
for subclass in subclasses:
    module_name = subclass.__module__.split(".")[-1]
    class_name = subclass.__name__
    module_and_class_list.append((module_name, class_name))


path_template = dir_here.joinpath("console.py.tpl")
template = Template(path_template.read_text())

path_console_py = dir_project_root / "aws_console_url" / "console.py"
path_console_py.write_text(template.render(module_and_class_list=module_and_class_list))
