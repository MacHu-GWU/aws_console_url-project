# -*- coding: utf-8 -*-

"""
Package Description.
"""


from ._version import __version__

__short_description__ = "AWS Console Url Builder."
__license__ = "MIT"
__author__ = "Sanhe Hu"
__author_email__ = "husanhe@gmail.com"
__github_username__ = "MacHu-GWU"

try:
    from .console import AWSConsole
except ImportError: # pragma: no cover
    pass