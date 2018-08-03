from kaggle.api.kaggle_api_extended import KaggleApi

import os  
import unittest

class TestAuthenticate(unittest.TestCase):
 
    def setUp(self):
        print("setup             class:%s" % self)
         
    def tearDown(self):
        print ("teardown          class:TestStuff")
  
    # Environment

    def test_environment_variables(self):
        print('testing initialization with environment variables')
        os.putenv('KAGGLE_USER','dinosaur')
        os.putenv('KAGGLE_KEY','xxxxxxxxxxxx')
        api = KaggleApi()
        
    # Configuration Actions

    def test_config_actions(self):
        print('testing default config directory is called .kaggle')
        api = KaggleApi()

        assert(api.get_config_dir().endswith('.kaggle'))
        self.assertEqual(api.get_config_dir(), api.config_dir)

        print('testing that asking for non-existent value returns none')
        self.assertEqual(api.get_config_value('doesntexist'), None)

 
if __name__ == '__main__':
    unittest.main()
