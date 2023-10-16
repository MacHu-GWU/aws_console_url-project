# -*- coding: utf-8 -*-

from aws_console_url.tests import console, prefix_snake


def test():
    stream = f"{prefix_snake}_test"
    stream_arn = console.kinesis.get_kinesis_stream_arn(stream)
    # --- arn

    # --- console
    print("-" * 80)
    print(console.kinesis.data_streams)

    print("-" * 80)
    print(console.kinesis.get_stream(stream))
    print(console.kinesis.get_stream(stream_arn))


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.kinesis", preview=False)
