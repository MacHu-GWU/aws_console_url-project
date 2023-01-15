# -*- coding: utf-8 -*-

import typing as T
import dataclasses

from boto_session_manager import BotoSesManager

from .compat import cached_property
{% for module_name, class_name in module_and_class_list %}
from .srv.{{ module_name }} import {{ class_name}}
{%- endfor %}


@dataclasses.dataclass
class AWSConsole:
    """
    Public API for AWS Console URL builder.

    :param aws_account_id: optional, explicit AWS account ID.
    :param aws_region: optional, explicit AWS region.
    :param is_us_gov_cloud: default False, is this AWS account in US Gov Cloud?
    :param bsm: optional, the ``boto_session_manager.BotoSesManager`` object.
        Sometimes we need to call AWS API for some information to build the console url.
    """
    aws_account_id: T.Optional[str] = dataclasses.field(default=None)
    aws_region: T.Optional[str] = dataclasses.field(default=None)
    is_us_gov_cloud: bool = dataclasses.field(default=False)
    bsm: BotoSesManager = dataclasses.field(default=lambda: BotoSesManager())
    {% for module_name, class_name in module_and_class_list %}
    @cached_property
    def {{ module_name }}(self) -> {{ class_name }}:
        return {{ class_name }}._from_aws_console(self)
    {% endfor %}