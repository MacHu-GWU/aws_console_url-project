Public API
==============================================================================
.. contents::
    :depth: 1
    :local:

a2i
------------------------------------------------------------------------------
- ``aws_console_url.AWSConsole.a2i.get_human_loop(flow_name_or_arn: str, human_loop_name_or_arn: str)``
- ``aws_console_url.AWSConsole.a2i.get_human_loop_arn(name: str)``
- ``aws_console_url.AWSConsole.a2i.get_human_review_workflow(name_or_arn: str)``
- ``aws_console_url.AWSConsole.a2i.get_human_review_workflow_arn(name: str)``
- ``aws_console_url.AWSConsole.a2i.get_worker_task_template(name_or_arn: str)``
- ``aws_console_url.AWSConsole.a2i.get_worker_task_template_arn(name: str)``
- ``aws_console_url.AWSConsole.a2i.human_review_workflows``
- ``aws_console_url.AWSConsole.a2i.human_review_workforces``
- ``aws_console_url.AWSConsole.a2i.worker_task_templates``

awslambda
------------------------------------------------------------------------------
- ``aws_console_url.AWSConsole.awslambda.filter_functions(name: str)``
- ``aws_console_url.AWSConsole.awslambda.functions``
- ``aws_console_url.AWSConsole.awslambda.get_function(name: str)``
- ``aws_console_url.AWSConsole.awslambda.get_function_alias(name: str, alias: str)``
- ``aws_console_url.AWSConsole.awslambda.get_function_alias_tab(name: str)``
- ``aws_console_url.AWSConsole.awslambda.get_function_arn(name: str, version: Union[int, NoneType] = None, alias: Union[str, NoneType] = None)``
- ``aws_console_url.AWSConsole.awslambda.get_function_code_tab(name: str)``
- ``aws_console_url.AWSConsole.awslambda.get_function_config_tab(name: str)``
- ``aws_console_url.AWSConsole.awslambda.get_function_monitor_tab(name: str)``
- ``aws_console_url.AWSConsole.awslambda.get_function_test_tab(name: str)``
- ``aws_console_url.AWSConsole.awslambda.get_function_version(name: str, version: int)``
- ``aws_console_url.AWSConsole.awslambda.get_function_version_tab(name: str)``
- ``aws_console_url.AWSConsole.awslambda.get_layer(name: str, version: int = 1)``
- ``aws_console_url.AWSConsole.awslambda.get_layer_arn(name: str, version: int)``
- ``aws_console_url.AWSConsole.awslambda.layers``

batch
------------------------------------------------------------------------------
- ``aws_console_url.AWSConsole.batch.compute_environments``
- ``aws_console_url.AWSConsole.batch.get_compute_environment(name_or_arn: str)``
- ``aws_console_url.AWSConsole.batch.get_compute_environment_arn(name: str)``
- ``aws_console_url.AWSConsole.batch.get_job(job_id_or_arn: str)``
- ``aws_console_url.AWSConsole.batch.get_job_arn(job_id: str)``
- ``aws_console_url.AWSConsole.batch.get_job_definition(name_or_arn: str, revision: Union[int, NoneType] = None)``
- ``aws_console_url.AWSConsole.batch.get_job_definition_arn(name: str, revision: int)``
- ``aws_console_url.AWSConsole.batch.get_job_queue(name_or_arn: str)``
- ``aws_console_url.AWSConsole.batch.get_job_queue_arn(name: str)``
- ``aws_console_url.AWSConsole.batch.job_definitions``
- ``aws_console_url.AWSConsole.batch.job_queues``
- ``aws_console_url.AWSConsole.batch.jobs``

