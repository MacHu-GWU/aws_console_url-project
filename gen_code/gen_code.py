# -*- coding: utf-8 -*-

"""
Automatically generate the console.py and resource.py as the public API
"""

import typing as T
import inspect
import importlib
from pathlib import Path
from jinja2 import Template

from aws_console_url.model import Service, Resource

# define some path
dir_here = Path(__file__).absolute().parent
dir_project_root = dir_here.parent
dir_srv = dir_project_root / "aws_console_url" / "srv"


# locate all service module under /srv
for path in dir_srv.glob("*.py"):
    if path.name == "__init__.py":
        continue
    module_name = path.stem
    module = importlib.import_module(f"aws_console_url.srv.{module_name}")


def find_all_subclass(
    base_klass,
    recursive: bool = True,
    _results: T.Optional[list] = None,
) -> list:
    """
    Recursively find all subclass of a base class.
    """
    if _results is None:
        _results = list()
    for klass in base_klass.__subclasses__():
        _results.append(klass)
        if recursive:
            find_all_subclass(klass, recursive=recursive, _results=_results)
    return _results


# --- console
subclasses = sorted(
    filter(
        lambda klass: not klass.__name__.startswith("Base"),
        find_all_subclass(Service, recursive=True),
    ),
    key=lambda subclass: subclass.__module__,
)
module_and_class_list = []
public_api_list = []
for subclass in subclasses:
    module_name = subclass.__module__.split(".")[-1]
    class_name = subclass.__name__
    module_and_class_list.append((module_name, class_name))

    for tp in filter(
        lambda tp: not tp[0].startswith("_"),
        inspect.getmembers(subclass),
    ):
        method_name, member = tp
        if callable(member):
            args = str(inspect.signature(member)).replace("(self, ", "(")
            if args.endswith(" -> str"):
                args = args[: -len(" -> str")]
            public_api = f"aws_console_url.AWSConsole.{module_name}.{method_name}{args}"
        else:
            public_api = f"aws_console_url.AWSConsole.{module_name}.{method_name}"
        public_api_list.append(public_api)

# console.py
path_template = dir_here.joinpath("console.py.tpl")
template = Template(path_template.read_text())
path_console_py = dir_project_root / "aws_console_url" / "console.py"
path_console_py.write_text(template.render(module_and_class_list=module_and_class_list))

# Public-API.rst
path_template = dir_here.joinpath("Public-API.rst.tpl")
template = Template(path_template.read_text())
path_public_api_rst = dir_project_root / "Public-API.rst"
path_public_api_rst.write_text(template.render(public_api_list=public_api_list))

# --- arn
subclasses = sorted(
    filter(
        lambda klass: not klass.__name__.startswith("Base"),
        find_all_subclass(Resource, recursive=True),
    ),
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
path_resource_py.write_text(
    template.render(module_and_class_list=module_and_class_list)
)
