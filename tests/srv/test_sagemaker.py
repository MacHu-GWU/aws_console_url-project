# -*- coding: utf-8 -*-

from aws_console_url.tests import resource, console


def test():
    # --- resource

    # --- console
    print(console.sagemaker.notebooks)
    print(console.sagemaker.training_jobs)
    print(console.sagemaker.processing_jobs)
    print(console.sagemaker.models)
    print(console.sagemaker.inference_endpoints)
    print(console.sagemaker.batch_transform_jobs)


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.sagemaker", preview=False)
