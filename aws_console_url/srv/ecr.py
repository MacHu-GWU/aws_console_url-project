# -*- coding: utf-8 -*-

import dataclasses

import aws_arns.api as aws_arns

from ..model import Service


@dataclasses.dataclass(frozen=True)
class ECR(Service):
    _AWS_SERVICE = "ecr"

    # --- arn
    def _get_repo_object(self, name_or_arn_or_uri: str) -> aws_arns.res.EcrRepository:
        if name_or_arn_or_uri.startswith("arn:"):
            return aws_arns.res.EcrRepository.from_arn(name_or_arn_or_uri)
        elif name_or_arn_or_uri[:12].isdigit():
            return aws_arns.res.EcrRepository.from_uri(name_or_arn_or_uri)
        else:
            return aws_arns.res.EcrRepository.new(
                self._account_id,
                self._region,
                name_or_arn_or_uri,
            )

    def get_repo_arn(self, name: str) -> str:
        """
        Get ECR repository ARN.
        """
        return self._get_repo_object(name).to_arn()

    def get_repo_uri(self, name: str) -> str:
        """
        Get ECR repository URI.
        """
        return self._get_repo_object(name).uri

    # --- dashboard
    @property
    def repos(self) -> str:
        return f"{self._service_root}/repositories?region={self._region}"

    # --- repo
    def get_repo(self, name_or_arn_or_uri: str) -> str:
        repo = self._get_repo_object(name_or_arn_or_uri)
        return (
            f"{self._service_root}/repositories/private"
            f"/{repo.aws_account_id}/{repo.repo_name}?region={repo.aws_region}"
        )
