# -*- coding: utf-8 -*-

import aws_cdk as cdk

from iac.main import MainStack
from aws_console_url.tests import bsm, prefix

app = cdk.App()

stack = MainStack(
    app,
    "AwsConsoleUrlTest",
    env=cdk.Environment(account=bsm.aws_account_id, region=bsm.aws_region),
    prefix=prefix,
    stack_name="aws-console-url-test",
)

app.synth()
