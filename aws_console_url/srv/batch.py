# -*- coding: utf-8 -*-

import typing as T
import dataclasses

import aws_arns.api as aws_arns

from ..model import Service


@dataclasses.dataclass(frozen=True)
class Batch(Service):
    _AWS_SERVICE = "batch"

    # --- arn
    def _get_compute_environment_obj(
        self,
        name_or_arn: str,
    ):
        if name_or_arn.startswith("arn:"):
            return aws_arns.res.BatchComputeEnvironment.from_arn(name_or_arn)
        else:
            return aws_arns.res.BatchComputeEnvironment.new(
                self._account_id,
                self._region,
                name_or_arn,
            )

    def _get_job_queue_obj(
        self,
        name_or_arn: str,
    ):
        if name_or_arn.startswith("arn:"):
            return aws_arns.res.BatchJobQueue.from_arn(name_or_arn)
        else:
            return aws_arns.res.BatchJobQueue.new(
                self._account_id,
                self._region,
                name_or_arn,
            )

    def _get_job_definition_obj(
        self,
        name_or_arn: str,
        revision: T.Optional[int] = None,
    ):
        if name_or_arn.startswith("arn:"):
            return aws_arns.res.BatchJobDefinition.from_arn(name_or_arn)
        else:
            return aws_arns.res.BatchJobDefinition.new(
                self._account_id,
                self._region,
                name_or_arn,
                revision,
            )

    def _get_job_obj(
        self,
        job_id_or_arn: str,
    ):
        if job_id_or_arn.startswith("arn:"):
            return aws_arns.res.BatchJob.from_arn(job_id_or_arn)
        else:
            return aws_arns.res.BatchJob.new(
                self._account_id,
                self._region,
                job_id_or_arn,
            )

    def get_compute_environment_arn(self, name: str) -> str:
        return self._get_compute_environment_obj(name).to_arn()

    def get_job_queue_arn(self, name: str) -> str:
        return self._get_job_queue_obj(name).to_arn()

    def get_job_definition_arn(self, name: str, revision: int) -> str:
        return self._get_job_definition_obj(name, revision).to_arn()

    def get_job_arn(self, job_id: str) -> str:
        return self._get_job_obj(job_id).to_arn()

    # --- dashboard
    @property
    def compute_environments(self) -> str:
        return f"{self._service_root}/home?region={self._region}#compute-environments"

    @property
    def job_queues(self) -> str:
        return f"{self._service_root}/home?region={self._region}#queues"

    @property
    def job_definitions(self) -> str:
        return f"{self._service_root}/home?region={self._region}#job-definition"

    @property
    def jobs(self) -> str:
        return f"{self._service_root}/home?region={self._region}#jobs"

    def get_compute_environment(self, name_or_arn: str) -> str:
        obj = self._get_compute_environment_obj(name_or_arn)
        return (
            f"{self._service_root}/home?region={obj.aws_region}#compute-environments"
            f"/detail/{obj.to_arn()}"
        )

    def get_job_queue(self, name_or_arn: str) -> str:
        obj = self._get_job_queue_obj(name_or_arn)
        return (
            f"{self._service_root}/home?region={obj.aws_region}#queues"
            f"/detail/{obj.to_arn()}"
        )

    def get_job_definition(
        self,
        name_or_arn: str,
        revision: T.Optional[int] = None,
    ) -> str:
        obj = self._get_job_definition_obj(name_or_arn, revision)
        return (
            f"{self._service_root}/home?region={obj.aws_region}#job-definition"
            f"/detail/{obj.to_arn()}"
        )

    def get_job(self, job_id_or_arn: str) -> str:
        obj = self._get_job_obj(job_id_or_arn)
        return f"{self._service_root}/home?region={obj.aws_region}#jobs/detail/{obj.batch_job_id}"
