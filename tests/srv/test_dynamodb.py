# -*- coding: utf-8 -*-

from aws_console_url.tests import resource, console


def test():
    # --- resource
    table1 = "aws_console_url_test_hash_key_only"
    table2 = "aws_console_url_test_hash_and_range_key"

    dynamodb_table = resource.DynamoDBTable.from_arn(
        resource.DynamoDBTable.make(console.aws_account_id, console.aws_region, table1).arn
    )
    assert dynamodb_table.name == table1

    # --- console
    print(console.dynamodb.get_table_arn(table1))
    print(console.dynamodb.get_table_arn(table2))

    print(console.dynamodb.tables)
    print(console.dynamodb.get_table_overview(table1))
    print(console.dynamodb.get_table_items(table1))

    print(console.dynamodb.get_item_details(table1, "pk-1"))
    print(console.dynamodb.get_item_details(table2, "pk-1", "sk-1"))


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.dynamodb", preview=False)
