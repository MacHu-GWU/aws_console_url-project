# -*- coding: utf-8 -*-

import typing as T
import dataclasses

from ..model import Service

@dataclasses.dataclass(frozen=True)
class OpenSearch(Service):
    _AWS_SERVICE = "aos"

    # --- arn

    # --- dashboard
    def _get_dashboard(self, menu: str) -> str:
        return f"{self._service_root}/home?region={self._region}#{menu}"

    @property
    def opensearch_service_dashboard(self) -> str:
        return self._get_dashboard("opensearch/dashboard")

    @property
    def opensearch_service_domain(self) -> str:
        return self._get_dashboard("opensearch/domains")

    @property
    def opensearch_service_reserved_instance_leases(self) -> str:
        return self._get_dashboard("opensearch/reserved-instances")

    @property
    def opensearch_service_packages(self) -> str:
        return self._get_dashboard("opensearch/custom-packages")

    @property
    def opensearch_service_vpc_endpoints(self) -> str:
        return self._get_dashboard("opensearch/vpc-endpoints")

    @property
    def opensearch_serverless_dashboard(self) -> str:
        return self._get_dashboard("opensearch/get-started-serverless")

    @property
    def opensearch_serverless_collections(self) -> str:
        return self._get_dashboard("opensearch/collections")

    @property
    def opensearch_serverless_security(self) -> str:
        return self._get_dashboard("opensearch/security")

    @property
    def opensearch_serverless_authentication(self) -> str:
        return self._get_dashboard("opensearch/security/authentication")

    @property
    def opensearch_serverless_access_policies(self) -> str:
        return self._get_dashboard("opensearch/security/access-policies")

    @property
    def opensearch_serverless_encryption_policies(self) -> str:
        return self._get_dashboard("opensearch/security/encryption-policies")

    @property
    def opensearch_serverless_network_policies(self) -> str:
        return self._get_dashboard("opensearch/security/network-policies")

    @property
    def opensearch_serverless_data_lifecycle_policies(self) -> str:
        return self._get_dashboard("opensearch/data-lifecycle-policies")

    @property
    def opensearch_serverless_vpc_endpoints(self) -> str:
        return self._get_dashboard("opensearch/vpcEndpoint")

    @property
    def opensearch_ingestion_dashboard(self) -> str:
        return self._get_dashboard("opensearch/ingestion-dashboard")

    @property
    def opensearch_ingestion_pipelines(self) -> str:
        return self._get_dashboard("opensearch/ingestion-pipelines")

    # --- get
    def _get_security_policy(self, type: str, name: str) -> str:
        return f"{self._service_root}/home?region={self._region}#opensearch/security/{type}/{name}"

    def get_access_policies(self, name: str) -> str:
        return self._get_security_policy("access-policies", name)

    def get_encryption_policies(self, name: str) -> str:
        return self._get_security_policy("encryption-policies", name)

    def get_network_policies(self, name: str) -> str:
        return self._get_security_policy("network-policies", name)
