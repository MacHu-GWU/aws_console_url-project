# -*- coding: utf-8 -*-

from aws_console_url.tests import console, prefix_snake


def test():
    name = f"{prefix_snake}_test"
    arn = console.sqs.get_queue_arn(name)
    url = console.sqs.get_queue_url(name)

    # --- console
    print(console.sqs.get_queue_arn(name))

    print(console.sqs.queues)
    print(console.sqs.get_queue(name))
    print(console.sqs.get_queue(arn))
    print(console.sqs.get_queue(url))
    print(console.sqs.get_queue_send_and_receive_message(name))
    print(console.sqs.get_queue_send_and_receive_message(arn))
    print(console.sqs.get_queue_send_and_receive_message(url))


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.sqs", preview=False)
