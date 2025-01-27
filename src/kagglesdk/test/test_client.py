from kagglesdk import kaggle_env
from kagglesdk import KaggleClient, KaggleEnv

# python -m unittest tests.test_authenticate

import os
import unittest


class TestClient(unittest.TestCase):

  def setUp(self):
    print("setup             class:%s" % self)

  def tearDown(self):
    print("teardown          class:TestStuff")

  # Environment

  def test_kaggle_environment(self):
    os.environ['KAGGLE_API_ENVIRONMENT'] = 'PROD'

    env = kaggle_env.get_env()
    self.assertEqual(env, KaggleEnv.PROD)

    endpoint = kaggle_env.get_endpoint(env)
    self.assertEqual(endpoint, 'https://www.kaggle.com')

  # Client

  def test_kaggle_client(self):
    client = KaggleClient(
        env=KaggleEnv.PROD,
        verbose=False,
        username='dinosaur',
        password='xxxxxxxxxxxx')

    self.assertEqual(client.username, 'dinosaur')
    self.assertEqual(client.password, 'xxxxxxxxxxxx')
    self.assertEqual(client.http_client()._endpoint, 'https://www.kaggle.com')
    self.assertEqual(client.http_client()._verbose, False)


if __name__ == '__main__':
  unittest.main()
