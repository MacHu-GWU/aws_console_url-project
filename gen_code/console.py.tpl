# -*- coding: utf-8 -*-

import typing as T
import dataclasses

from .compat import cached_property
{% for module_name, class_name in module_and_class_list %}
from .srv.{{ module_name }} import {{ class_name}}
{%- endfor %}


@dataclasses.dataclass
class AWSConsole:
    aws_account_id: T.Optional[str] = dataclasses.field(default=None)
    aws_region: T.Optional[str] = dataclasses.field(default=None)
    is_us_gov_cloud: bool = dataclasses.field(default=False)
    {% for module_name, class_name in module_and_class_list %}
    @cached_property
    def {{ module_name }}(self) -> {{ class_name }}:
        return {{ class_name }}._from_aws_console(self)
    {% endfor %}