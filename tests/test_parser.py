#!/usr/bin/python3

# python3 -m unittest tests.test_parser

# To run this from Rider:
# Create a new Python run config
# Set it to run a module, use "kaggle.test.test_parser" as the module name
# Set the working directory to the full path to ApiClients/python

import argparse
import unittest

from ..cli import parse_competitions, parse_datasets, parse_kernels, parse_models, parse_files, parse_config, Help


class TestParser(unittest.TestCase):
    """
    Test that the new options are parsed correctly for all cases:
    NOT competitions
    competitions files
    competitions submissions
    NOT datasets
    datasets files
    NOT kernels
    """

    def setUp(self):
        print("setup             test: %s" % self)

    def tearDown(self):
        print("teardown          test: %s" % self)

    # def test_comp_list(self):
    #     result = self._parse_command('c list --page-size=3 --page-token=abcd')
    #     self.assertEqual(result['page_size'], '3')
    #     self.assertEqual(result['page_token'], 'abcd')

    def test_comp_files(self):
        result = self._parse_command(
            'c files https://www.kaggle.com/competitions/titanic --page-size=4 --page-token=abcd'
        )
        self.assertEqual(result['page_size'], '4')
        self.assertEqual(result['page_token'], 'abcd')

    def test_comp_subs(self):
        result = self._parse_command(
            'c submissions https://www.kaggle.com/competitions/titanic --page-size=5 --page-token=abcd'
        )
        self.assertEqual(result['page_size'], '5')
        self.assertEqual(result['page_token'], 'abcd')

    # def test_datasets_list(self):
    #     result = self._parse_command('d list --page-size=6 --page-token=abcd')
    #     self.assertEqual(result['page_size'], '6')
    #     self.assertEqual(result['page_token'], 'abcd')

    def test_datasets_files(self):
        result = self._parse_command(
            'd files nelgiriyewithana/apple-quality --page-size=7 --page-token=abcd'
        )
        self.assertEqual(result['page_size'], '7')
        self.assertEqual(result['page_token'], 'abcd')

    # def test_kernels_list(self):
    #     result = self._parse_command('k list --page-size=7 --page-token=abcd')
    #     self.assertEqual(result['page_size'], '7')
    #     self.assertEqual(result['page_token'], 'abcd')

    def _parse_command(self, command):
        parser = argparse.ArgumentParser(
            formatter_class=argparse.RawTextHelpFormatter)
        subparsers = parser.add_subparsers(title='commands',
                                           help=Help.kaggle,
                                           dest='command')
        subparsers.required = True
        subparsers.choices = Help.kaggle_choices
        parse_competitions(subparsers)
        parse_datasets(subparsers)
        parse_kernels(subparsers)
        parse_models(subparsers)
        parse_files(subparsers)
        parse_config(subparsers)
        args = parser.parse_args(command.split())
        command_args = {}
        command_args.update(vars(args))
        return command_args


if __name__ == '__main__':
    unittest.main()
