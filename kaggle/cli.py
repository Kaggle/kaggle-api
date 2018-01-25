import argparse
import inspect
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
  parser_competitions_list.add_argument('--page', '-p', dest = 'page', default = 1, required = False, help = Help.page)
  parser_competitions_list.add_argument('--csv', '-s', dest = 'csv', action = 'store_true', help = Help.csv)
  parser_competitions_list.add_argument('--search', '-e', dest = 'search', required = False, help = Help.search)
  parser_competitions_list.set_defaults(func = api.competitionsListCli)

  parser_competitions_submit = subparsers_competitions.add_parser('submit', formatter_class = argparse.RawTextHelpFormatter)
  parser_competitions_submit.add_argument('--competition', '-c', dest = 'competition', required = True, help = Help.competition)
  parser_competitions_submit.add_argument('--file', '-f', dest = 'file', required = True, help = Help.upfile)
  parser_competitions_submit.add_argument('--description', '-d', dest = 'description', required = True, help = Help.description)
  parser_competitions_submit.set_defaults(func = api.competitionSubmit)

  parser_competitions_submissions = subparsers_competitions.add_parser('submissions', formatter_class = argparse.RawTextHelpFormatter)
  parser_competitions_submissions.add_argument('--competition', '-c', dest = 'competition', required = True, help = Help.competition)
  parser_competitions_submissions.add_argument('--csv', '-s', dest = 'csv', action = 'store_true', help = Help.csv)
  parser_competitions_submissions.set_defaults(func = api.competitionSubmissionsCli)  

  parser_competitions_list_files = subparsers_competitions.add_parser('list-files', formatter_class = argparse.RawTextHelpFormatter)
  parser_competitions_list_files.add_argument('--competition', '-c', dest = 'competition', required = True, help = Help.competition)
  parser_competitions_list_files.add_argument('--csv', '-s', dest = 'csv', action = 'store_true', help = Help.csv)
  parser_competitions_list_files.set_defaults(func = api.competitionListFilesCli)  

  parser_competitions_download_file = subparsers_competitions.add_parser('download-file', formatter_class = argparse.RawTextHelpFormatter)
  parser_competitions_download_file.add_argument('--competition', '-c', dest = 'competition', required = True, help = Help.competition)
  parser_competitions_download_file.add_argument('--file', '-f', dest = 'file', required = True, help = Help.competition_file)
  parser_competitions_download_file.add_argument('--path', '-p', dest = 'path', required = False, help = Help.path)
  parser_competitions_download_file.add_argument('--force', '-o', dest = 'force', action = 'store_true', help = Help.force)
  parser_competitions_download_file.add_argument('--verbose', '-v', dest = 'verbose', action = 'store_true', help = Help.verbose)
  parser_competitions_download_file.set_defaults(func = api.competitionDownloadFile)  

  parser_competitions_download_files = subparsers_competitions.add_parser('download-files', formatter_class = argparse.RawTextHelpFormatter)
  parser_competitions_download_files.add_argument('--competition', '-c', dest = 'competition', required = True, help = Help.competition)
  parser_competitions_download_files.add_argument('--path', '-p', dest = 'path', required = False, help = Help.path)
  parser_competitions_download_files.add_argument('--force', '-o', dest = 'force', action='store_true', help = Help.force)
  parser_competitions_download_files.add_argument('--verbose', '-v', dest = 'verbose', action='store_true', help = Help.verbose)
  parser_competitions_download_files.set_defaults(func = api.competitionDownloadFiles) 

