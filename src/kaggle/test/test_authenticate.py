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

        self.assertTrue(api.config_dir.endswith('kaggle'))
        self.assertEqual(api.get_config_value('doesntexist'), None)


if __name__ == '__main__':
    unittest.main()
