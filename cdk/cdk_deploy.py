# -*- coding: utf-8 -*-

import os
import subprocess
from pathlib import Path
from aws_console_url.tests import bsm

dir_here = Path(__file__).absolute().parent

pwd = os.getcwd()
os.chdir(str(dir_here))
with bsm.awscli():
    args = [
        "cdk",
        "deploy",
        "--require-approval",
        "never",
    ]
    subprocess.run(args, check=True)
os.chdir(pwd)
