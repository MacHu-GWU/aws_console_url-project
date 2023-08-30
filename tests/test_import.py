# -*- coding: utf-8 -*-

import pytest


def test():
    import aws_console_url

    _ = aws_console_url.BotoSesManager

    aws = aws_console_url.AWSConsole()

    
    _ = aws.vpc
    _ = aws.dynamodb
    _ = aws.codecommit
    _ = aws.iam
    _ = aws.sqs
    _ = aws.secretmanager
    _ = aws.cloudformation
    _ = aws.batch
    _ = aws.ground_truth
    _ = aws.codebuild
    _ = aws.glue
    _ = aws.step_function
    _ = aws.a2i
    _ = aws.sagemaker
    _ = aws.cloudwatch
    _ = aws.ec2
    _ = aws.ecr
    _ = aws.s3
    _ = aws.awslambda
    _ = aws.ssm
    _ = aws.ecs

    aws_res = aws_console_url.resource

    
    _ = aws_res.A2IFlowDefinition
    _ = aws_res.A2IHumanTaskUI
    _ = aws_res.A2IHumanLoop
    _ = aws_res.LambdaFunction
    _ = aws_res.LambdaLayer
    _ = aws_res.BatchComputeEnvironment
    _ = aws_res.BatchJobQueue
    _ = aws_res.BatchJobDefinition
    _ = aws_res.BatchJob
    _ = aws_res.CloudFormationStack
    _ = aws_res.CloudFormationStackSet
    _ = aws_res.CloudwatchLogGroup
    _ = aws_res.CloudwatchLogStream
    _ = aws_res.CodeBuildProject
    _ = aws_res.CodeBuildRun
    _ = aws_res.CodeCommitRepository
    _ = aws_res.DynamoDBTable
    _ = aws_res.ECRRepo
    _ = aws_res.ECSCluster
    _ = aws_res.ECSTaskDefinition
    _ = aws_res.GlueDatabase
    _ = aws_res.GlueJob
    _ = aws_res.GlueCrawler
    _ = aws_res.GlueRegistry
    _ = aws_res.GlueSchema
    _ = aws_res.GlueWorkflow
    _ = aws_res.GlueTable
    _ = aws_res.GroundTruthPrivateTeam
    _ = aws_res.IamUserGroup
    _ = aws_res.IamUser
    _ = aws_res.IamRole
    _ = aws_res.IamPolicy
    _ = aws_res.SQSQueue
    _ = aws_res.SSMParameter
    _ = aws_res.StepFunctionStatemachine
    _ = aws_res.StepFunctionStatemachineExecution


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])