# -*- coding: utf-8 -*-

import dataclasses
from functools import lru_cache

import aws_arns.api as aws_arns

from ..model import Service


@dataclasses.dataclass(frozen=True)
class GroundTruth(Service):
    _AWS_SERVICE = "sagemaker/groundtruth"

    def _get_workteam_obj(self, name_or_arn: str) -> aws_arns.res.SageMakerWorkteam:
        if name_or_arn.startswith("arn:"):
            return aws_arns.res.SageMakerWorkteam.from_arn(name_or_arn)
        else:
            return aws_arns.res.SageMakerWorkteam.new(
                self._account_id,
                self._region,
                name_or_arn,
            )

    # --- arn
    def get_workteam_arn(self, name: str) -> str:
        """
        Example: arn:aws:sagemaker:us-east-1:807388292768:workteam/my_workteam
        """
        return self._get_workteam_obj(name).to_arn()

    def get_private_workteam_arn(self, name: str) -> str:
        """
        Example: arn:aws:sagemaker:us-east-1:807388292768:workteam/private-crowd/my_private_workteam
        """
        if not name.startswith("private-crowd/"):
            name = "private-crowd/" + name
        return self._get_workteam_obj(name).to_arn()

    # --- Labeling Jobs
    @property
    def labeling_jobs(self) -> str:
        return f"{self._service_root}?region={self._region}#/labeling-jobs"

    # --- Labeling Datasets
    @property
    def labeling_datasets(self) -> str:
        return f"{self._service_root}?region={self._region}#/labeling-datasets"

    # --- Labeling Workforce
    @property
    def labeling_workforces(self) -> str:
        return f"{self._service_root}?region={self._region}#/labeling-workforces"

    @lru_cache(maxsize=32)
    def get_private_labeling_workforces_signin_url(self, team_name_or_arn: str) -> str:
        team_name = team_name_or_arn.split("/")[-1]
        response = self._bsm.sagemaker_client.describe_workteam(WorkteamName=team_name)
        sub_domain = response["Workteam"]["SubDomain"]
        return "https://" + sub_domain
