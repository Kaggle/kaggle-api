from __future__ import print_function
import argparse
from kaggle import api


def main():
  parser = argparse.ArgumentParser(
      formatter_class=argparse.RawTextHelpFormatter)
  subparsers = parser.add_subparsers(
      title='commands', help=Help.kaggle, dest='command')
  subparsers.required = True
  subparsers.choices = Help.kaggle_choices
  parse_competitions(subparsers)
  parse_datasets(subparsers)
  parse_config(subparsers)
  args = parser.parse_args()
  command_args = {}
  command_args.update(vars(args))
  del command_args['func']
  del command_args['command']
  out = args.func(**command_args)
  if out is not None:
    print(out, end='')


def parse_competitions(subparsers):
  parser_competitions = subparsers.add_parser(
      'competitions',
      formatter_class=argparse.RawTextHelpFormatter,
      help=Help.group_competitions)
  subparsers_competitions = parser_competitions.add_subparsers(
      title='commands', dest='command')
  subparsers_competitions.required = True
  subparsers_competitions.choices = Help.competitions_choices

  parser_competitions_list = subparsers_competitions.add_parser(
      'list',
      formatter_class=argparse.RawTextHelpFormatter,
      help=Help.command_competitions_list)
  parser_competitions_list_optional = parser_competitions_list._action_groups.pop(
  )
  parser_competitions_list_optional.add_argument(
      '-p',
      '--page',
      dest='page',
      default=1,
      required=False,
      help=Help.param_page)
  parser_competitions_list_optional.add_argument(
      '-s', '--search', dest='search', required=False, help=Help.param_search)
  parser_competitions_list_optional.add_argument(
      '-v', '--csv', dest='csv', action='store_true', help=Help.param_csv)
  parser_competitions_list._action_groups.append(
      parser_competitions_list_optional)
  parser_competitions_list.set_defaults(func=api.competitions_list_cli)

  parser_competitions_files = subparsers_competitions.add_parser(
      'files',
      formatter_class=argparse.RawTextHelpFormatter,
      help=Help.command_competitions_files)
  parser_competitions_files_optional = parser_competitions_files._action_groups.pop(
  )
  parser_competitions_files_required = parser_competitions_files.add_argument_group(
      'required arguments')
  parser_competitions_files_optional.add_argument(
      '-c',
      '--competition',
      dest='competition',
      required=False,
      help=Help.param_competition)
  parser_competitions_files_optional.add_argument(
      '-v', '--csv', dest='csv', action='store_true', help=Help.param_csv)
  parser_competitions_files_optional.add_argument(
      '-q', '--quiet', dest='quiet', action='store_true', help=Help.param_quiet)
  parser_competitions_files._action_groups.append(
      parser_competitions_files_optional)
  parser_competitions_files.set_defaults(func=api.competition_list_files_cli)

  parser_competitions_download = subparsers_competitions.add_parser(
      'download',
      formatter_class=argparse.RawTextHelpFormatter,
      help=Help.command_competitions_download)
  parser_competitions_download_optional = parser_competitions_download._action_groups.pop(
  )
  parser_competitions_download_required = parser_competitions_download.add_argument_group(
      'required arguments')
  parser_competitions_download_optional.add_argument(
      '-c',
      '--competition',
      dest='competition',
      required=False,
      help=Help.param_competition)
  parser_competitions_download_optional.add_argument(
      '-f',
      '--file',
      dest='file',
      required=False,
      help=Help.param_competition_file)
  parser_competitions_download_optional.add_argument(
      '-p', '--path', dest='path', required=False, help=Help.param_path)
  parser_competitions_download_optional.add_argument(
      '-w',
      '--wp',
      dest='path',
      action='store_const',
      const='.',
      required=False,
      help=Help.param_wp)
  parser_competitions_download_optional.add_argument(
      '-o', '--force', dest='force', action='store_true', help=Help.param_force)
  parser_competitions_download_optional.add_argument(
      '-q', '--quiet', dest='quiet', action='store_true', help=Help.param_quiet)
  parser_competitions_download._action_groups.append(
      parser_competitions_download_optional)
  parser_competitions_download.set_defaults(func=api.competition_download_cli)

  parser_competitions_submit = subparsers_competitions.add_parser(
      'submit',
      formatter_class=argparse.RawTextHelpFormatter,
      help=Help.command_competitions_submit)
  parser_competitions_submit_optional = parser_competitions_submit._action_groups.pop(
  )
  parser_competitions_submit_required = parser_competitions_submit.add_argument_group(
      'required arguments')
  parser_competitions_submit_optional.add_argument(
      '-c',
      '--competition',
      dest='competition',
      required=False,
      help=Help.param_competition)
  parser_competitions_submit_required.add_argument(
      '-f', '--file', dest='file', required=True, help=Help.param_upfile)
  parser_competitions_submit_required.add_argument(
      '-m', '--message', dest='message', required=True, help=Help.param_message)
  parser_competitions_submit_optional.add_argument(
      '-q', '--quiet', dest='quiet', action='store_true', help=Help.param_quiet)
  parser_competitions_submit._action_groups.append(
      parser_competitions_submit_optional)
  parser_competitions_submit.set_defaults(func=api.competition_submit)

  parser_competitions_submissions = subparsers_competitions.add_parser(
      'submissions',
      formatter_class=argparse.RawTextHelpFormatter,
      help=Help.command_competitions_submissions)
  parser_competitions_submissions_optional = parser_competitions_submissions._action_groups.pop(
  )
  parser_competitions_submissions_required = parser_competitions_submissions.add_argument_group(
      'required arguments')
  parser_competitions_submissions_optional.add_argument(
      '-c',
      '--competition',
      dest='competition',
      required=False,
      help=Help.param_competition)
  parser_competitions_submissions_optional.add_argument(
      '-v', '--csv', dest='csv', action='store_true', help=Help.param_csv)
  parser_competitions_submissions_optional.add_argument(
      '-q', '--quiet', dest='quiet', action='store_true', help=Help.param_quiet)
  parser_competitions_submissions._action_groups.append(
      parser_competitions_submissions_optional)
  parser_competitions_submissions.set_defaults(
      func=api.competition_submissions_cli)


