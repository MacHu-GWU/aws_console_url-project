# -*- coding: utf-8 -*-

import pytest


def test():
    import aws_console_url

    _ = aws_console_url.BotoSesManager

    aws = aws_console_url.AWSConsole()

    {% for module_name in module_name_list %}
    _ = aws.{{ module_name }}
    {%- endfor %}

    aws_res = aws_console_url.resource

    {% for class_name in resource_class_list %}
    _ = aws_res.{{ class_name }}
    {%- endfor %}


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
