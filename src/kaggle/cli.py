#!/usr/bin/python
#
# Copyright 2019 Kaggle Inc
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

# coding=utf-8
from __future__ import print_function
import argparse
import json
from kaggle import api
from kaggle import KaggleApi
from .rest import ApiException
import six


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('-v',
                        '--version',
                        action='version',
                        help='Print the Kaggle API version',
                        version='Kaggle API ' + KaggleApi.__version__)
    parser.add_argument('-W',
                        '--no-warn',
                        dest='disable_version_warning',
                        action='store_true',
                        help='Disable out-of-date API version warning')

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
    args = parser.parse_args()
    command_args = {}
    command_args.update(vars(args))
    del command_args['func']
    del command_args['command']
    if command_args['disable_version_warning']:
        KaggleApi.already_printed_version_warning = True
    del command_args['disable_version_warning']
    error = False
    try:
        out = args.func(**command_args)
    except ApiException as e:
        msg = '{} - {}'.format(str(e.status), e.reason)
        body = __parse_body(e.body)
        if body and 'message' in body:
            msg += ' - {}'.format(body['message'])
        print(msg)
        out = None
        error = True
    except ValueError as e:
        print(e)
        out = None
        error = True
    except KeyboardInterrupt:
        print('User cancelled operation')
        out = None
    if out is not None:
        print(out, end='')

    # This is so that scripts that pick up on error codes can tell when there was a failure
    if error:
        exit(1)


def __parse_body(body):
    try:
        return json.loads(body)
    except Exception as e:
        return {}


def parse_competitions(subparsers):
    if six.PY2:
        parser_competitions = subparsers.add_parser(
            'competitions',
            formatter_class=argparse.RawTextHelpFormatter,
            help=Help.group_competitions)
    else:
        parser_competitions = subparsers.add_parser(
            'competitions',
            formatter_class=argparse.RawTextHelpFormatter,
            help=Help.group_competitions,
            aliases=['c'])
    subparsers_competitions = parser_competitions.add_subparsers(
        title='commands', dest='command')
    subparsers_competitions.required = True
    subparsers_competitions.choices = Help.competitions_choices

    # Competitions list
    parser_competitions_list = subparsers_competitions.add_parser(
        'list',
        formatter_class=argparse.RawTextHelpFormatter,
        help=Help.command_competitions_list)
    parser_competitions_list_optional = parser_competitions_list._action_groups.pop(
    )
    parser_competitions_list_optional.add_argument(
        '--group',
        dest='group',
        required=False,
        help=Help.param_competition_group)
    parser_competitions_list_optional.add_argument(
        '--category',
        dest='category',
        required=False,
        help=Help.param_competition_category)
    parser_competitions_list_optional.add_argument(
        '--sort-by',
        dest='sort_by',
        required=False,
        help=Help.param_competition_sort_by)
    parser_competitions_list_optional.add_argument('-p',
                                                   '--page',
                                                   dest='page',
                                                   default=1,
                                                   required=False,
                                                   help=Help.param_page)
    parser_competitions_list_optional.add_argument('-s',
                                                   '--search',
                                                   dest='search',
                                                   required=False,
                                                   help=Help.param_search)
    parser_competitions_list_optional.add_argument('-v',
                                                   '--csv',
                                                   dest='csv_display',
                                                   action='store_true',
                                                   help=Help.param_csv)
    parser_competitions_list._action_groups.append(
        parser_competitions_list_optional)
    parser_competitions_list.set_defaults(func=api.competitions_list_cli)

    # Competitions list files
    parser_competitions_files = subparsers_competitions.add_parser(
        'files',
        formatter_class=argparse.RawTextHelpFormatter,
        help=Help.command_competitions_files)
    parser_competitions_files_optional = parser_competitions_files._action_groups.pop(
    )
    parser_competitions_files_optional.add_argument(
        'competition', nargs='?', default=None, help=Help.param_competition)
    parser_competitions_files_optional.add_argument('-c',
                                                    '--competition',
                                                    dest='competition_opt',
                                                    required=False,
                                                    help=argparse.SUPPRESS)
    parser_competitions_files_optional.add_argument('-v',
                                                    '--csv',
                                                    dest='csv_display',
                                                    action='store_true',
                                                    help=Help.param_csv)
    parser_competitions_files_optional.add_argument('-q',
                                                    '--quiet',
                                                    dest='quiet',
                                                    action='store_true',
                                                    help=Help.param_quiet)
    parser_competitions_files_optional.add_argument('--page-token',
                                                    dest='page_token',
                                                    required=False,
                                                    help=Help.param_page_token)
    parser_competitions_files_optional.add_argument('--page-size',
                                                    dest='page_size',
                                                    required=False,
                                                    default=20,
                                                    help=Help.param_page_size)
    parser_competitions_files._action_groups.append(
        parser_competitions_files_optional)
    parser_competitions_files.set_defaults(func=api.competition_list_files_cli)

    # Competitions download
    parser_competitions_download = subparsers_competitions.add_parser(
        'download',
        formatter_class=argparse.RawTextHelpFormatter,
        help=Help.command_competitions_download)
    parser_competitions_download_optional = parser_competitions_download._action_groups.pop(
    )
    parser_competitions_download_optional.add_argument(
        'competition', nargs='?', default=None, help=Help.param_competition)
    parser_competitions_download_optional.add_argument('-c',
                                                       '--competition',
                                                       dest='competition_opt',
                                                       required=False,
                                                       help=argparse.SUPPRESS)
    parser_competitions_download_optional.add_argument(
        '-f',
        '--file',
        dest='file_name',
        required=False,
        help=Help.param_competition_file)
    parser_competitions_download_optional.add_argument(
        '-p',
        '--path',
        dest='path',
        required=False,
        help=Help.param_downfolder)
    parser_competitions_download_optional.add_argument('-w',
                                                       '--wp',
                                                       dest='path',
                                                       action='store_const',
                                                       const='.',
                                                       required=False,
                                                       help=Help.param_wp)
    parser_competitions_download_optional.add_argument('-o',
                                                       '--force',
                                                       dest='force',
                                                       action='store_true',
                                                       help=Help.param_force)
    parser_competitions_download_optional.add_argument('-q',
                                                       '--quiet',
                                                       dest='quiet',
                                                       action='store_true',
                                                       help=Help.param_quiet)
    parser_competitions_download._action_groups.append(
        parser_competitions_download_optional)
    parser_competitions_download.set_defaults(
        func=api.competition_download_cli)

    # Competitions submit
    parser_competitions_submit = subparsers_competitions.add_parser(
        'submit',
        formatter_class=argparse.RawTextHelpFormatter,
        help=Help.command_competitions_submit)
    parser_competitions_submit_optional = parser_competitions_submit._action_groups.pop(
    )
    parser_competitions_submit_required = parser_competitions_submit.add_argument_group(
        'required arguments')
    parser_competitions_submit_optional.add_argument(
        'competition', nargs='?', default=None, help=Help.param_competition)
    parser_competitions_submit_optional.add_argument('-c',
                                                     '--competition',
                                                     dest='competition_opt',
                                                     required=False,
                                                     help=argparse.SUPPRESS)
    parser_competitions_submit_required.add_argument('-f',
                                                     '--file',
                                                     dest='file_name',
                                                     required=True,
                                                     help=Help.param_upfile)
    parser_competitions_submit_required.add_argument(
        '-m',
        '--message',
        dest='message',
        required=True,
        help=Help.param_competition_message)
    parser_competitions_submit_optional.add_argument('-q',
                                                     '--quiet',
                                                     dest='quiet',
                                                     action='store_true',
                                                     help=Help.param_quiet)
    parser_competitions_submit._action_groups.append(
        parser_competitions_submit_optional)
    parser_competitions_submit.set_defaults(func=api.competition_submit_cli)

    # Competitions list submissions
    parser_competitions_submissions = subparsers_competitions.add_parser(
        'submissions',
        formatter_class=argparse.RawTextHelpFormatter,
        help=Help.command_competitions_submissions)
    parser_competitions_submissions_optional = parser_competitions_submissions._action_groups.pop(
    )
    parser_competitions_submissions_optional.add_argument(
        'competition', nargs='?', default=None, help=Help.param_competition)
    parser_competitions_submissions_optional.add_argument(
        '-c',
        '--competition',
        dest='competition_opt',
        required=False,
        help=argparse.SUPPRESS)
    parser_competitions_submissions_optional.add_argument('-v',
                                                          '--csv',
                                                          dest='csv_display',
                                                          action='store_true',
                                                          help=Help.param_csv)
    parser_competitions_submissions_optional.add_argument(
        '-q',
        '--quiet',
        dest='quiet',
        action='store_true',
        help=Help.param_quiet)
    parser_competitions_submissions._action_groups.append(
        parser_competitions_submissions_optional)
    parser_competitions_submissions.set_defaults(
        func=api.competition_submissions_cli)

    # Competitions leaderboard
    parser_competitions_leaderboard = subparsers_competitions.add_parser(
        'leaderboard',
        formatter_class=argparse.RawTextHelpFormatter,
        help=Help.command_competitions_leaderboard)
    parser_competitions_leaderboard_optional = parser_competitions_leaderboard._action_groups.pop(
    )
    parser_competitions_leaderboard_optional.add_argument(
        'competition', nargs='?', default=None, help=Help.param_competition)
    parser_competitions_leaderboard_optional.add_argument(
        '-c',
        '--competition',
        dest='competition_opt',
        required=False,
        help=argparse.SUPPRESS)
    parser_competitions_leaderboard_optional.add_argument(
        '-s',
        '--show',
        dest='view',
        action='store_true',
        help=Help.param_competition_leaderboard_view)
    parser_competitions_leaderboard_optional.add_argument(
        '-d',
        '--download',
        dest='download',
        action='store_true',
        help=Help.param_competition_leaderboard_download)
    parser_competitions_leaderboard_optional.add_argument(
        '-p', '--path', dest='path', help=Help.param_downfolder)
    parser_competitions_leaderboard_optional.add_argument('-v',
                                                          '--csv',
                                                          dest='csv_display',
                                                          action='store_true',
                                                          help=Help.param_csv)
    parser_competitions_leaderboard_optional.add_argument(
        '-q',
        '--quiet',
        dest='quiet',
        action='store_true',
        help=Help.param_quiet)
    parser_competitions_leaderboard._action_groups.append(
        parser_competitions_leaderboard_optional)
    parser_competitions_leaderboard.set_defaults(
        func=api.competition_leaderboard_cli)


