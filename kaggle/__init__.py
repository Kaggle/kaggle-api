# coding=utf-8
from __future__ import absolute_import
from kaggle.api.kaggle_api_extended import KaggleApi

__version__ = "1.7.5.0.dev0"

api = KaggleApi()
api.authenticate()
