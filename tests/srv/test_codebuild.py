# -*- coding: utf-8 -*-

from aws_console_url.tests import resource, console


def test():
    project_name = "aws_idp_doc_store-project"
    run_id = "7ce187d9-887e-40c8-ba37-fa09f0c9b529"

    # --- resource
    build_project = resource.CodeBuildProject.from_arn(
        resource.CodeBuildProject.make(
            console.aws_account_id, console.aws_region, project_name
        ).arn
    )
    assert build_project.name == project_name

    build_run = resource.CodeBuildRun.from_arn(
        resource.CodeBuildRun.make(
            console.aws_account_id, console.aws_region, False, project_name, run_id
        ).arn
    )
    assert build_run.project_name == project_name

    # --- console
    print(console.codebuild.get_build_project_arn(project_name))
    print(console.codebuild.get_build_run_arn(False, project_name, run_id))

    print(console.codebuild.build_projects)
    print(console.codebuild.build_history)
    print(console.codebuild.report_groups)
    print(console.codebuild.report_history)
    print(console.codebuild.metrics)

    print(console.codebuild.get_project(project_name))
    print(console.codebuild.get_build_run(False, project_name, run_id))
    print(console.codebuild.get_build_run_phase(False, project_name, run_id))
    print(console.codebuild.get_build_run_env_var(False, project_name, run_id))


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.codebuild", preview=False)