def parse_datasets(subparsers):
    if six.PY2:
        parser_datasets = subparsers.add_parser(
            'datasets',
            formatter_class=argparse.RawTextHelpFormatter,
            help=Help.group_datasets)
    else:
        parser_datasets = subparsers.add_parser(
            'datasets',
            formatter_class=argparse.RawTextHelpFormatter,
            help=Help.group_datasets,
            aliases=['d'])
    subparsers_datasets = parser_datasets.add_subparsers(title='commands',
                                                         dest='command')
    subparsers_datasets.required = True
    subparsers_datasets.choices = Help.datasets_choices

    # Datasets list
    parser_datasets_list = subparsers_datasets.add_parser(
        'list',
        formatter_class=argparse.RawTextHelpFormatter,
        help=Help.command_datasets_list)
    parser_datasets_list_optional = parser_datasets_list._action_groups.pop()
    parser_datasets_list.add_argument('--sort-by',
                                      dest='sort_by',
                                      required=False,
                                      help=Help.param_dataset_sort_by)
    parser_datasets_list.add_argument('--size',
                                      dest='size',
                                      required=False,
                                      help=Help.param_dataset_size)
    parser_datasets_list.add_argument('--file-type',
                                      dest='file_type',
                                      required=False,
                                      help=Help.param_dataset_file_type)
    parser_datasets_list.add_argument('--license',
                                      dest='license_name',
                                      required=False,
                                      help=Help.param_dataset_license)
    parser_datasets_list.add_argument('--tags',
                                      dest='tag_ids',
                                      required=False,
                                      help=Help.param_dataset_tags)
    parser_datasets_list.add_argument('-s',
                                      '--search',
                                      dest='search',
                                      required=False,
                                      help=Help.param_search)
    parser_datasets_list.add_argument('-m',
                                      '--mine',
                                      dest='mine',
                                      action='store_true',
                                      help=Help.param_mine)
    parser_datasets_list.add_argument('--user',
                                      dest='user',
                                      required=False,
                                      help=Help.param_dataset_user)
    parser_datasets_list.add_argument('-p',
                                      '--page',
                                      dest='page',
                                      default=1,
                                      required=False,
                                      help=Help.param_page)
    parser_datasets_list.add_argument('-v',
                                      '--csv',
                                      dest='csv_display',
                                      action='store_true',
                                      help=Help.param_csv)
    parser_datasets_list.add_argument('--max-size',
                                      dest='max_size',
                                      required=False,
                                      help=Help.param_dataset_maxsize)
    parser_datasets_list.add_argument('--min-size',
                                      dest='min_size',
                                      required=False,
                                      help=Help.param_dataset_minsize)
    parser_datasets_list._action_groups.append(parser_datasets_list_optional)
    parser_datasets_list.set_defaults(func=api.dataset_list_cli)

    # Datasets file list
    parser_datasets_files = subparsers_datasets.add_parser(
        'files',
        formatter_class=argparse.RawTextHelpFormatter,
        help=Help.command_datasets_files)
    parser_datasets_files_optional = parser_datasets_files._action_groups.pop()
    parser_datasets_files_optional.add_argument('dataset',
                                                nargs='?',
                                                default=None,
                                                help=Help.param_dataset)
    parser_datasets_files_optional.add_argument('-d',
                                                '--dataset',
                                                dest='dataset_opt',
                                                required=False,
                                                help=argparse.SUPPRESS)
    parser_datasets_files_optional.add_argument('-v',
                                                '--csv',
                                                dest='csv_display',
                                                action='store_true',
                                                help=Help.param_csv)
    parser_datasets_files_optional.add_argument('--page-token',
                                                dest='page_token',
                                                required=False,
                                                help=Help.param_page_token)
    parser_datasets_files_optional.add_argument('--page-size',
                                                dest='page_size',
                                                required=False,
                                                default=20,
                                                help=Help.param_page_size)
    parser_datasets_files._action_groups.append(parser_datasets_files_optional)
    parser_datasets_files.set_defaults(func=api.dataset_list_files_cli)

    # Datasets download
    parser_datasets_download = subparsers_datasets.add_parser(
        'download',
        formatter_class=argparse.RawTextHelpFormatter,
        help=Help.command_datasets_download)
    parser_datasets_download_optional = parser_datasets_download._action_groups.pop(
    )
    parser_datasets_download_optional.add_argument('dataset',
                                                   nargs='?',
                                                   default=None,
                                                   help=Help.param_dataset)
    parser_datasets_download_optional.add_argument('-d',
                                                   '--dataset',
                                                   dest='dataset_opt',
                                                   required=False,
                                                   help=argparse.SUPPRESS)
    parser_datasets_download_optional.add_argument(
        '-f',
        '--file',
        dest='file_name',
        required=False,
        help=Help.param_dataset_file)
    parser_datasets_download_optional.add_argument('-p',
                                                   '--path',
                                                   dest='path',
                                                   required=False,
                                                   help=Help.param_downfolder)
    parser_datasets_download_optional.add_argument('-w',
                                                   '--wp',
                                                   dest='path',
                                                   action='store_const',
                                                   const='.',
                                                   required=False,
                                                   help=Help.param_wp)
    parser_datasets_download_optional.add_argument('--unzip',
                                                   dest='unzip',
                                                   action='store_true',
                                                   help=Help.param_unzip)
    parser_datasets_download_optional.add_argument('-o',
                                                   '--force',
                                                   dest='force',
                                                   action='store_true',
                                                   help=Help.param_force)
    parser_datasets_download_optional.add_argument('-q',
                                                   '--quiet',
                                                   dest='quiet',
                                                   action='store_true',
                                                   help=Help.param_quiet)
    parser_datasets_download._action_groups.append(
        parser_datasets_download_optional)
    parser_datasets_download.set_defaults(func=api.dataset_download_cli)

    # Datasets create
    parser_datasets_create = subparsers_datasets.add_parser(
        'create',
        formatter_class=argparse.RawTextHelpFormatter,
        help=Help.command_datasets_new)
    parser_datasets_create_optional = parser_datasets_create._action_groups.pop(
    )
    parser_datasets_create_optional.add_argument(
        '-p',
        '--path',
        dest='folder',
        required=False,
        help=Help.param_dataset_upfile)
    parser_datasets_create_optional.add_argument('-u',
                                                 '--public',
                                                 dest='public',
                                                 action='store_true',
                                                 help=Help.param_public)
    parser_datasets_create_optional.add_argument('-q',
                                                 '--quiet',
                                                 dest='quiet',
                                                 action='store_true',
                                                 help=Help.param_quiet)
    parser_datasets_create_optional.add_argument('-t',
                                                 '--keep-tabular',
                                                 dest='convert_to_csv',
                                                 action='store_false',
                                                 help=Help.param_keep_tabular)
    parser_datasets_create_optional.add_argument(
        '-r',
        '--dir-mode',
        dest='dir_mode',
        choices=['skip', 'zip', 'tar'],
        default='skip',
        help=Help.param_dir_mode)
    parser_datasets_create._action_groups.append(
        parser_datasets_create_optional)
    parser_datasets_create.set_defaults(func=api.dataset_create_new_cli)

    # Datasets update
    parser_datasets_version = subparsers_datasets.add_parser(
        'version',
        formatter_class=argparse.RawTextHelpFormatter,
        help=Help.command_datasets_new_version)
    parser_datasets_version_optional = parser_datasets_version._action_groups.pop(
    )
    parser_datasets_version_required = parser_datasets_version.add_argument_group(
        'required arguments')
    parser_datasets_version_required.add_argument(
        '-m',
        '--message',
        dest='version_notes',
        required=True,
        help=Help.param_dataset_version_notes)
    parser_datasets_version_optional.add_argument(
        '-p',
        '--path',
        dest='folder',
        required=False,
        help=Help.param_dataset_upfile)
    parser_datasets_version_optional.add_argument('-q',
                                                  '--quiet',
                                                  dest='quiet',
                                                  action='store_true',
                                                  help=Help.param_quiet)
    parser_datasets_version_optional.add_argument('-t',
                                                  '--keep-tabular',
                                                  dest='convert_to_csv',
                                                  action='store_false',
                                                  help=Help.param_keep_tabular)
    parser_datasets_version_optional.add_argument(
        '-r',
        '--dir-mode',
        dest='dir_mode',
        choices=['skip', 'zip', 'tar'],
        default='skip',
        help=Help.param_dir_mode)
    parser_datasets_version_optional.add_argument(
        '-d',
        '--delete-old-versions',
        dest='delete_old_versions',
        action='store_true',
        help=Help.param_delete_old_version)
    parser_datasets_version._action_groups.append(
        parser_datasets_version_optional)
    parser_datasets_version.set_defaults(func=api.dataset_create_version_cli)

    # Datasets init
    parser_datasets_init = subparsers_datasets.add_parser(
        'init',
        formatter_class=argparse.RawTextHelpFormatter,
        help=Help.command_datasets_init)
    parser_datasets_init_optional = parser_datasets_init._action_groups.pop()
    parser_datasets_init_optional.add_argument('-p',
                                               '--path',
                                               dest='folder',
                                               required=False,
                                               help=Help.param_dataset_upfile)
    parser_datasets_init._action_groups.append(parser_datasets_init_optional)
    parser_datasets_init.set_defaults(func=api.dataset_initialize_cli)

    # Datasets metadata
    parser_datasets_metadata = subparsers_datasets.add_parser(
        'metadata',
        formatter_class=argparse.RawTextHelpFormatter,
        help=Help.command_datasets_metadata)
    parser_datasets_metadata_optional = parser_datasets_metadata._action_groups.pop(
    )
    parser_datasets_metadata_optional.add_argument('dataset',
                                                   nargs='?',
                                                   default=None,
                                                   help=Help.param_dataset)
    parser_datasets_metadata_optional.add_argument('-d',
                                                   '--dataset',
                                                   dest='dataset_opt',
                                                   required=False,
                                                   help=argparse.SUPPRESS)
    parser_datasets_metadata_optional.add_argument(
        '--update',
        dest='update',
        action='store_true',
        help=Help.param_dataset_metadata_update)
    parser_datasets_metadata_optional.add_argument(
        '-p', '--path', dest='path', help=Help.param_dataset_metadata_dir)
    parser_datasets_metadata._action_groups.append(
        parser_datasets_metadata_optional)
    parser_datasets_metadata.set_defaults(func=api.dataset_metadata_cli)

    # Datasets status
    parser_datasets_status = subparsers_datasets.add_parser(
        'status',
        formatter_class=argparse.RawTextHelpFormatter,
        help=Help.command_datasets_status)
    parser_datasets_status_optional = parser_datasets_status._action_groups.pop(
    )
    parser_datasets_status_optional.add_argument('dataset',
                                                 nargs='?',
                                                 default=None,
                                                 help=Help.param_dataset)
    parser_datasets_status_optional.add_argument('-d',
                                                 '--dataset',
                                                 dest='dataset_opt',
                                                 required=False,
                                                 help=argparse.SUPPRESS)
    parser_datasets_status._action_groups.append(
        parser_datasets_status_optional)
    parser_datasets_status.set_defaults(func=api.dataset_status_cli)


