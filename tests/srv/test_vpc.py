# -*- coding: utf-8 -*-

from aws_console_url.tests import resource, console


def test():
    print("")
    facet = "dev"

    # --- resource

    # --- console
    print(console.vpc.vpcs)
    print(console.vpc.subnets)
    print(console.vpc.route_tables)
    print(console.vpc.internet_gateways)
    print(console.vpc.elastic_ips)
    print(console.vpc.endpoints)
    print(console.vpc.nat_gateways)
    print(console.vpc.network_acls)
    print(console.vpc.security_groups)

    print(console.vpc.filter_vpcs(facet))
    print(console.vpc.filter_subnets(facet))
    print(console.vpc.filter_route_tables(facet))
    print(console.vpc.filter_internet_gateways(facet))
    print(console.vpc.filter_elastic_ips(facet))
    print(console.vpc.filter_endpoints(facet))
    print(console.vpc.filter_nat_gateways(facet))
    print(console.vpc.filter_network_acls(facet))
    print(console.vpc.filter_security_groups(facet))


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.vpc", preview=False)
