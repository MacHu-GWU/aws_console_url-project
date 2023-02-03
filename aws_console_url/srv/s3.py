# -*- coding: utf-8 -*-

import dataclasses

from ..model import Service


@dataclasses.dataclass(frozen=True)
class S3(Service):
    _AWS_SERVICE = "s3"

    def __post_init__(self):
        raise NotImplementedError(
            "Consider using s3pathlib https://pypi.org/project/s3pathlib/ "
            "for s3 console url"
        )
