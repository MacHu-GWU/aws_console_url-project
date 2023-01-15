# -*- coding: utf-8 -*-

from aws_console_url.tests import console


def test():
    database = "sampledb"
    table = "elb_logs"
    print(console.glue.databases)
    print(console.glue.tables)
    print(console.glue.crawlers)
    print(console.glue.classifiers)
    print(console.glue.get_database(database))
    print(console.glue.get_table(database, table))


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.glue", preview=False)
