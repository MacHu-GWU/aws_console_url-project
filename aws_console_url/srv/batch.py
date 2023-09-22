# -*- coding: utf-8 -*-

import typing as T
import dataclasses

import aws_arns.api as aws_arns

from ..model import Service


@dataclasses.dataclass(frozen=True)
class Batch(Service):
    _AWS_SERVICE = "batch"

    # --- arn
    def get_compute_environment_arn(self, name: str) -> str:
        return aws_arns.res.BatchComputeEnvironment.new(
            self._account_id,
            self._region,
            name,
        ).to_arn()

    def get_job_queue_arn(self, name: str) -> str:
        return aws_arns.res.BatchJobQueue.new(
            self._account_id,
            self._region,
            name,
        ).to_arn()

    def get_job_definition_arn(self, name: str, revision: int) -> str:
        return aws_arns.res.BatchJobDefinition.new(
            self._account_id,
            self._region,
            name,
            revision,
        ).to_arn()

    def get_job_arn(self, job_id: str) -> str:
        return aws_arns.res.BatchJob.new(
            self._account_id,
            self._region,
            job_id,
        ).to_arn()

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

    def _arn_to_name(self, arn: str) -> str:
        return arn.split("/")[-1]

    def get_compute_environment(self, name_or_arn: str) -> str:
        name = self._ensure_name(name_or_arn, self._arn_to_name)
        return (
            f"{self._service_root}/home?region={self._region}#compute-environments"
            f"/detail/arn:aws:batch:{self._region}:{self._account_id}:compute-environment"
            f"/{name}"
        )

    def get_job_queue(self, name_or_arn: str) -> str:
        name = self._ensure_name(name_or_arn, self._arn_to_name)
        return (
            f"{self._service_root}/home?region={self._region}#queues"
            f"/detail/arn:aws:batch:{self._region}:{self._account_id}:job-queue"
            f"/{name}"
        )

    def get_job_definition(
        self,
        name_or_arn: str,
        revision: T.Optional[int] = None,
    ) -> str:
        if name_or_arn.startswith("arn:"):
            if revision is not None:  # pragma: no cover
                raise ValueError("revision must be None if name_or_arn is an ARN")
            else:
                name_and_revision = name_or_arn.split("/")[-1]
        else:
            if revision is None:  # pragma: no cover
                raise ValueError("revision must be specified if name_or_arn is a name")
            else:
                name_and_revision = f"{name_or_arn}:{revision}"
        return (
            f"{self._service_root}/home?region={self._region}#job-definition"
            f"/detail/arn:aws:batch:{self._region}:{self._account_id}:job-definition"
            f"/{name_and_revision}"
        )

    def get_job(self, job_id_or_arn: str) -> str:
        job_id = self._ensure_name(job_id_or_arn, self._arn_to_name)
        return f"{self._service_root}/home?region={self._region}#jobs/detail/{job_id}"