cloudformation
------------------------------------------------------------------------------
- ``aws_console_url.AWSConsole.cloudformation.ensure_arn(name_or_arn: str)``
- ``aws_console_url.AWSConsole.cloudformation.exports``
- ``aws_console_url.AWSConsole.cloudformation.filter_self_managed_stack_set(name: str)``
- ``aws_console_url.AWSConsole.cloudformation.filter_service_managed_stack_set(name: str)``
- ``aws_console_url.AWSConsole.cloudformation.filter_stack(name: str)``
- ``aws_console_url.AWSConsole.cloudformation.get_change_set(stack_name_or_arn: str, change_set_id: str)``
- ``aws_console_url.AWSConsole.cloudformation.get_change_set_changes(stack_name_or_arn: str, change_set_id: str)``
- ``aws_console_url.AWSConsole.cloudformation.get_change_set_hooks(stack_name_or_arn: str, change_set_id: str)``
- ``aws_console_url.AWSConsole.cloudformation.get_change_set_inputs(stack_name_or_arn: str, change_set_id: str)``
- ``aws_console_url.AWSConsole.cloudformation.get_change_set_json(stack_name_or_arn: str, change_set_id: str)``
- ``aws_console_url.AWSConsole.cloudformation.get_change_set_template(stack_name_or_arn: str, change_set_id: str)``
- ``aws_console_url.AWSConsole.cloudformation.get_stack(name_or_arn: str)``
- ``aws_console_url.AWSConsole.cloudformation.get_stack_arn(name: str)``
- ``aws_console_url.AWSConsole.cloudformation.get_stack_changesets(name_or_arn: str)``
- ``aws_console_url.AWSConsole.cloudformation.get_stack_events(name_or_arn: str)``
- ``aws_console_url.AWSConsole.cloudformation.get_stack_info(name_or_arn: str)``
- ``aws_console_url.AWSConsole.cloudformation.get_stack_outputs(name_or_arn: str)``
- ``aws_console_url.AWSConsole.cloudformation.get_stack_parameters(name_or_arn: str)``
- ``aws_console_url.AWSConsole.cloudformation.get_stack_resources(name_or_arn: str)``
- ``aws_console_url.AWSConsole.cloudformation.get_stack_set_arn(name: str, is_self_managed: bool = False, is_service_managed: bool = False)``
- ``aws_console_url.AWSConsole.cloudformation.get_stack_set_info(name_or_id_or_arn: str, is_self_managed: bool = False, is_service_managed: bool = False)``
- ``aws_console_url.AWSConsole.cloudformation.get_stack_set_instances(name_or_id_or_arn: str, is_self_managed: bool = False, is_service_managed: bool = False)``
- ``aws_console_url.AWSConsole.cloudformation.get_stack_set_operations(name_or_id_or_arn: str, is_self_managed: bool = False, is_service_managed: bool = False)``
- ``aws_console_url.AWSConsole.cloudformation.get_stack_set_parameters(name_or_id_or_arn: str, is_self_managed: bool = False, is_service_managed: bool = False)``
- ``aws_console_url.AWSConsole.cloudformation.get_stack_set_template(name_or_id_or_arn: str, is_self_managed: bool = False, is_service_managed: bool = False)``
- ``aws_console_url.AWSConsole.cloudformation.stacks``
- ``aws_console_url.AWSConsole.cloudformation.stacksets``
- ``aws_console_url.AWSConsole.cloudformation.stacksets_self_managed``
- ``aws_console_url.AWSConsole.cloudformation.stacksets_service_managed``

cloudwatch
------------------------------------------------------------------------------
- ``aws_console_url.AWSConsole.cloudwatch.filter_log_event(group_name: str, stream_name: str, pattern: str)``
- ``aws_console_url.AWSConsole.cloudwatch.filter_log_event_by_lambda_request_id(func_name: str, request_id: str, lookback_seconds: int = 86400)``
- ``aws_console_url.AWSConsole.cloudwatch.filter_log_groups(pattern: str)``
- ``aws_console_url.AWSConsole.cloudwatch.filter_log_streams(group_name: str, pattern: str)``
- ``aws_console_url.AWSConsole.cloudwatch.get_log_group(name: str)``
- ``aws_console_url.AWSConsole.cloudwatch.get_log_group_arn(name: str)``
- ``aws_console_url.AWSConsole.cloudwatch.get_log_group_log_streams_tab(name: str)``
- ``aws_console_url.AWSConsole.cloudwatch.get_log_stream(group_name: str, stream_name: str)``
- ``aws_console_url.AWSConsole.cloudwatch.log_groups``

