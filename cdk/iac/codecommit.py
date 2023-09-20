# -*- coding: utf-8 -*-

import typing as T

import aws_cdk as cdk
from aws_cdk import (
    aws_codecommit as codecommit,
    aws_codebuild as codebuild,
    aws_codepipeline as codepipeline,
    aws_codepipeline_actions as codepipeline_actions
)

if T.TYPE_CHECKING:
    from .main import MainStack


class CodeCommitMixin:
    def mk_codecommit(self: "MainStack"):
        self.codecommit_repo = codecommit.Repository(
            self,
            "CodeCommitRepo",
            repository_name=f"{self.prefix_snake}_test",
        )
        self.codecommit_repo.apply_removal_policy(cdk.RemovalPolicy.DESTROY)

        self.codebuild_project = codebuild.Project(
            self,
            "CodeBuildProject",
            project_name=f"{self.prefix_snake}_test",
            environment=codebuild.BuildEnvironment(
                build_image=codebuild.LinuxBuildImage.AMAZON_LINUX_2,
                compute_type=codebuild.ComputeType.SMALL,
            ),
            timeout=cdk.Duration.minutes(30),
            queued_timeout=cdk.Duration.minutes(15),
            concurrent_build_limit=1,
            source=codebuild.Source.code_commit(repository=self.codecommit_repo),
        )
        self.codebuild_project.apply_removal_policy(cdk.RemovalPolicy.DESTROY)

        self.code_pipeline = codepipeline.Pipeline(
            self,
            f"CodePipelinePipeline",
            pipeline_name=f"{self.prefix_snake}_test",
            # role=self.codepipeline_run_role,
            # artifact_bucket=self.i_codepipeline_artifact_bucket,
        )
        source_stage = self.code_pipeline.add_stage(stage_name="Source")
        source_artifact = codepipeline.Artifact("SourceArtifact")
        source_stage.add_action(
            codepipeline_actions.CodeCommitSourceAction(
                action_name="Source",
                repository=self.codecommit_repo,
                branch=f"release",
                output=source_artifact,
                trigger=codepipeline_actions.CodeCommitTrigger.EVENTS,
                variables_namespace="SourceVariables",
            )
        )
        approve_stage = self.code_pipeline.add_stage(stage_name="Approve")
        approve_stage.add_action(
            codepipeline_actions.ManualApprovalAction(
                action_name="Approve",
            )
        )