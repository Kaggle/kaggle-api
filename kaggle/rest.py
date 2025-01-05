# coding: utf-8

"""
    Kaggle API

    API for kaggle.com  # noqa: E501

    OpenAPI spec version: 1
    
   
"""


from __future__ import absolute_import

import io
import json
import logging
import re
import ssl

import certifi
# python 2 and python 3 compatibility library
import six
from six.moves.urllib.parse import urlencode

try:
    import urllib3
except ImportError:
    raise ImportError('Swagger python client requires urllib3.')


logger = logging.getLogger(__name__)


class RESTResponse(io.IOBase):

    def __init__(self, resp):
        self.urllib3_response = resp
        self.status = resp.status
        self.reason = resp.reason
        self.data = resp.data

    def getheaders(self):
        """Returns a dictionary of the response headers."""
        return dict(self.urllib3_response.headers)

    def getheader(self, name, default=None):
        """Returns a given response header."""
        return self.urllib3_response.headers.get(name, default) 