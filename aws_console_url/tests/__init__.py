# -*- coding: utf-8 -*-

from boto_session_manager import BotoSesManager
from ..console import AWSConsole
from .. import resource
from .helper import run_cov_test

bsm = BotoSesManager(profile_name="aws_data_lab_sanhe_us_east_1")

console = AWSConsole(
    aws_account_id=bsm.aws_account_id,
    aws_region=bsm.aws_region,
    bsm=bsm,
)

_ = resource
