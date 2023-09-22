# -*- coding: utf-8 -*-

from aws_console_url.tests import console


def test():
    team_name = "my-private-team"
    team_arn = console.ground_truth.get_private_workteam_arn(team_name)

    print(console.ground_truth.labeling_jobs)
    print(console.ground_truth.labeling_datasets)
    print(console.ground_truth.labeling_workforces)
    print(console.ground_truth.get_private_workteam_arn(team_name))
    print(console.ground_truth.get_private_labeling_workforces_signin_url(team_name))
    print(console.ground_truth.get_private_labeling_workforces_signin_url(team_arn))


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.ground_truth", preview=False)
