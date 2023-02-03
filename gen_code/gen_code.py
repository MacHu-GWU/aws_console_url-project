# -*- coding: utf-8 -*-

"""
Automatically generate the api.py file
"""

import importlib
from pathlib import Path
from jinja2 import Template
from aws_console_url.model import Service, Resource

dir_here = Path(__file__).absolute().parent
dir_project_root = dir_here.parent
dir_srv = dir_project_root / "aws_console_url" / "srv"

for path in dir_srv.glob("*.py"):
    if path.name == "__init__.py":
        continue
    module_name = path.stem
    module = importlib.import_module(f"aws_console_url.srv.{module_name}")

# --- console
subclasses = sorted(
    Service.__subclasses__(),
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

# --- arn
subclasses = sorted(
    Resource.__subclasses__(),
    key=lambda subclass: subclass.__module__,
)
module_and_class_list = []
for subclass in subclasses:
    module_name = subclass.__module__.split(".")[-1]
    class_name = subclass.__name__
    module_and_class_list.append((module_name, class_name))

path_resource_py_template = dir_here.joinpath("resource.py.tpl")
template = Template(path_resource_py_template.read_text())
path_resource_py = dir_project_root / "aws_console_url" / "resource.py"
path_resource_py.write_text(template.render(module_and_class_list=module_and_class_list))