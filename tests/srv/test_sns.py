# -*- coding: utf-8 -*-

from aws_console_url.tests import resource, console, prefix


def test():
    topic_name = f"{prefix}_test"
    subscription_id = "a07e1034-10c0-47a6-83c2-552cfcca42db"

    # --- resource
    topic = resource.SNSTopic.from_arn(
        resource.SNSTopic.make(
            console.aws_account_id, console.aws_region, topic_name
        ).arn
    )
    subscription = resource.SNSSubscription.from_arn(
        resource.SNSSubscription.make(
            console.aws_account_id, console.aws_region, topic_name, subscription_id
        ).arn
    )
    assert topic.name == topic_name
    assert subscription.topic_name == topic_name
    assert subscription.subscription_id == subscription_id

    # --- console
    print(console.sns.topics)
    print(console.sns.subscriptions)
    print(console.sns.get_topic(topic_name))
    print(console.sns.get_topic(topic.arn))
    print(console.sns.get_subscription(topic_name, subscription_id))
    print(console.sns.get_subscription(subscription.arn))


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.sns", preview=False)