codebuild
------------------------------------------------------------------------------
- ``aws_console_url.AWSConsole.codebuild.build_history``
- ``aws_console_url.AWSConsole.codebuild.build_projects``
- ``aws_console_url.AWSConsole.codebuild.get_build_project_arn(name: str)``
- ``aws_console_url.AWSConsole.codebuild.get_build_run(is_batch: bool, project_name: str, run_id: str)``
- ``aws_console_url.AWSConsole.codebuild.get_build_run_arn(is_batch: bool, project_name: str, run_id: str)``
- ``aws_console_url.AWSConsole.codebuild.get_build_run_env_var(is_batch: bool, project_name: str, run_id: str)``
- ``aws_console_url.AWSConsole.codebuild.get_build_run_phase(is_batch: bool, project_name: str, run_id: str)``
- ``aws_console_url.AWSConsole.codebuild.get_project(project: str)``
- ``aws_console_url.AWSConsole.codebuild.metrics``
- ``aws_console_url.AWSConsole.codebuild.report_groups``
- ``aws_console_url.AWSConsole.codebuild.report_history``

codecommit
------------------------------------------------------------------------------
- ``aws_console_url.AWSConsole.codecommit.get_browse_branch(repo: str, branch: str, path: Union[str, NoneType] = None)``
- ``aws_console_url.AWSConsole.codecommit.get_browse_commit(repo: str, commit_id: str, path: Union[str, NoneType] = None)``
- ``aws_console_url.AWSConsole.codecommit.get_browse_tag(repo: str, tag: str, path: Union[str, NoneType] = None)``
- ``aws_console_url.AWSConsole.codecommit.get_commit(repo: str, commit_id: str)``
- ``aws_console_url.AWSConsole.codecommit.get_pr(repo: str, pr_id: int)``
- ``aws_console_url.AWSConsole.codecommit.get_pr_activity(repo: str, pr_id: int)``
- ``aws_console_url.AWSConsole.codecommit.get_pr_approvals(repo: str, pr_id: int)``
- ``aws_console_url.AWSConsole.codecommit.get_pr_changes(repo: str, pr_id: int)``
- ``aws_console_url.AWSConsole.codecommit.get_pr_commits(repo: str, pr_id: int)``
- ``aws_console_url.AWSConsole.codecommit.get_pr_details(repo: str, pr_id: int)``
- ``aws_console_url.AWSConsole.codecommit.get_repo(repo: str)``
- ``aws_console_url.AWSConsole.codecommit.get_repo_arn(name: str)``
- ``aws_console_url.AWSConsole.codecommit.get_repo_branches(repo: str)``
- ``aws_console_url.AWSConsole.codecommit.get_repo_commits(repo: str)``
- ``aws_console_url.AWSConsole.codecommit.get_repo_prs(repo: str)``
- ``aws_console_url.AWSConsole.codecommit.get_repo_settings(repo: str)``
- ``aws_console_url.AWSConsole.codecommit.get_repo_tags(repo: str)``
- ``aws_console_url.AWSConsole.codecommit.repositories``

dynamodb
------------------------------------------------------------------------------
- ``aws_console_url.AWSConsole.dynamodb.get_item_details(table: str, hash_key: Any, range_key: Union[Any, NoneType] = None)``
- ``aws_console_url.AWSConsole.dynamodb.get_table_arn(name: str)``
- ``aws_console_url.AWSConsole.dynamodb.get_table_items(table: str)``
- ``aws_console_url.AWSConsole.dynamodb.get_table_overview(table: str)``
- ``aws_console_url.AWSConsole.dynamodb.tables``

