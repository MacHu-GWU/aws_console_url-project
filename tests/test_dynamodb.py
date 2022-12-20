# -*- coding: utf-8 -*-

from aws_console_url.srv.dynamodb import dynamodb


def test():
    table = "dynamodb-cache"
    print(dynamodb.tables)
    print(dynamodb.table_overview(table))
    print(dynamodb.table_items(table))
    print(dynamodb.item_details(table, "my_db_credential"))


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.dynamodb")
