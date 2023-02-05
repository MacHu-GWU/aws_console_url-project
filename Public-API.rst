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

cloudformation
------------------------------------------------------------------------------
- ``aws_console_url.AWSConsole.cloudformation.exports``
- ``aws_console_url.AWSConsole.cloudformation.get_change_set(name: str, change_set_id: str)``
- ``aws_console_url.AWSConsole.cloudformation.get_change_set_changes(name: str, change_set_id: str)``
- ``aws_console_url.AWSConsole.cloudformation.get_change_set_hooks(name: str, change_set_id: str)``
- ``aws_console_url.AWSConsole.cloudformation.get_change_set_inputs(name: str, change_set_id: str)``
- ``aws_console_url.AWSConsole.cloudformation.get_change_set_json(name: str, change_set_id: str)``
- ``aws_console_url.AWSConsole.cloudformation.get_change_set_template(name: str, change_set_id: str)``
- ``aws_console_url.AWSConsole.cloudformation.get_stack(name: str)``
- ``aws_console_url.AWSConsole.cloudformation.get_stack_arn(name: str)``
- ``aws_console_url.AWSConsole.cloudformation.get_stack_changesets(name: str)``
- ``aws_console_url.AWSConsole.cloudformation.get_stack_events(name: str)``
- ``aws_console_url.AWSConsole.cloudformation.get_stack_info(name: str)``
- ``aws_console_url.AWSConsole.cloudformation.get_stack_outputs(name: str)``
- ``aws_console_url.AWSConsole.cloudformation.get_stack_parameters(name: str)``
- ``aws_console_url.AWSConsole.cloudformation.get_stack_resources(name: str)``
- ``aws_console_url.AWSConsole.cloudformation.stacks``
- ``aws_console_url.AWSConsole.cloudformation.stacksets``

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