ec2
------------------------------------------------------------------------------
- ``aws_console_url.AWSConsole.ec2.amis``
- ``aws_console_url.AWSConsole.ec2.filter_amis_by_name(facets: Union[str, List[str]])``
- ``aws_console_url.AWSConsole.ec2.filter_instances_by_name(facets: Union[str, List[str]])``
- ``aws_console_url.AWSConsole.ec2.get_ami(image_id: str)``
- ``aws_console_url.AWSConsole.ec2.get_instance(instance_id: str)``
- ``aws_console_url.AWSConsole.ec2.instances``

ecr
------------------------------------------------------------------------------
- ``aws_console_url.AWSConsole.ecr.get_repo(name: str)``
- ``aws_console_url.AWSConsole.ecr.get_repo_uri(name: str)``
- ``aws_console_url.AWSConsole.ecr.repos``

ecs
------------------------------------------------------------------------------
- ``aws_console_url.AWSConsole.ecs.clusters``
- ``aws_console_url.AWSConsole.ecs.get_cluster_arn(name: str)``
- ``aws_console_url.AWSConsole.ecs.get_cluster_cluster_metrics(name_or_arn: str)``
- ``aws_console_url.AWSConsole.ecs.get_cluster_infrastructure(name_or_arn: str)``
- ``aws_console_url.AWSConsole.ecs.get_cluster_scheduled_tasks(name_or_arn: str)``
- ``aws_console_url.AWSConsole.ecs.get_cluster_services(name_or_arn: str)``
- ``aws_console_url.AWSConsole.ecs.get_cluster_tags(name_or_arn: str)``
- ``aws_console_url.AWSConsole.ecs.get_cluster_tasks(name_or_arn: str)``
- ``aws_console_url.AWSConsole.ecs.get_task_configuration(cluster_name_or_arn: str, task_id: str)``
- ``aws_console_url.AWSConsole.ecs.get_task_definition_arn(name: str, revision: int)``
- ``aws_console_url.AWSConsole.ecs.get_task_definition_revision_containers(name_or_arn: str, revision: Union[int, NoneType] = None)``
- ``aws_console_url.AWSConsole.ecs.get_task_definition_revision_json(name_or_arn: str, revision: Union[int, NoneType] = None)``
- ``aws_console_url.AWSConsole.ecs.get_task_definition_revision_storage(name_or_arn: str, revision: Union[int, NoneType] = None)``
- ``aws_console_url.AWSConsole.ecs.get_task_definition_revision_tags(name_or_arn: str, revision: Union[int, NoneType] = None)``
- ``aws_console_url.AWSConsole.ecs.get_task_definition_revisions(name_or_arn: str)``
- ``aws_console_url.AWSConsole.ecs.get_task_logs(cluster_name_or_arn: str, task_id: str)``
- ``aws_console_url.AWSConsole.ecs.get_task_networking(cluster_name_or_arn: str, task_id: str)``
- ``aws_console_url.AWSConsole.ecs.get_task_tags(cluster_name_or_arn: str, task_id: str)``
- ``aws_console_url.AWSConsole.ecs.task_definitions``

glue
------------------------------------------------------------------------------
- ``aws_console_url.AWSConsole.glue.classifiers``
- ``aws_console_url.AWSConsole.glue.crawlers``
- ``aws_console_url.AWSConsole.glue.databases``
- ``aws_console_url.AWSConsole.glue.get_crawler(name: str)``
- ``aws_console_url.AWSConsole.glue.get_crawler_arn(name: str)``
- ``aws_console_url.AWSConsole.glue.get_database(database: str, catalog_id: Union[str, NoneType] = None)``
- ``aws_console_url.AWSConsole.glue.get_database_arn(name: str)``
- ``aws_console_url.AWSConsole.glue.get_job(name: str)``
- ``aws_console_url.AWSConsole.glue.get_job_arn(name: str)``
- ``aws_console_url.AWSConsole.glue.get_table(database: str, table: str, catalog_id: Union[str, NoneType] = None)``
- ``aws_console_url.AWSConsole.glue.get_table_arn(database: str, table: str)``
- ``aws_console_url.AWSConsole.glue.jobs``
- ``aws_console_url.AWSConsole.glue.tables``

