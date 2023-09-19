# -*- coding: utf-8 -*-

import aws_cdk as cdk

from iac.main import MainStack
from aws_console_url.tests import prefix

app = cdk.App()

stack = MainStack(
    app,
    "AwsConsoleUrlTest",
    prefix=prefix,
    stack_name="aws-console-url-test",
)

app.synth()
