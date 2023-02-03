# -*- coding: utf-8 -*-

from aws_console_url.tests import resource, console


def test():
    name = "test"

    # --- resource
    queue = resource.SQSQueue.from_arn(
        resource.SQSQueue.make(console.aws_account_id, console.aws_region, name).arn
    )
    assert queue.name == name

    # --- console
    print(console.sqs.queues)
    print(console.sqs.get_queue(name))
    print(console.sqs.get_queue_url(name))
    print(console.sqs.get_queue_arn(name))
    print(console.sqs.get_queue_send_and_receive_message(name))


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.sqs", preview=False)