ground_truth
------------------------------------------------------------------------------
- ``aws_console_url.AWSConsole.ground_truth.get_private_labeling_workforces_signin_url(team_name_or_arn: str)``
- ``aws_console_url.AWSConsole.ground_truth.get_private_team_arn(name: str)``
- ``aws_console_url.AWSConsole.ground_truth.labeling_datasets``
- ``aws_console_url.AWSConsole.ground_truth.labeling_jobs``
- ``aws_console_url.AWSConsole.ground_truth.private_labeling_workforces``

iam
------------------------------------------------------------------------------
- ``aws_console_url.AWSConsole.iam.get_policy(name_or_arn: str)``
- ``aws_console_url.AWSConsole.iam.get_policy_arn(name: str)``
- ``aws_console_url.AWSConsole.iam.get_role(name_or_arn: str)``
- ``aws_console_url.AWSConsole.iam.get_role_arn(name: str)``
- ``aws_console_url.AWSConsole.iam.get_user(name_or_arn: str)``
- ``aws_console_url.AWSConsole.iam.get_user_arn(name: str)``
- ``aws_console_url.AWSConsole.iam.get_user_group(name_or_arn: str)``
- ``aws_console_url.AWSConsole.iam.get_user_group_arn(name: str)``
- ``aws_console_url.AWSConsole.iam.groups``
- ``aws_console_url.AWSConsole.iam.policies``
- ``aws_console_url.AWSConsole.iam.roles``
- ``aws_console_url.AWSConsole.iam.users``

rds
------------------------------------------------------------------------------
- ``aws_console_url.AWSConsole.rds.databases``
- ``aws_console_url.AWSConsole.rds.db_parameter_groups``
- ``aws_console_url.AWSConsole.rds.db_subnet_groups``
- ``aws_console_url.AWSConsole.rds.get_database_cluster(identifier: str)``
- ``aws_console_url.AWSConsole.rds.get_database_instance(identifier: str)``
- ``aws_console_url.AWSConsole.rds.get_db_parameter_group(name: str)``
- ``aws_console_url.AWSConsole.rds.get_db_subnet_group(name_or_arn: str)``
- ``aws_console_url.AWSConsole.rds.snapshots``

s3
------------------------------------------------------------------------------
- ``aws_console_url.AWSConsole.s3.buckets``
- ``aws_console_url.AWSConsole.s3.get_console_url(bucket: Union[str, NoneType] = None, prefix: Union[str, NoneType] = None, s3_uri: Union[str, NoneType] = None)``
- ``aws_console_url.AWSConsole.s3.get_s3_select_console_url(bucket: Union[str, NoneType] = None, key: Union[str, NoneType] = None, s3_uri: Union[str, NoneType] = None)``

sagemaker
------------------------------------------------------------------------------
- ``aws_console_url.AWSConsole.sagemaker.batch_transform_jobs``
- ``aws_console_url.AWSConsole.sagemaker.inference_endpoints``
- ``aws_console_url.AWSConsole.sagemaker.models``
- ``aws_console_url.AWSConsole.sagemaker.notebooks``
- ``aws_console_url.AWSConsole.sagemaker.processing_jobs``
- ``aws_console_url.AWSConsole.sagemaker.training_jobs``

secretmanager
------------------------------------------------------------------------------
- ``aws_console_url.AWSConsole.secretmanager.filter_secrets(facets: Union[str, List[str]])``
- ``aws_console_url.AWSConsole.secretmanager.get_secret(name: str)``
- ``aws_console_url.AWSConsole.secretmanager.secrets``

