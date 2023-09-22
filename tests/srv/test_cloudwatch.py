# -*- coding: utf-8 -*-

from aws_console_url.tests import console


def test():
    group_name = "/aws/lambda/aws-ci-bot"
    group_name_pattern = "/aws/lambda"
    stream_name = "2023/02/21/[$LATEST]71007e7ce7064b5ca23bd04deefeb2a7"
    stream_name_pattern = "71007e7ce7064b5ca23bd04deefeb2a7"
    lambda_func_name = "aws-ci-bot"
    request_id = "9952cc9c-ae5c-4a10-9eb5-49f6911c7947"

    print(console.cloudwatch.log_groups)
    print(console.cloudwatch.get_log_group(group_name))
    print(console.cloudwatch.get_log_group_log_streams_tab(group_name))
    print(console.cloudwatch.get_log_stream(group_name, stream_name))

    print(console.cloudwatch.filter_log_groups(group_name_pattern))
    print(console.cloudwatch.filter_log_streams(group_name, stream_name_pattern))
    print(console.cloudwatch.filter_log_event(group_name, stream_name, '"' + request_id + '"'))
    print(
        console.cloudwatch.filter_log_event_by_lambda_request_id(
            lambda_func_name, request_id
        )
    )


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.cloudwatch", preview=False)