def parse_kernels(subparsers):
    if six.PY2:
        parser_kernels = subparsers.add_parser(
            'kernels',
            formatter_class=argparse.RawTextHelpFormatter,
            help=Help.group_kernels)
    else:
        parser_kernels = subparsers.add_parser(
            'kernels',
            formatter_class=argparse.RawTextHelpFormatter,
            help=Help.group_kernels,
            aliases=['k'])
    subparsers_kernels = parser_kernels.add_subparsers(title='commands',
                                                       dest='command')
    subparsers_kernels.required = True
    subparsers_kernels.choices = Help.kernels_choices

    # Kernels list/search
    parser_kernels_list = subparsers_kernels.add_parser(
        'list',
        formatter_class=argparse.RawTextHelpFormatter,
        help=Help.command_kernels_list)
    parser_kernels_list_optional = parser_kernels_list._action_groups.pop()
    parser_kernels_list_optional.add_argument('-m',
                                              '--mine',
                                              dest='mine',
                                              action='store_true',
                                              help=Help.param_mine)
    parser_kernels_list_optional.add_argument('-p',
                                              '--page',
                                              dest='page',
                                              default=1,
                                              help=Help.param_page)
    parser_kernels_list_optional.add_argument('--page-size',
                                              dest='page_size',
                                              default=20,
                                              help=Help.param_page_size)
    parser_kernels_list_optional.add_argument('-s',
                                              '--search',
                                              dest='search',
                                              help=Help.param_search)
    parser_kernels_list_optional.add_argument('-v',
                                              '--csv',
                                              dest='csv_display',
                                              action='store_true',
                                              help=Help.param_csv)
    parser_kernels_list_optional.add_argument('--parent',
                                              dest='parent',
                                              required=False,
                                              help=Help.param_kernel_parent)
    parser_kernels_list_optional.add_argument(
        '--competition',
        dest='competition',
        required=False,
        help=Help.param_kernel_competition)
    parser_kernels_list_optional.add_argument('--dataset',
                                              dest='dataset',
                                              required=False,
                                              help=Help.param_kernel_dataset)
    parser_kernels_list_optional.add_argument('--user',
                                              dest='user',
                                              required=False,
                                              help=Help.param_kernel_user)
    parser_kernels_list_optional.add_argument('--language',
                                              dest='language',
                                              required=False,
                                              help=Help.param_kernel_language)
    parser_kernels_list_optional.add_argument('--kernel-type',
                                              dest='kernel_type',
                                              required=False,
                                              help=Help.param_kernel_type)
    parser_kernels_list_optional.add_argument(
        '--output-type',
        dest='output_type',
        required=False,
        help=Help.param_kernel_output_type)
    parser_kernels_list_optional.add_argument('--sort-by',
                                              dest='sort_by',
                                              required=False,
                                              help=Help.param_kernel_sort_by)
    parser_kernels_list._action_groups.append(parser_kernels_list_optional)
    parser_kernels_list.set_defaults(func=api.kernels_list_cli)

    # Kernels file list
    parser_kernels_files = subparsers_kernels.add_parser(
        'files',
        formatter_class=argparse.RawTextHelpFormatter,
        help=Help.command_kernels_files)
    parser_kernels_files_optional = parser_kernels_files._action_groups.pop()
    parser_kernels_files_optional.add_argument('kernel',
                                               nargs='?',
                                               default=None,
                                               help=Help.param_kernel)
    parser_kernels_files_optional.add_argument('-k',
                                               '--kernel',
                                               dest='kernel_opt',
                                               required=False,
                                               help=argparse.SUPPRESS)
    parser_kernels_files_optional.add_argument('-v',
                                               '--csv',
                                               dest='csv_display',
                                               action='store_true',
                                               help=Help.param_csv)
    parser_kernels_files_optional.add_argument('--page-token',
                                               dest='page_token',
                                               help=Help.param_page_token)
    parser_kernels_files_optional.add_argument('--page-size',
                                               dest='page_size',
                                               default=20,
                                               help=Help.param_page_size)
    parser_kernels_files._action_groups.append(parser_kernels_files_optional)
    parser_kernels_files.set_defaults(func=api.kernels_list_files_cli)

    # Kernels init
    parser_kernels_init = subparsers_kernels.add_parser(
        'init',
        formatter_class=argparse.RawTextHelpFormatter,
        help=Help.command_kernels_init)
    parser_kernels_init_optional = parser_kernels_init._action_groups.pop()
    parser_kernels_init_optional.add_argument('-p',
                                              '--path',
                                              dest='folder',
                                              required=False,
                                              help=Help.param_kernel_upfile)
    parser_kernels_init._action_groups.append(parser_kernels_init_optional)
    parser_kernels_init.set_defaults(func=api.kernels_initialize_cli)

    # Kernels push
    parser_kernels_push = subparsers_kernels.add_parser(
        'push',
        formatter_class=argparse.RawTextHelpFormatter,
        help=Help.command_kernels_push)
    parser_kernels_push_optional = parser_kernels_push._action_groups.pop()
    parser_kernels_push_optional.add_argument('-p',
                                              '--path',
                                              dest='folder',
                                              required=False,
                                              help=Help.param_kernel_upfile)
    parser_kernels_push._action_groups.append(parser_kernels_push_optional)
    parser_kernels_push.set_defaults(func=api.kernels_push_cli)

    # Kernels pull
    parser_kernels_pull = subparsers_kernels.add_parser(
        'pull',
        formatter_class=argparse.RawTextHelpFormatter,
        help=Help.command_kernels_pull)
    parser_kernels_pull_optional = parser_kernels_pull._action_groups.pop()
    parser_kernels_pull_optional.add_argument('kernel',
                                              nargs='?',
                                              default=None,
                                              help=Help.param_kernel)
    parser_kernels_pull_optional.add_argument('-k',
                                              '--kernel',
                                              dest='kernel',
                                              required=False,
                                              help=argparse.SUPPRESS)
    parser_kernels_pull_optional.add_argument('-p',
                                              '--path',
                                              dest='path',
                                              required=False,
                                              help=Help.param_downfolder)
    parser_kernels_pull_optional.add_argument('-w',
                                              '--wp',
                                              dest='path',
                                              action='store_const',
                                              const='.',
                                              required=False,
                                              help=Help.param_wp)
    parser_kernels_pull_optional.add_argument(
        '-m',
        '--metadata',
        dest='metadata',
        action='store_true',
        help=Help.param_kernel_pull_metadata)
    parser_kernels_pull._action_groups.append(parser_kernels_pull_optional)
    parser_kernels_pull.set_defaults(func=api.kernels_pull_cli)

    # Kernels output
    parser_kernels_output = subparsers_kernels.add_parser(
        'output',
        formatter_class=argparse.RawTextHelpFormatter,
        help=Help.command_kernels_output)
    parser_kernels_output_optional = parser_kernels_output._action_groups.pop()
    parser_kernels_output_optional.add_argument('kernel',
                                                nargs='?',
                                                default=None,
                                                help=Help.param_kernel)
    parser_kernels_output_optional.add_argument('-k',
                                                '--kernel',
                                                dest='kernel_opt',
                                                required=False,
                                                help=argparse.SUPPRESS)
    parser_kernels_output_optional.add_argument('-p',
                                                '--path',
                                                dest='path',
                                                required=False,
                                                help=Help.param_downfolder)
    parser_kernels_output_optional.add_argument('-w',
                                                '--wp',
                                                dest='path',
                                                action='store_const',
                                                const='.',
                                                required=False,
                                                help=Help.param_wp)
    parser_kernels_output_optional.add_argument('-o',
                                                '--force',
                                                dest='force',
                                                action='store_true',
                                                required=False,
                                                help=Help.param_force)
    parser_kernels_output_optional.add_argument('-q',
                                                '--quiet',
                                                dest='quiet',
                                                action='store_true',
                                                required=False,
                                                help=Help.param_quiet)
    parser_kernels_output._action_groups.append(parser_kernels_output_optional)
    parser_kernels_output.set_defaults(func=api.kernels_output_cli)

    # Kernels status
    parser_kernels_status = subparsers_kernels.add_parser(
        'status',
        formatter_class=argparse.RawTextHelpFormatter,
        help=Help.command_kernels_status)
    parser_kernels_status_optional = parser_kernels_status._action_groups.pop()
    parser_kernels_status_optional.add_argument('kernel',
                                                nargs='?',
                                                default=None,
                                                help=Help.param_kernel)
    parser_kernels_status_optional.add_argument('-k',
                                                '--kernel',
                                                dest='kernel_opt',
                                                required=False,
                                                help=argparse.SUPPRESS)
    parser_kernels_status._action_groups.append(parser_kernels_status_optional)
    parser_kernels_status.set_defaults(func=api.kernels_status_cli)


