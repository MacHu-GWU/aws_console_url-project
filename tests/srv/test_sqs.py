# -*- coding: utf-8 -*-

from aws_console_url.tests import aws


def test():
    name = "test"
    print(aws.sqs.queues)
    print(aws.sqs.get_queue(name))
    print(aws.sqs.get_queue_url(name))
    print(aws.sqs.get_queue_arn(name))


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.sqs", preview=False)
