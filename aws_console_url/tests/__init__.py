# -*- coding: utf-8 -*-

import hashlib
from boto_session_manager import BotoSesManager

from ..console import AWSConsole
from .helper import run_cov_test
from . import paths


bsm = BotoSesManager(
    profile_name="awshsh_app_dev_us_east_1",
    # profile_name="bmt_infra_us_east_1",
    # profile_name="bmt_app_dev_us_east_1",
    # profile_name="edf_sbx_eu_west_1_mfa",
    # region_name="us-east-1",
)

console = AWSConsole(
    aws_account_id=bsm.aws_account_id,
    aws_region=bsm.aws_region,
    bsm=bsm,
)

sha256 = hashlib.sha256()
sha256.update(f"{bsm.aws_account_id}-{bsm.aws_region}".encode("utf-8"))
prefix = f"acu_{sha256.hexdigest()[:8]}"
prefix_slug = prefix.replace("_", "-")
prefix_snake = prefix.replace("-", "_")
