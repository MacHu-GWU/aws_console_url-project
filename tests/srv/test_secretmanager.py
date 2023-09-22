# -*- coding: utf-8 -*-

from aws_console_url.tests import console, prefix_slug


def test():
    secret_name = f"{prefix_slug}-test"
    secret_arn = console.secretmanager.get_secret_arn(secret_name)

    # --- console
    print(console.secretmanager.secrets)
    print(console.secretmanager.filter_secrets(secret_name))
    print(console.secretmanager.filter_secrets([prefix_slug, "test"]))

    print(console.secretmanager.get_secret(secret_name))
    print(console.secretmanager.get_secret(secret_arn))


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.secretmanager", preview=False)
