# coding=utf-8
import json
import os
import sys
import time

from requests import HTTPError

from kaggle.rest import ApiException

sys.path.insert(0,'..')

from kaggle import api


# Run this script in the container with the server running.
# In the case of unresolvable failure, run reset_database.sh.

model_owner = api.config_values['username']
model_title = 'testing'
instance_name = 'test'
framework_name = 'jax'

kernel_name = 'testing'

# List kernels
print('List kernels')
kernels = api.kernels_list()
print(len(kernels))

# Initialize kernel
print('Initialize a kernel')
kernel_metadata_path = api.kernels_initialize('kernel')
print(kernel_metadata_path)

# Push a kernel
print('Push a kernel')
def update_kernel_metadata_file(metadata_file, k_name):
    with open(metadata_file) as f:
        meta_data = json.load(f)
        meta_id = meta_data['id']
        if 'INSERT_KERNEL_SLUG_HERE' in meta_id:
            meta_id = meta_id.replace('INSERT_KERNEL_SLUG_HERE', k_name)
        meta_title = meta_data['title']
        if 'INSERT_TITLE_HERE' == meta_title:
            meta_title = k_name
        meta_path = meta_data['code_file']
        if 'INSERT_CODE_FILE_PATH_HERE' == meta_path:
            meta_path = f'{k_name}.ipynb'
        meta_data['id'] = meta_id
        meta_data['title'] = meta_title
        meta_data['code_file'] = meta_path
        meta_data['language'] = 'python'
        meta_data['kernel_type'] ='notebook'
    with open(metadata_file, 'w') as f:
        json.dump(meta_data, f, indent=2)
    return meta_data
md = update_kernel_metadata_file(kernel_metadata_path, kernel_name)
push_result = api.kernels_push('kernel')
print(f'{push_result.ref} v{push_result.versionNumber}')

# Get kernel status
print('Get the status of a kernel')
kernel_slug = md['id']
status_result = api.kernels_status(kernel_slug)
print(status_result['status'])
start_time = time.time()
# If this loop is stuck because the kernel stays queued, go to the Kaggle web site
# on localhost and cancel the active event. That will exit the loop, but you may
# need to clean up other active kernels to get it to run again.
while status_result['status'] == 'running' or status_result['status'] == 'queued':
    time.sleep(5)
    status_result = api.kernels_status(kernel_slug)
    print(status_result['status'])
end_time = time.time()
print(f'Ready in {end_time-start_time}s')

# List output files
print('List kernel output files')
fs = api.kernels_list_files(kernel_slug)
print(len(fs.files))

# Download output files
print('Download kernel output files')
fs = api.kernels_output(kernel_slug, 'kernel/tmp')
print(fs)
for file in fs:
    os.remove(file)
os.rmdir('kernel/tmp')

# Pull a kernel
print('Pull a kernel')
fs = api.kernels_pull('stevemessick/testing', 'kernel/tmp', metadata=True)
print(fs)
os.remove(f'{fs}/{kernel_metadata_path.split("/")[1]}')
os.remove(f'{fs}/{kernel_name}.ipynb')
os.rmdir(fs)

pass

def create_dataset_metadata_file(dataset_dir):
    metadata_file = os.path.join(dataset_dir, api.DATASET_METADATA_FILE)
    try:
        with open(metadata_file) as f:
            original = json.load(f)
            if 'versionNumber' in original:
                version_num = int(original['versionNumber'])
            else:
                version_num = 0
    except FileNotFoundError:
        version_num = 0
        pass
    version_num += 1
    return version_num, metadata_file

def update_dataset_metadata_file(metadata_file, data_name, version_num):
    with open(metadata_file) as f:
        meta_data = json.load(f)
        meta_id = meta_data['id']
        if 'INSERT_SLUG_HERE' in meta_id:
            meta_id = meta_id.replace('INSERT_SLUG_HERE', data_name)
        meta_title = meta_data['title']
        if 'INSERT_TITLE_HERE' == meta_title:
            meta_title = data_name
        meta_data['id'] = meta_id
        meta_data['title'] = meta_title
        meta_data['versionNumber'] = version_num
    if not 'resources' in meta_data:
        resource_list = [
            {
                "path": "data.csv",
                "description": "Description",
                "schema": {
                    "fields": [
                        {
                            "name": "NumberField",
                            "description": "id",
                            "type": "number"
                        },
                        {
                            "name": "StringField",
                            "description": "label",
                            "type": "string"
                        }
                    ]
                }
            }
        ]
        meta_data.update({'resources': resource_list})
    with open(meta_file, 'w') as f:
        json.dump(meta_data, f)

