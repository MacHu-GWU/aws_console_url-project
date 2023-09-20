# -*- coding: utf-8 -*-

import typing as T
from functools import cached_property
from aws_console_url.tests import bsm

if T.TYPE_CHECKING:
    from .main import MainStack


class HelperMixin:
    @cached_property
    def default_vpc_id(self) -> str:
        res = bsm.ec2_client.describe_vpcs(
            Filters=[dict(Name="is-default", Values=["true"])],
        )
        vpc_id = res["Vpcs"][0]["VpcId"]
        return vpc_id

    @cached_property
    def default_subnet_id_list(self) -> T.List[str]:
        res = bsm.ec2_client.describe_subnets(
            Filters=[dict(Name="vpc-id", Values=[self.default_vpc_id])],
        )
        subnet_id_list = [dct["SubnetId"] for dct in res["Subnets"]]
        return subnet_id_list

    @cached_property
    def default_security_group_id(self) -> str:
        res = bsm.ec2_client.describe_security_groups(
            Filters=[dict(Name="vpc-id", Values=[self.default_vpc_id])],
        )
        default_sg_id = [
            dct["GroupId"]
            for dct in res["SecurityGroups"]
            if dct["GroupName"] == "default"
        ][0]
        return default_sg_id
