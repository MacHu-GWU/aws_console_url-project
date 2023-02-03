# -*- coding: utf-8 -*-

from aws_console_url.tests import resource, console


def test():
    secret_name = "my-example-secret"

    # --- resource

    # --- console
    print(console.secretmanager.secrets)
    print(console.secretmanager.filter_secrets(secret_name))
    print(console.secretmanager.get_secret(secret_name))


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.secretmanager", preview=False)