up_file = 'sample_submission.csv'
description = 'House prices submission message'
competition = 'house-prices-advanced-regression-techniques'
dataset_directory = 'dataset'

# List competitions
print('List competitions')
competitions = api.competitions_list()
print(len(competitions))

# Submit to a competition
print(f'Submit to competition: {competition}')
try:
    api.competition_submit(up_file, description, competition)
except HTTPError:
    print('Competition submission limit reached for the day')

# List submissions to a competition
print(f'List submissions of competition: {competition}')
submissions = api.competition_submissions(competition)
print(submissions)

# List competition files
print(f'List files of competition: {competition}')
competition_files = api.competition_list_files(competition).files
print(competition_files)

# Download competition data file
competition_file = competition_files[0]
print(f'Download competition data file: {competition_file.ref}')
api.competition_download_file(competition, competition_file.ref, force=True)
os.remove(competition_file.ref)

# Download all files for a competition
print(f'Download all files for competition: {competition}')
api.competition_download_files(competition)
os.remove(f'{competition}.zip')
print(f'Downloaded and deleted {competition}.zip')

# Show competition leaderboard
print(f'Show leaderboard for competition: {competition}')
result=api.competition_leaderboard_view(competition)
print(len(result))

# Download competition leaderboard
print(f'Download leaderboard for competition: {competition}')
api.competition_leaderboard_download(competition, 'tmp')
os.remove(f'tmp/{competition}.zip')
print('Downloaded and deleted {tmp/{competition}.zip}')

# List datasets
print('List datasets')
datasets = api.dataset_list(sort_by='votes')
print(len(datasets))

# Download dataset metadata
dataset = str(datasets[0])
print(f'Download dataset metadata: {dataset}')
m = api.dataset_metadata(dataset, None)
print(f'Downloaded {m}')

# Update dataset metadata
print(f'Update dataset metadata: {dataset}')
api.dataset_metadata_update(dataset, None)
os.remove(m)
print(f'Updated {dataset}')

# List files for a dataset
print(f'List files of dataset {dataset}')
dataset_files = api.dataset_list_files(dataset)
print(len(dataset_files.files))

# Get status of a dataset
print(f'Get status of dataset: {dataset}')
print(api.dataset_status(dataset))

# Download dataset file
dataset_file = dataset_files.files[0]
print(f'Download dataset file {dataset_file.ref}')
api.dataset_download_file(dataset, dataset_file.name, 'tmp')
os.remove(f'tmp/{dataset_file.name}')
os.rmdir('tmp')
print(f'Downloaded and deleted tmp/{dataset_file.name}')

# Download all files for a dataset
print(f'Download all files for dataset {dataset}')
api.dataset_download_files(dataset)
ds = dataset.split('/')
os.remove(f'{ds[1]}.zip')
print(f'Downloaded and deleted {ds[1]}.zip')

# Init metadata file
print(f'Create metadata for {dataset_directory}')
dataset_name = 'kaggleapitestdataset'
version_number, meta_file = create_dataset_metadata_file(dataset_directory)
api.dataset_initialize('dataset')
print(os.listdir(dataset_directory))

# Create a dataset
print('Create a new dataset')
update_dataset_metadata_file(meta_file, dataset_name, version_number)
new_dataset = api.dataset_create_new(dataset_directory)
print(new_dataset)

# Create a dataset version
print('Create a dataset version')
repeat = True
while repeat:
    try:
        # This may fail if the dataset hasn't been fully initialized yet.
        new_version = api.dataset_create_version(dataset_directory, "Notes")
        repeat = False
    except ApiException:
        time.sleep(5)
        print('try again')
# noinspection PyUnboundLocalVariable
print(new_version)
os.remove(meta_file)

# List models
print('List models')
ms = api.models_list()
print(len(ms['models']))

# Initialize model metadata
print('Initialize model metadata')
model_metadata_file = api.model_initialize('model')
print(model_metadata_file)

