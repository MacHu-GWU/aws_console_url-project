# -*- coding: utf-8 -*-

from aws_console_url.tests import console, resource


def test():
    ce = "awshsh-app-dev"
    job_queue = "awshsh-app-dev-default"
    job_def = "simple-batch-sbx"
    revision = 1
    job_id = "9afe38df-69cb-4354-9b79-aedbb7c6f4ed"

    # --- arn
    res_ce = resource.BatchComputeEnvironment.from_arn(
        console.batch.get_compute_environment_arn(ce)
    )
    res_job_queue = resource.BatchJobQueue.from_arn(
        console.batch.get_job_queue_arn(job_queue)
    )
    res_job_def = resource.BatchJobDefinition.from_arn(
        console.batch.get_job_definition_arn(job_def, revision)
    )
    res_job = resource.BatchJob.from_arn(console.batch.get_job_arn(job_id))

    assert res_ce == resource.BatchComputeEnvironment.from_arn(res_ce.arn)
    assert res_job_queue == resource.BatchJobQueue.from_arn(res_job_queue.arn)
    assert res_job_def == resource.BatchJobDefinition.from_arn(res_job_def.arn)
    assert res_job == resource.BatchJob.from_arn(res_job.arn)

    # --- console
    print(console.batch.compute_environments)
    print(console.batch.job_queues)
    print(console.batch.job_definitions)
    print(console.batch.jobs)
    print(console.batch.get_compute_environment(ce))
    print(console.batch.get_job_queue(job_queue))
    print(console.batch.get_job_definition(job_def, revision))
    print(console.batch.get_job(job_id))

    print(console.batch.get_compute_environment(res_ce.arn))
    print(console.batch.get_job_queue(res_job_queue.arn))
    print(console.batch.get_job_definition(res_job_def.arn))
    print(console.batch.get_job(res_job.arn))


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.batch", preview=False)