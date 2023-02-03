# -*- coding: utf-8 -*-

import dataclasses
from functools import lru_cache

from ..model import Service
from .sagemaker import BaseSageMakerResource


@dataclasses.dataclass(frozen=True)
class GroundTruthPrivateTeam(BaseSageMakerResource):
    _RESOURCE_TYPE = "workteam/private-crowd"


@dataclasses.dataclass(frozen=True)
class GroundTruth(Service):
    _AWS_SERVICE = "sagemaker/groundtruth"

    # --- arn
    def get_private_team_arn(self, name: str) -> str:
        return GroundTruthPrivateTeam.make(self._account_id, self._region, name).arn

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
    def private_labeling_workforces(self) -> str:
        return f"{self._service_root}?region={self._region}#/labeling-workforces"

    def _private_team_name_to_arn(self, arn: str) -> str:
        return GroundTruthPrivateTeam.from_arn(arn).name

    @lru_cache(maxsize=32)
    def get_private_labeling_workforces_signin_url(self, team_name_or_arn: str) -> str:
        work_team_name = self._ensure_name(
            team_name_or_arn, self._private_team_name_to_arn
        )
        response = self._bsm.sagemaker_client.describe_workteam(
            WorkteamName=work_team_name
        )
        sub_domain = response["Workteam"]["SubDomain"]
        return "https://" + sub_domain