def update_model_metadata(metadata_file, owner, title, slug):
    with open(metadata_file) as f:
        meta_data = json.load(f)
        meta_id = meta_data['ownerSlug']
        if 'INSERT_OWNER_SLUG_HERE' == meta_id:
            meta_id = owner
        meta_title = meta_data['title']
        if 'INSERT_TITLE_HERE' == meta_title:
            meta_title = title
        meta_path = meta_data['slug']
        if 'INSERT_SLUG_HERE' == meta_path:
            meta_path = slug
        meta_data['ownerSlug'] = meta_id
        meta_data['title'] = meta_title
        meta_data['slug'] = meta_path
    with open(metadata_file, 'w') as f:
        json.dump(meta_data, f, indent=2)
    return meta_data
model_meta_data = update_model_metadata(model_metadata_file, model_owner, model_title, model_title)

# Create a model
print('Create a mmodel')
model = api.model_create_new('model')
if model.hasError:
    # We don't really care about this.
    print(model.error)
else:
    print(model.ref)

# Get a model
print('Get a model')
model_data = api.model_get(f'{model_owner}/{model_title}')
print(model_data['ref'])

# Update a model
print('Update a model')
update_response = api.model_update('model')
print(update_response.ref)

# Initialize model metadata
print('Initialize model metadata')
model_metadata_file = api.model_initialize('model')
print(model_metadata_file)

# Initialize a model instance
print('Initialize a model instance')
instance_metadata_file = api.model_instance_initialize('model/instance')
print(instance_metadata_file)

def update_model_instance_metadata(metadata_file, owner, model_slug, instance_slug, framework):
    with open(metadata_file) as f:
        meta_data = json.load(f)
        meta_owner = meta_data['ownerSlug']
        if 'INSERT_OWNER_SLUG_HERE' == meta_owner:
            meta_owner = owner
        meta_framework = meta_data['framework']
        if 'INSERT_FRAMEWORK_HERE' == meta_framework:
            meta_framework = framework
        meta_instance = meta_data['instanceSlug']
        if 'INSERT_INSTANCE_SLUG_HERE' == meta_instance:
            meta_instance = instance_slug
        meta_model = meta_data['modelSlug']
        if 'INSERT_EXISTING_MODEL_SLUG_HERE' == meta_model:
            meta_model = model_slug
        meta_data['ownerSlug'] = meta_owner
        meta_data['modelSlug'] = meta_model
        meta_data['framework'] = meta_framework
        meta_data['instanceSlug'] = meta_instance
    with open(metadata_file, 'w') as f:
        json.dump(meta_data, f, indent=2)
    return meta_data
model_instance_meta_data = update_model_instance_metadata(
    instance_metadata_file, model_owner, model_meta_data['slug'], instance_name, framework_name)

# Create a model instance
print('Create a model instance')
inst_create_resp = api.model_instance_create('model/instance')
print(inst_create_resp.ref)

model_instance = f'{model_owner}/{model_meta_data["slug"]}/{framework_name}/{instance_name}'

# Get a model instance
print(f'Get a model instance {model_instance}')
repeat = True
while repeat:
    try:
        inst_get_resp = api.model_instance_get(model_instance)
        repeat = False
    except ApiException:
        print('try again')
# noinspection PyUnboundLocalVariable
print(inst_get_resp['url'])

# List files for a model instance
print('List files for a model instance')
inst_files_resp = api.model_instance_files(model_instance)
print(inst_files_resp.files[0])

# Update a model instance
print('Update a model instance')
inst_update_resp = api.model_instance_update('model/instance')
print(inst_update_resp)

# Create a model instance version
print('Initialize a model instance version')
version_metadata_resp = api.model_instance_version_create(model_instance, 'model/instance/version')
print(version_metadata_resp.ref)

# List files of a model instance version
print('List files of a model instance version')
r = api.model_instance_version_files(f'{model_instance}/1')
print(len(r.files))

# Download a model instance version
print('Download a model instance version')
version_file = api.model_instance_version_download(f'{model_instance}/1', 'tmp')
print(version_file)
os.remove(version_file)
os.rmdir('tmp')

# Delete a model instance version
print('Delete a model instance version')
version_delete_resp = api.model_instance_version_delete(f'{model_instance}/1', True)
print(not version_delete_resp.hasError)

# Delete a model instance
print('Delete a model instance')
inst_update_resp = api.model_instance_delete(model_instance, True)
print(inst_update_resp)

# Delete a model
print('Delete a model')
delete_response = api.model_delete(f'{model_owner}/{model_title}', True)
if delete_response.hasError:
   print(delete_response.error)
else:
   print('Deleted')

print("Finished running tests")
