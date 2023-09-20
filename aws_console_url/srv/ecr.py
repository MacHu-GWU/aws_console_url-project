# -*- coding: utf-8 -*-

import typing as T
import dataclasses

from ..model import BaseServiceResourceV1, Service


@dataclasses.dataclass(frozen=True)
class ECRRepo(BaseServiceResourceV1):
    name: T.Optional[str] = dataclasses.field(default=None)

    _SERVICE_NAME = "ecr"
    _RESOURCE_TYPE = "repository"

    @property
    def uri(self) -> str:
        return (
            f"{self.aws_account_id}.dkr.ecr.{self.aws_region}.amazonaws.com/{self.name}"
        )

    @classmethod
    def from_uri(cls, uri: str) -> "ECRRepo":
        domain, name = uri.split("/", 1)
        parts = domain.split(".")
        aws_account_id = parts[0]
        aws_region = parts[3]
        return cls(
            aws_account_id=aws_account_id,
            aws_region=aws_region,
            name=name,
        )


@dataclasses.dataclass(frozen=True)
class ECR(Service):
    _AWS_SERVICE = "ecr"

    # --- arn
    def get_repo_arn(self, name: str) -> str:
        """
        Get ECR repository ARN.
        """
        return ECRRepo.make(self._account_id, self._region, name).arn

    def get_repo_uri(self, name: str) -> str:
        """
        Get ECR repository URI.
        """
        return ECRRepo(self._account_id, self._region, name).uri

    # --- dashboard
    @property
    def repos(self) -> str:
        return f"{self._service_root}/repositories?region={self._region}"

    # --- repo
    def get_repo(self, name: str) -> str:
        return f"{self._service_root}/repositories/private/{self._account_id}/{name}?region={self._region}"
