# coding=utf-8
from __future__ import absolute_import
from kaggle import configuration
from kaggle.api.kaggle_api_extended import KaggleApi

__version__ = kaggle.__version__

api = KaggleApi()
api.authenticate()
