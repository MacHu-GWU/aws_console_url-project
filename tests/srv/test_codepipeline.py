# -*- coding: utf-8 -*-

from aws_console_url.tests import resource, console, prefix_snake


def test():
    pipeline = "multi_env_simple_lambda"
    exec_id = "4493cd9f-69b0-4eef-89ee-73672d4c331f"

    # --- resource

    # --- console
    print(console.codepipeline.pipelines)
    print(console.codepipeline.get_pipeline(pipeline))
    print(console.codepipeline.get_pipeline_execution_history(pipeline))
    print(console.codepipeline.get_pipeline_execution(pipeline, exec_id))


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.codecommit", preview=False)
