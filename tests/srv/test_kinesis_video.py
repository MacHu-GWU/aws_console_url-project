# -*- coding: utf-8 -*-

from aws_console_url.tests import console, prefix_snake


def test():
    name = f"{prefix_snake}_test"
    stream_arn = console.kinesis_video.get_kinesis_video_stream_arn(
        name, creation_time="1697463457847"
    )
    print(stream_arn)
    channel_arn = console.kinesis_video.get_kinesis_video_channel_arn(
        name, creation_time="1697463458279"
    )
    print(channel_arn)
    # --- arn

    # --- console
    print("-" * 80)
    print(console.kinesis_video.streams)
    print(console.kinesis_video.channels)

    print("-" * 80)
    print(console.kinesis_video.get_stream(name))
    print(console.kinesis_video.get_stream(stream_arn))

    print(console.kinesis_video.get_channel(name))
    print(console.kinesis_video.get_channel(channel_arn))


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.kinesis_video", preview=False)
