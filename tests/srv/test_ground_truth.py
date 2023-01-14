# -*- coding: utf-8 -*-

from aws_console_url.tests import aws


def test():
    team_name = "sanhe-labeling-workforce"
    team_arn = "arn:aws:sagemaker:us-east-1:669508176277:workteam/private-crowd/sanhe-labeling-workforce"
    print(aws.ground_truth.labeling_jobs)
    print(aws.ground_truth.labeling_datasets)
    print(aws.ground_truth.private_labeling_workforces)
    assert aws.ground_truth.to_private_team_arn(team_name) == team_arn
    assert aws.ground_truth.to_private_team_name(team_arn) == team_name
    print(aws.ground_truth.get_private_labeling_workforces_signin_url(team_name))
    print(aws.ground_truth.get_private_labeling_workforces_signin_url(team_arn))


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.ground_truth", preview=False)