sns
------------------------------------------------------------------------------
- ``aws_console_url.AWSConsole.sns.get_subscription(topic_name_or_subscription_arn: str, subscription_id: Union[str, NoneType] = None)``
- ``aws_console_url.AWSConsole.sns.get_subscription_arn(topic_name: str, subscription_id: str)``
- ``aws_console_url.AWSConsole.sns.get_topic(name_or_arn: str)``
- ``aws_console_url.AWSConsole.sns.get_topic_arn(name: str)``
- ``aws_console_url.AWSConsole.sns.subscriptions``
- ``aws_console_url.AWSConsole.sns.topics``

sqs
------------------------------------------------------------------------------
- ``aws_console_url.AWSConsole.sqs.get_queue(name: str)``
- ``aws_console_url.AWSConsole.sqs.get_queue_arn(name: str)``
- ``aws_console_url.AWSConsole.sqs.get_queue_send_and_receive_message(name: str)``
- ``aws_console_url.AWSConsole.sqs.get_queue_url(name: str)``
- ``aws_console_url.AWSConsole.sqs.queues``

ssm
------------------------------------------------------------------------------
- ``aws_console_url.AWSConsole.ssm.filter_parameters(facets: Union[str, List[str]])``
- ``aws_console_url.AWSConsole.ssm.get_parameter(name_or_arn: str)``
- ``aws_console_url.AWSConsole.ssm.get_parameter_arn(name: str)``
- ``aws_console_url.AWSConsole.ssm.parameters``

step_function
------------------------------------------------------------------------------
- ``aws_console_url.AWSConsole.step_function.get_state_machine_arn(name: str)``
- ``aws_console_url.AWSConsole.step_function.get_state_machine_edit_tab(name_or_arn: str)``
- ``aws_console_url.AWSConsole.step_function.get_state_machine_execution(name_or_arn: str, short_id: Union[str, NoneType] = None)``
- ``aws_console_url.AWSConsole.step_function.get_state_machine_execution_arn(name: str, short_id: str)``
- ``aws_console_url.AWSConsole.step_function.get_state_machine_view_tab(name_or_arn: str)``
- ``aws_console_url.AWSConsole.step_function.get_state_machine_visual_editor(name_or_arn: str)``
- ``aws_console_url.AWSConsole.step_function.state_machines``

vpc
------------------------------------------------------------------------------
- ``aws_console_url.AWSConsole.vpc.elastic_ips``
- ``aws_console_url.AWSConsole.vpc.endpoints``
- ``aws_console_url.AWSConsole.vpc.filter_elastic_ips(facets: Union[str, List[str]])``
- ``aws_console_url.AWSConsole.vpc.filter_endpoints(facets: Union[str, List[str]])``
- ``aws_console_url.AWSConsole.vpc.filter_internet_gateways(facets: Union[str, List[str]])``
- ``aws_console_url.AWSConsole.vpc.filter_nat_gateways(facets: Union[str, List[str]])``
- ``aws_console_url.AWSConsole.vpc.filter_network_acls(facets: Union[str, List[str]])``
- ``aws_console_url.AWSConsole.vpc.filter_route_tables(facets: Union[str, List[str]])``
- ``aws_console_url.AWSConsole.vpc.filter_security_groups(facets: Union[str, List[str]])``
- ``aws_console_url.AWSConsole.vpc.filter_subnets(facets: Union[str, List[str]])``
- ``aws_console_url.AWSConsole.vpc.filter_vpcs(facets: Union[str, List[str]])``
- ``aws_console_url.AWSConsole.vpc.internet_gateways``
- ``aws_console_url.AWSConsole.vpc.nat_gateways``
- ``aws_console_url.AWSConsole.vpc.network_acls``
- ``aws_console_url.AWSConsole.vpc.route_tables``
- ``aws_console_url.AWSConsole.vpc.security_groups``
- ``aws_console_url.AWSConsole.vpc.subnets``
- ``aws_console_url.AWSConsole.vpc.vpcs``