def parse_models(subparsers):
    parser_models = subparsers.add_parser(
        'models',
        formatter_class=argparse.RawTextHelpFormatter,
        help=Help.group_models,
        aliases=['m'])

    subparsers_models = parser_models.add_subparsers(title='commands',
                                                     dest='command')
    subparsers_models.required = True
    subparsers_models.choices = Help.models_choices

    # Models Instances.
    parse_model_instances(subparsers_models)

    # Models get
    parser_models_get = subparsers_models.add_parser(
        'get',
        formatter_class=argparse.RawTextHelpFormatter,
        help=Help.command_models_get)
    parser_models_get_optional = parser_models_get._action_groups.pop()
    parser_models_get_optional.add_argument('model', help=Help.param_model)
    parser_models_get_optional.add_argument('-p',
                                            '--path',
                                            dest='folder',
                                            required=False,
                                            help=Help.param_model_downfile)
    parser_models_get._action_groups.append(parser_models_get_optional)
    parser_models_get.set_defaults(func=api.model_get_cli)

    # Models list
    parser_models_list = subparsers_models.add_parser(
        'list',
        formatter_class=argparse.RawTextHelpFormatter,
        help=Help.command_models_list)
    parser_models_list_optional = parser_models_list._action_groups.pop()
    parser_models_list.add_argument('--sort-by',
                                    dest='sort_by',
                                    required=False,
                                    help=Help.param_model_sort_by)
    parser_models_list.add_argument('-s',
                                    '--search',
                                    dest='search',
                                    required=False,
                                    help=Help.param_search)
    parser_models_list.add_argument('--owner',
                                    dest='owner',
                                    required=False,
                                    help=Help.param_model_owner)
    parser_models_list.add_argument('--page-size',
                                    dest='page_size',
                                    default=20,
                                    help=Help.param_page_size)
    parser_models_list.add_argument('--page-token',
                                    dest='page_token',
                                    required=False,
                                    help=Help.param_page_token)
    parser_models_list.add_argument('-v',
                                    '--csv',
                                    dest='csv_display',
                                    action='store_true',
                                    help=Help.param_csv)
    parser_models_list._action_groups.append(parser_models_list_optional)
    parser_models_list.set_defaults(func=api.model_list_cli)

    # Models init
    parser_models_init = subparsers_models.add_parser(
        'init',
        formatter_class=argparse.RawTextHelpFormatter,
        help=Help.command_models_init)
    parser_models_init_optional = parser_models_init._action_groups.pop()
    parser_models_init_optional.add_argument('-p',
                                             '--path',
                                             dest='folder',
                                             required=False,
                                             help=Help.param_model_upfile)
    parser_models_init._action_groups.append(parser_models_init_optional)
    parser_models_init.set_defaults(func=api.model_initialize_cli)

    # Models create
    parser_models_create = subparsers_models.add_parser(
        'create',
        formatter_class=argparse.RawTextHelpFormatter,
        help=Help.command_models_new)
    parser_models_create_optional = parser_models_create._action_groups.pop()
    parser_models_create_optional.add_argument('-p',
                                               '--path',
                                               dest='folder',
                                               required=False,
                                               help=Help.param_model_upfile)
    parser_models_create._action_groups.append(parser_models_create_optional)
    parser_models_create.set_defaults(func=api.model_create_new_cli)

    # Models delete
    parser_models_delete = subparsers_models.add_parser(
        'delete',
        formatter_class=argparse.RawTextHelpFormatter,
        help=Help.command_models_delete)
    parser_models_delete_optional = parser_models_delete._action_groups.pop()
    parser_models_delete_optional.add_argument('model', help=Help.param_model)
    parser_models_delete_optional.add_argument('-y',
                                               '--yes',
                                               dest='yes',
                                               action='store_true',
                                               help=Help.param_yes)
    parser_models_delete._action_groups.append(parser_models_delete_optional)
    parser_models_delete.set_defaults(func=api.model_delete_cli)

    # Models update
    parser_models_update = subparsers_models.add_parser(
        'update',
        formatter_class=argparse.RawTextHelpFormatter,
        help=Help.command_models_update)
    parser_models_update_optional = parser_models_update._action_groups.pop()
    parser_models_update_optional.add_argument('-p',
                                               '--path',
                                               dest='folder',
                                               required=False,
                                               help=Help.param_model_upfile)
    parser_models_update._action_groups.append(parser_models_update_optional)
    parser_models_update.set_defaults(func=api.model_update_cli)


