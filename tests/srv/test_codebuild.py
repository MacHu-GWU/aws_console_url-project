# -*- coding: utf-8 -*-

from aws_console_url.tests import resource, console, prefix_snake


def test():
    project_name = "acu_e5f245a1_test"
    project_arn = console.codebuild.get_build_project_arn(project_name)
    run_id = "08805851-8a0a-4968-9d08-c7cc0623db7b"
    run_arn = console.codebuild.get_build_run_arn(is_batch=False, project_name=project_name, run_id=run_id)

    # --- resource

    # --- console
    print(console.codebuild.build_projects)
    print(console.codebuild.build_history)
    print(console.codebuild.report_groups)
    print(console.codebuild.report_history)
    print(console.codebuild.metrics)

    print(console.codebuild.get_project(project_name))
    print(console.codebuild.get_project(project_arn))
    print(console.codebuild.get_build_run(False, project_name, run_id))
    print(console.codebuild.get_build_run(False, run_arn=run_arn))
    print(console.codebuild.get_build_run_phase(False, project_name, run_id))
    print(console.codebuild.get_build_run_phase(False, run_arn=run_arn))
    print(console.codebuild.get_build_run_env_var(False, project_name, run_id))
    print(console.codebuild.get_build_run_env_var(False, run_arn=run_arn))



if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.codebuild", preview=False)
