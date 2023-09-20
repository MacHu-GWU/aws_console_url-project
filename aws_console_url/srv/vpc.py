# -*- coding: utf-8 -*-

import typing as T
import dataclasses

from ..model import Service


def _normalize_id(id_: str, prefix: str) -> str:
    if id_.startswith(prefix):
        return id_
    else:
        return f"{prefix}{id_}"


def _normalize_vpc_id(vpc_id: str) -> str:
    return _normalize_id(vpc_id, "vpc-")


def _normalize_subnet_id(subnet_id: str) -> str:
    return _normalize_id(subnet_id, "subnet-")


def _normalize_route_table(rtb_id: str) -> str:
    return _normalize_id(rtb_id, "rtb-")


def _normalize_vpc_endpoint_id(vpce_id: str) -> str:
    return _normalize_id(vpce_id, "vpce-")


def _normalize_security_group_id(sg_id: str) -> str:
    return _normalize_id(sg_id, "sg-")


@dataclasses.dataclass(frozen=True)
class VPC(Service):
    _AWS_SERVICE = "vpc"

    # --- arn

    # --- dashboard
    def _get_dashboard(self, menu: str) -> str:
        return f"{self._service_root}/home?region={self._region}#{menu}:"

    @property
    def vpcs(self) -> str:
        return self._get_dashboard("vpcs")

    @property
    def subnets(self) -> str:
        return self._get_dashboard("subnets")

    @property
    def route_tables(self) -> str:
        return self._get_dashboard("RouteTables")

    @property
    def internet_gateways(self) -> str:
        return self._get_dashboard("igws")

    @property
    def elastic_ips(self) -> str:
        return self._get_dashboard("Addresses")

    @property
    def endpoints(self) -> str:
        return self._get_dashboard("Endpoints")

    @property
    def nat_gateways(self) -> str:
        return self._get_dashboard("NatGateways")

    @property
    def network_acls(self) -> str:
        return self._get_dashboard("acls")

    @property
    def security_groups(self) -> str:
        return self._get_dashboard("SecurityGroups")

    # --- instance
    def _get_dashboard_filter(
        self, menu: str, facets: T.Union[str, T.List[str]]
    ) -> str:
        if isinstance(facets, str):
            facets = [
                facets,
            ]
        search = ",".join(facets)
        return f"{self._service_root}/home?region={self._region}#{menu}:search={search}"

    def filter_vpcs(self, facets: T.Union[str, T.List[str]]) -> str:
        return self._get_dashboard_filter("vpcs", facets)

    def filter_subnets(self, facets: T.Union[str, T.List[str]]) -> str:
        return self._get_dashboard_filter("subnets", facets)

    def filter_route_tables(self, facets: T.Union[str, T.List[str]]) -> str:
        return self._get_dashboard_filter("RouteTables", facets)

    def filter_internet_gateways(self, facets: T.Union[str, T.List[str]]) -> str:
        return self._get_dashboard_filter("igws", facets)

    def filter_elastic_ips(self, facets: T.Union[str, T.List[str]]) -> str:
        return self._get_dashboard_filter("Addresses", facets)

    def filter_endpoints(self, facets: T.Union[str, T.List[str]]) -> str:
        return self._get_dashboard_filter("Endpoints", facets)

    def filter_nat_gateways(self, facets: T.Union[str, T.List[str]]) -> str:
        return self._get_dashboard_filter("NatGateways", facets)

    def filter_network_acls(self, facets: T.Union[str, T.List[str]]) -> str:
        return self._get_dashboard_filter("acls", facets)

    def filter_security_groups(self, facets: T.Union[str, T.List[str]]) -> str:
        return self._get_dashboard_filter("SecurityGroups", facets)

    def get_vpc(self, vpc_id: str) -> str:
        vpc_id = _normalize_vpc_id(vpc_id)
        return (
            f"{self._service_root}/home?region={self._region}#VpcDetails:VpcId={vpc_id}"
        )

    def get_subnet(self, subnet_id: str) -> str:
        subnet_id = _normalize_subnet_id(subnet_id)
        return (
            f"{self._service_root}/home?region={self._region}#SubnetDetails:subnetId={subnet_id}"
        )

    def get_route_table(self, rtb_id: str) -> str:
        rtb_id = _normalize_route_table(rtb_id)
        return (
            f"{self._service_root}/home?region={self._region}#RouteTableDetails:RouteTableId={rtb_id}"
        )

    def get_vpc_endpoint(self, vpce_id: str) -> str:
        vpce_id = _normalize_vpc_endpoint_id(vpce_id)
        return (
            f"{self._service_root}/home?region={self._region}#EndpointDetails:vpcEndpointId={vpce_id}"
        )

    def get_security_group(self, sg_id: str) -> str:
        sg_id = _normalize_security_group_id(sg_id)
        return (
            f"{self._service_root}/home?region={self._region}#SecurityGroup:groupId={sg_id}"
        )