def parse_model_instances(subparsers):
    parser_model_instances = subparsers.add_parser(
        'instances',
        formatter_class=argparse.RawTextHelpFormatter,
        help=Help.group_model_instances,
        aliases=['mi'])

    subparsers_model_instances = parser_model_instances.add_subparsers(
        title='commands', dest='command')
    subparsers_model_instances.required = True
    subparsers_model_instances.choices = Help.model_instances_choices

    # Models Instances Versions.
    parse_model_instance_versions(subparsers_model_instances)

    # Models Instances get
    parser_model_instance_get = subparsers_model_instances.add_parser(
        'get',
        formatter_class=argparse.RawTextHelpFormatter,
        help=Help.command_model_instances_get)
    parser_model_instance_get_optional = parser_model_instance_get._action_groups.pop(
    )
    parser_model_instance_get_optional.add_argument(
        'model_instance', help=Help.param_model_instance)
    parser_model_instance_get_optional.add_argument(
        '-p',
        '--path',
        dest='folder',
        required=False,
        help=Help.param_model_instance_downfile)
    parser_model_instance_get._action_groups.append(
        parser_model_instance_get_optional)
    parser_model_instance_get.set_defaults(func=api.model_instance_get_cli)

    # Model Instances init
    parser_model_instances_init = subparsers_model_instances.add_parser(
        'init',
        formatter_class=argparse.RawTextHelpFormatter,
        help=Help.command_model_instances_init)
    parser_model_instances_init_optional = parser_model_instances_init._action_groups.pop(
    )
    parser_model_instances_init_optional.add_argument(
        '-p',
        '--path',
        dest='folder',
        required=False,
        help=Help.param_model_instance_upfile)
    parser_model_instances_init._action_groups.append(
        parser_model_instances_init_optional)
    parser_model_instances_init.set_defaults(
        func=api.model_instance_initialize_cli)

    # Model Instances create
    parser_model_instances_create = subparsers_model_instances.add_parser(
        'create',
        formatter_class=argparse.RawTextHelpFormatter,
        help=Help.command_model_instances_new)
    parser_model_instances_create_optional = parser_model_instances_create._action_groups.pop(
    )
    parser_model_instances_create_optional.add_argument(
        '-p',
        '--path',
        dest='folder',
        required=False,
        help=Help.param_model_instance_upfile)
    parser_model_instances_create_optional.add_argument('-q',
                                                        '--quiet',
                                                        dest='quiet',
                                                        action='store_true',
                                                        help=Help.param_quiet)
    parser_model_instances_create_optional.add_argument(
        '-r',
        '--dir-mode',
        dest='dir_mode',
        choices=['skip', 'zip', 'tar'],
        default='skip',
        help=Help.param_dir_mode)
    parser_model_instances_create._action_groups.append(
        parser_model_instances_create_optional)
    parser_model_instances_create.set_defaults(
        func=api.model_instance_create_cli)

    # Model Instances files
    parser_model_instances_files = subparsers_model_instances.add_parser(
        'files',
        formatter_class=argparse.RawTextHelpFormatter,
        help=Help.command_model_instances_files)
    parser_model_instances_files_optional = parser_model_instances_files._action_groups.pop(
    )
    parser_model_instances_files_optional.add_argument(
        'model_instance', help=Help.param_model_instance)
    parser_model_instances_files_optional.add_argument('-v',
                                                       '--csv',
                                                       dest='csv_display',
                                                       action='store_true',
                                                       help=Help.param_csv)
    parser_model_instances_files_optional.add_argument(
        '--page-size', dest='page_size', default=20, help=Help.param_page_size)
    parser_model_instances_files_optional.add_argument(
        '--page-token',
        dest='page_token',
        required=False,
        help=Help.param_page_token)
    parser_model_instances_files._action_groups.append(
        parser_model_instances_files_optional)
    parser_model_instances_files.set_defaults(
        func=api.model_instance_files_cli)

    # Models Instances delete
    parser_model_instances_delete = subparsers_model_instances.add_parser(
        'delete',
        formatter_class=argparse.RawTextHelpFormatter,
        help=Help.command_model_instances_delete)
    parser_model_instances_delete_optional = parser_model_instances_delete._action_groups.pop(
    )
    parser_model_instances_delete_optional.add_argument(
        'model_instance', help=Help.param_model_instance)
    parser_model_instances_delete_optional.add_argument('-y',
                                                        '--yes',
                                                        dest='yes',
                                                        action='store_true',
                                                        help=Help.param_yes)
    parser_model_instances_delete._action_groups.append(
        parser_model_instances_delete_optional)
    parser_model_instances_delete.set_defaults(
        func=api.model_instance_delete_cli)

    # Models Instances update
    parser_model_instances_update = subparsers_model_instances.add_parser(
        'update',
        formatter_class=argparse.RawTextHelpFormatter,
        help=Help.command_model_instances_update)
    parser_model_instances_update_optional = parser_model_instances_update._action_groups.pop(
    )
    parser_model_instances_update_optional.add_argument(
        '-p',
        '--path',
        dest='folder',
        required=False,
        help=Help.param_model_instance_upfile)
    parser_model_instances_update._action_groups.append(
        parser_model_instances_update_optional)
    parser_model_instances_update.set_defaults(
        func=api.model_instance_update_cli)


