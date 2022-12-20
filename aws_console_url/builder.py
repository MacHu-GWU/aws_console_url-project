# -*- coding: utf-8 -*-

import typing as T
import dataclasses


@dataclasses.dataclass
class Builder:
    aws_service: str = dataclasses.field()
    is_us_gov_cloud: bool = dataclasses.field(default=False)
    aws_account_id: T.Optional[str] = dataclasses.field(default=None)
    aws_region: T.Optional[str] = dataclasses.field(default=None)

    @property
    def _root_sub_domain(self) -> str:
        if self.is_us_gov_cloud:
            return "console.amazonaws-us-gov.com"
        else:
            return "console.aws.amazon.com"

    @property
    def _sub_domain(self) -> str:
        if self.aws_region:
            return f"https://{self.aws_region}.{self._root_sub_domain}"
        else:
            return f"https://{self._root_sub_domain}"

    @property
    def _service_root(self) -> str:
        return f"{self._sub_domain}/{self.aws_service}/"