def parse_datasets(subparsers):
  parser_datasets = subparsers.add_parser(
      'datasets',
      formatter_class=argparse.RawTextHelpFormatter,
      help=Help.group_datasets)
  subparsers_datasets = parser_datasets.add_subparsers(
      title='commands', dest='command')
  subparsers_datasets.required = True
  subparsers_datasets.choices = Help.datasets_choices

  parser_datasets_list = subparsers_datasets.add_parser(
      'list',
      formatter_class=argparse.RawTextHelpFormatter,
      help=Help.command_datasets_list)
  parser_datasets_list_optional = parser_datasets_list._action_groups.pop()
  parser_datasets_list.add_argument(
      '-p',
      '--page',
      dest='page',
      default=1,
      required=False,
      help=Help.param_page)
  parser_datasets_list.add_argument(
      '-s', '--search', dest='search', required=False, help=Help.param_search)
  parser_datasets_list.add_argument(
      '-v', '--csv', dest='csv', action='store_true', help=Help.param_csv)
  parser_datasets_list._action_groups.append(parser_datasets_list_optional)
  parser_datasets_list.set_defaults(func=api.datasets_list_cli)

  parser_datasets_files = subparsers_datasets.add_parser(
      'files',
      formatter_class=argparse.RawTextHelpFormatter,
      help=Help.command_datasets_files)
  parser_datasets_files_optional = parser_datasets_files._action_groups.pop()
  parser_datasets_files_required = parser_datasets_files.add_argument_group(
      'required arguments')
  parser_datasets_files_required.add_argument(
      '-d', '--dataset', dest='dataset', required=True, help=Help.param_dataset)
  parser_datasets_files_optional.add_argument(
      '-v', '--csv', dest='csv', action='store_true', help=Help.param_csv)
  parser_datasets_files._action_groups.append(parser_datasets_files_optional)
  parser_datasets_files.set_defaults(func=api.dataset_list_files_cli)

  parser_datasets_download = subparsers_datasets.add_parser(
      'download',
      formatter_class=argparse.RawTextHelpFormatter,
      help=Help.command_datasets_download)
  parser_datasets_download_optional = parser_datasets_download._action_groups.pop(
  )
  parser_datasets_download_required = parser_datasets_download.add_argument_group(
      'required arguments')
  parser_datasets_download_required.add_argument(
      '-d', '--dataset', dest='dataset', required=True, help=Help.param_dataset)
  parser_datasets_download_optional.add_argument(
      '-f', '--file', dest='file', required=False, help=Help.param_dataset_file)
  parser_datasets_download_optional.add_argument(
      '-p', '--path', dest='path', required=False, help=Help.param_path)
  parser_datasets_download_optional.add_argument(
      '-w',
      '--wp',
      dest='path',
      action='store_const',
      const='.',
      required=False,
      help=Help.param_wp)
  parser_datasets_download_optional.add_argument(
      '-o', '--force', dest='force', action='store_true', help=Help.param_force)
  parser_datasets_download_optional.add_argument(
      '-q', '--quiet', dest='quiet', action='store_true', help=Help.param_quiet)
  parser_datasets_download._action_groups.append(
      parser_datasets_download_optional)
  parser_datasets_download.set_defaults(func=api.dataset_download_cli)

  parser_datasets_create = subparsers_datasets.add_parser(
      'create',
      formatter_class=argparse.RawTextHelpFormatter,
      help=Help.command_datasets_new)
  parser_datasets_create_optional = parser_datasets_create._action_groups.pop()
  parser_datasets_create_required = parser_datasets_create.add_argument_group(
      'required arguments')
  parser_datasets_create_required.add_argument(
      '-p', '--path', dest='folder', required=True, help=Help.param_upfolder)
  parser_datasets_create_optional.add_argument(
      '-u',
      '--public',
      dest='public',
      action='store_true',
      help=Help.param_public)
  parser_datasets_create_optional.add_argument(
      '-q', '--quiet', dest='quiet', action='store_true', help=Help.param_quiet)
  parser_datasets_create._action_groups.append(parser_datasets_create_optional)
  parser_datasets_create.set_defaults(func=api.dataset_create_new_cli)

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
      help=Help.param_version_notes)
  parser_datasets_version_required.add_argument(
      '-p', '--path', dest='folder', required=True, help=Help.param_upfolder)
  parser_datasets_version_optional.add_argument(
      '-q', '--quiet', dest='quiet', action='store_true', help=Help.param_quiet)
  parser_datasets_version._action_groups.append(
      parser_datasets_version_optional)
  parser_datasets_version.set_defaults(func=api.dataset_create_version_cli)

  parser_datasets_init = subparsers_datasets.add_parser(
      'init',
      formatter_class=argparse.RawTextHelpFormatter,
      help=Help.command_datasets_init)
  parser_datasets_init_optional = parser_datasets_init._action_groups.pop()
  parser_datasets_init_required = parser_datasets_init.add_argument_group(
      'required arguments')
  parser_datasets_init_required.add_argument(
      '-p', '--path', dest='folder', required=True, help=Help.param_upfolder)
  parser_datasets_init._action_groups.append(parser_datasets_init_optional)
  parser_datasets_init.set_defaults(func=api.dataset_initialize)