def parse_model_instance_versions(subparsers):
    parser_model_instance_versions = subparsers.add_parser(
        'versions',
        formatter_class=argparse.RawTextHelpFormatter,
        help=Help.group_model_instance_versions,
        aliases=['miv'])

    subparsers_model_intance_versions = parser_model_instance_versions.add_subparsers(
        title='commands', dest='command')
    subparsers_model_intance_versions.required = True
    subparsers_model_intance_versions.choices = Help.model_instance_versions_choices

    # Model Instance Versions create
    parser_model_instance_versions_create = subparsers_model_intance_versions.add_parser(
        'create',
        formatter_class=argparse.RawTextHelpFormatter,
        help=Help.command_model_instance_versions_new)
    parser_model_instance_versions_create_optional = parser_model_instance_versions_create._action_groups.pop(
    )
    parser_model_instance_versions_create_optional.add_argument(
        'model_instance', help=Help.param_model_instance)
    parser_model_instance_versions_create_optional.add_argument(
        '-p',
        '--path',
        dest='folder',
        required=False,
        help=Help.param_model_instance_version_upfile)
    parser_model_instance_versions_create_optional.add_argument(
        '-n',
        '--version-notes',
        dest='version_notes',
        required=False,
        help=Help.param_model_instance_version_upfile)
    parser_model_instance_versions_create_optional.add_argument(
        '-q',
        '--quiet',
        dest='quiet',
        action='store_true',
        help=Help.param_quiet)
    parser_model_instance_versions_create_optional.add_argument(
        '-r',
        '--dir-mode',
        dest='dir_mode',
        choices=['skip', 'zip', 'tar'],
        default='skip',
        help=Help.param_dir_mode)
    parser_model_instance_versions_create._action_groups.append(
        parser_model_instance_versions_create_optional)
    parser_model_instance_versions_create.set_defaults(
        func=api.model_instance_version_create_cli)

    # Models Instance Versions download
    parser_model_instance_versions_download = subparsers_model_intance_versions.add_parser(
        'download',
        formatter_class=argparse.RawTextHelpFormatter,
        help=Help.command_model_instance_versions_download)
    parser_model_instance_versions_download_optional = parser_model_instance_versions_download._action_groups.pop(
    )
    parser_model_instance_versions_download_optional.add_argument(
        'model_instance_version', help=Help.param_model_instance_version)
    parser_model_instance_versions_download_optional.add_argument(
        '-p',
        '--path',
        dest='path',
        required=False,
        help=Help.param_downfolder)
    parser_model_instance_versions_download_optional.add_argument(
        '--untar', dest='untar', action='store_true', help=Help.param_untar)
    parser_model_instance_versions_download_optional.add_argument(
        '-f',
        '--force',
        dest='force',
        action='store_true',
        help=Help.param_force)
    parser_model_instance_versions_download_optional.add_argument(
        '-q',
        '--quiet',
        dest='quiet',
        action='store_true',
        help=Help.param_quiet)
    parser_model_instance_versions_download._action_groups.append(
        parser_model_instance_versions_download_optional)
    parser_model_instance_versions_download.set_defaults(
        func=api.model_instance_version_download_cli)

    # Models Instance Versions files
    parser_model_instance_versions_files = subparsers_model_intance_versions.add_parser(
        'files',
        formatter_class=argparse.RawTextHelpFormatter,
        help=Help.command_model_instance_versions_files)
    parser_model_instance_versions_files_optional = parser_model_instance_versions_files._action_groups.pop(
    )
    parser_model_instance_versions_files_optional.add_argument(
        'model_instance_version', help=Help.param_model_instance_version)
    parser_model_instance_versions_files_optional.add_argument(
        '-v',
        '--csv',
        dest='csv_display',
        action='store_true',
        help=Help.param_csv)
    parser_model_instance_versions_files_optional.add_argument(
        '--page-size', dest='page_size', default=20, help=Help.param_page_size)
    parser_model_instance_versions_files_optional.add_argument(
        '--page-token',
        dest='page_token',
        required=False,
        help=Help.param_page_token)
    parser_model_instance_versions_files._action_groups.append(
        parser_model_instance_versions_files_optional)
    parser_model_instance_versions_files.set_defaults(
        func=api.model_instance_version_files_cli)

    # Models Instance Versions delete
    parser_model_instance_versions_delete = subparsers_model_intance_versions.add_parser(
        'delete',
        formatter_class=argparse.RawTextHelpFormatter,
        help=Help.command_model_instance_versions_delete)
    parser_model_instance_versions_delete_optional = parser_model_instance_versions_delete._action_groups.pop(
    )
    parser_model_instance_versions_delete_optional.add_argument(
        'model_instance_version', help=Help.param_model_instance_version)
    parser_model_instance_versions_delete_optional.add_argument(
        '-y', '--yes', dest='yes', action='store_true', help=Help.param_yes)
    parser_model_instance_versions_delete._action_groups.append(
        parser_model_instance_versions_delete_optional)
    parser_model_instance_versions_delete.set_defaults(
        func=api.model_instance_version_delete_cli)


def parse_files(subparsers):
    parser_files = subparsers.add_parser(
        'files',
        formatter_class=argparse.RawTextHelpFormatter,
        help=Help.group_files,
        aliases=['f'])

    subparsers_files = parser_files.add_subparsers(title='commands',
                                                   dest='command')
    subparsers_files.required = True
    subparsers_files.choices = Help.files_choices

    # Files upload
    parser_files_upload = subparsers_files.add_parser(
        'upload',
        formatter_class=argparse.RawTextHelpFormatter,
        help=Help.command_files_upload,
        aliases=['u'])
    parser_files_upload_optional = parser_files_upload._action_groups.pop()
    parser_files_upload_optional.add_argument(
        '-i',
        '--inbox-path',
        dest='inbox_path',
        required=False,
        default='',
        help=Help.param_files_upload_inbox_path)
    parser_files_upload_optional.add_argument(
        'local_paths',
        metavar='local-path',
        nargs='+',
        help=Help.param_files_upload_local_paths)
    parser_files_upload_optional.add_argument(
        '--no-resume',
        dest='no_resume',
        action='store_true',
        required=False,
        default=False,
        help=Help.param_files_upload_no_resume)
    parser_files_upload_optional.add_argument(
        '--no-compress',
        dest='no_compress',
        action='store_true',
        required=False,
        default=False,
        help=Help.param_files_upload_no_compress)
    parser_files_upload._action_groups.append(parser_files_upload_optional)
    parser_files_upload.set_defaults(func=api.files_upload_cli)


