# -*- coding: utf-8 -*-

import dataclasses
import aws_arns.api as aws_arns

from ..model import Service


@dataclasses.dataclass(frozen=True)
class AWSApiGateway(Service):
    _AWS_SERVICE = "apigateway"

    def _get_v1_rest_api(self, rest_api_id_or_arn: str):
        if rest_api_id_or_arn.startswith("arn:"):
            return aws_arns.res.ApiGatewayV1RestApi.from_arn(rest_api_id_or_arn)
        else:
            return aws_arns.res.ApiGatewayV1RestApi.new(
                aws_region=self._region,
                api_id=rest_api_id_or_arn,
            )

    def _get_v2_api(self, api_id_or_arn: str):
        if api_id_or_arn.startswith("arn:"):
            return aws_arns.res.ApiGatewayV2Api.from_arn(api_id_or_arn)
        else:
            return aws_arns.res.ApiGatewayV2Api.new(
                aws_region=self._region,
                api_id=api_id_or_arn,
            )

    def get_v1_rest_api_arn(self, rest_api_id: str) -> str:
        return self._get_v1_rest_api(rest_api_id).to_arn()

    def get_v2_api_arn(self, api_id: str) -> str:
        return self._get_v2_api(api_id).to_arn()

    # --- dashboard
    def _get_dashboard(self, name: str) -> str:
        return f"{self._service_root}/main/{name}?api=unselected&region={self._region}"

    @property
    def apis(self) -> str:
        return self._get_dashboard("apis")

    @property
    def custom_domain_names(self) -> str:
        return self._get_dashboard("publish/domain-names")

    @property
    def vpc_links(self) -> str:
        return self._get_dashboard("vpc-links")

    @property
    def usage_plans(self) -> str:
        return self._get_dashboard("usage-plans")

    @property
    def client_certificates(self) -> str:
        return self._get_dashboard("client-certificates")

    @property
    def settings(self) -> str:
        return self._get_dashboard("settings")

    # --- resource
    def _get_v1_rest_api_tab(
        self,
        rest_api_id: str,
        tab: str,
    ) -> str:
        obj = self._get_v1_rest_api(rest_api_id)
        return f"{self._service_root}/main/apis/{obj.api_id}/{tab}?api={obj.api_id}&region={self._region}"

    def get_v1_rest_api(self, rest_api_id: str) -> str:
        return self._get_v1_rest_api_tab(rest_api_id, "resources")

    def get_v1_rest_api_resources_tab(self, rest_api_id: str) -> str:
        return self._get_v1_rest_api_tab(rest_api_id, "resources")

    def get_v1_rest_api_stages_tab(self, rest_api_id: str) -> str:
        return self._get_v1_rest_api_tab(rest_api_id, "stages")

    def get_v1_rest_api_authorizers_tab(self, rest_api_id: str) -> str:
        return self._get_v1_rest_api_tab(rest_api_id, "authorizers")

    def get_v1_rest_api_gateway_responses_tab(self, rest_api_id: str) -> str:
        return self._get_v1_rest_api_tab(rest_api_id, "gateway-responses")

    def get_v1_rest_api_models_tab(self, rest_api_id: str) -> str:
        return self._get_v1_rest_api_tab(rest_api_id, "models")

    def get_v1_rest_api_resource_policy_tab(self, rest_api_id: str) -> str:
        return self._get_v1_rest_api_tab(rest_api_id, "resource-policy")

    def get_v1_rest_api_documentation_tab(self, rest_api_id: str) -> str:
        return self._get_v1_rest_api_tab(rest_api_id, "documentation")

    def get_v1_rest_api_dashboard_tab(self, rest_api_id: str) -> str:
        return self._get_v1_rest_api_tab(rest_api_id, "dashboard")

    def get_v1_rest_api_api_detail_tab(self, rest_api_id: str) -> str:
        return self._get_v1_rest_api_tab(rest_api_id, "api-detail")

    def _get_v2_api_tab(
        self,
        api_id: str,
        tab: str,
    ) -> str:
        obj = self._get_v2_api(api_id)
        return f"{self._service_root}/main/{tab}?api={obj.api_id}&region={self._region}"

    def get_v2_api(self, rest_api_id: str) -> str:
        return self._get_v2_api_tab(rest_api_id, "develop/routes")

    def get_v2_api_routes_tab(self, rest_api_id: str) -> str:
        return self._get_v2_api_tab(rest_api_id, "develop/routes")

    def get_v2_api_authorization_tab(self, rest_api_id: str) -> str:
        return self._get_v2_api_tab(rest_api_id, "develop/auth/attach")

    def get_v2_api_integrations_tab(self, rest_api_id: str) -> str:
        return self._get_v2_api_tab(rest_api_id, "develop/integrations")

    def get_v2_api_cors_tab(self, rest_api_id: str) -> str:
        return self._get_v2_api_tab(rest_api_id, "develop/cors")

    def get_v2_api_reimport_tab(self, rest_api_id: str) -> str:
        return self._get_v2_api_tab(rest_api_id, "develop/reimport")

    def get_v2_api_export_tab(self, rest_api_id: str) -> str:
        return self._get_v2_api_tab(rest_api_id, "develop/export")

    def get_v2_api_stages_tab(self, rest_api_id: str) -> str:
        return self._get_v2_api_tab(rest_api_id, "deploy/stages")

    def get_v2_api_metrics_tab(self, rest_api_id: str) -> str:
        return self._get_v2_api_tab(rest_api_id, "monitor/metrics")

    def get_v2_api_logging_tab(self, rest_api_id: str) -> str:
        return self._get_v2_api_tab(rest_api_id, "monitor/logging")

    def get_v2_api_throttling_tab(self, rest_api_id: str) -> str:
        return self._get_v2_api_tab(rest_api_id, "protect/throttling")
