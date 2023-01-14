# -*- coding: utf-8 -*-

from aws_console_url.tests import aws


def test():
    project = "aws_idp_doc_store-project"
    build_id = "aws_idp_doc_store-project:7ce187d9-887e-40c8-ba37-fa09f0c9b529"

    print(aws.codebuild.build_projects)
    print(aws.codebuild.build_history)
    print(aws.codebuild.report_groups)
    print(aws.codebuild.report_history)
    print(aws.codebuild.metrics)

    print(aws.codebuild.get_project(project))
    print(aws.codebuild.get_build_run(project, build_id))

if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.codebuild", preview=False)
