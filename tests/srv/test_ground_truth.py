# -*- coding: utf-8 -*-

from aws_console_url.tests import resource, console


def test():
    team_name = "sanhe-labeling-workforce"
    team_arn = "arn:aws:sagemaker:us-east-1:669508176277:workteam/private-crowd/sanhe-labeling-workforce"

    private_team = resource.GroundTruthPrivateTeam.from_arn(
        resource.GroundTruthPrivateTeam.make(
            console.aws_account_id, console.aws_region, team_name
        ).arn
    )
    assert private_team.name == team_name
    assert private_team.arn == team_arn

    print(console.ground_truth.labeling_jobs)
    print(console.ground_truth.labeling_datasets)
    print(console.ground_truth.private_labeling_workforces)
    print(console.ground_truth.get_private_labeling_workforces_signin_url(team_name))
    print(console.ground_truth.get_private_labeling_workforces_signin_url(team_arn))


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.ground_truth", preview=False)
