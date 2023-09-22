# -*- coding: utf-8 -*-

from aws_console_url.tests import console, prefix


def test():
    topic_name = f"{prefix}_test"
    subscription_id = "a07e1034-10c0-47a6-83c2-552cfcca42db"
    topic_arn = console.sns.get_topic_arn(topic_name)
    subscription_arn = console.sns.get_subscription_arn(topic_name, subscription_id)

    # --- console
    print(console.sns.topics)
    print(console.sns.subscriptions)
    print(console.sns.get_topic(topic_name))
    print(console.sns.get_topic(topic_arn))
    print(console.sns.get_subscription(subscription_id, topic_name))
    print(console.sns.get_subscription(subscription_arn))


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.sns", preview=False)
