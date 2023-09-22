# -*- coding: utf-8 -*-

from aws_console_url.tests import console, prefix_snake


def test():
    repo_name = f"{prefix_snake}_test"
    repo_arn = console.ecr.get_repo_arn(repo_name)
    repo_uri = console.ecr.get_repo_uri(repo_name)
    assert "None" not in repo_arn

    # --- console
    print(console.ecr.repos)
    print(console.ecr.get_repo(repo_name))
    print(console.ecr.get_repo(repo_arn))
    print(console.ecr.get_repo(repo_uri))


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.ecr", preview=False)
