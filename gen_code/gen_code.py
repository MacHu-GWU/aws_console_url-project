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
def list_all_service_module() -> T.List[str]:
    module_name_list = list()
    for path in dir_srv.glob("*.py"):
        if path.name == "__init__.py":
            continue
        module_name = path.stem
        module_name_list.append(module_name)
    return module_name_list


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


def import_all_service_module(
    module_name_list: T.List[str],
) -> list:
    imported_module_list = list()
    for module_name in module_name_list:
        imported_module = importlib.import_module(f"aws_console_url.srv.{module_name}")
        imported_module_list.append(imported_module)
    return imported_module_list


def get_public_api(
    resource_subclasses: T.List[T.Type[Resource]],
    service_subclasses: T.List[T.Type[Service]],
) -> T.Dict[str, T.List[str]]:
    public_apis: T.Dict[str, T.List[str]] = dict()
    for service_subclass in service_subclasses:
        module_name = service_subclass.__module__.split(".")[-1]
        for member_name, member in filter(
            lambda tp: not tp[0].startswith("_"),
            inspect.getmembers(service_subclass),
        ):
            if callable(member):
                args = str(inspect.signature(member)).replace("(self, ", "(")
                if args.endswith(" -> str"):
                    args = args[: -len(" -> str")]
                public_api = (
                    f"aws_console_url.AWSConsole.{module_name}.{member_name}{args}"
                )
            else:
                public_api = f"aws_console_url.AWSConsole.{module_name}.{member_name}"
            try:
                public_apis[module_name].append(public_api)
            except:
                public_apis[module_name] = [
                    public_api,
                ]
    return public_apis


module_name_list = list_all_service_module()
imported_module_list = import_all_service_module(module_name_list)

resource_subclasses: T.List[T.Type[Resource]] = sorted(
    filter(
        lambda klass: not klass.__name__.startswith("Base"),
        find_all_subclass(Resource, recursive=True),
    ),
    key=lambda subclass: subclass.__module__,
)

service_subclasses: T.List[T.Type[Service]] = sorted(
    filter(
        lambda klass: not klass.__name__.startswith("Base"),
        find_all_subclass(Service, recursive=True),
    ),
    key=lambda subclass: subclass.__module__,
)

public_apis = get_public_api(resource_subclasses, service_subclasses)


def create_console_py(
    service_subclasses: T.List[T.Type[Service]],
):
    module_and_service_list: T.List[T.Tuple[str, str]] = list()
    for service_subclass in service_subclasses:
        module_name = service_subclass.__module__.split(".")[-1]
        class_name = service_subclass.__name__
        module_and_service_list.append((module_name, class_name))

    path_template = dir_here.joinpath("console.py.tpl")
    template = Template(path_template.read_text())
    path_console_py = dir_project_root / "aws_console_url" / "console.py"
    path_console_py.write_text(
        template.render(module_and_service_list=module_and_service_list)
    )

create_console_py(service_subclasses)


def create_public_api_rst(
    public_apis: T.Dict[str, T.List[str]],
):
    path_template = dir_here.joinpath("Public-API.rst.tpl")
    template = Template(path_template.read_text())
    path_public_api_rst = dir_project_root / "Public-API.rst"
    path_public_api_rst.write_text(template.render(public_apis=public_apis))

create_public_api_rst(public_apis)


def create_resource_py(
    resource_subclasses: T.List[T.Type[Resource]],
):
    module_and_resource_list = []
    for resource_subclass in resource_subclasses:
        module_name = resource_subclass.__module__.split(".")[-1]
        class_name = resource_subclass.__name__
        module_and_resource_list.append((module_name, class_name))

    # resource.py
    path_resource_py_template = dir_here.joinpath("resource.py.tpl")
    template = Template(path_resource_py_template.read_text())
    path_resource_py = dir_project_root / "aws_console_url" / "resource.py"
    path_resource_py.write_text(
        template.render(module_and_resource_list=module_and_resource_list)
    )

# create_resource_py(resource_subclasses)

def create_import_py(
    resource_subclasses: T.List[T.Type[Resource]],
    module_name_list: T.List[str],
):
    resource_class_list = [
        resource_subclass.__name__
        for resource_subclass in resource_subclasses
    ]
    path_template = dir_here.joinpath("test_import.py.tpl")
    template = Template(path_template.read_text())
    path_test_import_py = dir_project_root / "tests" / "test_import.py"
    path_test_import_py.write_text(
        template.render(
            module_name_list=module_name_list,
            resource_class_list=resource_class_list,
        )
    )

create_import_py(resource_subclasses, module_name_list)
