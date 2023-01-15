# -*- coding: utf-8 -*-

from aws_console_url.tests import console


def test():
    name = "test"
    print(console.sqs.queues)
    print(console.sqs.get_queue(name))
    print(console.sqs.get_queue_url(name))
    print(console.sqs.get_queue_arn(name))


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.sqs", preview=False)