def parse_config(subparsers):
  parser_config = subparsers.add_parser(
      'config',
      formatter_class=argparse.RawTextHelpFormatter,
      help=Help.group_config)
  subparsers_config = parser_config.add_subparsers(
      title='commands', dest='command')
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
  parser_config_set_optional = parser_config_set._action_groups.pop()
  parser_config_set_required = parser_config_set.add_argument_group(
      'required arguments')
  parser_config_set_required.add_argument(
      '-n', '--name', dest='name', required=True, help=Help.param_config_name)
  parser_config_set_required.add_argument(
      '-v',
      '--value',
      dest='value',
      required=True,
      help=Help.param_config_value)
  parser_config_set.set_defaults(func=api.set_config_value)

  parser_config_unset = subparsers_config.add_parser(
      'unset',
      formatter_class=argparse.RawTextHelpFormatter,
      help=Help.command_config_unset)
  parser_config_unset_optional = parser_config_unset._action_groups.pop()
  parser_config_unset_required = parser_config_unset.add_argument_group(
      'required arguments')
  parser_config_unset_required.add_argument(
      '-n', '--name', dest='name', required=True, help=Help.param_config_name)
  parser_config_unset.set_defaults(func=api.unset_config_value)


class Help:
  kaggle_choices = ['competitions', 'datasets', 'config']
  competitions_choices = ['list', 'files', 'download', 'submit', 'submissions']
  datasets_choices = ['list', 'files', 'download', 'create', 'version', 'init']
  config_choices = ['view', 'set', 'unset']

  kaggle = 'Use one of:\ncompetitions {' + ', '.join(
      competitions_choices) + '}\ndatasets {' + ', '.join(
          datasets_choices) + '}\nconfig {' + ', '.join(config_choices) + '}'

  group_datasets = 'Commands related to Kaggle datasets'
  group_competitions = 'Commands related to Kaggle competitions'
  group_config = 'Configuration settings'

  command_competitions_list = 'List available competitions'
  command_competitions_files = 'List competition files'
  command_competitions_download = 'Download competition files'
  command_competitions_submit = 'Make a new competition submission'
  command_competitions_submissions = 'Show your competition submissions'
  command_datasets_list = 'List available datasets'
  command_datasets_files = 'List dataset files'
  command_datasets_download = 'Download dataset files'
  command_datasets_new = 'Create a new dataset'
  command_datasets_new_version = 'Create a new dataset version'
  command_datasets_init = 'Initialize metadata file for dataset creation'
  command_config_path = ('Set folder where competition or dataset files will be'
                         ' downloaded')
  command_config_proxy = 'Set proxy server'
  command_config_competition = 'Set default competition'
  command_config_view = 'View current config values'
  command_config_set = 'Set a configuration value'
  command_config_unset = 'Clear a configuration value'

  param_competition = ('Competition URL suffix (use "kaggle competitions list" '
                       'to show options)\nIf empty, the default competition '
                       'will be used (use "kaggle config set competition")"')
  param_competition_nonempty = ('Competition URL suffix (use "kaggle '
                                'competitions list" to show options)')
  param_path = 'Folder where file(s) will be downloaded, defaults to ' + api.config_path
  param_wp = 'Download files to current working path'
  param_proxy = 'Proxy for HTTP requests'
  param_quiet = 'Suppress printing information about download progress'
  param_public = 'Create the Dataset publicly (default is private)'
  param_force = ('Skip check whether local version of file is up to date, force'
                 ' file download')
  param_dataset = ('Dataset URL suffix in format <owner>/<dataset-name> (use '
                   '"kaggle datasets list" to show options)')
  param_upfile = 'File for upload (full path)'
  param_upfolder = ('Folder for upload, containing data files and a special '
                    'metadata.json file '
                    '(https://github.com/Kaggle/kaggle-api/wiki/Metadata)')
  param_version_notes = 'Message describing the new version'
  param_csv = 'Print results in CSV format (if not set print in table format)'
  param_page = 'Page number for results paging'
  param_search = 'Term(s) to search for'
  param_competition_file = ('File name, all files downloaded if not '
                            'provided\n(use "kaggle competitions files -c '
                            '<competition>" to show options)')
  param_dataset_file = ('File name, all files downloaded if not provided\n(use '
                        '"kaggle datasets files -d <dataset>" to show options)')
  param_message = 'Message describing this submission'
  param_config_name = ('Name of the configuration parameter\n(one of '
                       'competition, path, proxy)')
  param_config_value = (
      'Value of the configuration parameter, valid values '
      'depending on name\n- competition: '
  ) + param_competition_nonempty + '\n- path: ' + param_path + '\n- proxy: ' + param_proxy
