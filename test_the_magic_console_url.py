# -*- coding: utf-8 -*-

"""
AWS has a magic console url that f"https://us-east-1.console.aws.amazon.com/go/view?arn={arn}"
can jump to the specific resource. However, it is not documented anywhere and it is only working
for some of AWS services.
"""


def print_console_url(arn: str):
    url = f"https://us-east-1.console.aws.amazon.com/go/view?arn={arn}"
    print(url)


arn_list = [
    "arn:aws:iam::aws:policy/AdministratorAccess",
]
for arn in arn_list:
    print_console_url(arn)
