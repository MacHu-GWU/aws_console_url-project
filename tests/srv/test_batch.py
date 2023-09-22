# -*- coding: utf-8 -*-

from aws_console_url.tests import console, prefix_snake


def test():
    ce = f"{prefix_snake}_test"
    ce_arn = console.batch.get_compute_environment_arn(ce)
    job_queue = f"{prefix_snake}_test"
    job_queue_arn = console.batch.get_job_queue_arn(job_queue)
    job_def = f"{prefix_snake}_test"
    revision = 1
    job_def_arn = console.batch.get_job_definition_arn(job_def, revision)
    job_name = "job1"
    job_id = console.bsm.batch_client.list_jobs(
        jobQueue=job_queue,
        filters=[
            dict(name="JOB_NAME", values=[job_name]),
        ]
    )["jobSummaryList"][0]["jobId"]
    job_arn = console.batch.get_job_arn(job_id)

    # --- arn

    # --- console
    print("-" * 80)
    print(console.batch.compute_environments)
    print(console.batch.job_queues)
    print(console.batch.job_definitions)
    print(console.batch.jobs)

    print("-" * 80)
    print(console.batch.get_compute_environment(ce))
    print(console.batch.get_compute_environment(ce_arn))

    print(console.batch.get_job_queue(job_queue))
    print(console.batch.get_job_queue(job_queue_arn))

    print(console.batch.get_job_definition(job_def, revision))
    print(console.batch.get_job_definition(job_def_arn))

    print(console.batch.get_job(job_id))
    print(console.batch.get_job(job_arn))


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.batch", preview=False)