def parse_config(subparsers):
    parser_config = subparsers.add_parser(
        'config',
        formatter_class=argparse.RawTextHelpFormatter,
        help=Help.group_config)
    subparsers_config = parser_config.add_subparsers(title='commands',
                                                     dest='command')
    subparsers_config.required = True
    subparsers_config.choices = Help.config_choices

    parser_config_view = subparsers_config.add_parser(
        'view',
        formatter_class=argparse.RawTextHelpFormatter,
        help=Help.command_config_view)
    parser_config_view.set_defaults(func=api.print_config_values)

    parser_config_set = subparsers_config.add_parser(
        'set',
        formatter_class=argparse.RawTextHelpFormatter,
        help=Help.command_config_set)
    parser_config_set._action_groups.pop()
    parser_config_set_required = parser_config_set.add_argument_group(
        'required arguments')
    parser_config_set_required.add_argument('-n',
                                            '--name',
                                            dest='name',
                                            required=True,
                                            help=Help.param_config_name)
    parser_config_set_required.add_argument('-v',
                                            '--value',
                                            dest='value',
                                            required=True,
                                            help=Help.param_config_value)
    parser_config_set.set_defaults(func=api.set_config_value)

    parser_config_unset = subparsers_config.add_parser(
        'unset',
        formatter_class=argparse.RawTextHelpFormatter,
        help=Help.command_config_unset)
    parser_config_unset._action_groups.pop()
    parser_config_unset_required = parser_config_unset.add_argument_group(
        'required arguments')
    parser_config_unset_required.add_argument('-n',
                                              '--name',
                                              dest='name',
                                              required=True,
                                              help=Help.param_config_name)
    parser_config_unset.set_defaults(func=api.unset_config_value)


