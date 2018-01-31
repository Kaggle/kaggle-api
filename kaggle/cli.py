from __future__ import print_function
import argparse
from kaggle import api

def main():
  parser = argparse.ArgumentParser(formatter_class = argparse.RawTextHelpFormatter)
  subparsers = parser.add_subparsers(title = 'commands', help = Help.kaggle, dest = 'command')
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
    print(out,end='')

def parse_competitions(subparsers):
  parser_competitions = subparsers.add_parser('competitions', formatter_class = argparse.RawTextHelpFormatter)
  subparsers_competitions = parser_competitions.add_subparsers(title = 'commands', dest = 'command')
  subparsers_competitions.required = True
  subparsers_competitions.choices = Help.competitions_choices

  parser_competitions_list = subparsers_competitions.add_parser('list', formatter_class = argparse.RawTextHelpFormatter)
  parser_competitions_list_optional = parser_competitions_list._action_groups.pop()
  parser_competitions_list_optional.add_argument('-p', '--page', dest = 'page', default = 1, required = False, help = Help.page)
  parser_competitions_list_optional.add_argument('-s', '--search', dest = 'search', required = False, help = Help.search)
  parser_competitions_list_optional.add_argument('-v', '--csv', dest = 'csv', action = 'store_true', help = Help.csv)
  parser_competitions_list._action_groups.append(parser_competitions_list_optional)
  parser_competitions_list.set_defaults(func = api.competitionsListCli)

  parser_competitions_files = subparsers_competitions.add_parser('files', formatter_class = argparse.RawTextHelpFormatter)
  parser_competitions_files_optional =  parser_competitions_files._action_groups.pop()
  parser_competitions_files_required = parser_competitions_files.add_argument_group('required arguments')
  parser_competitions_files_required.add_argument('-c', '--competition', dest = 'competition', required = True, help = Help.competition)
  parser_competitions_files_optional.add_argument('-v', '--csv', dest = 'csv', action = 'store_true', help = Help.csv)
  parser_competitions_files._action_groups.append(parser_competitions_files_optional)
  parser_competitions_files.set_defaults(func = api.competitionListFilesCli)  

  parser_competitions_download = subparsers_competitions.add_parser('download', formatter_class = argparse.RawTextHelpFormatter)
  parser_competitions_download_optional = parser_competitions_download._action_groups.pop()
  parser_competitions_download_required = parser_competitions_download.add_argument_group('required arguments')
  parser_competitions_download_required.add_argument('-c', '--competition', dest = 'competition', required = True, help = Help.competition)
  parser_competitions_download_optional.add_argument('-f', '--file', dest = 'file', required = False, help = Help.competition_file)
  parser_competitions_download_optional.add_argument('-p', '--path', dest = 'path', required = False, help = Help.path)
  parser_competitions_download_optional.add_argument('-w', '--wp', dest = 'path', action = 'store_const', const = '.', required = False, help = Help.wp)
  parser_competitions_download_optional.add_argument('-o', '--force', dest = 'force', action = 'store_true', help = Help.force)
  parser_competitions_download_optional.add_argument('-q', '--quiet', dest = 'quiet', action = 'store_true', help = Help.quiet)
  parser_competitions_download._action_groups.append(parser_competitions_download_optional)
  parser_competitions_download.set_defaults(func = api.competitionDownloadCli)  

  parser_competitions_submit = subparsers_competitions.add_parser('submit', formatter_class = argparse.RawTextHelpFormatter)
  parser_competitions_submit_optional = parser_competitions_submit._action_groups.pop()
  parser_competitions_submit_required = parser_competitions_submit.add_argument_group('required arguments')
  parser_competitions_submit_required.add_argument('-c', '--competition', dest = 'competition', required = True, help = Help.competition)
  parser_competitions_submit_required.add_argument('-f', '--file', dest = 'file', required = True, help = Help.upfile)
  parser_competitions_submit_required.add_argument('-m', '--message', dest = 'message', required = True, help = Help.message)
  parser_competitions_submit._action_groups.append(parser_competitions_submit_optional)
  parser_competitions_submit.set_defaults(func = api.competitionSubmit)

  parser_competitions_submissions = subparsers_competitions.add_parser('submissions', formatter_class = argparse.RawTextHelpFormatter)
  parser_competitions_submissions_optional =  parser_competitions_submissions._action_groups.pop()
  parser_competitions_submissions_required = parser_competitions_submissions.add_argument_group('required arguments')
  parser_competitions_submissions_required.add_argument('-c', '--competition', dest = 'competition', required = True, help = Help.competition)
  parser_competitions_submissions_optional.add_argument('-v', '--csv', dest = 'csv', action = 'store_true', help = Help.csv)
  parser_competitions_submissions._action_groups.append(parser_competitions_submissions_optional)
  parser_competitions_submissions.set_defaults(func = api.competitionSubmissionsCli)  


