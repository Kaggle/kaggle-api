# coding=utf-8
from kaggle import api

up_file = 'sample_submission.csv'
description = 'House prices submission message'
competition = 'house-prices-advanced-regression-techniques'

# List competitions
print('List competitions')
competitions = api.competitions_list()

# Submit to a competition
print(f'Submit to competition: {competition}')
submit_result = api.competition_submit(up_file, description, competition)

# List submissions to a competition
print(f'List submissions of competition: {competition}')
submissions = api.competition_submissions(competition)

# List competition files
print(f'List files of competition: {competition}')
competition_files = api.competition_list_files(competition)

# Download competition data file
competition_file = competition_files[0]
print(f'Download competition data file: {competition_file.ref}')
api.competition_download_file(competition, competition_file.ref)

# Download all files for a competition
print(f'Download all files for competition: {competition}')
api.competition_download_files(competition)

# List datasets
print('List datasets')
datasets = api.dataset_list(sort_by='votes')

# List files for a dataset
dataset = datasets[0]
print(f'List files of dataset {dataset}')
dataset_files = api.dataset_list_files(dataset.ref)

# Download dataset file
dataset_file = dataset_files.files[0]
print(f'Download dataset file {dataset_file.ref}')
api.dataset_download_file(dataset.ref, dataset_file.ref)

# Download all files for a dataset
print(f'Download all fields for dataset {dataset.ref}')
api.dataset_download_files(dataset.ref)

print("Finished running tests")