class Help(object):
    kaggle_choices = [
        'competitions', 'c', 'datasets', 'd', 'kernels', 'k', 'models', 'm',
        'files', 'f', 'config'
    ]
    competitions_choices = [
        'list', 'files', 'download', 'submit', 'submissions', 'leaderboard'
    ]
    datasets_choices = [
        'list', 'files', 'download', 'create', 'version', 'init', 'metadata',
        'status'
    ]
    kernels_choices = [
        'list', 'files', 'init', 'push', 'pull', 'output', 'status'
    ]
    models_choices = [
        'instances', 'get', 'list', 'init', 'create', 'delete', 'update'
    ]
    model_instances_choices = [
        'versions', 'get', 'files', 'init', 'create', 'delete', 'update'
    ]
    model_instance_versions_choices = [
        'init', 'create', 'download', 'delete', 'files'
    ]
    files_choices = ['upload']
    config_choices = ['view', 'set', 'unset']

    kaggle = 'Use one of:\ncompetitions {' + ', '.join(
        competitions_choices) + '}\ndatasets {' + ', '.join(
            datasets_choices) + '}\nkernels {' + ', '.join(
                kernels_choices) + '}\nmodels {' + ', '.join(
                    models_choices) + '}\nmodels instances {' + ', '.join(
                        model_instances_choices
                    ) + '}\nmodels instances versions {' + ', '.join(
                        model_instance_versions_choices
                    ) + '}\nconfig {' + ', '.join(config_choices) + '}'

    group_competitions = 'Commands related to Kaggle competitions'
    group_datasets = 'Commands related to Kaggle datasets'
    group_kernels = 'Commands related to Kaggle kernels'
    group_models = 'Commands related to Kaggle models'
    group_model_instances = 'Commands related to Kaggle model instances'
    group_model_instance_versions = 'Commands related to Kaggle model instance versions'
    group_files = 'Commands related files'
    group_config = 'Configuration settings'

    # Competitions commands
    command_competitions_list = 'List available competitions'
    command_competitions_files = 'List competition files'
    command_competitions_download = 'Download competition files'
    command_competitions_submit = 'Make a new competition submission'
    command_competitions_submissions = 'Show your competition submissions'
    command_competitions_leaderboard = 'Get competition leaderboard information'

    # Datasets commands
    command_datasets_list = 'List available datasets'
    command_datasets_files = 'List dataset files'
    command_datasets_download = 'Download dataset files'
    command_datasets_new = 'Create a new dataset'
    command_datasets_new_version = 'Create a new dataset version'
    command_datasets_init = 'Initialize metadata file for dataset creation'
    command_datasets_metadata = 'Download metadata about a dataset'
    command_datasets_status = 'Get the creation status for a dataset'

    # Kernels commands
    command_kernels_list = (
        'List available kernels. By default, shows 20 results sorted by '
        'hotness')
    command_kernels_files = 'List kernel output files'
    command_kernels_init = 'Initialize metadata file for a kernel'
    command_kernels_push = 'Push new code to a kernel and run the kernel'
    command_kernels_pull = 'Pull down code from a kernel'
    command_kernels_output = 'Get data output from the latest kernel run'
    command_kernels_status = 'Display the status of the latest kernel run'

    # Models commands
    command_models_files = 'List model files'
    command_models_get = 'Get a model'
    command_models_list = 'List models'
    command_models_init = 'Initialize metadata file for model creation'
    command_models_new = 'Create a new model'
    command_models_delete = 'Delete a model'
    command_models_update = 'Update a model'

    # Files commands
    command_files_upload = 'Upload files'

    # Config commands
    command_config_path = (
        'Set folder where competition or dataset files will be '
        'downloaded')
    command_config_proxy = 'Set proxy server'
    command_config_competition = 'Set default competition'
    command_config_view = 'View current config values'
    command_config_set = 'Set a configuration value'
    command_config_unset = 'Clear a configuration value'

    # General params
    param_downfolder = (
        'Folder where file(s) will be downloaded, defaults to current working '
        'directory')
    param_wp = 'Download files to current working path'
    param_proxy = 'Proxy for HTTP requests'
    param_quiet = (
        'Suppress printing information about the upload/download progress')
    param_public = 'Create publicly (default is private)'
    param_keep_tabular = (
        'Do not convert tabular files to CSV (default is to convert)')
    param_dir_mode = (
        'What to do with directories: "skip" - ignore; "zip" - compressed upload; "tar" - '
        'uncompressed upload')
    param_delete_old_version = 'Delete old versions of this dataset'
    param_force = (
        'Skip check whether local version of file is up to date, force'
        ' file download')
    param_upfile = 'File for upload (full path)'
    param_csv = 'Print results in CSV format (if not set print in table format)'
    param_page = 'Page number for results paging. Page size is 20 by default'
    # NOTE: Default and max page size are set by the mid-tier code.
    param_page_size = (
        'Number of items to show on a page. Default size is 20, '
        'max is 200')
    param_page_token = 'Page token for results paging.'
    param_search = 'Term(s) to search for'
    param_mine = 'Display only my items'
    param_unzip = (
        'Unzip the downloaded file. Will delete the zip file when completed.')
    param_untar = (
        'Untar the downloaded file. Will delete the tar file when completed.')
    param_yes = (
        'Sets any confirmation values to "yes" automatically. Users will not be asked to confirm.'
    )

    # Competitions params
    param_competition = (
        'Competition URL suffix (use "kaggle competitions list" '
        'to show options)\nIf empty, the default competition '
        'will be used (use "kaggle config set competition")"')
    param_competition_nonempty = (
        'Competition URL suffix (use "kaggle competitions list" to show '
        'options)')
    param_competition_leaderboard_view = 'Show the top of the leaderboard'
    param_competition_leaderboard_download = 'Download entire leaderboard'
    param_competition_file = (
        'File name, all files downloaded if not provided\n(use "kaggle '
        'competitions files -c <competition>" to show options)')
    param_competition_message = 'Message describing this submission'
    param_competition_group = (
        'Search for competitions in a specific group. Default is \'general\'. '
        'Valid options are \'general\', \'entered\', and \'inClass\'')
    param_competition_category = (
        'Search for competitions of a specific category. Default is \'all\'. '
        'Valid options are \'all\', \'featured\', \'research\', '
        '\'recruitment\', \'gettingStarted\', \'masters\', and \'playground\'')
    param_competition_sort_by = (
        'Sort list results. Default is \'latestDeadline\'. Valid options are '
        '\'grouped\', \'prize\', \'earliestDeadline\', \'latestDeadline\', '
        '\'numberOfTeams\', and \'recentlyCreated\'')

    # Datasets params
    param_dataset = (
        'Dataset URL suffix in format <owner>/<dataset-name> (use '
        '"kaggle datasets list" to show options)')
    param_dataset_file = (
        'File name, all files downloaded if not provided\n(use '
        '"kaggle datasets files -d <dataset>" to show options)')
    param_dataset_version_notes = 'Message describing the new version'
    param_dataset_upfile = (
        'Folder for upload, containing data files and a '
        'special datasets-metadata.json file '
        '(https://github.com/Kaggle/kaggle-api/wiki/Dataset-Metadata). '
        'Defaults to current working directory')
    param_dataset_sort_by = (
        'Sort list results. Default is \'hottest\'. Valid options are '
        '\'hottest\', \'votes\', \'updated\', and \'active\'')
    param_dataset_size = (
        'DEPRECATED. Please use --max-size and --min-size to filter dataset sizes.'
    )
    param_dataset_file_type = (
        'Search for datasets with a specific file type. Default is \'all\'. '
        'Valid options are \'all\', \'csv\', \'sqlite\', \'json\', and '
        '\'bigQuery\'. Please note that bigQuery datasets cannot be downloaded'
    )
    param_dataset_license = (
        'Search for datasets with a specific license. Default is \'all\'. '
        'Valid options are \'all\', \'cc\', \'gpl\', \'odb\', and \'other\'')
    param_dataset_tags = (
        'Search for datasets that have specific tags. Tag list should be '
        'comma separated')
    param_dataset_user = (
        'Find public datasets owned by a specific user or organization')
    param_dataset_metadata_dir = (
        'Location to download dataset metadata to. Defaults to current working '
        'directory')
    param_dataset_metadata_update = ('A flag to indicate whether the dataset'
                                     'metadata should be updated.')
    param_dataset_maxsize = 'Specify the maximum size of the dataset to return (bytes)'
    param_dataset_minsize = 'Specify the minimum size of the dataset to return (bytes)'

    # Kernels params
    param_kernel = (
        'Kernel URL suffix in format <owner>/<kernel-name> (use "kaggle '
        'kernels list" to show options)')
    param_kernel_init = (
        'Create a metadata file for an existing kernel URL suffix in format '
        '<owner>/<kernel-name> (use "kaggle kernels list" to show options)')
    param_kernel_upfile = (
        'Folder for upload, containing data files and a '
        'special kernel-metadata.json file '
        '(https://github.com/Kaggle/kaggle-api/wiki/Kernel-Metadata). '
        'Defaults to current working directory')
    param_kernel_parent = 'Find children of the specified parent kernel'
    param_kernel_competition = 'Find kernels for a given competition slug'
    param_kernel_dataset = ('Find kernels for a given dataset slug. Format is '
                            '{username/dataset-slug}')
    param_kernel_user = 'Find kernels created by a given username'
    # TODO(b/129357583): Pull these from the same spot as the api impl
    param_kernel_language = (
        'Specify the language the kernel is written in. Default is \'all\'. '
        'Valid options are \'all\', \'python\', \'r\', \'sqlite\', and '
        '\'julia\'')
    param_kernel_type = (
        'Specify the type of kernel. Default is \'all\'. Valid '
        'options are \'all\', \'script\', and \'notebook\'')
    param_kernel_output_type = (
        'Search for specific kernel output types. '
        'Default is \'all\'.  Valid options are \'all\', '
        '\'visualizations\', and \'data\'')
    param_kernel_sort_by = (
        'Sort list results. Default is \'hotness\'. Valid '
        'options are \'hotness\', \'commentCount\', '
        '\'dateCreated\', \'dateRun\', \'relevance\', '
        '\'scoreAscending\', \'scoreDescending\', '
        '\'viewCount\', and \'voteCount\'. \'relevance\' '
        'is only applicable if a search term is specified.')
    param_kernel_pull_metadata = 'Generate metadata when pulling kernel'

    # Models params
    param_model = ('Model URL suffix in format <owner>/<model-name>')
    param_model_sort_by = (
        'Sort list results. Default is \'hotness\'. Valid options are '
        '\'hotness\', \'downloadCount\', \'voteCount\', \'notebookCount\' and \'createTime\''
    )
    param_model_owner = (
        'Find public models owned by a specific user or organization')
    param_model_downfile = (
        'Folder containing the special model-metadata.json file '
        '(https://github.com/Kaggle/kaggle-api/wiki/Model-Metadata).')
    param_model_upfile = (
        'Folder containing the special model-metadata.json file '
        '(https://github.com/Kaggle/kaggle-api/wiki/Model-Metadata). '
        'Defaults to current working directory')

    # Model Instances params
    param_model_instance = (
        'Model Instance URL suffix in format <owner>/<model-name>/<framework>/<instance-slug>'
    )
    command_model_instances_get = 'Get a model instance'
    command_model_instances_init = 'Initialize metadata file for model instance creation'
    command_model_instances_files = 'List files for the current version of a model instance'
    command_model_instances_new = 'Create a new model instance'
    param_model_instance_downfile = (
        'Folder for downloading the special model-instance-metadata.json file '
        '(https://github.com/Kaggle/kaggle-api/wiki/Model-Metadata#model-instance). '
    )
    param_model_instance_upfile = (
        'Folder for upload, containing data files and a '
        'special model-instance-metadata.json file '
        '(https://github.com/Kaggle/kaggle-api/wiki/Model-Metadata#model-instance). '
        'Defaults to current working directory')
    command_model_instances_delete = 'Delete a model instance'
    command_model_instances_update = 'Update a model instance'

    # Model Instance Versions params
    param_model_instance_version = (
        'Model Instance Version URL suffix in format <owner>/<model-name>/<framework>/<instance-slug>/<version-number>'
    )

    # Model Instance Versions params
    command_model_instance_versions_new = 'Create a new model instance version'
    param_model_instance_version_upfile = (
        'Folder for upload, containing data files and a '
        'special model-instance_version-metadata.json file '
        '(https://github.com/Kaggle/kaggle-api/wiki/ModelInstanceVersion-Metadata). '
        'Defaults to current working directory')
    command_model_instance_versions_delete = 'Delete a model instance version'
    command_model_instance_versions_download = 'Download model instance version files'
    command_model_instance_versions_files = 'List model instance version files'
    param_model_instance_version_notes = 'Version notes to record for the new model instance version'

    # Files params
    param_files_upload_inbox_path = 'Virtual path on the server where the uploaded files will be stored'
    param_files_upload_local_paths = (
        'List of local filesystem paths. Each path creates a separate file on the server. '
        'Directories are uploaded as zip archives by default (e.g., a directory called '
        '"data" will be uploaded as "data.zip")')
    param_files_upload_no_compress = 'Whether to compress directories (zip) or not (tar)'
    param_files_upload_no_resume = 'Whether to skip resumable uploads.'

    # Config params
    param_config_name = ('Name of the configuration parameter\n(one of '
                         'competition, path, proxy)')
    param_config_value = (
        ('Value of the configuration parameter, valid values '
         'depending on name\n- competition: ') + param_competition_nonempty +
        '\n- path: ' + param_downfolder + '\n- proxy: ' + param_proxy)


if __name__ == '__main__':
    main()
