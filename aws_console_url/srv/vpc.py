# -*- coding: utf-8 -*-

import typing as T
import dataclasses

from ..model import Service


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
        self,
        menu: str,
        facets: T.Union[str, T.List[str]]
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
