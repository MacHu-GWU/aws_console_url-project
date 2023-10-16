# -*- coding: utf-8 -*-

from aws_console_url.tests import console, prefix_snake


def test():
    bus = f"{prefix_snake}_test"
    bus_arn = console.eventbridge.get_event_bus_arn(bus)
    default_rule = f"{prefix_snake}_default_test"
    custom_rule = f"{prefix_snake}_custom_test"
    default_rule_arn = console.eventbridge.get_event_bus_rule_arn(
        default_rule, "default"
    )
    custom_rule_arn = console.eventbridge.get_event_bus_rule_arn(custom_rule, bus)

    # --- console
    print(console.eventbridge.event_buses)
    print(console.eventbridge.event_rules)

    print(console.eventbridge.get_event_bus("default"))
    print(console.eventbridge.get_event_bus(bus))
    print(console.eventbridge.get_event_bus(bus_arn))

    print(console.eventbridge.get_event_rule(default_rule, "default"))
    print(console.eventbridge.get_event_rule(default_rule_arn))
    print(console.eventbridge.get_event_rule(custom_rule, bus))
    print(console.eventbridge.get_event_rule(custom_rule_arn))


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.eventbridge", preview=False)
