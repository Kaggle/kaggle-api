# coding=utf-8
import json
import unittest
import os
import sys
import time

from requests import HTTPError

from kaggle.rest import ApiException

sys.path.insert(0,'..')

sys.path.insert(0,'..')

from kaggle import api


# Unit test names include a letter to sort them in run order.
# That seemed easier and more obvious than defining a test suite.

# Run these tests in the container with the server running.
# In the case of unresolvable failure, run reset_database.sh.

# To run from Rider, create a Python tests>Unittests run config.
# Give it the module: unit_tests.TestKaggleApi
# Set the working directory to: kaggle-api/tests
# Define some envars:
# KAGGLE_API_ENDPOINT=http://localhost
# KAGGLE_API_ENVIRONMENT=LOCALHOST
# KAGGLE_CONFIG_DIR=/home/kaggle/.config/kaggle/dev
# KAGGLE_KEY=local_api_token
# KAGGLE_USERNAME=<kaggle-user-name>

# Add those envars to the Python Tests>Unittest template to
# make running individual tests easier.

test_user = api.config_values['username']
model_title = 'testing'
instance_name = 'test'
framework_name = 'jax'
kernel_name = 'testing'
dataset_name = 'kaggleapitestdataset'
up_file = 'sample_submission.csv'
description = 'House prices submission message'
competition = 'house-prices-advanced-regression-techniques'
dataset_directory = 'dataset'
kernel_directory = 'kernel'
model_directory = 'model'
model_inst_directory = os.path.join(model_directory, 'instance')
model_inst_vers_directory = os.path.join(model_inst_directory, 'version')

# Max retries to get kernel status
max_status_tries = 10

def tearDownModule():
    file = os.path.join(dataset_directory, api.DATASET_METADATA_FILE)
    if os.path.exists(file):
        os.remove(file)
    file = os.path.join(kernel_directory, api.KERNEL_METADATA_FILE)
    if os.path.exists(file):
        os.remove(file)
    file = os.path.join(model_directory, api.MODEL_METADATA_FILE)
    if os.path.exists(file):
        os.remove(file)
    file = os.path.join(model_inst_directory, api.MODEL_INSTANCE_METADATA_FILE)
    if os.path.exists(file):
        os.remove(file)


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

def initialize_dataset_metadata_file(dataset_dir):
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
    with open(metadata_file, 'w') as f:
        json.dump(meta_data, f)

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


