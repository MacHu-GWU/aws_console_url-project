# -*- coding: utf-8 -*-

from aws_console_url.tests import resource, console, prefix_snake


def test():
    # --- resource
    table1 = f"{prefix_snake}_test_key_only"
    table2 = f"{prefix_snake}_test_key_and_range"

    table1_arn = console.dynamodb.get_table_arn(table1)
    table2_arn = console.dynamodb.get_table_arn(table2)

    assert resource.DynamoDBTable.from_arn(table1_arn).arn == table1_arn
    assert resource.DynamoDBTable.from_arn(table2_arn).arn == table2_arn

    # --- console
    print(console.dynamodb.tables)
    print(console.dynamodb.get_table_overview(table1))
    print(console.dynamodb.get_table_items(table1))

    print(console.dynamodb.get_item_details(table1, "pk-1"))
    print(console.dynamodb.get_item_details(table2, "pk-1", "sk-1"))


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.dynamodb", preview=False)
