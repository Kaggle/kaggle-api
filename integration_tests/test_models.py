import os
import unittest
from typing import List

from kaggle.api.kaggle_api_extended import KaggleApi

MODEL_HANDLE = "keras/bert"
MODEL_ID = 2819

# TODO(messick) Add a test that creates a dataset w/o specifying privacy that is created private.

class TestModels(unittest.TestCase):
    def setUp(self):
        self.api = KaggleApi()
        self.api.authenticate()

    def test_list_models(self) -> None:
        models = self.api.model_list()
        self.assertGreater(len(models), 0)

    def test_get_model(self) -> None:
        model = self.api.model_get(MODEL_HANDLE)
        self.assertEqual(MODEL_ID, model.id)