class TestKaggleApi(unittest.TestCase):

    version_number, meta_file = initialize_dataset_metadata_file(dataset_directory)
    
    # Initialized from Response objects.
    competition_file = None
    kernel_slug = ''
    kernel_metadata_path = ''
    dataset = ''
    dataset_file = None
    model_instance = ''
    model_meta_data = None
    model_metadata_file = ''
    instance_metadata_file = ''
    
    # Kernels

    def test_kernels_a_list(self):
        try:
            kernels = api.kernels_list()
            self.assertGreater(len(kernels), 0)  # Assuming there should be some kernels
        except ApiException as e:
            self.fail(f"kernels_list failed: {e}")

    def test_kernels_b_initialize(self):
        try:
            self.kernel_metadata_path = api.kernels_initialize(kernel_directory)
            self.assertTrue(os.path.exists(self.kernel_metadata_path))
        except ApiException as e:
            self.fail(f"kernels_initialize failed: {e}")

    def test_kernels_c_push(self):
        if self.kernel_metadata_path == '':
            self.test_kernels_b_initialize()
        try:
            md = update_kernel_metadata_file(self.kernel_metadata_path, kernel_name)
            push_result = api.kernels_push(kernel_directory)
            self.assertIsNotNone(push_result.ref)
            self.assertIsNotNone(push_result.versionNumber)
            self.kernel_slug = md['id']
        except ApiException as e:
            self.fail(f"kernels_push failed: {e}")

    def test_kernels_d_status(self):
        if self.kernel_slug == '':
            self.test_kernels_c_push()
        try:
            status_result = api.kernels_status(self.kernel_slug)
            start_time = time.time()
            # If this loop is stuck because the kernel stays queued, go to the Kaggle website
            # on localhost and cancel the active event. That will exit the loop, but you may
            # need to clean up other active kernels to get it to run again.
            count = 0
            while status_result['status'] == 'running' or status_result['status'] == 'queued' or count >= max_status_tries:
                time.sleep(5)
                status_result = api.kernels_status(self.kernel_slug)
                print(status_result['status'])
            end_time = time.time()
            print(f'kernels_status ready in {end_time-start_time}s')
        except ApiException as e:
            self.fail(f"kernels_status failed: {e}")

    def test_kernels_e_list_files(self):
        if self.kernel_slug == '':
            self.test_kernels_c_push()
        try:
            fs = api.kernels_list_files(self.kernel_slug)
            self.assertGreaterEqual(len(fs.files), 0)  # Adjust expectation if needed
        except ApiException as e:
            self.fail(f"kernels_list_files failed: {e}")

    def test_kernels_f_output(self):
        fs = []
        if self.kernel_slug == '':
            self.test_kernels_c_push()
        try:
            fs = api.kernels_output(self.kernel_slug, 'kernel/tmp')
            self.assertIsInstance(fs, list)  # Assuming it returns a list of files, but may be empty
        except ApiException as e:
            self.fail(f"kernels_output failed: {e}")
        finally:
            for file in fs:
                if os.path.exists(file):
                    os.remove(file)
            if os.path.exists('kernel/tmp'):
                os.rmdir('kernel/tmp')

    def test_kernels_g_pull(self):
        if self.kernel_metadata_path == '':
            self.test_kernels_b_initialize()
        fs = ''
        try:
            fs = api.kernels_pull(f'{test_user}/testing', 'kernel/tmp', metadata=True)
            self.assertTrue(os.path.exists(fs))
        except ApiException as e:
            self.fail(f"kernels_pull failed: {e}")
        finally:
            for file in [f'{fs}/{self.kernel_metadata_path.split("/")[1]}', f'{fs}/{kernel_name}.ipynb']:
                if os.path.exists(file):
                    os.remove(file)
            if os.path.exists(fs):
                os.rmdir(fs)

    # Competitions

    def test_competition_a_list(self):
        try:
            competitions = api.competitions_list()
            self.assertGreater(len(competitions), 0)  # Assuming there should be some competitions
        except ApiException as e:
            self.fail(f"competitions_list failed: {e}")

    def test_competition_b_submit(self):
        try:
            api.competition_submit(up_file, description, competition)
        except HTTPError:
            # Handle submission limit reached gracefully (potentially skip the test)
            print('Competition submission limit reached for the day')
            pass
        except ApiException as e:
            self.fail(f"competition_submit failed: {e}")

    def test_competition_c_submissions(self):
        try:
            submissions = api.competition_submissions(competition)
            self.assertIsInstance(submissions, list)  # Assuming it returns a list of submissions
            self.assertGreater(len(submissions), 0)
        except ApiException as e:
            self.fail(f"competition_submissions failed: {e}")

    def test_competition_d_list_files(self):
        try:
            competition_files = api.competition_list_files(competition).files
            self.assertIsInstance(competition_files, list)
            self.assertGreater(len(competition_files), 0)
            self.competition_file = competition_files[0]
        except ApiException as e:
            self.fail(f"competition_list_files failed: {e}")

    def test_competition_e_download_file(self):
        if self.competition_file is None:
            self.test_competition_d_list_files()
        try:
            api.competition_download_file(competition, self.competition_file.ref, force=True)
            self.assertTrue(os.path.exists(self.competition_file.ref))
        except ApiException as e:
            self.fail(f"competition_download_file failed: {e}")
        finally:
            if os.path.exists(self.competition_file.ref):
                os.remove(self.competition_file.ref)

    def test_competition_f_download_files(self):
        try:
            api.competition_download_files(competition)
            self.assertTrue(os.path.exists(f'{competition}.zip'))
            self.assertTrue(os.path.getsize(f'{competition}.zip') > 0)
        except ApiException as e:
            self.fail(f"competition_download_files failed: {e}")
        finally:
            if os.path.exists(f'{competition}.zip'):
                os.remove(f'{competition}.zip')

    def test_competition_g_leaderboard_view(self):
        try:
            result = api.competition_leaderboard_view(competition)
            self.assertIsInstance(result, list)
            self.assertGreater(len(result), 0)
        except ApiException as e:
            self.fail(f"competition_leaderboard_view failed: {e}")

    def test_competition_h_leaderboard_download(self):
        try:
            api.competition_leaderboard_download(competition, 'tmp')
            self.assertTrue(os.path.exists(f'tmp/{competition}.zip'))
        except ApiException as e:
            self.fail(f"competition_leaderboard_download failed: {e}")
        finally:
            if os.path.exists(f'tmp/{competition}.zip'):
                os.remove(f'tmp/{competition}.zip')
            if os.path.exists('tmp'):
                os.rmdir('tmp')

    # Datasets

    def test_dataset_a_list(self):
        try:
            datasets = api.dataset_list(sort_by='votes')
            self.assertGreater(len(datasets), 0)  # Assuming there should be some datasets
            self.dataset = str(datasets[0])
        except ApiException as e:
            self.fail(f"dataset_list failed: {e}")

    def test_dataset_b_metadata(self):
        if self.dataset == '':
            self.test_dataset_a_list()
        m = ''
        try:
            m = api.dataset_metadata(self.dataset, dataset_directory)
            self.assertTrue(os.path.exists(m))
        except ApiException as e:
            self.fail(f"dataset_metadata failed: {e}")

    def test_dataset_c_metadata_update(self):
        if self.dataset == '':
            self.test_dataset_a_list()
        if not os.path.exists(os.path.join(dataset_directory, api.DATASET_METADATA_FILE)):
            self.test_dataset_b_metadata()
        try:
            api.dataset_metadata_update(self.dataset, dataset_directory)
            # TODO Make the API method return something, and not exit when it fails.
        except ApiException as e:
            self.fail(f"dataset_metadata_update failed: {e}")

    def test_dataset_d_list_files(self):
        if self.dataset == '':
            self.test_dataset_a_list()
        try:
            dataset_files = api.dataset_list_files(self.dataset)
            self.assertIsInstance(dataset_files.files, list)
            self.assertGreater(len(dataset_files.files), 0)
            self.dataset_file = dataset_files.files[0]
        except ApiException as e:
            self.fail(f"dataset_list_files failed: {e}")

    def test_dataset_e_status(self):
        if self.dataset == '':
            self.test_dataset_a_list()
        try:
            status = api.dataset_status(self.dataset)
            self.assertIn(status, ['ready', 'pending', 'error'])
        except ApiException as e:
            self.fail(f"dataset_status failed: {e}")

    def test_dataset_f_download_file(self):
        if self.dataset_file is None:
            self.test_dataset_d_list_files()
        try:
            api.dataset_download_file(self.dataset, self.dataset_file.name, 'tmp')
            self.assertTrue(os.path.exists(f'tmp/{self.dataset_file.name}'))
        except ApiException as e:
            self.fail(f"dataset_download_file failed: {e}")
        finally:
            if os.path.exists(f'tmp/{self.dataset_file.name}'):
                os.remove(f'tmp/{self.dataset_file.name}')
            if os.path.exists('tmp'):
                os.rmdir('tmp')

    def test_dataset_g_download_files(self):
        if self.dataset == '':
            self.test_dataset_a_list()
        ds = ['a', 'b']
        try:
            api.dataset_download_files(self.dataset)
            ds = self.dataset.split('/')
            self.assertTrue(os.path.exists(f'{ds[1]}.zip'))
        except ApiException as e:
            self.fail(f"dataset_download_files failed: {e}")
        finally:
            if os.path.exists(f'{ds[1]}.zip'):
                os.remove(f'{ds[1]}.zip')

    def test_dataset_h_initialize(self):
        try:
            api.dataset_initialize('dataset')
            self.assertTrue(os.path.exists(os.path.join(dataset_directory, api.DATASET_METADATA_FILE)))
        except ApiException as e:
            self.fail(f"dataset_initialize failed: {e}")

    def test_dataset_i_create_new(self):
        if not os.path.exists(os.path.join(dataset_directory, api.DATASET_METADATA_FILE)):
            self.test_dataset_h_initialize()
        try:
            update_dataset_metadata_file(self.meta_file, dataset_name, self.version_number)
            new_dataset = api.dataset_create_new(dataset_directory)
            self.assertIsNotNone(new_dataset)
            if new_dataset.hasError:
                print(new_dataset.error) # This is likely to happen, and that's OK.
        except ApiException as e:
            self.fail(f"dataset_create_new failed: {e}")

    def test_dataset_j_create_version(self):
        try:
            new_version = api.dataset_create_version(dataset_directory, "Notes")
            self.assertIsNotNone(new_version)
            self.assertFalse(new_version.hasError)
            self.assertTrue(new_version.hasRef)
        except ApiException as e:
            self.fail(f"dataset_create_version failed: {e}")

    # Models

    def test_model_a_list(self):
        try:
            ms = api.model_list()
            self.assertIsInstance(ms, list)
            self.assertGreater(len(ms), 0)
        except ApiException as e:
            self.fail(f"models_list failed: {e}")

    def test_model_b_initialize(self):
        try:
            self.model_metadata_file = api.model_initialize(model_directory)
            self.assertTrue(os.path.exists(self.model_metadata_file))
            self.model_meta_data = update_model_metadata(self.model_metadata_file, test_user, model_title, model_title)
            self.model_instance = f'{test_user}/{self.model_meta_data["slug"]}/{framework_name}/{instance_name}'
        except ApiException as e:
            self.fail(f"model_initialize failed: {e}")

    def test_model_c_create_new(self):
        if self.model_metadata_file == '':
            self.test_model_b_initialize()
        try:
            model = api.model_create_new(model_directory)
            if model.hasError:
                self.fail(model.error)
            else:
                self.assertIsNotNone(model.ref)
                self.assertGreater(len(model.ref), 0)
        except ApiException as e:
            self.fail(f"model_create_new failed: {e}")

    def test_model_d_get(self):
        try:
            model_data = api.model_get(f'{test_user}/{model_title}')
            self.assertIsNotNone(model_data['ref'])
            self.assertGreater(len(model_data['ref']), 0)
            self.assertEquals(model_data['title'], model_title)
        except ApiException as e:
            self.fail(f"model_get failed: {e}")

    def test_model_e_update(self):
        try:
            update_response = api.model_update(model_directory)
            self.assertIsNotNone(update_response.ref)
            self.assertGreater(len(update_response.ref), 0)
        except ApiException as e:
            self.fail(f"model_update failed: {e}")

    # Model instances

    def test_model_instance_a_initialize(self):
        try:
            self.instance_metadata_file = api.model_instance_initialize(model_inst_directory)
            self.assertTrue(os.path.exists(self.instance_metadata_file))
        except ApiException as e:
            self.fail(f"model_instance_initialize failed: {e}")

    def test_model_instance_b_create(self):
        if self.model_meta_data is None:
            self.test_model_b_initialize()
        if self.instance_metadata_file == '':
            self.test_model_instance_a_initialize()
        try:
            update_model_instance_metadata(
                self.instance_metadata_file, test_user, self.model_meta_data['slug'], instance_name, framework_name)
            inst_create_resp = api.model_instance_create(model_inst_directory)
            self.assertIsNotNone(inst_create_resp.ref)
            self.assertGreater(len(inst_create_resp.ref), 0)
        except ApiException as e:
            self.fail(f"model_instance_create failed: {e}")

    def test_model_instance_b_wait_after_create(self):
        # When running all tests sequentially, give the new model some time to stabilize.
        time.sleep(10) # TODO: Find a better way to detect model stability.

    def test_model_instance_c_get(self):
        if self.model_instance == '':
            self.test_model_b_initialize()
        try:
            inst_get_resp = api.model_instance_get(self.model_instance)
            self.assertIsNotNone(inst_get_resp['url'])
            self.assertGreater(len(inst_get_resp['url']), 0)
        except ApiException as e:
            self.fail(f"model_instance_get failed: {e}")

    def test_model_instance_d_files(self):
        if self.model_instance == '':
            self.test_model_b_initialize()
        try:
            inst_files_resp = api.model_instance_files(self.model_instance)
            self.assertIsInstance(inst_files_resp.files, list)
            self.assertGreater(len(inst_files_resp.files), 0)
        except ApiException as e:
            self.fail(f"model_instance_files failed: {e}")

    def test_model_instance_e_update(self):
        if self.model_instance == '':
            self.test_model_b_initialize()
        try:
            inst_update_resp = api.model_instance_update(model_inst_directory)
            self.assertIsNotNone(inst_update_resp)
            self.assertIsNotNone(inst_update_resp.ref)
            self.assertGreater(len(inst_update_resp.ref), 0)
        except ApiException as e:
            self.fail(f"model_instance_update failed: {e}")

    # Model instance versions

    def test_model_instance_version_a_create(self):
        if self.model_instance == '':
            self.test_model_b_initialize()
        try:
            version_metadata_resp = api.model_instance_version_create(self.model_instance, model_inst_vers_directory)
            self.assertIsNotNone(version_metadata_resp.ref)
        except ApiException as e:
            self.fail(f"model_instance_version_create failed: {e}")

    def test_model_instance_version_b_files(self):
        if self.model_instance == '':
            self.test_model_b_initialize()
        try:
            r = api.model_instance_version_files(f'{self.model_instance}/1')
            self.assertIsInstance(r.files, list)
            self.assertGreater(len(r.files), 0)
        except ApiException as e:
            self.fail(f"model_instance_version_files failed: {e}")

    def test_model_instance_version_c_download(self):
        if self.model_instance == '':
            self.test_model_b_initialize()
        version_file = ''
        try:
            version_file = api.model_instance_version_download(f'{self.model_instance}/1', 'tmp')
            self.assertTrue(os.path.exists(version_file))
        except KeyError:
            pass # TODO Create a version that has content.
        except ApiException as e:
            self.fail(f"model_instance_version_download failed: {e}")
        finally:
            if os.path.exists(version_file):
                os.remove(version_file)
            if os.path.exists('tmp'):
                os.rmdir('tmp')

    # Model deletion

    def test_model_instance_version_d_delete(self):
        if self.model_instance == '':
            self.test_model_b_initialize()
        try:
            version_delete_resp = api.model_instance_version_delete(f'{self.model_instance}/1', True)
            self.assertFalse(version_delete_resp.hasError)
        except ApiException as e:
            self.fail(f"model_instance_version_delete failed: {e}")

    def test_model_instance_x_delete(self):
        if self.model_instance == '':
            self.test_model_b_initialize()
        try:
            inst_update_resp = api.model_instance_delete(self.model_instance, True)
            self.assertIsNotNone(inst_update_resp)
        except ApiException as e:
            self.fail(f"model_instance_delete failed: {e}")

    def test_model_z_delete(self):
        try:
            delete_response = api.model_delete(f'{test_user}/{model_title}', True)
            if delete_response.hasError:
                self.fail(delete_response.error)
            else:
                pass
        except ApiException as e:
            self.fail(f"model_delete failed: {e}")


if __name__ == '__main__':
    unittest.main()