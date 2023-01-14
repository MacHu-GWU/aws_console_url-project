# -*- coding: utf-8 -*-

import typing as T
import dataclasses

if T.TYPE_CHECKING:
    from .console import AWSConsole


@dataclasses.dataclass
class Builder:
    """
    Per AWS Service Console URL builder.
    """

    aws_service: str = dataclasses.field()
    aws_account_id: T.Optional[str] = dataclasses.field(default=None)
    aws_region: T.Optional[str] = dataclasses.field(default=None)
    is_us_gov_cloud: bool = dataclasses.field(default=False)

    _AWS_SERVICE: T.Optional[str] = None

    @property
    def _sub_domain(self) -> str:
        if self.is_us_gov_cloud: # pragma: no cover
            return "console.amazonaws-us-gov.com"
        else:
            return "console.aws.amazon.com"

    @property
    def _root_url(self) -> str:
        """
        Example: https://console.aws.amazon.com/ or
        https://us-east-1.console.aws.amazon.com/
        """
        if self.aws_region:
            return f"https://{self.aws_region}.{self._sub_domain}"
        else:
            return f"https://{self._sub_domain}"

    @property
    def _service_root(self) -> str:
        """
        Example: https://us-east-1.console.aws.amazon.com/s3
        """
        return f"{self._root_url}/{self.aws_service}"

    @classmethod
    def _make(
        cls,
        aws_account_id: T.Optional[str],
        aws_region: T.Optional[str],
        is_us_gov_cloud: bool,
    ) -> "Builder":
        return cls(
            aws_service=cls._AWS_SERVICE,
            aws_account_id=aws_account_id,
            aws_region=aws_region,
            is_us_gov_cloud=is_us_gov_cloud,
        )

    @classmethod
    def _from_aws_console(cls, aws_console: "AWSConsole") -> "Builder":
        return cls._make(
            aws_account_id=aws_console.aws_account_id,
            aws_region=aws_console.aws_region,
            is_us_gov_cloud=aws_console.is_us_gov_cloud,
        )
