#!/usr/bin/python
#
# Copyright 2018 Kaggle Inc
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from kaggle.api.kaggle_api_extended import KaggleApi

# python -m unittest tests.test_authenticate

import os
import unittest


class TestAuthenticate(unittest.TestCase):
    def setUp(self):
        print("setup             class:%s" % self)

    def tearDown(self):
        print("teardown          class:TestStuff")

    # Environment

    def test_environment_variables(self):
        os.environ['KAGGLE_USERNAME'] = 'dinosaur'
        os.environ['KAGGLE_KEY'] = 'xxxxxxxxxxxx'
        api = KaggleApi()

        # We haven't authenticated yet
        self.assertTrue("key" not in api.config_values)
        self.assertTrue("username" not in api.config_values)
        api.authenticate()

        # Should be set from the environment
        self.assertEqual(api.config_values['key'], 'xxxxxxxxxxxx')
        self.assertEqual(api.config_values['username'], 'dinosaur')

    # Configuration Actions

    def test_config_actions(self):
        api = KaggleApi()

        self.assertTrue(api.config_dir.endswith('.kaggle'))
        self.assertEqual(api.get_config_value('doesntexist'), None)


if __name__ == '__main__':
    unittest.main()
