# -*- coding: utf-8 -*-

from aws_console_url.model import (
    Resource,
    BaseServiceResourceV1,
    BaseServiceResourceV2,
)

class SFNStateMachine(BaseServiceResourceV2):
    _SERVICE_NAME = "states"
    _RESOURCE_TYPE = "stateMachine"


class TestBaseServiceResourceV2:
    def test(self):
        SFNStateMachine.make()


if __name__ == "__main__":
    from aws_console_url.tests import run_cov_test

    run_cov_test(__file__, "aws_console_url.model", preview=False)
