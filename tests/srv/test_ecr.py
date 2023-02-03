# -*- coding: utf-8 -*-

from aws_console_url.tests import resource, console


def test():
    repo_name = "hello-world"
    repo_uri = "669508176277.dkr.ecr.us-east-1.amazonaws.com/hello-world"

    # --- resource
    repo = resource.ECRRepo.make(console.aws_account_id, console.aws_region, repo_name)
    assert repo.uri == repo_uri

    # --- console
    print(console.ecr.repos)
    print(console.ecr.get_repo(repo_name))


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.ecr", preview=False)
