# -*- coding: utf-8 -*-

from aws_console_url.tests import console, prefix_snake


def test():
    pipeline = f"{prefix_snake}_test"
    pipeline_arn = console.codepipeline.get_pipeline_arn(pipeline)
    exec_id = console.bsm.codepipeline_client.list_pipeline_executions(
        pipelineName=pipeline,
    )["pipelineExecutionSummaries"][0]["pipelineExecutionId"]

    # --- console
    print(console.codepipeline.pipelines)
    print(console.codepipeline.get_pipeline(pipeline))
    print(console.codepipeline.get_pipeline(pipeline_arn))
    print(console.codepipeline.get_pipeline_execution_history(pipeline))
    print(console.codepipeline.get_pipeline_execution_history(pipeline_arn))
    print(console.codepipeline.get_pipeline_execution(pipeline, exec_id))
    print(console.codepipeline.get_pipeline_execution(pipeline_arn, exec_id))


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.codepipeline", preview=False)
