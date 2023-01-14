# -*- coding: utf-8 -*-

import dataclasses
from functools import lru_cache

from ..builder import Builder


@dataclasses.dataclass(frozen=True)
class GroundTruth(Builder):
    _AWS_SERVICE = "sagemaker/groundtruth"

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

    def to_private_team_arn(self, team: str) -> str:
        return f"arn:aws:sagemaker:{self._region}:{self._account_id}:workteam/private-crowd/{team}"

    def to_private_team_name(self, arn: str) -> str:
        return arn.split("/")[-1]

    @lru_cache(maxsize=32)
    def get_private_labeling_workforces_signin_url(self, team: str) -> str:
        work_team_name = self._ensure_name(team, self.to_private_team_name)
        response = self.bsm.sagemaker_client.describe_workteam(
            WorkteamName=work_team_name
        )
        sub_domain = response["Workteam"]["SubDomain"]
        return "https://" + sub_domain
