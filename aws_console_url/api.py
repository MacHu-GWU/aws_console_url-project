# -*- coding: utf-8 -*-

"""
Usage example::

    from boto_session_manager import BotoSesManager
    import aws_console_url.api as aws_console_url

    bsm = BotoSesManager()
    aws_console = aws_console_url.AWSConsole(
        aws_account_id=bsm.aws_account_id,
        aws_region=bsm.aws_region,
        bsm=bsm,
    )
    print(aws_console.ec2.get_instance("i-1234567890abcdef0"))
"""

from .console import AWSConsole
from .utils import encode_arn_in_url
