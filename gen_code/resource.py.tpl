# -*- coding: utf-8 -*-
{% for module_name, class_name in module_and_class_list %}
from .srv.{{ module_name }} import {{ class_name}}
{%- endfor %}
