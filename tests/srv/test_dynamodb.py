# -*- coding: utf-8 -*-

from aws_console_url.tests import console


def test():
    table = "dynamodb-cache"
    print(console.dynamodb.tables)
    print(console.dynamodb.get_table_overview(table))
    print(console.dynamodb.get_table_items(table))
    print(console.dynamodb.get_item_details(table, "my_db_credential"))
    print(console.dynamodb.get_item_details(
        table="data-quality-governor-dev-statistics-tracker",
        hash_key="s3://aws-data-lab-sanhe-for-everything/poc/2022-02-01-aws_data_quality_governor/person-pii/",
        range_key="2022-02-09",
    ))


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.dynamodb", preview=False)
