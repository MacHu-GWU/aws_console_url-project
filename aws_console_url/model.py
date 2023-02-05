# -*- coding: utf-8 -*-

import typing as T
import dataclasses

from boto_session_manager import BotoSesManager

if T.TYPE_CHECKING:  # pragma: no cover
    from .console import AWSConsole
    from .resource import AWSResource


@dataclasses.dataclass(frozen=True)
class Resource:
    """
    Represent an AWS Resource. Resource usually has an Amazon Resource Name (ARN).
    This class is the base class for all Amazon Resource.

    Some AWS resource is global and some AWS resource is regional.

    Ref:

    - AWS Regional Services: https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/?p=ngi&loc=4
    """

    aws_account_id: T.Optional[str] = dataclasses.field(default=None)
    aws_region: T.Optional[str] = dataclasses.field(default=None)

    @classmethod
    def make(cls, **kwargs) -> "Resource":
        """
        An abstract factory method that creates an instance of a :class:`Resource`.
        """
        raise NotImplementedError

    @property
    def arn(self) -> str:
        """
        A property method that returns the ARN string.
        """
        raise NotImplementedError

    @classmethod
    def from_arn(cls, arn: str) -> "Resource":
        """
        An abstract class method that creates an instance of a :class:`Resource`
        from ARN.
        """
        raise NotImplementedError


@dataclasses.dataclass(frozen=True)
class BaseServiceResourceV1(Resource):
    name: T.Optional[str] = dataclasses.field(default=None)

    _service_name: T.Optional[str] = dataclasses.field(default=None)
    _resource_type: T.Optional[str] = dataclasses.field(default=None)

    _SERVICE_NAME: T.Optional[str] = None
    _RESOURCE_TYPE: T.Optional[str] = None

    @classmethod
    def make(
        cls,
        aws_account_id: str,
        aws_region: str,
        name: str,
    ) -> "BaseServiceResourceV1":
        return cls(
            aws_account_id=aws_account_id,
            aws_region=aws_region,
            name=name,
            _service_name=cls._SERVICE_NAME,
            _resource_type=cls._RESOURCE_TYPE,
        )

    @property
    def arn(self) -> str:
        return f"arn:aws:{self._service_name}:{self.aws_region}:{self.aws_account_id}:{self._resource_type}/{self.name}"

    @classmethod
    def from_arn(cls, arn: str) -> "BaseServiceResourceV1":
        parts = arn.split(":")
        aws_account_id = parts[4]
        aws_region = parts[3]
        name = parts[5].split("/")[-1]
        return cls.make(aws_account_id, aws_region, name)


@dataclasses.dataclass(frozen=True)
class Service:
    """
    Represent an AWS Service. This class is mainly for creating AWS console urls.

    This class is the base class for all Amazon Service. All methods not start
    with "_" are public API.


    :param aws_service: the URL component right after the "aws.amazon.com/".
        for example, the S3 console url is https://us-east-1.console.aws.amazon.com/s3/buckets?region=us-east-1
        then the aws_service is "s3".
    :param aws_account_id: the aws account id.
    :param aws_region: the aws region.
    :param is_us_gov_cloud: is this US gov cloud.
    :param bsm: the ``boto_session_manager.BotoSesManager`` object, will be used
        to call AWS API.
    """

    _aws_service: T.Optional[str] = dataclasses.field(default=None)
    _aws_account_id: T.Optional[str] = dataclasses.field(default=None)
    _aws_region: T.Optional[str] = dataclasses.field(default=None)
    _is_us_gov_cloud: bool = dataclasses.field(default=False)
    _bsm: BotoSesManager = dataclasses.field(default=lambda: BotoSesManager())

    _AWS_SERVICE: T.Optional[str] = None

    @classmethod
    def _make(
        cls,
        aws_account_id: T.Optional[str],
        aws_region: T.Optional[str],
        is_us_gov_cloud: bool,
        bsm: BotoSesManager,
    ) -> "Service":
        return cls(
            _aws_service=cls._AWS_SERVICE,
            _aws_account_id=aws_account_id,
            _aws_region=aws_region,
            _is_us_gov_cloud=is_us_gov_cloud,
            _bsm=bsm,
        )

    @property
    def _sub_domain(self) -> str:
        if self._is_us_gov_cloud:  # pragma: no cover
            return "console.amazonaws-us-gov.com"
        else:
            return "console.aws.amazon.com"

    @property
    def _account_id(self) -> str:
        """

        :return:
        """
        if self._aws_account_id:
            return self._aws_account_id
        else:  # pragma: no cover
            raise ValueError("aws_account_id is required!")

    @property
    def _region(self) -> str:
        if self._aws_region:
            return self._aws_region
        else:  # pragma: no cover
            raise ValueError("aws_region is required!")

    @property
    def _root_url(self) -> str:
        """
        Example: https://console.aws.amazon.com/ or
        https://us-east-1.console.aws.amazon.com/
        """
        if self._aws_region:
            return f"https://{self._aws_region}.{self._sub_domain}"
        else:  # pragma: no cover
            return f"https://{self._sub_domain}"

    @property
    def _service_root(self) -> str:
        """
        Example: https://us-east-1.console.aws.amazon.com/ec2
        """
        return f"{self._root_url}/{self._aws_service}"

    @classmethod
    def _from_aws_console(cls, aws_console: "AWSConsole") -> "Service":
        """
        Create a builder from AWSConsole object.
        """
        return cls._make(
            aws_account_id=aws_console.aws_account_id,
            aws_region=aws_console.aws_region,
            is_us_gov_cloud=aws_console.is_us_gov_cloud,
            bsm=aws_console.bsm,
        )

    def _ensure_name(self, name_or_arn: str, converter: T.Callable) -> str:
        """
        Ensure that the given value is a short name of an Amazon Resource.

        :param name_or_arn: the given value
        :param converter: convert to name if the given value is arn.
        """
        return converter(name_or_arn) if name_or_arn.startswith("arn:") else name_or_arn

    def _ensure_arn(self, name_or_arn: str, converter: T.Callable) -> str:
        """
        Ensure that the given value is an Amazon Resource Name (ARN).

        :param name_or_arn: the given value
        :param converter: convert to arn if the given value is a short name.
        """
        return name_or_arn if name_or_arn.startswith("arn:") else converter(name_or_arn)
