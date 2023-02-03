# -*- coding: utf-8 -*-

from ._version import __version__

__short_description__ = "Build AWS Console Url for debugging."
__license__ = "MIT"
__author__ = "Sanhe Hu"
__author_email__ = "husanhe@gmail.com"
__github_username__ = "MacHu-GWU"

try:
    from boto_session_manager import BotoSesManager

    from .console import AWSConsole
    from . import resource as aws_resource
except ImportError:  # pragma: no cover
    pass
