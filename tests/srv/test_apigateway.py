# -*- coding: utf-8 -*-

from aws_console_url.tests import console


def test():
    rest_api_id = "bd6adna8zc"
    api_id = "6lzpmnaqgk"

    rest_api_arn = console.apigateway.get_v1_rest_api_arn(rest_api_id)
    api_arn = console.apigateway.get_v2_api_arn(api_id)

    # --- console
    print("-" * 80)
    print(console.apigateway.apis)
    print(console.apigateway.custom_domain_names)
    print(console.apigateway.vpc_links)
    print(console.apigateway.usage_plans)
    print(console.apigateway.client_certificates)
    print(console.apigateway.settings)

    print("-" * 80)
    "https://eu-west-1.console.aws.amazon.com/apigateway/main/apis/bd6adna8zc/resources?api=bd6adna8zc&region=eu-west-1"
    "https://eu-west-1.console.aws.amazon.com/apigateway/main/apis/eu-west-1/resources?api=eu-west-1&region=eu-west-1"
    print(console.apigateway.get_v1_rest_api(rest_api_id))
    print(console.apigateway.get_v1_rest_api_resources_tab(rest_api_id))
    print(console.apigateway.get_v1_rest_api_stages_tab(rest_api_id))
    print(console.apigateway.get_v1_rest_api_authorizers_tab(rest_api_id))
    print(console.apigateway.get_v1_rest_api_gateway_responses_tab(rest_api_id))
    print(console.apigateway.get_v1_rest_api_models_tab(rest_api_id))
    print(console.apigateway.get_v1_rest_api_resource_policy_tab(rest_api_id))
    print(console.apigateway.get_v1_rest_api_documentation_tab(rest_api_id))
    print(console.apigateway.get_v1_rest_api_dashboard_tab(rest_api_id))
    print(console.apigateway.get_v1_rest_api_api_detail_tab(rest_api_id))

    print("-" * 80)
    print(console.apigateway.get_v2_api(api_id))
    print(console.apigateway.get_v2_api_routes_tab(api_id))
    print(console.apigateway.get_v2_api_authorization_tab(api_id))
    print(console.apigateway.get_v2_api_integrations_tab(api_id))
    print(console.apigateway.get_v2_api_cors_tab(api_id))
    print(console.apigateway.get_v2_api_reimport_tab(api_id))
    print(console.apigateway.get_v2_api_export_tab(api_id))
    print(console.apigateway.get_v2_api_stages_tab(api_id))
    print(console.apigateway.get_v2_api_metrics_tab(api_id))
    print(console.apigateway.get_v2_api_logging_tab(api_id))
    print(console.apigateway.get_v2_api_throttling_tab(api_id))


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.srv.a2i", preview=False)