def parse_datasets(subparsers):
  parser_datasets = subparsers.add_parser('datasets', formatter_class = argparse.RawTextHelpFormatter)
  subparsers_datasets = parser_datasets.add_subparsers(title = 'commands', dest = 'command')
  subparsers_datasets.required = True
  subparsers_datasets.choices = Help.datasets_choices

  parser_datasets_list = subparsers_datasets.add_parser('list', formatter_class = argparse.RawTextHelpFormatter)
  parser_datasets_list_optional = parser_datasets_list._action_groups.pop()
  parser_datasets_list.add_argument('-p', '--page', dest = 'page', default = 1, required = False, help = Help.page)
  parser_datasets_list.add_argument('-s', '--search', dest = 'search', required = False, help = Help.search)
  parser_datasets_list.add_argument('-v', '--csv', dest = 'csv', action = 'store_true', help = Help.csv)
  parser_datasets_list._action_groups.append(parser_datasets_list_optional)
  parser_datasets_list.set_defaults(func = api.datasetsListCli)

  parser_datasets_files = subparsers_datasets.add_parser('files', formatter_class = argparse.RawTextHelpFormatter)
  parser_datasets_files_optional = parser_datasets_files._action_groups.pop()
  parser_datasets_files_required = parser_datasets_files.add_argument_group('required arguments')
  parser_datasets_files_required.add_argument('-d', '--dataset', dest = 'dataset', required = True, help = Help.dataset)
  parser_datasets_files_optional.add_argument('-v', '--csv', dest = 'csv', action = 'store_true', help = Help.csv)
  parser_datasets_files._action_groups.append(parser_datasets_files_optional)
  parser_datasets_files.set_defaults(func = api.datasetListFilesCli)  

  parser_datasets_download = subparsers_datasets.add_parser('download', formatter_class = argparse.RawTextHelpFormatter)
  parser_datasets_download_optional = parser_datasets_download._action_groups.pop()
  parser_datasets_download_required = parser_datasets_download.add_argument_group('required arguments')
  parser_datasets_download_required.add_argument('-d', '--dataset', dest = 'dataset', required = True, help = Help.dataset)
  parser_datasets_download_optional.add_argument('-f', '--file', dest = 'file', required = False, help = Help.dataset_file)
  parser_datasets_download_optional.add_argument('-p', '--path', dest = 'path', required = False, help = Help.path)
  parser_datasets_download_optional.add_argument('-w', '--wp', dest = 'path', action = 'store_const', const = '.', required = False, help = Help.wp)
  parser_datasets_download_optional.add_argument('-o', '--force', dest = 'force', action = 'store_true', help = Help.force)
  parser_datasets_download_optional.add_argument('-q', '--quiet', dest = 'quiet', action = 'store_true', help = Help.quiet)
  parser_datasets_download._action_groups.append(parser_datasets_download_optional)
  parser_datasets_download.set_defaults(func = api.datasetDownloadCli)  

def parse_config(subparsers):
  parser_config = subparsers.add_parser('config', formatter_class = argparse.RawTextHelpFormatter)
  subparsers_config = parser_config.add_subparsers(title = 'commands', dest = 'command')
  subparsers_config.required = True
  subparsers_config.choices = Help.config_choices

  parser_config_path = subparsers_config.add_parser('path', formatter_class = argparse.RawTextHelpFormatter, help = Help.download_path)
  parser_config_path_optional = parser_config_path._action_groups.pop()
  parser_config_path_optional.add_argument('-p', '--path', dest = 'path', required = False, help = Help.path)
  parser_config_path._action_groups.append(parser_config_path_optional)
  parser_config_path.set_defaults(func = api.downloadPath)  

class Help:  
  kaggle_choices = ['competitions', 'datasets', 'config']
  competitions_choices = ['list', 'files', 'download', 'submit', 'submissions']
  datasets_choices = ['list', 'files', 'download']
  config_choices = ['path']

  kaggle = 'Use one of:\ncompetitions {' + ', '.join(competitions_choices) +'}\ndatasets {' + ', '.join(datasets_choices) + '}\nconfig {' + ', '.join(config_choices) + '}'
  competition = 'competition URL suffix\n(use "kaggle competitions list" to show options)'
  path = 'folder where file(s) will be downloaded, defaults to ' + api.configPath
  force = 'skip check whether local version of file is up to date, force file download'
  quiet = 'suppress printing information about download progress'
  dataset = 'dataset URL suffix in format <owner>/<dataset-name>\n(use "kaggle datasets list" to show options)'
  page = 'page number'
  upfile = 'file for upload, including path'
  message = 'message describing this submission'
  competition_file = 'file name, all files downloaded if not provided\n(use "kaggle competitions files -c <competition>" to show options)'
  dataset_file = 'file name, all files downloaded if not provided\n(use "kaggle datasets files -d <dataset>" to show options)'
  download_path = 'check or set folder where files will be downloaded'
  csv = 'print in CSV format\n(if not set print in table format)'
  search = 'term(s) to search for'
  wp = 'download to current working path'