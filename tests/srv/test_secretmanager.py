# -*- coding: utf-8 -*-

from aws_console_url.tests import resource, console, prefix_slug


def test():
    secret_name = f"{prefix_slug}-test"
    name = f"{prefix_slug}-test-ABCDEF"

    # --- resource
    secret = resource.SecretManagerSecret.make(
        aws_account_id=console.aws_account_id,
        aws_region=console.aws_region,
        name=name,
    )
    assert secret.secret_name == secret_name
    assert resource.SecretManagerSecret.from_arn(secret.arn) == secret

    # --- console
    print(console.secretmanager.secrets)
    print(console.secretmanager.filter_secrets(secret_name))
    print(console.secretmanager.filter_secrets([prefix_slug, "test"]))

    print(console.secretmanager.get_secret(secret_name))
    print(console.secretmanager.get_secret(secret.arn))


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.secretmanager", preview=False)
