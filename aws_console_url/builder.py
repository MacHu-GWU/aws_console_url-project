# -*- coding: utf-8 -*-

import typing as T
import dataclasses

from boto_session_manager import BotoSesManager

if T.TYPE_CHECKING:  # pragma: no cover
    from .console import AWSConsole
    from .resource import AWSResource


@dataclasses.dataclass(frozen=True)
class ArnBuilder:
    """
    Abstract Amazon Resource Name builder for different AWS services.
    """

    aws_account_id: T.Optional[str] = dataclasses.field(default=None)
    aws_region: T.Optional[str] = dataclasses.field(default=None)

    @classmethod
    def make(cls, **kwargs) -> "ArnBuilder":
        raise NotImplementedError

    @property
    def arn(self) -> str:
        raise NotImplementedError

    @classmethod
    def from_arn(cls, arn: str) -> "ArnBuilder":
        raise NotImplementedError

    @classmethod
    def _make(
        cls,
        aws_account_id: T.Optional[str],
        aws_region: T.Optional[str],
    ) -> "ArnBuilder":
        return cls(
            aws_account_id=aws_account_id,
            aws_region=aws_region,
        )

    @classmethod
    def _from_aws_resource(cls, aws_resource: "AWSResource") -> "ArnBuilder":
        """
        Create a builder from AWSConsole object.
        """
        return cls._make(
            aws_account_id=aws_resource.aws_account_id,
            aws_region=aws_resource.aws_region,
        )


@dataclasses.dataclass(frozen=True)
class ConsoleUrlBuilder:
    """
    Per AWS Service Console URL builder.

    Note:

        This class is for internal implementation only. User should never
        create instance of this class themselves. It is managed by
        :class:`aws_console_url.console.AWSConsole` API class as property methods.
    """

    aws_service: str = dataclasses.field()
    aws_account_id: T.Optional[str] = dataclasses.field(default=None)
    aws_region: T.Optional[str] = dataclasses.field(default=None)
    is_us_gov_cloud: bool = dataclasses.field(default=False)
    bsm: BotoSesManager = dataclasses.field(default=lambda: BotoSesManager())

    _AWS_SERVICE: T.Optional[str] = None

    @property
    def _sub_domain(self) -> str:
        if self.is_us_gov_cloud:  # pragma: no cover
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
        else:  # pragma: no cover
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
        bsm: BotoSesManager,
    ) -> "ConsoleUrlBuilder":
        return cls(
            aws_service=cls._AWS_SERVICE,
            aws_account_id=aws_account_id,
            aws_region=aws_region,
            is_us_gov_cloud=is_us_gov_cloud,
            bsm=bsm,
        )

    @classmethod
    def _from_aws_console(cls, aws_console: "AWSConsole") -> "ConsoleUrlBuilder":
        """
        Create a builder from AWSConsole object.
        """
        return cls._make(
            aws_account_id=aws_console.aws_account_id,
            aws_region=aws_console.aws_region,
            is_us_gov_cloud=aws_console.is_us_gov_cloud,
            bsm=aws_console.bsm,
        )

    @property
    def _account_id(self) -> str:
        if self.aws_account_id:
            return self.aws_account_id
        else:  # pragma: no cover
            raise ValueError("aws_account_id is required!")

    @property
    def _region(self) -> str:
        if self.aws_region:
            return self.aws_region
        else:  # pragma: no cover
            raise ValueError("aws_region is required!")

    def _ensure_name(self, name_or_arn: str, converter: T.Callable) -> str:
        return converter(name_or_arn) if name_or_arn.startswith("arn:") else name_or_arn

    def _ensure_arn(self, name_or_arn: str, converter: T.Callable) -> str:
        return name_or_arn if name_or_arn.startswith("arn:") else converter(name_or_arn)
