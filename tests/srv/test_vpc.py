# -*- coding: utf-8 -*-

from aws_console_url.tests import console


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

    # --- specific
    res = console.bsm.ec2_client.describe_vpcs(
        Filters=[dict(Name="is-default", Values=["true"])],
    )
    lst = res.get("Vpcs", [])
    if lst:
        vpc_id = lst[0]["VpcId"]
        print(console.vpc.get_vpc(vpc_id))

    res = console.bsm.ec2_client.describe_subnets()
    lst = res.get("Subnets", [])
    if lst:
        subnet_id = lst[0]["SubnetId"]
        print(console.vpc.get_subnet(subnet_id))

    res = console.bsm.ec2_client.describe_route_tables()
    lst = res.get("RouteTables", [])
    if lst:
        rtb_id = lst[0]["RouteTableId"]
        print(console.vpc.get_route_table(rtb_id))

    res = console.bsm.ec2_client.describe_vpc_endpoints()
    lst = res.get("VpcEndpoints", [])
    if lst:
        vpce_id = lst[0]["VpcEndpointId"]
        print(console.vpc.get_vpc_endpoint(vpce_id))

    res = console.bsm.ec2_client.describe_security_groups()
    lst = res.get("SecurityGroups", [])
    if lst:
        sg_id = lst[0]["GroupId"]
        print(console.vpc.get_security_group(sg_id))


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.vpc", preview=False)