def parse_datasets(subparsers):
  parser_datasets = subparsers.add_parser('datasets', formatter_class = argparse.RawTextHelpFormatter)
  subparsers_datasets = parser_datasets.add_subparsers(title = 'commands', dest = 'command')
  subparsers_datasets.required = True
  subparsers_datasets.choices = Help.datasets_choices

  parser_datasets_list = subparsers_datasets.add_parser('list', formatter_class = argparse.RawTextHelpFormatter)
  parser_datasets_list.add_argument('--page', '-p', dest = 'page', default = 1, required = False, help = Help.page)
  parser_datasets_list.add_argument('--csv', '-s', dest = 'csv', action = 'store_true', help = Help.csv)
  parser_datasets_list.add_argument('--search', '-e', dest = 'search', required = False, help = Help.search)
  parser_datasets_list.set_defaults(func = api.datasetsListCli)

  parser_datasets_list_files = subparsers_datasets.add_parser('list-files', formatter_class = argparse.RawTextHelpFormatter)
  parser_datasets_list_files.add_argument('--dataset', '-d', dest = 'dataset', required = True, help = Help.dataset)
  parser_datasets_list_files.add_argument('--csv', '-s', dest = 'csv', action = 'store_true', help = Help.csv)
  parser_datasets_list_files.set_defaults(func = api.datasetListFilesCli)  

  parser_datasets_download_file = subparsers_datasets.add_parser('download-file', formatter_class = argparse.RawTextHelpFormatter)
  parser_datasets_download_file.add_argument('--dataset', '-d', dest = 'dataset', required = True, help = Help.dataset)
  parser_datasets_download_file.add_argument('--file', '-f', dest = 'file', required = True, help = Help.dataset_file)
  parser_datasets_download_file.add_argument('--path', '-p', dest = 'path', required = False, help = Help.path)
  parser_datasets_download_file.add_argument('--force', '-o', dest = 'force', action = 'store_true', help = Help.force)
  parser_datasets_download_file.add_argument('--verbose', '-v', dest = 'verbose', action = 'store_true', help = Help.verbose)
  parser_datasets_download_file.set_defaults(func = api.datasetDownloadFile)  

  parser_datasets_download_files = subparsers_datasets.add_parser('download-files', formatter_class = argparse.RawTextHelpFormatter)
  parser_datasets_download_files.add_argument('--dataset', '-d', dest = 'dataset', required = True, help = Help.dataset)
  parser_datasets_download_files.add_argument('--path', '-p', dest = 'path', required = False, help = Help.path)
  parser_datasets_download_files.add_argument('--force', '-o', dest = 'force', action = 'store_true', help = Help.force)
  parser_datasets_download_files.add_argument('--verbose', '-v', dest = 'verbose', action = 'store_true', help = Help.verbose)
  parser_datasets_download_files.set_defaults(func = api.datasetDownloadFiles) 

def parse_config(subparsers):
  parser_config = subparsers.add_parser('config', formatter_class = argparse.RawTextHelpFormatter)
  subparsers_config = parser_config.add_subparsers(title = 'commands', dest = 'command')
  subparsers_config.required = True
  subparsers_config.choices = Help.config_choices

  parser_config_download_path = subparsers_config.add_parser('download-path', formatter_class = argparse.RawTextHelpFormatter, help = Help.download_path)
  parser_config_download_path.add_argument('--path', '-p', dest = 'path', required = False, help = Help.path)
  parser_config_download_path.set_defaults(func = api.downloadPath)  

class Help:  
  kaggle_choices = ['competitions', 'datasets', 'config']
  competitions_choices = ['list', 'submit', 'submissions', 'list-files', 'download-file', 'download-files']
  datasets_choices = ['list', 'list-files', 'download-file', 'download-files']
  config_choices = ['download-path']

  kaggle = 'Use one of:\ncompetitions {' + ', '.join(competitions_choices) +'}\ndatasets {' + ', '.join(datasets_choices) + '}\nconfig {' + ', '.join(config_choices) + '}'
  competition = 'competition URL suffix\n(use "kaggle competitions list" to show options)'
  path = 'folder where file(s) will be downloaded, defaults to ' + api.configPath
  force = 'skip check whether local version of file is up to date, force file download'
  verbose = 'print information about download progress'
  dataset = 'dataset URL suffix in format <owner>/<dataset-name>\n(use "kaggle datasets list" to show options)'
  page = 'page number'
  upfile = 'file for upload, including path'
  description = 'description message for this submission'
  competition_file = 'file name\n(use "kaggle competitions list-files -c <competition>" to show options)'
  dataset_file = 'file name\n(use "kaggle datasets list-files -d <dataset>" to show options)'
  download_path = 'check or set folder where files will be downloaded'
  csv = 'print in CSV format\n(if not set print in table format)'
  search = 'term(s) to search for'